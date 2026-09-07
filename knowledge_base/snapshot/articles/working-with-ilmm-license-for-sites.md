---
title: "Working with ILMM License for Sites"
slug: "working-with-ilmm-license-for-sites"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/working-with-ilmm-license-for-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with ILMM License for Sites

The ILMM Sites screen gives you a comprehensive overview of the Socket sites in your account and lets you manage the licenses for the ILMM service.

## Showing ILMM Sites

The ILMM sites screen shows the ILMM license status for your account. In addition, the screen shows which country the site is physically located in, the number of WAN links, and the contact information for the site.

The screen only shows site types that are supported by the ILMM service: X1500, X1600, X1700 Sockets, and ESX vSockets. AWS and Azure vSocket sites are not monitored by the ILMM service.

**To show the ILMM sites screen:**

- From the navigation menu, select **Network > ILMM Service**, and then select the **Sites** page.

### Re-Assigning ILMM Licenses

The Sites screen shows the total number of Socket sites and ILMM licenses that are already allocated or available. If you need to move an ILMM license between two sites, first disable it on the original site and then enable it for the other site.

In the Links screen, links for sites that don’t have an ILMM license, are shown as disabled (greyed-out) and the site is designated as unlicensed. When you disable the ILMM license for a site, it’s links are no longer monitored by the ILMM service.

**To manage ILMM licenses for sites:**

1. From the navigation menu, select **Network > ILMM Service**, and then select the **Sites** page.
2. Disable the ILMM license for a site, to make a license available for a different site, click **Deallocate**.
3. Enable the ILMM license for the site your are starting to monitor, click **Allocate**.

The ILMM service is now allocated to the other site. Review the link settings for the site, the ILMM service only monitors links that are in **Completed** status. For more information about onboarding a link to ILMM, see [Managing ILMM for Your Account](/v1/docs/managing-ilmm-for-your-account).

## Explanation of ILMM Sites Fields

This section explains the columns that you can see in the table of sites.

![ILMM_Sites.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247964415261.png)

| Item | Description |
| --- | --- |
| Site | Name of the Socket site (configured in Network > Sites > {site name} > Site Configuration > General) |
| Type | Type of Socket model (ie. X1500, X1600, X1700, ...) |
| Country | Country where the site is physically located (configured in Network > Sites > {site name} > Site Configuration > General) |
| WAN Links | Number of WAN links defined for the Socket (configured in Network > Sites > {site name} > Site Configuration > Socket) |
| Contact Persons | Individuals who Cato can contact to check on the physical status of the Socket (click the site to configure the **Contact Persons**) |
| License | ILMM license is enabled or disabled for this site |
