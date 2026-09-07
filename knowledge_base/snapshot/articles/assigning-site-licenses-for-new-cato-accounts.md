---
title: "Assigning Site Licenses for New Cato Accounts"
slug: "assigning-site-licenses-for-new-cato-accounts"
updated: 2026-06-15T09:34:34Z
published: 2026-06-22T09:20:31Z
canonical: "knowledge.catonetworks.com/assigning-site-licenses-for-new-cato-accounts"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Assigning Site Licenses for New Cato Accounts

This article describes the process of moving PoC Cato accounts from a Trial account status to a Commercial account status, and assigning bandwidth licenses to sites.

## Overview

Prospective customers running a PoC with Cato Networks are assigned a trial account and have full access to the Cato platform. They can use the Cato Management Application (CMA) as the unified console to manage their account. Once the customer signs the contract with Cato, the account starts the process of moving from a Trial account status to a Commercial status.

During an account's Trial term status, sites do not require licenses. When moving from a trial account to a commercial account, it is necessary to assign licenses to all sites created during the PoC, otherwise, the site may be disabled and stop passing traffic.

Some services are not included in the default Cato trial accounts, such as EPP and managed services (eg. Managed XDR). To enable EPP for an account, please contact your Cato representative.

### Commercial Bandwidth Licenses vs. Scheduled Bandwidth Licenses

When the Commercial term for a new account starts, it's necessary to assign licenses for the site bandwidth in the account. When assigning licenses, the license status depends on the start date:

- Commercial licenses - The license is active and traffic passes (from the start date)
- Scheduled license - The license is not active and traffic does not pass (the start date is a future date)

Assigning a scheduled license to a site will cause the site not to pass traffic until the license moves into a staging status.

For more information about license statuses, see [Working with Cato License Types](/v1/docs/working-with-cato-license-types).

## New Accounts Moving to Commercial Status

During the process of moving from Trial account status to Commercial account status, the purchased licenses are added to the account in the CMA, with a Commercial or Scheduled status depending on the license start date.

**Staging Site Status**

For accounts where the Commercial status start date and the site license start date are 7 days or less apart, these sites are automatically assigned Staging licenses. For example, if the commercial account start date is June 1, and there are site licenses that start on June 5, those sites are assigned Staging licenses.

**Lock and Disabled Site Status**

When the Trial status ends, sites are automatically assigned a license with the Lock status for 14 days (the grace period) and continue to pass traffic. After 14 days, the licenses expire and sites that were not assigned a commercial license are disabled and stop passing traffic.

### Sample Timeline of an Account Moving from Trial to Commercial

This section contains an example timeline of the site license status for an account that moves from Trial to Commercial.

1. June 1 - Example Company starts a PoC with Cato Networks and an account with status Trial is created in the CMA.
  1. The CMA shows that there are no licenses for sites or services.
  2. All traffic passes for Example Company account.
  3. The Trial account is active for 30 days and expires on June 30.
2. June 10 - Example Company signs a contract with Cato Networks.
  1. The trial ends and the account moves to the Commercial state, purchased licenses are added to the CMA for the account.
    - Licenses for services will be available based on their start date.
    - Services that were enabled during the trial period but were not purchased, are no longer available.
  2. The CMA admins start assigning the licenses to the account sites.
    - Licenses with a start date of June 10 are active Commercial licenses and sites that are assigned these licenses will pass traffic.
    - Licenses with a start date of Sept 15 are Scheduled licenses and sites that are assigned the Scheduled licenses do not pass traffic.

On Sept 8, the licenses for these sites will move to a Staging status and start passing traffic.
3. July 14 - The 14-day grace period ends, and sites that were not assigned licenses are moved to the Disabled state and do not pass traffic.
