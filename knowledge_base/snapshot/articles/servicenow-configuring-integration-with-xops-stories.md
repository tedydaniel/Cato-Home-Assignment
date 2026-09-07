---
title: "ServiceNow: Configuring Integration with XOps Stories"
slug: "servicenow-configuring-integration-with-xops-stories"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/servicenow-configuring-integration-with-xops-stories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ServiceNow: Configuring Integration with XOps Stories

## Overview

XOps supports bi-directional synchronization between XOps stories and an external service management platform. This integration helps keep investigation activity aligned across platforms, so updates made in one platform are reflected in the other.

For more information, see [Creating Bi-directional Integrations With Service Management Platforms](/v1/docs/creating-bi-directional-integrations-with-service-management-platforms).

## Configuring the ServiceNow Integration

To configure the ServiceNow integration, complete these five steps.

### Step 1: Create Custom Fields

Create fields to be populated when a ticketed in the Cato Management Application (CMA).

**To create custom fields:**

1. Log in to the ServiceNow platform.
2. Open any Incident.
3. From the top banner, right-click and navigate to **Configure > Form Builder**.
4. If required, agree to try the Form Builder and select the Default view.
5. Click **Add a new field in the Incident Table**.
6. Add these fields:
  - CMA Account ID
    - Type: Integer
    - Properties: Read Only, Mandatory, Active
  - CMA Story ID
    - Type: String
    - Properties: Read Only, Mandatory, Active

### Step 2: Create a Service API Key in the CMA

Service API keys enable scalable integration with external tools and services and are created in this format: `R=&lt;...&gt;|K=&lt;...&gt;`. For more information and detailed information about how to create a Service API key, see [Generating API Keys for the Cato API](/v1/docs/generating-api-keys-for-the-cato-api).

Once you have created the Service API key, copy and save it so it can be entered into the ServiceNow Platform.

### Step 3: Store API Key Securely in a Secure System Property

In the ServiceNow Platform, create a secure system property to store the API key.

**To create a secure system property:**

1. Navigate to https://<your instance>.service-now.com/sys_properties_list.do
2. Click **New**.
3. In the **System Properties New Record** form, add these details:

![SN5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35697265552285.png)
  - Name: cma_prod_api_key
  - Type: Password2
  - Value: The Service API key you created in step 2
4. Click **Submit**.

### Step 4: Create a REST Message

Create a REST message to send details from ServiceNow incidents to Cato:

**To create a REST message:**

1. In your ServiceNow Platform, navigate to **All>System Web Services > Outbound > REST Message**.
2. Click **New**.
3. In the **REST Message** form, add these details:
  - Name: Add a name for the REST Message
  - Endpoint: https://<your Cato account name>.cc.catonetworks.com/api/v1/graphql2
  - Authentication type: No authentication
  - HTTP Methods: Click **New** and add these details:
    - Name: Add a name
    - HTTP method: POST
    - Endpoint: https://<your Cato account name>.cc.catonetworks.com/api/v1/graphql2
4. Click **Submit**.

### Step 5: Create a Business Rule

Create a business rule to trigger the REST message.

**To create a business rule:**

1. In your ServiceNow Platform, navigate to **All > System Definitions > Business Rule**.
2. Click **New**.
3. In the **Business Rule New Record** form, add these details:

![SN6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35697286501149.png)
  - Name: Add a name for the Business Rule
  - Table: Incident
  - When: After
  - Update: True (Check the checkbox)
  - Filter Condition: Comments changes
4. On the **Advanced** tab, add this script:

```plaintext
(function executeRule(current, previous) {
  try {
    var lastComment = current.comments.getJournalEntry(1) || '';
    lastComment = stripJournalHeader(lastComment);
    if (!lastComment) {
      gs.info("GraphQL webhook: Empty comment, skipping " + current.number);
      return;
    }
    var accountId = current.u_cma_account_id;
    var storyId = current.u_cma_story_id;
        gs.info("GraphQL webhook: accountId " + accountId + " story " + storyId);
    if (!accountId || !storyId) {
      gs.error("GraphQL webhook: Missing accountId/storyId for " + current.number);
      return;
    }
    var gqlQuery =
      "mutation CreateStoryComment($accountId: ID!, $input: AddStoryCommentInput!) {" +
      "  xdr(accountId: $accountId) {" +
      "    addStoryComment(input: $input) {" +
      "      comment { id type __typename }" +
      "      __typename" +
      "    }" +
      "    __typename" +
      "  }" +
      "}";
    var body = {
      query: gqlQuery,
      variables: {
        accountId: accountId.toString(),
        input: {
          type: "USER",
          storyId: storyId.toString(),
          text: lastComment
        }
      }
    };
        var apiKey = gs.getProperty('cma_prod_api_key');
    var r = new sn_ws.RESTMessageV2('Update XDR story comments CMA Prod', 'post');
    r.setRequestHeader('Content-Type', 'application/json');
    r.setRequestHeader('Accept', 'application/json');
        r.setRequestHeader('x-api-key', apiKey);
    r.setRequestBody(JSON.stringify(body));
    //var response = r.execute(); // can be changed to Async - only for debug purposes
        var eccSysId = r.executeAsync();
    gs.info("GraphQL webhook queued, ECC sys_id=" + eccSysId);
    var status = response.getStatusCode();
    var responseBody = response.getBody();
  // Safe logging (see next section for masking)
     gs.info("GraphQL webhook: status=" + status);
     gs.info("GraphQL webhook: responseBody=" + responseBody);
  } catch (ex) {
    gs.info("GraphQL webhook: Failed: " + ex.message);
  }
  function stripJournalHeader(text) {
    text = text || '';
    if (text.indexOf('\n') > -1) {
      return text.split('\n').slice(1).join('\n').trim();
    }
    return text.trim();
  }
})(current, previous);
```
5. Click **Submit**.

## Troubleshooting

You can identify issues and errors at either:

- System Logs: Navigate to **System Logs > All** and search for messages containing `GraphQL webhook`.
- ECC record: Navigate to https://<instance>.service-now.com/sys_ecc_queue_list.do and locate the ECC record with the logged `ECC sys_id`.

### Common Issues

These are a list of common issues and their cause:

| Issue | Cause |
| --- | --- |
| Comment not sent | Comment text empty |
| Missing account/story IDs | Custom fields not populated |
| API returns 400 | Incorrect request format |
| API returns 401 | Invalid API key |
