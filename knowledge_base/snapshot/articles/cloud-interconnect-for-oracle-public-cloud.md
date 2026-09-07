---
title: "Cloud Interconnect for Oracle Public Cloud"
slug: "cloud-interconnect-for-oracle-public-cloud"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/cloud-interconnect-for-oracle-public-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud Interconnect for Oracle Public Cloud

This guide explains how to connect Oracle Cloud Infrastructure (OCI) to the Cato Cloud via Cloud Interconnect.

For more information about Cloud Interconnect sites, see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).

## Overview of Cloud Interconnect for OCI

Cato supports Active-Passive model only for a Cloud Interconnect site with 2 circuits. BGP is used to exchange the routing information between Cato PoPs and OCI edge routers and also to determine the active acting circuit for the site. Cato will advise which FastConnect partner to use for a Cloud Interconnect site.

**Best Practice:** Cato recommends connecting two circuits in OCI for resiliency and redundancy scenarios. Single circuit configurations are also supported.

### Preparing to Create a Cloud Interconnect Site

When you create an OCI Cloud Interconnect site it's necessary to configure settings for your OCI tenant and the Cato Management Application.

Before you start deploying a Cloud Interconnect site, it is important to verify that the use case for the Primary and Secondary connection is supported by the Cato PoP locations, the cloud providers, and the fabric providers. For more information about preparing for Cloud Interconnect sites, see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).

> [!NOTE]
> Note:
> 
> To deploy the Cloud Interconnect site, Cato provides a seamless configuration using some basic credentials, to create the connection with the fabric provider (e.g Equinix). If your use case is not supported through the automated configuration, contact your account representative (PS/SE/CSM) to deploy the connection manually.

For issues you encounter after deploying your Cloud Interconnect site, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

### High Level Overview of Configuring a Cloud Interconnect Site

| ![image2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474216774813.png) |
| --- |

This is a high-level overview of the process to configure Cloud Interconnect for a OCI Cato site:

1. Verify that the use case is supported by the Cato PoP location, the cloud provider, and the fabric provider.
  1. For PoP locations that are immediately available, continue with step 2.
  2. For PoP locations that are available at a future date, wait for Cato to complete the manual backend settings before configuring the Cloud Interconnect site.
2. Create two Virtual Circuits in OCI.
3. In the Cato Management Application create a new site and choose site type as **Cloud Interconnect**.
  1. Configure /30 IP subnets for the primary and secondary circuits for the site. This needs to be the same value that you enter in the Customer BGP IPv4 address in OCI.
  2. Configure the bandwidth per circuit.
4. Configure BGP between Cato and OCI:
  1. In the Cato Management Application - Configure BGP peer settings for the primary and secondary circuits. (Cato automatically prefers the primary peer’s metrics)
5. Test connectivity with your new site.

Below is a low-level example topology of an Oracle Cloud environment connected to Cato via Cloud Interconnect.

![OCI_topology.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474216795549.png)

## Configuring the Settings in the OCI Account

This section describes how to configure the settings for an OCI data center so it can connect to the Cloud Interconnect site in your Cato account.

**To configure the OCI tenant settings for the** **Cloud Interconnect** **site:**

1. In OCI, create a new Virtual Circuit under **Networking > Customer Connectivity > FastConnect > Create FastConnect**.
2. In **Connection Type**, select **FastConnect Partner** and click **Next**.

Cato uses OCI’s supported providers for connectivity. (ie. Equinix, Megaport)
3. Define the Virtual Circuit settings:
  1. Select the relevant **Compartment** for this tenant.
  2. Select **Virtual Circuit Type** as the **Private Virtual Circuit**.
  3. Each Virtual Circuit requires a **Dynamic Routing Gateway** to connect to.

The Dynamic Routing Gateway (DRG) is responsible for connecting your OCI VCN to the Cloud Interconnect site. In a redundant pair environment, both Virtual Circuits use the same DRG.

If you do not already have a pre-existing DRG for your connection, please read [more](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm) in Oracle’s documentation.
  4. In **Provisioned Bandwidth** select the bandwidth for this connection.
  5. **Customer BGP IPV4 Address** – Configure a /30 IP address that will be used as the peering IP for Cato.
  6. **Oracle BGP IPV4 Address** – Configure an IP address in the same /30 block as above to be used as Oracle’s peering IP.
  7. **Customer BGP ASN** - This is the ASN which will be used to represent the Cato side in the OCI configuration. You can use any private ASN for the Cato side (the peer ASN).
  8. **MD5** – Required authentication value for an additional layer of security.
  9. **MTU** – Select 1500. Cato does not support jumbo frames
  10. Click **Create**.

![virtual_circuit.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202512541.png)
4. Once the Virtual Circuits are deployed successfully, a OCID Key for each circuit is automatically generated. Send the the **Service Key** to your Cato representative.

Currently, it is not possible to configure the circuits peering until they are completely provisioned by the **Service Provider**. (I.e. Equinix, Megaport).

To complete the provisioning process the Cloud Interconnect datacenter provider requires the unique **OCID Key** generated by OCI for each circuit.

![Connection_created.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202534685.png)

**Note:** The provisioning process with service provider may take up to 24 hours to be reflected in the OCI portal
5. Once provisioned, the circuits will appear as **Provisioned** in the **Lifecycle State** column.

![provisioned.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474228956317.png)

## Creating the Cloud Interconnect Site

In the Cato Management Application, create a new site for the Cloud Interconnect provider.

This article assumes that you are creating an HA Active-Passive Cloud Interconnect site. If you are creating a single circuit Cloud Interconnect site, please create only one primary FastConnect Circuit. (Only recommended for testing purposes)

For the Cloud Interconnect site, we recommend that you create the site at the same time that you send the initial request for provisioning. This lets you set up the Cato configuration for this site more quickly.

**To create the** **Cloud Interconnect** **site:**

1. In the CMA, under **Network > Sites**, click **New** to create a new site.
2. Select the **Connection Type** as **Cloud Interconnect** and define the settings for the site.

![image8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474241566749.png)
3. Click **Apply**.
4. Select the new site and go to **Site Configuration > Cloud Interconnect** and click **New Connection**.
  1. Under **Connection Type**, select **Public Cloud Connection**.
  2. Under **Cloud Provider**, select **OCI FastConnect**.
  3. Under **Cato PoP Location**, select the PoP in the same Oracle Cloud region in which your tenant resides.
  4. Under **Oracle FastConnect Configuration**, enter the OCID.
  5. Click **Validate**. The Bandwidth and Cloud region will be populated.
  6. Under **Configure Network Settings**, and configure the **Primary** and **Secondary** links. Define the **Subnet** and peering private IPs similarly to the previous steps in OCI for each Cloud Interconnect circuit.
  7. Click **Apply**. After creating the connection, you are prompted to configure the BGP settings for the site.

### Defining the BGP Settings for the Site

This section explains how to define the BGP session on top of the existing private peering connection.

The Cloud Interconnect site is shown in the **Connected** state when at least one BGP peer is reachable, regardless of the provisioning status with your cloud provider.

BGP establishment is the sole indicator of site connectivity. BGP also allows for determining routing exchange and tunnel failover.

**To configure the BGP settings for the** **Cloud Interconnect** **site:**

1. For each circuit, go to **Site Configuration > BGP** and click **New**.
2. Under **ASN Settings** configure the Cato ASN as the value of your choice (make sure it matches the **Peer ASN** previously configured on the OCI Virtual Circuit configuration page)
3. Configure the **Peer** ASN as **31898**. This is a reserved ASN notation used by OCI for Virtual Circuits.
4. Under **IP** settings configure the **Peer** IP. This is the same IP as configured in the Cloud Interconnect settings as **Site**. (This IP represents the cloud provider peer IP.)

The **Cato** IP is automatically selected based on the **Cloud Interconnect** settings.

![image10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202607261.png)
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

![BGP_Policy_options.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474217002653.png)
6. Configure the **Additional Settings** for the BGP routes:

![image12.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474241639837.png)
  1. MD5 – An additional layer of security. This field is mandatory for Cloud Interconnect.
  2. Metric – Peer priority may be changed.

The expected configuration profile is to set a better metric for the primary peer than the secondary peer.
  3. **Hold time** and **Keepalive interval** values.
  4. **Track > Email Notification** – Optional alerts for BGP connectivity changes.
7. Click **Apply**.

The Cloud Interconnect site is configured. Verify that the site is working correctly, see below [Monitoring and Testing Connectivity for the Cloud Interconnect Site](/v1/docs/cloud-interconnect-for-oracle-public-cloud#monitoring-and-testing-connectivity-for-the-cloud-interconnect-site).

#### Sample BGP Policy for a Cloud Interconnect Site

See the following example of two peers in the supported Active-Passive configuration with Cato. (Primary peer metric is 90, secondary peer metric is 100)

![image13.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474194927517.png)

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

| ![image16.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474217070237.png) |
| --- |

This is an example of an email notification for LAN Monitoring:

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202727197.png)

### BGP Status

In Site Configuration > BGP, the **Show BGP Status** confirms the connectivity of each circuit.

The status outputs granular information on the subnets learned, advertised, and additional data on the BGP peers.

Sample of BGP status output:

| ![image15.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474194958621.png) |
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

![BGPemail.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474241727645.png)

### Routing Table

The Monitoring > Routing Table screen shows all routes of your account including dynamic routes.

The routing table can be used to determine which tunnel, primary or secondary, is responsible for adverting these routes based on the Next Hop, PoP and Tunnel Metric.

Routes originating from BGP appear as a **Dynamic** routing type. Routes from the Passive circuit’s peer appear as greyed out. The point-to-point subnets of both circuits appear as a **Static** routing type on the routing table.

For example, the following dynamic route 172.29.0.0/24 is advertised from the New York PoP and has a metric of 5 (highest) which is the primary and currently active tunnel.

The same route is advertised by the secondary tunnel on Ashburn PoP as well with a lower metric of 10.

In case the secondary tunnel on Ashburn PoP would become the active tunnel, the routing table would adjust accordingly for this route.

| ![image18.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474245320221.png) |
| --- |

The BGP peers are **Static** and have their own routing table entry. This peers server as the **Next Hop** for the **Dynamic** BGP routes advertised behind them. Similarly as other routes, Metric information can be discerned to understand which peer is currently active with a higher metric and through which Cato PoP location.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474229180317.png)

### Events

In the **Site Monitoring > Events** screen, Cato aggregates all logged events related to the site.

Key events can be used to analyze a timeline of events such as. You can filter the relevant Events using the following event sub-types:

- **BGP Session** – Notify of BGP session establishment or disconnection. An identified reason for disconnection can be inspected in the expanded event log. (Under the ‘+’ icon)
- **BGP Routing** – BGP route changes such as addition or removal of new routes from the BGP peer.
- **LAN Monitoring** – These events are logged as part of the LAN Monitoring setup you configured. If LAN Monitoring is not set these events would not be logged.

![BGPevent.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202784029.png)

### Site Network Analytics

Site analytics lets you monitor the site’s traffic and throughput and includes these dashboards:

- **Network Analytics** – Analyze connectivity state changes, number of **Flows**, **Hosts** and **Throughput**.

It is important to remember the Cloud Interconnect site connectivity is based on the BGP peers. If both BGP peers are unreachable, the site is considered **Disconnected**.

![xconn-mbps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202798237.png)
- **Events** - Site events feed.
- **Application Analytics** - This dashboard dissects hosts throughput and application usage. It is possible to add filters such as IP/host, Application, Category, etc...

![AppAnalytics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474241811357.png)
- **Priority Analyzer** - This dashboard allows analyzing QoS distribution over time. (read more about [Priority Analyzer](/v1/docs/analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer))
- **Known Hosts** – A real-time dashboard for hosts behind the site. IP, OS type and Host Activity are among the data points available per host.

![knownHosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474245400349.png)
- **Real Time** - This dashboard allows for real-time monitoring of active hosts, throughput, top applications, active QoS and more.

![RealTime.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202832925.png)

## Cloud Interconnect Limitations with OCI

The following is a highlight list of limitations to consider before setting up an OCI Cloud Interconnect site:

- When advertising routes, OCI does not have an option to exclude/include routes from the VCN. The whole VCN is advertised.
- OCI allows advertising up to 2,000 prefixes.
- OCI does not offer a way to validate propagated routes from Cato on the Oracle portal. For this, the Cato Management Application’s BGP status feature may be used.
- A virtual circuit can be assigned only 1 Dynamic Routing gateway.
- OCI billing model is based on fixed BW port hours and not data transfer consumption. (Billing begins once a virtual circuit is either provisioned or after 30 days, the earlier of which to be applied.
- If the prefix limit is met, OCI tears down the BGP connection for 60 minutes and re-attempts to establish connection until limit capacity is restored.

You may read more on OCI’s [official FastConnect documentation](https://www.oracle.com/cloud/networking/fastconnect/faq/).
