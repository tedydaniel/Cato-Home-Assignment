---
title: "Microsoft Defender for Office 365: Configuring the XOps Email Security Integration"
slug: "microsoft-defender-office-365-configuring-xops-email-security-integration"
updated: 2026-08-10T07:18:06Z
published: 2026-08-10T07:18:06Z
canonical: "knowledge.catonetworks.com/microsoft-defender-office-365-configuring-xops-email-security-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Defender for Office 365: Configuring the XOps Email Security Integration

## Overview

The email security integration lets you import email security events into XOps, so you can investigate phishing and other email-based threats with more context and from a single workflow. This helps reduce investigation time, improve threat correlation, and make it easier to identify related activity across email, network, and endpoint data sources.

Email attacks are often part of a broader attack flow. A phishing email, malicious attachment, or suspicious sending activity can lead to user access to malicious domains, additional network-based indicators, or related endpoint detections. With this integration, XOps can include email security events as part of the investigation flow and provide broader visibility into the attack.

When an Incident is created in Microsoft Defender for Office 365, a story is created in XOps. This lets you retain the original detection logic in Cato and investigate the alert as part of the broader activity in your account.

### Use Case

Company XYZ uses Microsoft Defender for Office 365 to protect users from phishing emails, malicious links, and other email-based threats. However, email alerts alone do not always provide the full attack context. Security teams also need to understand whether users interacted with the malicious content and whether the activity led to related detections in the network or on endpoints.

The company integrates XOps with Microsoft Defender for Office 365. When Microsoft Defender for Office 365 generates an alert, XOps automatically ingests the alert and creates a story in the Stories Workbench. This preserves the original detection logic from Microsoft and adds Cato’s network and security context to the investigation.

From the XOps story, the company can:

- Investigate whether users clicked a malicious link or accessed a suspicious domain
- Review related network and endpoint activity connected to the email alert
- Determine whether the alert is part of a broader attack flow affecting additional users or assets

By combining Microsoft Defender for Office 365 email detections with Cato’s contextual analytics, Company XYZ can investigate phishing and other email-based attacks with greater visibility. This helps reduce investigation time, improve threat correlation, and support faster response.

### Understanding Stories Created by the Integration

Stories generated from the integration are processed by the Generic Incident producer. The table below explains the widgets in these stories.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(141).png)

| Name | Description |
| --- | --- |
| Summary widget | A summary of basic information about the story, including the: - Criticality of the threat - Summary of the story details - Severity of the threat as determined by an analyst - Verdict for the threat as determined by an analyst |
| Details | A summary explanation of the story and metadata. |
| Timeline | A timeline of events or actions taken in the story. |
| Entities | The entities where the stories occurred. These could be Users, Sites, Data stores, applications, etc. |
| Evidence | Supporting evidence to explain why an XOps story was generated. |
| Raw Data | Dynamic table containing the raw events that generated the story. |

## Configuring the Microsoft Defender for Office 365 Integration

To configure the Email Security integration, you need to:

1. Create a MS Tenant integration as the parent connector
2. Create the API connector for Microsoft Defender for Office 365

### Prerequisites

- Microsoft 365 E3 License

#### Step 1: Create the MS Tenant Integration

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

**To create the MS Tenant integration:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(142).png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(143).png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

#### Step 2: Create the API Connector for Email Security

After you have set up the parent connector, add the details of the Interconnected Apps integration in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select **Microsoft Defender for Office 365**
5. In the **Auth** drop down, select the **Microsoft Primary Tenant** that was created in Step 1.
6. (Optional) Add a description.
7. Click **Save**.

The CMA connects to the vendor
8. Click **Authorize**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(144).png)

A Microsoft permissions screen will appear.
9. Review the requested permissions and click **Accept**.
10. The app is visible on the **Integrated Apps** table with a **Connected** status.

## Viewing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench, see [Reviewing Detection & Response XOps Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) For more information on reviewing XOps stories, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)
