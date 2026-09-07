---
title: "Managing ILMM for Your Account"
slug: "managing-ilmm-for-your-account"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/managing-ilmm-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing ILMM for Your Account

This article explains how to manage the sites and links for the Intelligent Last-Mile Monitoring (ILMM) service.

## Overview

Use the Cato Management Application to onboard your account to Cato's ILMM service and for ongoing management tasks.

### Preparing to Onboard a Site to ILMM

You need to provide the following information for each link in a Socket site that the ILMM service is monitoring:

- LOA - Letter of Authorization that lets Cato legally act on behalf of the customer with the ISP
- ISP account ID - ID for the customer's account with the ISP
- ISP link ID - ID for the link that connects the Socket to the ISP
- ISP contact information - Phone number and email to contact the ISP support team
- Site contact person - Individual(s) who Cato can contact for any issues related to the Socket at the physical site and notify in event of link issues

### High-Level Onboarding Process

The following diagram illustrates the ILMM onboarding process between the Cato customer and the NOC team, the numbers correspond to the items in the steps below:

![Validating_LInks_callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34511203227933.png)

1. Create ISP account (ISPs Info & LOA).

Includes: LOA, ISP account ID, and ISP contact information
2. Allocate the ILMM licenses to the sites that Cato is monitoring and enter the site contact person (Sites).
3. For each site, associate the link with the correct ISP (Links).

ILMM status for the link changes to **Pending ISP Validation**.
4. NOC team verifies the link information with the ISP.
  1. If the ISP data isn't correct, the ILMM status for the link changes to **Failed ISP Validation**.
5. Onboarding is complete, and the NOC team monitors the status of all licensed sites and links in the account.

## Allocating an ILMM License to a Site

The Sites page is automatically populated with all the physical Socket sites in your account. Enable the ILMM license for the sites that Cato is actively monitoring. You can also choose to disable ILMM for a site and assign the license to a different site for Cato to monitor.

We recommend that you enter the details for a contact person that Cato can contact if there is an issue related to the physical Socket. You can also define email notifications for the specific site. For more about configuring email notifications, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).

![ILMM_Sites.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34511203245725.png)

**To allocate an ILMM license to a site:**

1. From the navigation menu, select **Network > ILMM Service**, and then select the **Sites** page.
2. Select the site. The **Edit Site Details** panel for that site opens.
3. In the **License Status** section, enable the license.

The toggle is green ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34511233314589.png) when enabled.
4. Expand the **Contact Persons** section, and define one or more people that the NOC team can contact for issues related to the physical site and the monitored links.
  1. Click **Add Contact Person**.
  2. Enter the **Name**, **Email**, and **Phone** for this person.
  3. Repeat the previous two steps for up to ten contact persons per site.
5. (Optional) Configure tracking options to generate **Events** and **Send Notifications**.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
6. Click **Save**. The ILMM license is allocated to the site.

## Defining the ISP

Use the ISP Info & LOA page to define the ISP that is providing the last-mile Internet service between the physical site and the Cato Cloud.

You can download a template for the Letter of Authorization (LOA) from this page, which you can use to create the actual letter that will be sent to the ISP. When the LOA is complete, you can upload it to the Links page, and the NOC team will use it to contact the ISP.

![ISPs_Info___LOA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34511171779869.png)

**To define the ISP in the Cato Management Application:**

1. From the navigation menu, select **Network > ILMM Service**, and then select the **ISP Info & LOA** page.
2. Click **New**. The **Add ISP Contact Details** panel opens.

![Add_ISP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34511171804189.png)
3. Enter the **ISP Name**.
4. Enter the **Account ID** for your account with this ISP.
5. Enter the contact information for the ISP, the **Support Phone** and **Support Email**.
6. **(Optional)** Enter information related to the ISP in the Description. For example, people in your organization that are CCed on emails to the ISP.
7. Expand the **LOA Form** section and upload the completed LOA for this ISP.

If you save the ISP without the LOA form, then any links associated with the ISP are changed to the ILMM status **Missing ISP Info**.
8. Click **Save**. The ISP information is saved to your account.

Any links associated with the ISP are changed to the ILMM status **Pending ISP Validation**.

## Defining the Link for a Site

For the Socket sites that are enabled for the ILMM service, for each link select the ISP and provide the ISP ID. If the ISP was not defined in the previous section, you can create a new ISP and then enter the information for the link.

![ILMM_Links.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34511233395101.png)

**To define a link for a site:**

1. From the navigation menu, select **Network > ILMM Service**, and then select the **Link** page.
2. Select the link for a site. The **ISP Details** panel opens for that link.
3. In **ISP**, select the ISP that provides connectivity for this link.
4. In **ISP Link ID**, enter the unique ID that identifies this link for the ISP.
5. Click **Save**. The ISP for the link is defined. The NOC team can start validating the information with the ISP.

### Link Validation Process with the NOC Team

After you define the ISP for the link, the NOC team can start the process to validate the account and link information with the ISP. This is an iterative process within the Cato Management Application. If the link fails validation, then the status of the link changes, and the reason is shown in the Links page. You can update the information for the link, or the ISP and the NOC team will continue the validation process with the ISP.

| Link Status | Description |
| --- | --- |
| Disabled | ILMM monitoring is disabled for the site that contains this link. The row for this link is greyed out in the page. |
| Disabled (unlicensed) | A link belongs to a site without an ILMM license. The row for this link is greyed out in the page. |
| Missing ISP Info | ILMM monitoring is enabled for the site that contains the link, but the **ISP** and/or **ISP Link ID** is not yet defined for this link. |
| Pending ISP Validation | The ISP related information for the link is defined. The NOC team is validating the following information with the ISP: Account ID, ISP Link ID, LOA, and so on. An email notification is sent to the mailing list defined in the ILMM Notifications page. |
| Failed ISP Validation | The NOC team wasn't able to validate the information for this link with the ISP. The tooltip for the status shows the reason why the link failed the validation. For example, an incorrect ISP Link ID. When the link fails to validate with the ISP, the ILMM link status changes from **Pending ISP Validation** to **ISP Validation Failed**. An email notification is sent to the mailing list defined in the ILMM Notifications page. |
| Completed | The link is validated with the ISP, and the NOC team is monitoring this link. An email notification is sent to the mailing list defined in the ILMM Notifications page. |

## Defining the Mailing List for Email Notifications

ILMM email notifications are primarily for onboarding sites to ILMM, and they are sent to indicate a change in the link status:

- Link fails validation with the ISP - the ILMM link status changes from **Pending ISP Validation** to **ISP Validation Failed**
- Link is successfully validated - the ILMM link status changes from **Pending ISP Validation** to **Completed**

Select an existing mailing list in the Cato Management Application, or you can create a new one for the ILMM notifications. You can add external email addresses to the mailing list for individuals who don't have admin accounts.

If you customize the **Track** options for a site, then the mailing list for that site overrides the global setting in the ILMM Notifications page.

| ![ILMM_Notifications.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34511203414173.png) |
| --- |

**To define the mailing list for ILMM notifications:**

1. From the navigation menu, select **Network > ILMM Service**, and then select the **ILMM Notifications** page.
2. From the Mailing List drop-down menu, select the list of recipients for the ILMM email notifications.
3. Click **Save**.
