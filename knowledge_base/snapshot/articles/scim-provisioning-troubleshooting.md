---
title: "SCIM Provisioning Troubleshooting"
slug: "scim-provisioning-troubleshooting"
updated: 2026-08-10T10:56:55Z
published: 2026-08-10T10:56:55Z
canonical: "knowledge.catonetworks.com/scim-provisioning-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Provisioning Troubleshooting

SCIM provisioning is a directory services feature from an Identity Provider (IdP) used to provision users inside the Cato Management Application (CMA). Being unable to complete this provisioning means that users will not be added to the CMA. This playbook looks to provide guidance on troubleshooting issues with the SCIM provisioning process.

# Symptoms

Issues with SCIM Provisioning can manifest in a number of ways. An administrator may note the following symptoms:

- SCIM provisioning cannot be enabled
- No users can be added to CMA via SCIM provisioning
- New users are added to CMA, but are not working correctly
- Additional users are unable to be added to CMA via SCIM provisioning
- SCIM users have been updated, but the changes are not reflected in CMA

# Possible Causes

The following are possible causes that you can identify while troubleshooting

- The account does not meet the requirements for SCIM provisioning
- There is a credentials mismatch between the IdP and CMA
- Attributes are missing in the IdP and cannot be propagated to CMA
- There are insufficient licenses to provision the users
- Groups in the IdP are not assigned to the application
- The User or Group is not scoped correctly in the provisioning application
- The required Users or Groups are nested in the IdP
- The User or Group has not updated the relevant fields from the provisioning application to CMA

## Troubleshooting

Steps to troubleshoot the symptoms an Administrator may encounter are listed below. These steps are intended to identify possible causes for the issues faced. The resolution steps will be highlighted later in the playbook.

### Troubleshooting SCIM provisioning cannot be enabled

#### Ensure the account meets the requirements for SCIM provisioning

When attempting to enable SCIM note the error message that is presented. In this case *"Can't enable SCIM provisioning. Please contact Support and refer to Account ID Configuration - Email"*

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(148).png)

### Troubleshooting initial SCIM provisioning fails to add users to CMA

#### Confirm the credentials are correct in the provisioning application

Go to **the SCIM Application > Provisioning > Provisioning > Admin Credentials** press **Test Connection** and review the error message:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(149).png)

#### Check the available licences

Check the events for the account under **Monitoring** **>** **Events** apply a filter: **Event Type is System** check for events with **Sub-Type Sdp licence**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(150).png)

### Troubleshooting new users are added to CMA but are not working correctly

#### Confirm attributes are being correctly populated in CMA

CMA cannot assign licenses to users that do not have the mandatory email attribute.

Check the users entry in **Access > Users > Users Directory** and confirm the E-mail field has valid content.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(151).png)

Check the events for the account under **Monitoring** **>** **Events** apply a filter: **Event Type is System**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(152).png)

#### Check the available licences

Check the events for the account under **Monitoring** **>** **Events** apply a filter: **Event Type is System** check for events with **Sub-Type Sdp licence**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(153).png)

### Troubleshooting additional users are unable to be added to CMA via SCIM provisioning

#### Check where users or groups are not present in CMA

If you cannot see expected users or groups in the CMA under **Access > Users > Users Directory** or **Access > Users Groups.**

For **Users Directory** you can filter by **Source SCIM**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(154).png)

For **Users Groups** see **Type: SCIM Defined.**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(155).png)

#### Verify the reason for a failure to provision using the provision on demand feature

In the provisioning application, you can confirm the scoping of a user by making use of the **Provision on demand** feature. Go to **Enterprise applications > Cato Provisioning Application > Provisioning > Provision on demand** enter the users details and press **Provision**.

Once it fails, you can view details of the skipped action

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(156).png)In this scenario, we can see the user is part of the department **Brotherhood** which does not fit with the **scoping** rule *'No Mutants'*, which has the clause **department NOT EQUALS ‘Brotherhood’**

#### ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(157).png)Checking for other provisioning errors.

There can be other scenarios where the group is not part of the application, review the message presented and identify the cause.

In this case the group is **active** and meets the **scoping** but is reported as **not** **assigned to the application**:

### ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(158).png)Troubleshooting SCIM users have been updated, but the changes are not reflected in CMA

Users may have attributes updated in the SCIM provisioning application, but this is not reflected when a provisioning sync is completed.

## Resolving Discovered Issues

### Resolving the account does not meet the requirements for SCIM provisioning

You will need to raise a case with Cato Support. Please see the Raising Cases to Cato Support section below.

### Resolving there is a credentials mismatch between the IdP and CMA

Go to the **SCIM Application > Provisioning > Provisioning > Admin Credentials**. Ensure that the credentials (Tenant URL and Token) for the application are valid.

The credentials are available in CMA under **Access > Directory Services > SCIM**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(159).png)

This can be verified by pressing the Test Connection button from within the provisioning application.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(160).png)

### Resolving attributes are missing in the IdP and cannot be propagated to CMA

Go to **Enterprise applications > Cato Provisioning Application > Provisioning > Provisioning > Mappings** then select the **Provision Microsoft Entra ID Users** in the **Attribute Mappings** section confirm that the **userPrincipalName** is being mapped as well as **Email** address.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(161).png)

### Resolving there are insufficient licenses to provision the users

In the CMA go to **Administration > License > Users** and verify that there are sufficient licenses to provision the number of users you are attempting to add.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(162).png)If you are lacking sufficient licences please unassign/disable/delete inactive users or reach out to your sales team for further licence options.

### Resolving groups in the IdP are not assigned to the provisioning application

Go to **Enterprise applications > Cato Provisioning Application > User & Groups** and verify that the user/group is listed.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(163).png)If not present it can be added via the **Add user/group** Button

### Resolving the user or group is not scoped correctly in the provisioning application

Go to **Enterprise applications > Cato Provisioning Application > Provisioning > Provisioning > Mappings** then select the **Users** or **Group** mapping. Verify that the Source Object Scope filters include the relevant user/group.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(165).png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(166).png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(169).png)

**Note:** Multiple scoping filters use the OR logic, whereas, multiple attributes within a filter use the AND logic.

### Resolving the required Users or Groups are nested in the IdP

Confirm that when adding groups to the provisioning application that they are added as individual entries and are not nested within other groups.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(168).png)

### Resolving SCIM users have been updated, but the changes are not reflected in CMA

When a sync is performed, confirm that one of the following fields for the user in your IdP has been updated.

- Email
- UPN
- First Name
- Last Name
- Phone Number

If the issue still occurs, attempt to remove the user from your IdP, where possible and then check to see if the user goes into a disabled state on CMA.

If not, then please raise to Support.

# Raising Cases to Cato Support

If following this playbook has not resolved the issue, submit a Support ticket using this [Knowledge Base article](https://support.catonetworks.com/hc/en-us/articles/360017066338-Submitting-a-Support-Ticket).

In order to get the most helpful response to a request, an administrator should provide the results of troubleshooting steps taken throughout the use of this playbook. Including for example:

- The Account Name/Number
- Details of the IdP provider in use
- Screenshots from the IdP containing the relevant user UPNs
- Details of the User groups from the IdP
