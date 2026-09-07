---
title: "Working with Cato License Types"
slug: "working-with-cato-license-types"
updated: 2026-07-20T11:30:48Z
published: 2026-07-20T11:30:48Z
canonical: "knowledge.catonetworks.com/working-with-cato-license-types"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Cato License Types

> [!NOTE]
> Note:
> 
> Cato account licenses use one of two models. This article applies to the Enforcement Model only and is not relevant to the [Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) (starting in January 2027). Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

## 

## Overview of Cato License Lifecycle and Notifications

Cato provides two types of account licenses: commercial and trial. Customers purchase commercial licenses from Cato for one or more years. The default length of a trial license is 30 days. The start date of Cato licenses is based on UTC and the ending date of Cato licenses is based on UTC-12.

To purchase, upgrade, or renew a license, please contact your Cato representative or reseller.

### Life Cycle for Accounts

The different statuses that are part of the life cycle for your Cato account, as displayed in the **Account > Licenses > General** tab in the **Account Status** field.

- Trial - A temporary account status that is valid for an ongoing PoC
  - During the account trial, all sites and services are enabled
  - Admins can create sites without assigning a license to the site
- Commercial - The Cato platform is active, and the account includes licenses for all purchased services
  - The account moves status from Trial to Commercial when the contract is signed and completed
  - The **License Expiration** shows the current end date of the Commercial account term
- Lock - Cato customers that need to renew their Cato service, and the platform is still active
  - When the account is locked, admins can't log in to the Cato Management Application (CMA)
  - All services and traffic are active. However, some CMA features are not available, for example, the Monitoring > Best Practices page
  - The account is locked 12 hours after the account expiration date for Trial and Commercial accounts (at 12:00 UTC). It will stay locked for 30 days. For example, if the expiration date is Dec 31, the account will be locked on Jan 1 at 12:00 UTC and stay locked until Jan 31 at 12:00 UTC
- Disable - The account service is expired, the account doesn't pass traffic, remote users can't connect via the Cato Client, and admins can't log in to the CMA

Cato sends notifications to customers and partners about the expiring Commercial term as follows:

- 30, 14, 7, and 3 days before the license expires
- When the account moves to a different status

> [!NOTE]
> **Note:**
> 
> Notifications for expiring licenses are only sent when the **License Updated** option is enabled for the [System Notifications](/v1/docs/account-level-alerts-and-system-notifications).

### Life Cycle for Licenses

The different statuses of your licenses are displayed in the **Account > Licenses > Bandwidth** tab.

There are two types of licenses for site bandwidth and services:

- **Trial licenses** are used to test the Cato platform and services, and are valid from the moment they are added to the account for 30 days.
- **Commercial licenses** for site bandwidth and services have the same expiration date as the account term (Cato refers to this as co-term).

These are the different license statuses:

- Trial - A temporary license that is used to test a site or specific service
  - Trial licenses are valid for 30 days.
  - When there are sites with trial licenses that are expired or about to expire, the Cato Management Application shows a banner indicating the expiration date for these licenses. The banner is displayed on all pages until all sites have valid licenses.
- Commercial - The license is active

For more information about licenses for site bandwidth, see [Managing Site Bandwidth in Licenses](/v1/docs/managing-site-bandwidth-in-licenses).
- Scheduled - a purchased license that is scheduled to start at a future date
  - When you assign a Scheduled license to a site, the site remains disabled, and no traffic passes until 7 days before the start date (Staging - see below).

For IPsec sites, the expected behavior is that the tunnel is only established when the license switches to Staging.

You can [allocate IP addresses](/v1/docs/allocating-ip-addresses-for-the-account) to accounts with a **Scheduled** license, the same IP addresses remain allocated to the account after a license moves to the **Commercial** status.
- Staging - 7 days before the license start date, it automatically moves to the Staging status.
  - The sites and services are ready for you to verify that the settings are configured correctly and that traffic passes
  - Once the start date is reached, it automatically converts to a Commercial license
- Lock - The trial license for the site or service has expired
  - The site still passes traffic, and the services are active
- Disable - The trial license for the site or service has expired
  - The site still does NOT pass traffic, and the services are NOT active

Cato sends notifications to customers and partners about expiring licenses as follows:

- 14, 7, and 3 days before the license expires

#### Assigning Site Licenses for Accounts that Move from Trial to Commercial

For trial accounts, all the sites are assigned trial licenses and traffic and services are active. When the account reaches the Commercial term start date, the site licenses expire and are moved to the Lock status. For more information, see [Assigning Site Licenses for New Cato Accounts](/v1/docs/assigning-site-licenses-for-new-cato-accounts-1).

- The sites pass traffic, and the services are active
- Admins can't make changes to the sites
- A banner is shown on each page in the Cato Management Application with the list of sites that are in the Lock state
- Email notifications are sent to admins 14, 7, and 3 days before the license expires

Assign a Commercial license to each site. For more information, see [Managing Site Bandwidth in Licenses](/v1/docs/managing-site-bandwidth-in-licenses).

## Showing the Licenses

The **License** window shows sections with the following information:

- **General:** Shows the status of the account license
- **Bandwidth:** Shows the site licenses, usage, status, and the licenses assigned to each site
- **Users:** Shows the number of licenses for remote users
- **Services:** Shows license information about the different services that customers can purchase from Cato, for example: Threat Prevention, CASB, DLP, XDR Pro, and Experience Monitoring
- **IPs:** The **IPs** section shows the number of public IP addresses allocated for the account
- **Account Life Cycle:** Shows the history of changes to your account status

**To show the details and status of the licenses:**

- From the navigation menu, click **Account > License**.

![License_General.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25050639510813(1).png)

## Understanding the General License Section

These are the fields for the **General** account license:

- **License Type** - Shows the account license type: Commercial, Trial, Locked, or Disabled.
- **License Expiration** - Shows the calendar date when the account license will expire.
- **DPA Version** - Shows the version of the Data Processing Agreement (DPA) that your company signed with Cato.

For more information about Cato's data retention policy, see [Guide to Cato Data Lake](/v1/docs/guide-to-cato-data-lake).
- **Data Retention Period (Months)** - Shows the number of months that Cato stores the data for your account.

## Understanding the Services Section

The commercial license life cycle for Cato services is the same as the account license, and both licenses expire on the same date. Cato sends notifications to customers about an expiring license 14, 7, and 3 days before the license expires. Examples of service licenses include: Threat Prevention, CASB, DLP, XDR Pro, and SaaS Security API.

For trial Services licenses, the expiration date is usually different than the account.

These are the fields for a **Services** license:

- **Service** - Name of the Cato service.
- **Enabled** - When enabled, the license is active, and the service can be enabled for the account.
- **Total Licenses** - Total number of licenses available for the relevant services. For example, the ILMM license shows the number of sites that are monitored.
- **Life Cycle** - Shows the service license type: Commercial or Trial.
- **Expiration** - For trial licenses, shows the expiration date.

**Note:** For **AI Security End Users** and **AI Security Applications** services, **Prior license** indicates customers that were migrated to Cato.

## Understanding the IPs Section

By default, accounts include three Cato-allocated public IPs (subject to change without notification). These are the fields for public **IPs** for the account:

- **Licensed** - Number of IP addresses assigned to the account
- **Used** - Number of IP addresses that are already allocated in **Network > IP Allocation**
- **Unused** - Number of IP addresses that are currently unassigned and waiting to be allocated

## Understanding the Users Section

The **Users** section shows the number of available licenses for ZTNA users. Each user can connect to the Cato Cloud with one or more of the Clients for the different operating systems. Disabled ZTNA users don't use a ZTNA user license. By default, accounts include five ZTNA users (subject to change without notification).

### Assigning ZTNA User Licenses to Different Users

If you have more users than available ZTNA user licenses, you can choose to assign the licenses to different users. Disable the current users that no longer require a license, and then enable existing users or create new ones.

For more about assigning licenses to users, see [Defining Remote Access for Users](/v1/docs/assigning-ztna-licenses-to-users).

## Understanding the Lifecycle Section

The **Lifecycle** section in the **Licenses** window shows the timestamp for changes that were made to licenses in your account.
