---
title: "Refreshing Cato Socket Hardware"
slug: "refreshing-cato-socket-hardware"
updated: 2026-08-26T12:54:16Z
published: 2026-08-26T12:54:16Z
canonical: "knowledge.catonetworks.com/refreshing-cato-socket-hardware"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Refreshing Cato Socket Hardware

This article explains how to replace Cato Socket hardware as part of the hardware refresh process.

For more about the refresh process and Socket product lifecycle, see these articles:

- [Cato Socket Hardware Refresh Policy](https://support.catonetworks.com/hc/en-us/articles/33217895595549-Cato-Socket-Hardware-Refresh-Policy)
- [Product Lifecycle Notice - End of Support for Cato Socket Hardware](https://support.catonetworks.com/hc/en-us/articles/34050766925597-Product-Lifecycle-Notice-End-of-Support-for-Cato-Socket-Hardware)

Ready to replace to an existing Socket, watch this [video](/v1/docs/refreshing-cato-socket-hardware#replacing-the-existing-socket).

## Overview

Cato may refresh specific Socket hardware models when they approach end-of-support (EOS). This can happen for reasons such as hardware lifecycle maturity, technology innovation, or the introduction of platforms with expanded capabilities. The refresh process helps customers plan and manage hardware replacement in alignment with Cato’s supported service lifecycle.

Customers are eligible for Socket refresh upon renewal. Prior to renewal, your existing install base is reviewed against the Cato [EOS policy](https://support.catonetworks.com/hc/en-us/articles/34050766925597-Product-Lifecycle-Notice-End-of-Support-for-Cato-Socket-Hardware), and when your account receives a quote for renewal, the Cato Customer Experience team also notifies the parties receiving the quote of any Sockets that require a refresh. If there are such Sockets, then upon renewal Cato automatically assigns dedicated Sockets to your account for the refresh process, at no extra cost. These Sockets appear as a refresh Socket order in the Cato Management Application (CMA). After the customer provides the shipping details, Cato ships the replacement Socket and the customer is responsible for physically replacing and installing the Socket hardware at the site.

The [Refresh Start Date](https://support.catonetworks.com/hc/en-us/articles/33217895595549-Cato-Socket-Hardware-Refresh-Policy#h_01KEY8057QK18H15KBF9D4PDWX) generally corresponds with the new subscription renewal date. An email notification is sent 30 days before the Start Date.

For more information about hardware ownership, refresh schedules, costs, refresh windows, and EOS milestones, see [Cato Socket Hardware Refresh Policy](https://support.catonetworks.com/hc/en-us/articles/33217895595549-Cato-Socket-Hardware-Refresh-Policy).

### Socket Models Included in the Refresh

The list of Socket models that the refresh process applies to is available in [this article](https://support.catonetworks.com/hc/en-us/articles/34050766925597-Product-Lifecycle-Notice-End-of-Support-for-Cato-Socket-Hardware). To determine if your account has hardware that may require a refresh, review that article and then view your account Socket inventory in the [Sockets & Accessories](https://support.catonetworks.com/hc/en-us/articles/6409092874013-Using-the-Socket-Assignment-Page) page. The page provides details of the Socket types and specific hardware models in your account. Compare your account hardware models to the list in the article to see if you have hardware that may require a refresh.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-euo0irxx.png)

## Understanding the Socket Refresh Process

This is the high-level workflow for replacing Socket hardware that is being refreshed due to approaching EOS. Further details of the required procedures appear in the following sections.

1. As part of the renewal process, when your account receives a quote for renewal, the Cato Customer Experience team also notifies the parties receiving the quote that one or more Sockets require refresh.
2. Upon renewal, Cato automatically assigns dedicated Sockets to your account for the refresh process. These Sockets appear in the CMA **Account > Sockets & Accessories > Shipping** tab with the **Order Type** of **Refresh**.
3. Once the Sockets for the refresh process appear in the CMA, you provide shipping details in the **Account > Sockets & Accessories > Shipping** tab. If the customer does not provide the shipping details, Cato cannot ship the Sockets.
4. Cato ships the replacement Socket using the standard Socket order fulfillment process.
5. You physically install the Socket and configure it In the CMA as the replacement for the existing Socket at the site.
6. The previous Socket remains available for rollback for 14 days.
7. The previous Socket is deactivated after the rollback period. You can dispose of the Socket. If you need assistance in disposing of the Socket, contact your Cato representative.

## Providing Shipping Details for Refresh Sockets

Replacement Sockets for the refresh appear in the **Account > Sockets & Accessories > Shipping** tab. These Sockets are labeled **Refresh** in the **Order Type** column so you can distinguish them from regular Socket purchases. In the row for the new Socket, complete the shipping details as you would for any new Socket order. Cato uses this information to ship the replacement hardware to the correct location. For more information about providing shipping details, see [Monitoring Socket Shipping](https://support.catonetworks.com/hc/en-us/articles/27131241018525-Monitoring-Socket-Shipping).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-qnzbnb6c.png)

**To provide shipping details for a refresh Socket:**

1. From the navigation menu, select **Account** > **Sockets & Accessories**.
2. Select the **Shipping** tab.
3. Click in the row of the refresh Socket order.
4. Enter the required shipping details. For more about shipping information, see [Monitoring Socket Shipping](https://support.catonetworks.com/hc/en-us/articles/27131241018525-Monitoring-Socket-Shipping).
5. Click **Save**.

## Replacing the Existing Socket

The replacement process depends on whether you’re replacing a single Socket or two Sockets in a high availability (HA) configuration, and whether the site Sockets use add-on cards. The procedures below relate to these different scenarios.

Cato ships the replacement Sockets with a USB flash drive to be used as part of the replacement process. This flash drive contains software that automatically copies connectivity settings from the existing Socket to the replacement Socket. This lets the replacement Socket connect to the Internet and receive its configuration from Cato. After the Socket connects to Cato, you perform a replace action in the Cato Management Application (CMA) to automatically unassign the existing Socket from the site and assign the replacement.

Watch this video for a guided walkthrough for replacing a Socket:

[Embedded content](https://catonetworks.wistia.com/medias/defhq8p130)

#### Prerequisites

- Verify that the existing Socket is connected to Cato and running Socket version 26.0 or higher.
  - To verify the Socket is connected to Cato and to check the Socket version, in the CMA, navigate to **Network > Sites > [site name] > Socket**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-1eqabn38.png)
- Identify the serial numbers of the existing Socket and the replacement Socket before starting the replacement procedure.
  - The serial number is printed on a label on the physical socket device itself, typically on the rear panel or underside of the unit. The following image shows examples of the serial number sticker. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-o0bpr2l8.png) **Important!** If you do not know the serial numbers of the existing Socket and the replacement Socket, you may replace the wrong Socket or assign the replacement Socket to the wrong site.

#### Known Limitations

- The X1500C Socket supports only autonegotiation mode for link negotiation. For more information, see the X1500 Socket Deployment Guide.

### Replacing an Existing Socket with the Replacement Socket

Use this procedure to replace an existing site Socket with the replacement refresh Socket.

If the existing Socket uses an add-on card, see below Replacing an X1700A Socket with an Add-On.

If you are replacing Sockets for a High Availability (HA) site, see below Replacing a Socket in an HA Site.

**Note**: For a single Socket site, downtime for this procedure is up to 30 minutes. For HA sites, failover is expected during the process and no downtime is anticipated.

**To replace an existing Socket with the replacement Socket:**

1. Unbox the replacement Socket. If rack mounting is required, see the relevant [Socket deployment guide](https://support.catonetworks.com/hc/en-us/articles/360001679717-Cato-Socket-Deployment-Guides-and-Data-Sheets).
2. Connect the power supply and power on the replacement Socket. Wait 3 minutes for the Socket to boot. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-ny78ci82.png)
3. Insert the USB flash drive shipped with the replacement into any of the USB ports on the **existing** Socket. See the images below for location of the USB ports. **Note:** The existing Socket must be connected to Cato. See above, Prerequisites. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-9c5o2qq5.png)
4. Wait 3 minutes. The connectivity settings are copied to the USB drive.
5. Remove the USB flash drive.
6. Insert the USB flash drive into any of the USB ports on the replacement Socket. See the images below for location of the USB ports. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-bt8iqbgl.png)
7. Wait 3 minutes. The connectivity settings are copied to the replacement Socket.
8. Remove the USB flash drive.
9. Move each network cable (LAN and WAN) from the existing Socket to the corresponding port on the replacement Socket. **Note:** To avoid potential issues, use the same Internet cables that were connected to the existing Socket. The following images show sample cabling configurations. Your configuration may differ. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-ppysgnn7.png)
10. Wait until the Socket connects to the Cato Cloud and completes any required version update and configuration. When this process completes, a notification appears in the CMA notification area (see the following image). This process may take up to 20 minutes. **If no notification appears in the CMA after 30 minutes, contact Support**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-btc6droi.png)
11. In the **Account > Sockets & Accessories > Socket Assignment** page, identify the row of the replacement Socket based on the **Serial Number**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-epv6wvj1.png)
12. In the **Account > Sockets & Accessories > Socket Assignment** page, in the row of the replacement Socket, click **Assign**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-0qqdf8xc.png)
13. In the **Assign Socket** window, select the site for the Socket. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-8u0kmc2v.png)
14. Select **Replace current Socket**.
15. Click **OK**. The existing Socket is unassigned from the site and the replacement is assigned to it. The replacement Socket appears in the **Network > Sites > [site name] > Socket** page as connected. **Note:** For Sockets with add-ons, the **Replace current Socket** action automatically configures the add-on type in the CMA to match the add-on card in the replacement Socket.

### Replacing an X1700A Socket with an Add-On

This section describes the procedure for replacing an X1700A Socket with an add-on card.

#### Understanding X1700C Add-On Replacements

When Cato ships a replacement X1700C Socket for an X1700A Socket with an add-on, the shipment includes a new add-on card to be used in the replacement Socket. This replacement add-on may not be identical to the existing add-on. Cato ships a supported X1700C add-on that provides equivalent or expanded connectivity.

The following changes may apply:

- Existing 2-port copper add-ons are replaced with 4-port copper add-ons
- Existing 4-port copper add-ons are replaced with fiber add-ons, and Cato includes copper SFPs to maintain copper connectivity
- Existing 4x10G supported add-ons are replaced with an equivalent add-on type

Use the new add-on when you install the replacement X1700C Socket.

**To replace an X1700 Socket with add-on:**

1. Unbox the replacement Socket and, with the power off, install the add-on card shipped with the Socket. The add-on card should be installed in the same slot as the add-on in the existing Socket.
2. Connect the power supply and power up the replacement Socket. Wait for 3 minutes for the Socket to boot.
3. Continue with Step 3 in the procedure above in the section Replacing a Socket with the Refresh Replacement.

### Replacing a Socket in an HA Site

For HA sites, first identify the site’s primary and secondary Sockets. You can identify a Socket as primary or secondary by its serial number (S/N) as shown in the **Network > Sites > [site name] > Socket** page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-8aueklf3.png)

To identify the corresponding physical Socket, check the sticker showing the serial number. The sticker may appear on the rear panel or underside of the Socket. The images below show Socket serial number stickers.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-rjjct9x8.png)

After identifying the Sockets, replace the secondary Socket first using the procedure described above in the section Replacing a Socket with the Refresh Replacement, with the following addition to step 12:

- When the **Assign Socket** pop-up appears, you must select the Socket being replaced. Use the serial numbers you identified above to select the correct Socket. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-51uasl62.png)

In the CMA, check **Network > Sites > [site name] > Socket** to verify that the replacement secondary Socket is connected, stable, and the site has an HA Ready status. Then repeat the process for the primary Socket. When the procedure is complete, the replacement for the existing secondary Socket will have the role of primary Socket.

## Managing Socket Replacement Issues

If you experience any issues during the Socket replacement process, contact Cato Support.

After you replace the Socket, the previous Socket remains available for rollback for 14 days. This helps you restore the previous hardware if there is an issue with the replacement process. In any case where rollback is required, please contact Support to guide you through the process. During the 14-day period, the previous Socket appears in the **Account > Sockets & Accessories > Socket Assignment** page with **Pending Decommission** status. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/refreshing-cato-socket-hardware-image-6avxusex.png)

After 14 days, the previous Socket is deactivated and can no longer be used for rollback.
