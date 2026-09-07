---
title: "Cloud Interconnect for Azure Public Cloud"
slug: "cloud-interconnect-for-azure-public-cloud"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/cloud-interconnect-for-azure-public-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud Interconnect for Azure Public Cloud

This guide explains how to connect Azure to the Cato Cloud via Cloud Interconnect.

For more information about Cloud Interconnect sites, see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).

## Overview of Cloud Interconnect for Azure

Cato supports Active-Passive model only for Cloud Interconnect site with 2 circuits. BGP is used to exchange the routing information between Cato PoPs and Azure edge routers and also to determine the active acting circuit for the site.

**Best Practice:** Cato recommends connecting two circuits in Azure for resiliency and redundancy scenarios. Single circuit configurations are also supported.

### Preparing to Create a Cloud Interconnect Site

When you create an Azure Cloud Interconnect site it's necessary to configure settings for your Azure tenant and the Cato Management Application.

Before you start deploying a Cloud Interconnect site, it is important to verify that the use case for the Primary and Secondary connection is supported by the Cato PoP locations, the cloud providers, and the fabric providers. For more information about preparing for Cloud Interconnect sites, see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).

> [!NOTE]
> Note:
> 
> To deploy the Cloud Interconnect site, Cato provides a seamless configuration using some basic credentials, to create the connection with the fabric provider (e.g Equinix). If your use case is not supported through the automated configuration, contact your account representative (PS/SE/CSM) to deploy the connection manually.

For issues you encounter after deploying your Cloud Interconnect site, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

### High Level Overview of Configuring a Cloud Interconnect Site

| ![image2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193209885.png) |
| --- |

This is a high-level overview of the process to configure Cloud Interconnect for an Azure Cato site:

1. Verify that the use case is supported by the Cato PoP location, the cloud provider, and the fabric provider.
  1. For PoP locations that are immediately available, continue with step 2.
  2. For PoP locations that are available at a future date, wait for Cato to complete the manual backend settings before configuring the Cloud Interconnect site.
2. Create two ExpressRoute circuits in Azure.
  1. If requested by Cato support, send the Service Keys for the created circuits to Cato for provisioning.
3. In the Cato Management Application create a new site and choose site type as Cloud Interconnect.
  1. Configure /30 IP subnets for the primary and secondary circuits for the site.
  2. Configure the Bandwidth per circuit.
4. Configure BGP between Cato and Azure:
  1. In Azure - Once provisioned, configure the ExpressRoute circuit peering and configure the same IP subnets as added to the Cato Management Application.
  2. In the Cato Management Application - Configure BGP peer settings for the primary and secondary circuits. (Cato automatically prefers the primary peer’s metrics)
5. Connect your Azure Virtual Network Gateway to the primary and secondary ExpressRoute circuits.
6. Test connectivity with your new site.

Below is a low-level example topology of an Azure cloud environment connected to Cato via Cloud Interconnect.

![AzureHighLevel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474239877149.png)

## Configuring the Settings in the Azure Account

This section describes how to configure the settings for an Azure data center so it can connect to the Cloud Interconnect site in your Cato account.

**To configure Azure settings for the** **Cloud Interconnect** **site:**

1. In Azure, create a new ExpressRoute circuit under **ExpressRoute Circuits > Create**.
2. Under **Basics**, select the Resource Group and region of instance.

![CreateExpressRoute.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474224466461.png)
3. In the **Configuration** tab, configure these settings:
  1. Select the **Port Type** as **provider**, and select a Cloud Interconnect Provider from the **Provider** dropdown list.

**Note:** The currently supported provider is **EquinixCloud Exchange (ECX).** Additional providers will be supported in the future.
  2. In **Peering Location**, select the same location as the PoP to which you are connecting.

> [!NOTE]
> Note:
> 
> If your Azure instance is located in US East or US East 2, select Washington DC as your peering connection.
  3. **Bandwidth:** Select the bandwidth aligned with your Cato license.
  4. **SKU:** Select **Standard** or **Premium**.

Premium allows connecting a high number of VNets to the circuit while Standard is limited to **10 Virtual Networks**.
  5. **Billing Model Metered:** is a per-consumption basis cost analysis while **unlimited** is a fixed monthly fee for this circuit.

**Note:** Changing the billing model from **Unlimited** to **Metered** is NOT supported by Azure. However, you can change from **Metered** to **Unlimited** at any time.

![CreateExpressRoute_config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193289373.png)
  6. Review and click **Create** the ExpressRoute circuit.
4. Once the ExpressRoute circuit is deployed successfully, it will appear as **Unprovisioned**. At this stage it is not possible to configure the circuits peering until they are completely provisioned by the **Service Provider**. (I.e. Equinix)

![unprovisioned.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474210793885.png)

To complete the provisioning process the Cloud Interconnect datacenter service provider requires the unique **Service Key** generated by Azure for each ExpressRoute circuit. (Seen in the **Overview** page)
  1. Copy the **Service Key**. You will need it when using the automated connection wizard in the Cato Management Application. If you are creating the connection manually, send the **Service Key** to your Cato representative for provisioning with the service provider.
  2. You **cannot** continue to the next steps of this guide until the provisioning is complete.
5. Once provisioned, the circuit configuration becomes editable and the circuit status on Azure portal will change from **Unprovisioned** to **Provisioned**.

The next step is to associate the ExpressRoute circuit and BGP peering (The following configuration will be completely replicated on the Cato Management Application in the next steps)
  1. Under **Peerings**, these˛ are the options - **Azure private**, **Azure public** and **Microsoft**.

**Azure public** is deprecated for new circuits and **Microsoft** is used for Azure PaaS services. For this circuit we will select **Azure private** (More information is available [here](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-circuit-peerings))
  2. **Peer ASN** – This is the ASN which will be used to represent the Cato side in the Azure configuration. You can use any private ASN for the Cato side (The ‘Peer’ ASN).
  3. **Subnets** – IPv4.
  4. **Primary and secondary subnets** – Unique address spaces are required for the peering, each subnet has to be defined by a /30 notation. As a Microsoft Azure standard, the first usable IP serves as the **peer IP** for the customer’s router while the second IP serves as **Microsoft’s router IP**. (For example, a primary subnet of 172.16.0.0/30 uses 172.16.0.1 as the **Cato router** and 172.16.0.2 as the **MS router**)

Azure requires both a primary and secondary subnet to be configured but Cato uses **only** the primary subnet for each ExpressRoute circuit. (In case of HA configuration)

Therefore, a dummy “fake” secondary subnet is required to satisfy Azure’s requirements but will NOT be used in the Cloud Interconnect peering configurations.

The primary subnet configured here will be used in the Cato Management Application configuration steps as well.
  5. **VLAN ID** – Mandatory field: The same settings as the VLAN ID configured in the Cato Management Application by Cato’s team. This VLAN ID is denoted in all parties for the connection – The cloud provider, Equinix colocation and the Cato PoP. This VLAN ID will be decided by Cato and has to be configured the same for your cloud providers peering, if required.

### **Linking a VNet in Azure to the ExpressRoute Circuit**

Once the circuit is provisioned, what remains is connecting resources to the ExpressRoute circuit and establishing connectivity between Azure and the Cato Management Application.

This section covers the former, if you wish to establish connectivity with the Cato Management Application first please skip to [Completing the Cloud Interconnect Configuration](/v1/docs/cloud-interconnect-for-azure-public-cloud#completing-the-cloud-interconnect-configuration).

**Limitations for Linking an Azure VNet with an ExpressRoute Circuit**

- According to Azure, deploying a VNet Gateway may take up to ~45 minutes.
- Make sure to avoid associating network security groups with the Gateway subnet, this may cause the VNet Gateway to stop functioning.
- VNets connected to an ExpressRoute can communicate with one another by default. Microsoft recommends to use VNet Peering.
- The number of address spaces advertised from the local or peered virtual networks needs to be equal to or less than 1,000.
- With a **Standard** ExpressRoute circuit SKU, you can link up to 10 virtual networks. (VNets) All virtual networks must be in the same cloud region while a **Premium** ExpressRoute circuit allows more than 10 VNets in multiple cloud regions. (The SKU per circuit can be edited in the circuit’s Configuration page)

![SKU_standard.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474201174941.png)

Before the ExpressRoute circuit can be linked you **must** create a Subnet Gateway and a Virtual Network Gateway or have pre-existing ones available. More on how to do this can be found [here](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-howto-add-gateway-portal-resource-manager) in Azure’s official documentation.

**To link a Virtual Network Gateway:**

1. On the ExpressRoute circuit page go to **Connections > Add**.
2. In the **Create connection** page, select Connection type as **ExpressRoute** along with a given name and region and select **Next**.

![CreateConnection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474215470109.png)
3. Select the Gateway to link under **Virtual Network Gateway** and select your provisioned circuit under **ExpressRoute Circuit**.
4. The connection now appears under the circuit information.

![Connection_done.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474201253149.png)

## Creating the Cloud Interconnect Site

In the Cato Management Application, create a new site for the Cloud Interconnect provider.

This article assumes that you are creating an HA Active-Passive Cloud Interconnect site. If you are creating a single circuit Cloud Interconnect site, please create only one primary ExpressRoute Circuit. (Only recommended for testing purposes)

For an Azure Cloud Interconnect site, we recommend that you create the site at the same time that you send the initial request for provisioning. This lets you set up the Cato configuration for this site more quickly.

**To create the** **Cloud Interconnect** **site:**

1. In the Cato Management Application, under **Network > Sites**, click **New** to create a new site.
2. Select the **Connection Type** as **Cloud Interconnect** and define the settings for the site.

| ![image8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474201281693.png) |
| --- |
3. Click **Apply**, and then click **Save**.
4. Select the new site and go to Site Configuration > Cloud Interconnect and click **New Connection**.

> [!NOTE]
> Note:
> 
> For HA deployments, make sure to create the Primary connection first.

![azure-cross-connect.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474201304477.png)

## Completing the Cloud Interconnect Configuration

After creating the Express Route, continue with the Cloud Interconnect site configuration you started above.

![azure-cross-connect.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474201304477.png)

1. Under **Azure Express Route Configuration**, enter your Azure Express Route Service Key that you created.
2. Under **Validate Your Connection**, click **Validate**. The Bandwidth and Azure Peering Location are automatically populated.
3. Click **Apply**.

After the connection is established, proceed to configure BGP.

### Defining the BGP Settings for the Site

This section explains how to define the BGP session on top of the existing private peering connection.

The cross-connect site is shown in the **Connected** state when at least one BGP peer is reachable, regardless of the provisioning status with your cloud provider.

BGP establishment is the sole indicator of site connectivity. BGP also allows for determining routing exchange and tunnel failover.

**To configure the BGP settings for the** **Cloud Interconnect** **site:**

1. Configure the same settings in the BGP tab as in the Cloud Interconnect site configuration. For each circuit, go to **Site Configuration > BGP** and click **New**.
2. Under ASN Settings configure the Cato ASN as the value of your choice (make sure it matches the Peer ASN previously configured on the Azure ExpressRoute configuration page)
3. Configure the **Peer** ASN as **12076**. This is a reserved ASN notation used by Azure for ExpressRoute circuits.
4. Under **IP** settings configure the **Peer** IP. This is the same IP as configured in the Cloud Interconnect settings as **Site**. (This IP represents the cloud provider peer IP.)

The **Cato** IP is automatically selected based on the **Cloud Interconnect** settings.

| ![image10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193516829.png) |
| --- |
5. Define the BGP routing policy - It is possible to manipulate the routes advertisement policy for each peer.

We recommend that there be equal policies for both peers in a Cloud Interconnect site to avoid routing discrepancies.
  1. The **Advertise** options let you configure how the site advertises the BGP routes for this neighbor.
    - **Default route** - The site advertises a default route (0/0) to BGP neighbors. The neighbors can send all traffic to this default route, even if it is not in the routing table. You can add BGP community tags to the default route. For more about BGP communities, see [Working with BGP Filtering](/v1/docs/working-with-bgp-filtering).
    - **All routes** - The site advertises the internal routing table for the entire account to the BGP neighbor. These routes include static and floating ranges, in addition to routes that are learned from other peers in this site and across your network. This option is often enabled to send the WAN traffic to the BGP neighbor.

**Note:** The entire range of SDP users is advertised to the BGP peer as a single route.
    - **Summary routes** - The site advertising a summary route instead of multiple unique routes, BGP peers can simplify their forwarding decisions and minimize the computational resources required for route lookup. See, [Working with BGP Summary Routes](/v1/docs/working-with-bgp-summary-routes).
  2. In the **Accept** section, select whether the site accepts or drops the dynamic IP addresses that are published by this neighbor. When you select a Drop option, you are limiting the dynamic propagation from this BGP neighbor. For more information about lists of BGP routes, see [Working with BGP Filtering](/v1/docs/working-with-bgp-filtering).

For example, in deployments that use AWS Direct Connect, BGP is required but you do not want to accept the AWS dynamic addresses. In these deployments, we recommend that you select **Drop All**.
  3. In the **NAT** section, select **Perform Hide SNAT** for the site to perform SNAT to all IPs and the traffic is translated to the LAN IP address.

![BGP_Policy_options.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474224714525.png)
6. Configure the **Additional Settings** for the BGP routes:

| ![image12.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193556253.png) |
| --- |
  1. **MD5** – An additional layer of security. This field is **mandatory.** (In Azure this is the Shared Key attribute)
  2. **Metric** – Peer priority may be changed.

The expected configuration profile is to have a better metric for the primary peer than the secondary peer.
  3. **Hold time** and **Keepalive interval** values.
  4. **Track > Email Notification** – Optional alerts for BGP connectivity changes.
7. Click **Apply**.

The Cloud Interconnect site is configured. Verify that the site is working correctly, see below [Monitoring and Testing Connectivity for the Cloud Interconnect Site](/v1/docs/cloud-interconnect-for-azure-public-cloud#monitoring-and-testing-connectivity-for-the-cloud-interconnect-site).

#### Sample BGP Policy for Cloud Interconnect Site

See the following example of two peers in the supported Active-Passive configuration with Cato. (Primary peer metric is 90, secondary peer metric is 100)

| ![image13.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474211036573.png) |
| --- |

## Monitoring and Testing Connectivity for the Cloud Interconnect Site

Now that the site setup is complete, let's review how the connection can be tested and monitored.

Cato provides multiple tools to help you monitor your Cloud Interconnect site and troubleshoot any potential issues, including:

### Test Connectivity Tool

You can test the point-to-point Cloud Interconnect IP reachability of each circuit by using the **Test Connectivity** tool.

The **Test Connectivity** tool in **Site Configuration > Cloud Interconnect** sends ICMP probes from the Cato PoP IP to the site remote IP of either the primary or secondary connection.

These are the results of the ICMP probes:

- Success - Test executed successfully
- Error - Test was not executed. (Test timed out by the Cato PoP or unable to be executed)
- Failed - Test performed successfully with no response from the remote peer IP

### LAN Monitoring

You can use the [LAN Monitoring](/v1/docs/configuring-lan-monitoring-for-a-site) feature to:

- Perform continuous ICMP probing from the Cato PoP to the primary circuit remote IP.

**Note:** LAN Monitoring only monitors the primary circuit for the Cloud Interconnect site.
- Hosts liveliness state changes for instances within the Cloud Provider network.

It is possible to set custom thresholds and ICMP Intervals and define email notifications to a mailing list upon meeting these thresholds.

| ![image16.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474240310813.png) |
| --- |

This is an example of an email notification for LAN Monitoring:

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474201446557.png)

### BGP Status

In Site Configuration > BGP, the **Show BGP Status** confirms the connectivity of each circuit.

The status outputs granular information on the subnets learned, advertised, and additional data on the BGP peers.

Sample of BGP status output:

| ![image15.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193656605.png) |
| --- |

#### BGP Email Notifications

For each peer, we recommend configuring BGP neighbor status change notifications. Email Notifications are sent directly to an admin mailing list upon a BGP peer connection state change.

Configure email notifications in **Site Configuration > BGP > BGP Neighbor > Additional Settings > Track**.

Select the **Frequency** of alerting and **Mailing List**.

Cato allows for the following Frequency configuration:

- **Immediate** - Notification sent to recipients for every occurrence
- **Hourly** - Send notification with the first occurrence. Do not send additional emails if there are more occurrences within an hour.
- **Daily** - Send notification with the first occurrence. Do not send additional ones if there are more occurrences within a day.
- **Weekly** - Send notification with the first occurrence. Do not send additional ones if there are more occurrences within a week.

Sample BGP email notification:

![BGPemail.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474201500573.png)

### Routing Table

The Monitoring > Routing Table screen shows all routes of your account including dynamic routes.

The routing table can be used to determine which tunnel, primary or secondary, is responsible for adverting these routes based on the Next Hop, PoP and Tunnel Metric.

Routes originating from BGP appear as a **Dynamic** routing type. Routes from the Passive circuit’s peer appear as greyed out. The point-to-point subnets of both circuits appear as a **Static** routing type on the routing table.

For example, the following dynamic route 172.29.0.0/24 is advertised from the New York PoP and has a metric of 5 (highest) which is the primary and currently active tunnel.

The same route is advertised by the secondary tunnel on Ashburn PoP as well with a lower metric of 10.

In case the secondary tunnel on Ashburn PoP would become the active tunnel, the routing table would adjust accordingly for this route.

| ![image18.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193698205.png) |
| --- |

The BGP peers are **Static** and have their own routing table entry. This peers server as the **Next Hop** for the **Dynamic** BGP routes advertised behind them. Similarly as other routes, Metric information can be discerned to understand which peer is currently active with a higher metric and through which Cato PoP location.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193735197.png)

### Events

In the **Site Monitoring > Events** screen, Cato aggregates all logged events related to the site.

Key events can be used to analyze a timeline of events such as. You can filter the relevant Events using the following event sub-types:

- **BGP Session** – Notify of BGP session establishment or disconnection. An identified reason for disconnection can be inspected in the expanded event log. (Under the ‘+’ icon)
- **BGP Routing** – BGP route changes such as addition or removal of new routes from the BGP peer.
- **LAN Monitoring** – These events are logged as part of the LAN Monitoring setup you configured. If LAN Monitoring is not set these events would not be logged.

![BGPevent.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474240470685.png)

### Site Network Analytics

Site analytics lets you monitor the site’s traffic and throughput and includes these dashboards:

- **Network Analytics** – Analyze connectivity state changes, number of **Flows**, **Hosts** and **Throughput**.

It is important to remember the Cloud Interconnect site connectivity is based on the BGP peers. If both BGP peers are unreachable, the site is considered **Disconnected**.

![xconn-mbps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193799069.png)
- **Events** - Site events feed.
- **Application Analytics** - This dashboard dissects hosts throughput and application usage. It is possible to add filters such as IP/host, Application, Category, etc...

![AppAnalytics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474211290013.png)
- **Priority Analyzer** - This dashboard allows analyzing QoS distribution over time. (read more about [Priority Analyzer](/v1/docs/analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer))
- **Known Hosts** – A real-time dashboard for hosts behind the site. IP, OS type and Host Activity are among the data points available per host.

![knownHosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193837469.png)
- **Real Time** - This dashboard allows for real-time monitoring of active hosts, throughput, top applications, active QoS and more.

![RealTime.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193865501.png)

## Cloud Interconnect Limitations with Azure

The following is a highlight list of limitations to consider before setting up an Azure Cloud Interconnect site:

- The peering IPs are predetermined – The first usable IP represents the “On-Prem” peer and the consequent IP represents the MS Azure router.
- Each tunnel VLAN ID is assigned by Cato and has to be configured in the Azure settings. Without the Cato assigned VLAN ID the setup would not work.
- When advertising routes, Azure does not have an option to exclude/include routes from the VNet. The whole VNet is advertised.
- ExpressRoute allows advertising up to 1,000 IPv4 prefixes and 100 IPv6 prefixes.
- ExpressRoute allows receiving up to 4,000 prefixes from Cato. (Cato has an option for custom route summarization. If you would like to configure route summarization with BGP, please contact Cato Support)
- ExpressRoute Premium allows for more than 10 VNets attachments in multiple Azure regions and up to 10,000 received prefixes.
  - If the prefix limit is met, Azure tears down the BGP connection until limit capacity is restored.

You may read more on Azure’s [official ExpressRoute documentation](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-faqs).
