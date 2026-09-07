---
title: "Overriding Bandwidth Management Profiles for a Site"
slug: "overriding-bandwidth-management-profiles-for-a-site"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/overriding-bandwidth-management-profiles-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overriding Bandwidth Management Profiles for a Site

This article explains how you can override account-level Bandwidth Management profiles at the site level.

## Overview of Bandwidth Settings for a Site

By default, the Bandwidth Management profiles (see [What are the Cato Bandwidth Management Profiles](/v1/docs/what-are-the-cato-bandwidth-management-profiles)) for the entire account also apply to all the sites. Since sites are not necessarily equal in terms of connectivity (available transports and links), you can override Bandwidth Management profiles for individual sites or even a specific link (such as ISPx vs ISPy, or ISP vs MPLS).

![overrideBW.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28249657789085.png)

## Overriding the Account Bandwidth Profile for a Site

For any profile that is overridden, the **Account Default** column displays the global upstream (**U**) and downstream (**D**) limits, and the **RESTORE** button is displayed.

We recommend that you use the **%** unit of measurement for Bandwidth Management profiles at the global level, and **Mbps** at the site level if you are overriding global profiles.

**To override a global Bandwidth Management Profile for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Bandwidth Management**.
3. If the site has multiple internet links, configure one of these options:
  - Select the **Apply settings on all Internet interfaces** option to apply the Bandwidth Management settings to all Internet links (default). In this case, only one set of Bandwidth profiles appears for Internet Transports.

**Note:** By default, the Cato Cloud assumes that all Internet links are used similarly in regard to QoS and, specifically, in applying limits on QoS. You can change this default behavior by clearing this check box as explained following.
  - Clear the **Apply settings on all Internet interfaces** check box to individually configure the Bandwidth Management settings for each Internet link. In this case, a set of Bandwidth profiles appears for each link.
4. Click on the profile you wish to override. The **Edit Bandwidth** panel opens.
5. Modify the profile details as follows:
  1. **Override:** Enable or disable by clicking on the slider. Green indicates that the global profile for the account is overridden by the limits configured for this site.
  2. **Limits**: Select if and how to limit the bandwidth for this priority as follows:
    - **No Limit** - do not force any bandwidth limits.

**Note:** If you select **No Limit**, this priority can potentially starve traffic with lower priorities.
    - **Always Limit** - always enforce the limit according to the upload/download values you define below.
    - **Limit only when line is congested** - When the line has more than 100% traffic, limit this priority based on the setting below.

For example, if P30 is limited to 30%, that means only 30% of the link is allocated to lower priority traffic. Ensuring that higher priority traffic can use the remaining 70% of the link.
  3. **Upload Limit**/**Download Limit**: Type the required value and select the unit of measurement (% or Mbps).
6. Click **Apply**. The profile configuration is added.
7. Click **Save**. The profile configuration is saved.

For any profile that was overridden, the **Account Defaults** column display is updated to indicate the account default values for upstream and downstream limits.

### Restoring the Account Defaults to a Site

When you override a Bandwidth Management profile for a site, the Bandwidth Management screen for the site shows the values of the Account Defaults profile. You can choose to stop overriding that profile and restore the default account settings.

**To restore the default account Bandwidth Management settings to a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Bandwidth Management**.
3. In the row for the Bandwidth Management profile, click **Restore**.

The custom values are removed from the profile, and the default account values are restored.
4. Click **Save**. The account defaults for the Bandwidth Management profile are restored.
