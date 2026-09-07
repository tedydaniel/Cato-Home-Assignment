---
title: "Working with Cato Account License Lifecycle – (Bursting Model License only)"
slug: "working-with-cato-account-license-lifecycle-jan-2027-license"
updated: 2026-07-06T08:10:16Z
published: 2026-07-06T08:10:16Z
canonical: "knowledge.catonetworks.com/working-with-cato-account-license-lifecycle-jan-2027-license"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Cato Account License Lifecycle – (Bursting Model License only)

This article explains the different Cato licenses and information in the License page.

> [!NOTE]
> Note
> 
> Cato account licenses use one of two models. This article only applies to the [Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) (starting in January 2027) and is not relevant for accounts using the Enforcement Model. Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

## Overview of Cato License Lifecycle and Notifications

Cato provides two types of account licenses: commercial and trial. Customers purchase commercial licenses from Cato for one or more years. The default length of a trial license is 30 days. The start date of Cato licenses is based on UTC and the ending date of Cato licenses is based on UTC-12.

To purchase, upgrade, or renew a license, please contact your Cato representative or reseller.

### Life Cycle for Accounts

The different statuses that are part of the life cycle for your Cato account, are displayed in the **Account > Licenses > Overview** tab in the **Account Status** field.

- Trial - A temporary account status that is valid for an ongoing PoC
  - During the account trial, all sites and services are enabled
  - Admins can create sites
  - Admins can import users, log into the Client, and connect to the Cato Cloud
- Commercial - The Cato platform is active, and the account includes licenses for all purchased services
  - The account moves status from Trial to Commercial when the contract is signed and completed
  - The **License Expiration** shows the current end date of the Commercial account term
- Lock - Cato customers that need to renew their Cato service, and the platform is still active
  - When the account is locked, admins can't log in to the Cato Management Application (CMA)
  - All services and traffic are active, however some CMA features are not available
  - The account is locked 12 hours after the account expiration date for Trial and Commercial accounts (at 12:00 UTC). For example, if the expiration date is Dec 31, the account will be locked on Jan 1 at 12:00 UTC.
- Disable - The account service is expired, the account doesn't pass traffic, remote users can't connect via the Cato Client, and admins can't log in to the CMA

Cato sends notifications to customers and partners about the expiring Commercial term as follows:

- 30, 14, 7, and 3 days before the license expires
- When the account moves to a different status

> [!NOTE]
> Note
> 
> Notifications for expiring licenses are only sent when the **License Updated** option is enabled for the [System Notifications](/v1/docs/account-level-alerts-and-system-notifications).

### Understanding the Floating Period

Once an account moves to Commercial, it may enter a Floating Period which ends on the commercial license's start date.

The Floating Period allows your account to begin using licensed capacity before the official license start date. During the Floating Period, services can operate normally even if the contract start date has not yet been reached. If Cato detects usage that exceeds your currently active licenses, the system may automatically activate additional license capacity from your floating licenses. Once activated, this capacity becomes billable and remains active until the end of the floating period and the original contract start date. Floating licenses help ensure uninterrupted service during deployment while aligning license activation with actual usage.

For more information, see [Floating License](/v1/docs/floating-licenses).

### Life Cycle for Licenses

The different statuses of your licenses are displayed in the **Account > Licenses** page. Every license has both a Plan and a Status.

#### Understanding License Plans

The license plan describes the type of license:

- Commercial: The license was purchased and usually expires on the same day as the account expiration date.
- Trial: The license was provided for testing and evaluation purposes. These usually expire within 30 days.

#### Understanding License Status

The License Status describes the state of the license:

- Active: License is active
- Disabled: License has expired and is no longer active. Cato sends notifications to customers and partners about expiring licenses as follows:
  - 14, 7, and 3 days before the license expires
- Floating: The license has a future start date, and the account is within the Floating Period.
- Scheduled: The license has a future start date (and is not part of the Floating Process)
- Floating Activated: The license was automatically added in the Floating Period. The license expires when the Floating Period ends.

## Showing the Licenses

The **License** page consists of a number of tabs that contain comprehensive information about the licenses for your account.

**To access the licenses page:**

- From the navigation menu, click **Account > License**.

## Understanding the Overview Tab

The **Overview** tab provides basic information about your account.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(42).png)

- **Account Status** - Shows the account status: Commercial, Trial, Locked, or Disabled.
- **License Expiration** - Shows the calendar date when the account license will expire.
- **Data Retention Period (Months)** - Shows the number of months that Cato stores the data for your account.
- **Data units** - The number of data units in your account.

## Understanding the Base Products Tab

The **Base Products** tab displays information about your Base Products licenses.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(43).png)

The **Base Products** tab has two sections:

- **Overview Bar** - For each of your Base Products, the licensed capacity (Mbps or Users) you have purchased for each license is displayed.
- **Purchased Licenses Details** - For each of your Base Products, you can drill down into the licensed capacity and start and end date for each region group. This section can be filtered by Plan or Status.

## Understanding the Premium Security Tab

The **Premium Security** tab displays information about your Premium Security licenses.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(44).png)

For each of your Premium Security capabilities, you can drill down into the licensed capacity and start and end date for each license. This section can be filtered by Plan or Status.

## Understanding the Insights Tab

The **Insights** tab displays information about your Insights licenses.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(45).png)

For each of your Insights licenses, you can drill down into the licensed capacity and start and end date for each license. This section can be filtered by Plan or Status.

## Understanding the Hardware Tab

The **Hardware** tab displays information about your Socket licenses.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(46).png)

You can drill down into information about the Sockets in your account. Purchased IP address licenses are displayed on the Hardware tab.

## Understanding the Services Tab

The **Services** tab displays information about your Services.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(47).png)

You can drill down into information about the Services for your account.

## Understanding the Account Life Cycle Tab

The **Account Life Cycle** tab displays what license changes have been made to your account.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(48).png)
