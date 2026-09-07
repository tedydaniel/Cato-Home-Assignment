---
title: "SCIM Sync and Provisioning Troubleshooting"
slug: "scim-sync-and-provisioning-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/scim-sync-and-provisioning-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Sync and Provisioning Troubleshooting

## Overview

SCIM (System for Cross-domain Identity Management) synchronization and user provisioning are essential for automating identity management and ensuring secure, streamlined access to applications and resources. However, challenges can occur that interrupt this automation, potentially leading to access issues or compliance risks. This playbook is designed to address common SCIM sync and provisioning problems in Cato and offer effective solutions for resolving them.

## Symptoms

Failures with SCIM provisioning can manifest in several ways. An administrator may note the following symptoms:

- Error message when enabling SCIM
- Users are not provisioned to the CMA
- Test Connection from IdP to CMA fails
- Provisioned Users fail to connect to SDP clients
- Duplicate Users in CMA

## Possible Causes

List the possible causes that they will try and identify while troubleshooting

- Misconfiguration
- Wrong Admin Credentials Used
- Licensing
- Duplicate User provisioned via IdP

## Troubleshooting the Issue

Before diving into the troubleshooting steps, the diagram below offers a high-level overview of how SCIM provisioning functions. Unlike LDAP, which relies on a pull-based approach, SCIM uses a push mechanism to deliver user updates directly to the Cato Management Application (CMA).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26455622955165.png)

Cato supports SCIM provisioning for users through Azure, Okta, and One Login. For more information on configuring SCIM provisioning for each identity provider (IdP), see [Provisioning Users with SCIM](/v1/docs/scim-user-provisioning). This playbook specifically focuses on SCIM provisioning with Azure (Entra ID), but the core concepts and troubleshooting techniques are applicable to other IdPs as well.

### Error When Enabling SCIM

When enabling SCIM in CMA, the following error is observed, "Can't enable SCIM provisioning. Please contact Support and refer to the Account ID Configuration - Email".

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26606350511773.png)

When you encounter this error, please contact [Support](/v1/docs/submitting-a-support-ticket) to modify the User ID type in your account.

### Users Are Not Getting Provisioned to CMA

This section will show some of the common reasons why users are not getting provisioned to the CMA.

#### Validate Admin Credentials

- Go to SCIM Application > Provisioning > Update Credentials. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26511743159325.png)
- Expand Admin Credentials and click on Test Connection ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26511683786909.png)
- For successful integration and provisioning with CMA, you should see the following result. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26511683788189.png)
- If the Test Connection fails, refer to [Resolving Admin Credentials](/v1/docs/scim-sync-and-provisioning-troubleshooting#resolving-admin-credentials) for how to resolve this.

#### Mandatory Attributes

- Certain attributes are required and mandatory for SCIM Provisioning with Microsoft Entra ID. If any of these required attributes are missing, user provisioning may fail, or the provisioned user may be unable to connect.
- The screenshot below shows the mandatory fields required for provisioning to work. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26513224640157.png)
- If the email field is missing, the user will still be provisioned to the CMA, but will not be able to connect to the SDP client.
- Refer to the [resolving Mandatory Attribute](/v1/docs/scim-sync-and-provisioning-troubleshooting#resolving-mandatory-attribute) section to validate whether this is causing the issue and how to resolve it.

#### Users/Groups Not Assigned to the Enterprise Application in the Azure Portal

Users and groups need to be added to the Cato Provisioning Application in the Azure portal before they can be synced into CMA. This section provides step-by-step instructions on how to validate this.

- Go to Enterprise applications > Cato Provisioning Application > User & Groups and verify that the user or group is listed.
- In the below example, we can see that 1 group and 1 user are assigned to the "Cato Networks Provisioning—APJ T1 Lab" application. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26513224640669.png)
- If the user or groups are not listed under your Provisioning Application in Azure, refer to [Assigning Users/Groups to Provisioning Application](/v1/docs/scim-sync-and-provisioning-troubleshooting#assigning-usersgroups-to-provisioning-application).

#### Scoping Filter in Users/Groups

- Check if scoping filters are configured for users or groups in the provisioning setup.
- Navigate to Enterprise Applications > Cato Provisioning Application > Provisioning > Mappings, then select the User or Group mapping.
- Review the Source Object Scope filters to see if they could be excluding the user or group in question.
- If provisioning fails due to a scoping filter, the user/group will be skipped, and Azure will show a reason for the failure. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26514553909149.png)
- To resolve this, refer to [Resolving Scoping Filters in Users/Groups](/v1/docs/scim-sync-and-provisioning-troubleshooting#resolving-scoping-filters-in-usersgroups).

### Provisioned Users Failing to Connect to SDP Client

- After being SCIM provisioned in the CMA, users encounter the following error when attempting to connect through the SDP client, specifically after entering their email address and subdomain. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26623066681885.png)
- One possible cause of this failure is the licensing issue
- Refer to the [Resolving the licensing issue](/v1/docs/scim-sync-and-provisioning-troubleshooting#resolving-the-licensing-issue) section to learn how to validate whether this issue is related to licensing and how to go about resolving it.

### Duplicate Users in CMA

Duplicate users with the same email address may appear in the CMA. Typically, one user is disabled, while the other has the SDP license assigned.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26700725460893.png)

Refer to the [Resolving Duplicate Users in CMA](/v1/docs/scim-sync-and-provisioning-troubleshooting#resolving-duplicate-users-in-cma) section for the possible reason why this happened and how to resolve it.

## Resolving Discovered Issues

### Resolving Admin Credentials

- Log in to your CMA and navigate to Access > Directory Services > SCIM to validate that the Base URL is the same as the Tenant URL configured in Azure. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26511683788445.png)
- If the Base URL is the same, try generating a new token. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26511743168541.png)
- Copy the new token *before* saving the configuration on the CMA. Once that is done, input the new token in Azure and click on **Test Connection** again.

### Resolving Mandatory Attribute

- The email attribute is mandatory. If this field is missing in the user information within the Identity Provider (IdP), the user will still be provisioned to the CMA, but their profile will lack an email address. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26625524742941.png)
- When the email field is absent from the user's profile, the system cannot assign an SDP license, which prevents the user from successfully connecting via the SDP client.

### Assigning Users/Groups to Provisioning Application

- To assign users or groups to your Provisioning Application, click on Add user/group, and then select "User and groups."
- Then, the right pane will appear for you to select the respective users/groups to be added. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26513224642205.png)
- Optionally, after adding the Users and Groups to the Provisioning Application, instead of waiting for the regular automated provisioning cycle, you can manually provision these users/groups in CMA through "Provision on Demand." ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26886686855069.png)**NOTE**: Nested groups provisioning is not supported

### Resolving Scoping Filters in Users/Groups

- If a scoping filter is excluding the user or group unintentionally:
  - Adjust the scoping filter criteria to ensure it includes the user/group.
  - Confirm the logic of your filters (AND/OR) matches the intended behavior.
- For more details, refer to the Microsoft document - [Scoping users or groups to be provisioned with scoping filters](https://learn.microsoft.com/en-us/azure/active-directory/app-provisioning/define-conditional-rules-for-provisioning-user-accounts?pivots=app-provisioning).
- After making adjustments, rerun the provisioning on demand to verify that the user/group is now included.

### Resolving the Licensing Issue

- Navigate to Access > Users, and click on User Directory. Validate if the user was assigned an SDP license. The screenshot below shows that the Scim User was not assigned any SDP license. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26624060542365.png)
- Next, navigate to *Access > License Assignment* to verify whether the "**Assign SDP license to all users**" option is enabled.
  - If it is, check whether the Total Number of Users exceeds the Total Number of SDP Licenses. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26624624598045.png)
  - If the number of users exceeds the available licenses, please contact your Cato sales representative to explore options for acquiring additional SDP licenses.
  - If you are unsure about who they are, please feel free to contact [Support](/v1/docs/submitting-a-support-ticket).
- If "**Assign SDP license to selected users or groups**" is selected, ensure that SCIM-provisioned users are included in the assigned groups. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26624104674205.png)

### Resolving Duplicate Users in CMA

- When a user is deleted in Azure, the system prepends the ObjectID value to the UPN value and sets the user’s active status to false. This action deactivates the user in the SCIM database and updates the UPN value to include the ObjectID+UPN. This behavior aligns with [Microsoft documentation](https://learn.microsoft.com/en-us/answers/questions/129068/azure-ad-scim-adding-suffix-and-prefix-to-username).![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26860424599069.png)
- If the same user is recreated in Azure using the same email address, a duplicate user will be created in both the SCIM database and CMA with a different ObjectID. At this stage, the UPN for the duplicate users will differ. In this scenario, the disabled user should be deleted in CMA to avoid duplication.
- Cato permits users with duplicate email addresses; however, only one duplicate user can be assigned an SDP license. It is important to note that UPN and ObjectID must remain unique across all SCIM Directory Services.

## Notes and Limitations

1. Different users can be provisioned through SCIM and LDAP. However, if a user is provisioned through both SCIM and LDAP, the SCIM provisioning takes precedence. As a result, the user is removed from LDAP-provisioned groups and added to SCIM-provisioned groups. For more details, refer to [Provisioning Users with SCIM and LDAP](/v1/docs/provisioning-users-with-scim-and-ldap).
2. If you plan to switch between SCIM and LDAP provisioning, read [Changing Between SCIM and LDAP User Provisioning](/v1/docs/changing-between-scim-and-ldap-user-provisioning) first to ensure a smooth transition.
3. Although users and groups can be deleted in the CMA, we recommend you do delete users directly in your SCIM app. Refer to [Removing Users or Groups from the SCIM App](/v1/docs/provisioning-users-with-scim) for details on the proper way to do this.

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

1. Issue Description and User Impact
  - A clear description of the issue encountered during SCIM provisioning.
  - An overview of the scope and impact on affected users (e.g., number of users impacted, error messages received, etc.).
2. Provisioning Status to CMA
  - Were the affected users successfully provisioned to CMA?
    - If not, examining the logs can offer additional insights and help identify the underlying cause of the problem, facilitating further troubleshooting and resolution.
      - Log in to [www.portal.azure.com](http://www.portal.azure.com). Go to Enterprise Application > Cato Provisioning Application > Provisioning
      - Click on "Provisioning Logs" to view the provisioning history.
      - Clicking into a specific provision will open up the "Provisioning log details" pane on the right. From the below, we can see that the synchronization for this object was skipped because it was not assigned to the application. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26676034994845.png)
    - Please also try to attempt on-demand provisioning for the impacted users and include:
      - A screenshot of the result (success or error message)
      - The exact timestamp of when the on-demand provisioning was performed
3. Connectivity to SDP Client
  - Are users who are provisioned successfully able to connect to the SDP client?
    - If not, please provide a screenshot of the client UI showing the error when the user tried connecting
    - Provide the client's logs by using the [Record Issue](/v1/docs/recording-issues-using-the-cato-client) feature.
