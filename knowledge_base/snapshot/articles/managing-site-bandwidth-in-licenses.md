---
title: "Managing Site Bandwidth (Enforcement Model License only)"
slug: "managing-site-bandwidth-in-licenses"
updated: 2026-07-06T14:03:30Z
published: 2026-07-06T14:03:30Z
canonical: "knowledge.catonetworks.com/managing-site-bandwidth-in-licenses"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Site Bandwidth (Enforcement Model License only)

> [!NOTE]
> Note:
> 
> Cato account licenses use one of two models. This article applies to the Enforcement Model only and is not relevant to the [Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) (starting in January 2027). Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

## Overview of Site and Bandwidth Pooled Licenses

Licenses manage the total upstream and downstream WAN traffic for a site over the Cato Cloud. There are two bandwidth license models to meet the different requirements of your organization:

- **Pooled bandwidth licenses** - A bandwidth pool that you can divide and assign bandwidth to different sites in the same region.

You can use the available bandwidth in a pool to easily increase the bandwidth for a site. In addition, you can reduce the bandwidth for a site and create more available bandwidth in the pool.
- **Site licenses** - Fixed bandwidth license for a site, and you can unassign the license from one site and reassign it to a different site.

### Working with Unlicensed Sites

Sites in your account can be unlicensed, and these sites do not pass any traffic. When you create a new site, you can choose not to assign a license to it. You can also disable a site and then unassign the license from it.

When you unassign a license from a site, all traffic is immediately disabled for the site, even if the site is still enabled.

You can have up to 1000 unlicensed sites in your account.

### Understanding Site License Types

There are two types of licenses for sites in your account, depending on how the site connects to the Cato Cloud.

- SASE license
  - Supports all networking (SD-WAN) and security features
  - Socket and vSocket sites must use SASE licenses
  - IPsec sites can choose to use SASE licenses
- SSE license
  - Supports all security features, partial support of networking features (no SD-WAN)
  - IPsec sites can use SSE licenses

### Geographical Regions for Site Bandwidth Licenses

Licenses for site bandwidth are based on geographical **License Groups**. For more information, see [Country's Allocation to License Groups and ZTNA Users](/v1/docs/country-s-allocation-to-license-groups-and-ztna-users).

## Calculating Bandwidth License Capacity

For all license types, bandwidth is assigned per site and includes traffic in all active links. The bandwidth assigned is for both upstream and downstream capacity. This means that a 500 Mbps site license provides capacity for 500 Mbps download and 500 Mbps upload across all active links in the site.

For example, let's say that you have a site with two active links and you want to determine how much bandwidth is needed. You calculate the max upload and download requirements of each link and assess them as follows:

| Link | Max Download (Mbps) | Max Upload (Mbps) |
| --- | --- | --- |
| Link 1 | 50 | 80 |
| Link 2 | 80 | 40 |
| **Total** | **130** | **120** |

To ensure full coverage, your **site license must match the higher of**:

- The total max download: 50 + 80 = **130 Mbps**
- The total max upload: 80 + 40 = **120 Mbps**

Therefore, you would need a site license with **130 Mbps**, which will include up to 130 Mbps upload capacity and 130 Mbps download capacity.

## Viewing the Bandwidth Licenses for Your Account

You can view the details for each bandwidth license that is used for sites in your account. The screen shows the total number of licenses, trial licenses, and licenses that are currently available to assign to sites.

![License_screen.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151821747229.png)

**To show the bandwidth licenses for your account**

1. From the navigation menu, click **Account > License** and select the **Bandwidth** tab.
2. To show the details of sites that are using a Pooled license, click the Pooled license.

The **Pooled License** panel opens, and the **Pooled Usage** section shows the allocated bandwidth for each site.

![Pooled_usage.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151798048413.png)

### Understanding the Bandwidth Licenses

This section explains the fields in the Bandwidth screen.

#### Summary of Pooled and Site Licenses

The following fields summarize the status of the site licenses:

- **Site Licenses** and **Pooled Licenses** - Total number of site or pooled licenses in the account
- **Trial** - Temporary licenses that are currently valid
- **Commercial** - Purchased license that is currently valid
- **Scheduled** - Purchased licenses that are scheduled to start at a future date

#### Pooled and Site License Details

The following fields explain the details of the site bandwidth licenses:

- **License Group** - Group of geographical regions for the license as follows:
  - Group1 - NAM (North America) and EMEA (Europe)
  - Group2 - APJ (Asia, Pacific), ANZ (Australia, New Zealand), LATAM (Central and South America), Africa, Middle East, Dubai
  - China, Morocco, Vietnam
- **Type** - SASE or SSE license
- **BW (Mbps)** - Maximum available bandwidth over the Cato Cloud for the site
- **State** - Shows the site license type: Commercial, Trial, Locked, or Disabled
- **Start Date** - License starting date
- Pooled license details:
  - **Sites** - Number of sites using this pooled license
  - **Allocated** - Bandwidth (Mbps) already allocated to sites
  - **Available** - Bandwidth (Mbps) available for sites
- **Country** - (for site licensees) Country for the physical site (**Network > Sites > Site Configuration > General**)
- **Expires** - Expiration date for the license

## Assigning a Pooled License to a Site

This section explains how to manage site bandwidth using a pooled license. You can assign bandwidth to a site from multiple pools for the same region.

Pooled licenses are not supported for non-tiered regions, such as China and Vietnam.

### Creating a New Site with a Pooled License

When you are [creating a new site](/v1/docs/using-the-cma-to-add-sites), you can use a Pooled license for the site bandwidth license.

![Add_site_pool.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151821789213.png)

**To create a new site that uses a Pooled license:**

1. In the **General** section of the **Add Site** panel, in **License Type** select **Pooled license**.
2. In **License**, select the Pooled license from the region for the site's **Country**.

In the example above, the site is located in **Italy** and the Pooled license is for **Europe**.
3. Set the **Allocate Bandwidth** for the site.

The amount of available bandwidth for the Pooled license is shown as the **Max** bandwidth for the site.
4. Click **Add**. The bandwidth pool is added to the site.
5. Repeat steps 2-4 to add bandwidth pools from other Pooled licenses in the same region to the site.
6. Configure the other settings for the site.
7. Click **Apply**.

### Editing the Pooled License for a Site

For sites that are assigned a Pooled license, you can increase or decrease the site bandwidth.

The following example shows a site that has 200 Mbps bandwidth as of June 12, 2023, and is edited to add another 100 Mbps starting on August 1, 2023.

![Edit_site_pool.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151798088477.png)

**To edit the bandwidth for a site with a Pooled license:**

1. From the navigation pane, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > License**.
3. Define the Pooled licenses for the site:
  1. In **License Type** select **Pooled license**.
  2. In **License**, select the Pooled license from the region for the site's **Country**.
  3. Set the **Allocate Bandwidth** for the site.

The amount of available bandwidth for the Pooled license is shown as the **Max** bandwidth for the site.
  4. Click **Add**. The bandwidth pool is added to the site.
4. Repeat step 3 to add bandwidth pools from other Pooled licenses in the same region to the site.
5. Click **Save**. The Pooled license for the site bandwidth is updated.

## Changing License Types

You can change the bandwidth license type for a site from using a Site license to a Pooled license or the opposite. If you had Site licenses and switched to Pooled when you renewed your license, Cato gives you 30 days after the Site licenses expire to migrate your sites to the pooled license.

There is no impact to the site traffic (no downtime) when you change the site bandwidth settings or assign a new license type to a site.

However, if you save a site to the Unassigned state, the site is disabled and disconnects from the Cato Cloud.

**To change the license type for a site:**

1. From the navigation pane, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > License**.
3. Make these changes:
  1. To change from a Site license to Pooled license, perform these steps:
    1. In **License Type** change **Site license** to **Pooled license**.
    2. In the confirmation window, click **Yes, Continue**.
    3. In **License**, select the Pooled license from the region for the site's **Country**.
    4. Set the **Allocate Bandwidth** for the site.

The amount of available bandwidth for the Pooled license is shown as the **Max** bandwidth for the site.
    5. Click **Add**. The bandwidth pool is added to the site.
  2. To change from a Pooled license to a Site license, perform these steps:
    1. In **License Type** change **Pooled license** to **Site license**.
    2. In the confirmation window, click **Yes, Continue**.
    3. In **License**, select the site license.
4. Click **Save**. The license type for the site is now changed.

## Allocating a Site License to a Different Site

In some situations, it's necessary to unassign the bandwidth license for a site so you can assign it to a different site. When a site is unassigned and has no license, it's disconnected from the Cato Cloud and doesn't pass traffic.

Before removing a license from a site, the site must be disabled.

**To allocate a license to a different site:**

1. From the navigation pane, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > License**.
3. In the **Allocate Bandwidth** section set the **License** to **Unassigned**.
4. In the confirmation window, click **OK**.
5. Click **Save**. The license is removed from the site.
6. Select a different site, and in the **Allocate Bandwidth** section, assign the **License** to the site.
7. Click **Save**. The license is assigned to the different site.
