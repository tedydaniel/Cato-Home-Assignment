---
title: "Redundant VPN Connection to Oracle Cloud using BGP"
slug: "redundant-vpn-connection-to-oracle-cloud-using-bgp"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/redundant-vpn-connection-to-oracle-cloud-using-bgp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Redundant VPN Connection to Oracle Cloud using BGP

## Redundant VPN Connection to Oracle Cloud using BGP

The procedure in this article shows you how you can set up a redundant VPN connection between the Cato Cloud and the Oracle cloud using a BGP.

**To set up an IKEv1 BGP connection with Oracle Cloud (OCI):**

1. From the Cato Management Application, select **Network > IP Allocation** make sure that your account has two IP addresses that are appropriate to where your OCI Virtual Network resides.

For more information, see [Allocating IP Addresses for the Account](/v1/docs/allocating-ip-addresses-for-the-account).
2. In the **Network > Sites** page, click **New** to create a new site for the OCI.

Make sure that the **Native Range** is the same as the Oracle Cloud VCN’s range.
3. From the OCI portal, create your VCN if it doesn’t already exist.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248106687773.png)
4. From the navigation pane, select **Virtual Cloud Networks**, and click **Create Virtual Cloud Network**.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248136565405.png)
5. Give your VCN a name, a range and click **Create Virtual Cloud Network**.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248136665245.png)
6. Create two Customer-Premises Equipment objects, one for each of the two CATO PoP IP addresses that you allocated in Step 1.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248153629341.png)
  1. Create the first Customer-Premises Equipment object, and configure it with the IP address for the first PoP.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248153711645.png)
  2. Create the second Customer-Premises Equipment object, and configure it with the IP address for the second PoP.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248113285661.png)

There are now two Customer-Premises Equipment objects in your VCN.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248107264285.png)
7. From the left-hand navigation pane, select **Dynamic Routing Gateways** and click **Create a Dynamic Routing Gateway**.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248137115037.png)
8. Enter the **Name** and click **Create Dynamic Routing Gateway**.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248129987741.png)
9. From the left-hand navigation pane, select **IPSec Connections**, and click **Create IPSec Connection**.

You need to create two IPsec Connections.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248122030237.png)
  1. Create an IPSec connection using the first PoP Customer-Premises Equipment object.

Make sure to enter a **Static Toute CIDR** near the bottom of the window. This can match the CATO Mobile VPN network (10.41.0.0/16) to keep things simple and uniform.

> [!NOTE]
> Note:
> 
> Before clicking **Create IPSec Connection**, click the **Show Advanced Options** hyperlink at the bottom of the window.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248107583005.png)
  2. From the **Advanced Options >Tunnel 1** tab, configure these settings:
    1. Enter your own custom **Shared Secret** [32 character limit].
    2. From **Routing Type**, click the **BGP Dynamic Routing** option.
    3. In **BGP ASN**, enter the default CATO ASN of **64515**.
    4. Set a CATO inside tunnel interface (CPE) IP address and an Oracle inside tunnel interface IP address.
    5. Click **Create IPSec Connection**.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248113815325.png)
  3. Repeat the previous two steps above to create the second IPSec connection.

Make sure to use the second PoP Customer-Premises Equipment object.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248107736349.png) ![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248107809693.png)

Your two IPSec connections are in a Lifecycle state of **Provisioning** and can take up to 15 minutes before they are **Available**.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248130412317.png)
10. Save the Oracle Cloud IPSec peer IP addresses for each of the IPSec Connections that you created. You can find these IP addresses when you click on the IPSec connection name to show it’s details.

Ignore the generically labeled tunnel name in the details screen and only the VPN IP address of the tunnel that you specifically configured and labeled is necessary.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248114152221.png)
11. From the Cato Management Application, from the navigation pane click **Network > Sites** and select the site for the Oracle VCN.
  1. From the navigation pane, select **IPsec** and expand the **General** and **Primary** sections.
  2. Set the **Service Type** to **Generic**, and make sure that the CATO PoP Peer IPs match the respective Oracle Cloud peer IPs.

![oracle_ikev1](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248114248733.png)
  3. Make sure that the IP addresses inside the Cato IPsec tunnel is the same as the respective Oracle Cloud peer IP addresses. In Private IPs:
    - The IP address in **Cato** is the same as the IP address in **CPE** in the Oracle Cloud
    - The IP address in **Site** is the same as the IP address in **Oracle** in the Oracle Cloud
  4. Set the **Primary** and **Secondary PSK** settings to match the Oracle Cloud’s **Shared Secret**.
  5. Set your **IKEv1 Phase 1** and Phase 2 Parameters to match the settings in the Oracle Cloud.

In general, you don't need to change the default Cato settings.
  6. Click **Save**.
12. In the Cato Management Application, select **Site Configuration > BGP**.

> [!NOTE]
> Note:
> 
> Make sure to set a higher Metric value on the BGP neighbor for the PoP further away from your Oracle Region. In the example below, a metric of 101 is applied to the BGP Neighbor associated with the Cato New York PoP.
  1. Specify two BGP Neighbors. CATO’s default ASN is already set as 64515. This setting matches what you configured in the **Advanced Options** in the Oracle IPSec Tunnel configuration.
  2. Set the Oracle ASN (the neighbor) to **31898**, and specify the Oracle inside interface IP address as the neighbor. This IP address matches what you defined in the IPSec settings section in step 11 above.
13. Save the settings in the Cato Management Application.
14. In the Oracle Cloud Portal, wait until your IPSec Connections are **Available**.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248114341149.png)
15. You can validate Tunnel and BGP status in both Oracle Cloud and the CATO Management Application.
  1. Validating the Oracle Cloud:

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248138005789.png)![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248130894237.png)
  2. Before updating the routes in the Oracle Cloud, first make sure that your Dynamic Routing Gateway is attached to your Oracle Virtual Cloud Network. Click **Dynamic Routing Gateways** and select your DRG.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248155035293.png)
  3. From the navigation pane, click **Virtual Cloud Networks**.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248138286749.png)
  4. Confirm that your DRG is attached to your VCN. If it is not, attach it now.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248131179421.png)
  5. Update your routing table to send the appropriate traffic over the IPSec connection.

The following screenshots shows how to set the default route over the IPSec connection from Oracle to Cato.

![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248123350173.png)![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248123465245.png)![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248108910749.png)![A screenshot of a cell phone Description automatically generated](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248131528733.png)
