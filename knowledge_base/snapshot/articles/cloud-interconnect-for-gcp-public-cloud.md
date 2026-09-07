---
title: "Cloud Interconnect for GCP Public Cloud"
slug: "cloud-interconnect-for-gcp-public-cloud"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/cloud-interconnect-for-gcp-public-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud Interconnect for GCP Public Cloud

This guide explains how to connect Google Cloud Platform (GCP) to the Cato Cloud via Cloud Interconnect.

For more information about Cloud Interconnect sites, see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).

## Overview of Cloud Interconnect for GCP

Cato supports Active-Passive model only for Cloud Interconnect site with 2 circuits. BGP is used to exchange the routing information between Cato PoPs and GCP edge routers and also to determine the active acting circuit for the site.

**Best Practice:** Cato recommends connecting two circuits in GCP for resiliency and redundancy scenarios. Single circuit configurations are also supported.

### Preparing to Create a Cloud Interconnect Site

When you create an GCP Cloud Interconnect site it's necessary to configure settings for your GCP tenant and the Cato Management Application.

Before you start deploying a Cloud Interconnect site, it is important to verify that the use case for the Primary and Secondary connection is supported by the Cato PoP locations, the cloud providers, and the fabric providers. For more information about preparing for Cloud Interconnect sites, see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).

> [!NOTE]
> Note:
> 
> To deploy the Cloud Interconnect site, Cato provides a seamless configuration using some basic credentials, to create the connection with the fabric provider (e.g Equinix). If your use case is not supported through the automated configuration, contact your account representative (PS/SE/CSM) to deploy the connection manually.

For issues you encounter after deploying your Cloud Interconnect site, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

### High Level Overview or Configuring a Cloud Interconnect Site

| ![image2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474240652701.png) |
| --- |

This is a high-level overview of the process to configure Cloud Interconnect for a GCP Cato site:

1. Verify that the use case is supported by the Cato PoP location, the cloud provider, and the fabric provider.
  1. For PoP locations that are immediately available, continue with step 2.
  2. For PoP locations that are available at a future date, wait for Cato to complete the manual backend settings before configuring the Cloud Interconnect site.
2. Create two VLAN Attachment circuits in GCP.
3. In the Cato Management Application create a new site and choose site type as Cloud Interconnect.
  1. Configure /30 IP subnets for the primary and secondary circuits for the site.
  2. Configure the Bandwidth per circuit.
4. Configure BGP between Cato and GCP:
  1. In GCP - Once provisioned, Accept the Direct Connect circuit peering and configure the same IP subnets as added to the Cato Management Application.
  2. In the Cato Management Application - Configure BGP peer settings for the primary and secondary circuits. (Cato automatically prefers the primary peer’s metrics)
5. Connect your GCP Cloud Router to the primary and secondary circuits.
6. Test connectivity with your new site.

Below is a low-level example topology of a Google cloud environment connected to Cato via Cloud Interconnect.

![XconnectGCP_Overview.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474225135517.png)

## Configuring the Settings in the GCP Account

This section describes how to configure the settings for a GCP data center so it can connect to the Cloud Interconnect site in your Cato account.

The diagram below shows the GCP configuration for a Cloud Interconnect site.

![XconnectGCP_GoogleTopology.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474225173021.png)

**To configure the GCP tenant settings for the** **Cloud Interconnect** **site:**

1. In GCP, create a new VLAN Attachment circuit under **Networking > Hybrid Connectivity > Interconnect > Add VLAN Attachment**.

![GCP_step1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474216157853.png)
2. Select **Partner Interconnect Connection** and click **Continue**.

Cato uses GCP’s supported providers for connectivity.

![GCP_step2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474225231517.png)
3. Define the VLAN Attachment settings:
  1. Select **I already have a service provider**.
  2. Under **Redundancy**, select between **Create a redundant pair of VLAN Attachments** to **Create a single VLAN**. (The former is highly recommended. We recommend creating a single VLAN Attachment **only** for testing purposes).
  3. Select the **Network** and **Region** for Cloud Interconnect. This cannot be changed afterwards and is enforced for both VLAN Attachments.
  4. Each VLAN Attachment requires a **Name**, an **MTU** value and a **Cloud Router** to connect to.

The Cloud Router is responsible for connecting your GCP VPC to the Cloud Interconnect site. In a redundant pair environment, both VLAN Attachment use the same Cloud Router. If you do not already have a pre-existing Cloud Router for your connection, please read more [here](https://cloud.google.com/network-connectivity/docs/router/concepts/overview) in Google’s official documentation.

![GCP_step3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474240864669.png)
  5. Click **Create**.
4. Once the VLAN Attachment circuits are deployed successfully, a Pairing Key for each VLAN is automatically generated. Send the the **Service Key** to your Cato representative.

Currently, it is not possible to configure the circuits peering until they are completely provisioned by the **Service Provider**. (e.g. Megaport).

To complete the provisioning process the Cloud Interconnect datacenter provider requires the unique **Pairing Key** generated by GCP for each circuit.

![GCP_step4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474201880989.png)

Note: The provisioning process with service provider may take up to 24 hours to be reflected in the GCP portal.
5. Once provisioned, the circuit configuration becomes editable and an **Activate** button will appear next to the circuit. Click to activate.

![GCP_step5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474194104861.png)

The fields are described below.
  - **Configure BGP** - Configure the Peer ASN to reflect the ASN which will be used to represent the Cato side in the GCP configuration. You can use any private ASN for the Cato side.

Optionally, you may configure **MD5** authentication method.
  - **Bandwidth** – This is the bandwidth as defined by the Service Provider. Only the Service Provider may alter the Bandwidth. If a Bandwidth change is required, please contact your **Cato representative**.
  - **VLAN ID** – The VLAN ID is generated by GCP and represents Google Cloud traffic only. This VLAN ID is decoupled from any traffic on the Cato Cloud.
  - **Cloud Router IP** – This IP represents GCP in the BGP peering.
  - **On-Premises Router IP** – This IP represents Cato in the BGP peering.
  - **Interconnect** – This field represents the service provider vendor and data center location.

Below is an example of two activated VLAN Attachments:

![GCP_example.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474194131229.png)

## Creating the Cloud Interconnect Site

In the Cato Management Application, create a new site for the Cloud Interconnect provider.

This article assumes that you are creating an HA Active-Passive Cloud Interconnect site. If you are creating a single circuit Cloud Interconnect site, please create only one primary Direct Connect Circuit. (Only recommended for testing purposes)

For the Cloud Interconnect site, we recommend that you create the site at the same time that you send the initial request for provisioning. This lets you set up the Cato configuration for this site more quickly.

**To create the** **Cloud Interconnect** **site:**

1. In the CMA, under **Network > Sites**, click **New** to create a new site.
2. Select the **Connection Type** as **Cloud Interconnect** and define the settings for the site.

| ![image8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474240968477.png) |
| --- |
3. Click **Apply**.
4. Select the new site and go to Site Configuration > Cloud Interconnect and click **New Connection**.

![gcp-cross-connect.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202010141.png)
  1. Under **Connection Type**, select **Public Cloud Connection**.
  2. Under **Cloud Provider**, and select **Google Interconnect**.
  3. Under **Cato PoP Location**, select the PoP nearest to the GCP region in which your tenant resides.
  4. Under **Google Interconnect Configuration**, enter your pairing key.
  5. Click **Validate**. The cloud region is automatically populated.
  6. Under **Bandwidth**, enter the value that aligns with your Cato license.
  7. Under **Configure Network Settings**, configure the Subnet and peering private IPs.
  8. Click **Apply**.

After the connection is established, proceed to configure BGP.

### Defining the BGP Settings for the Site

This section explains how to define the BGP session on top of the existing private peering connection.

The cross-connect site is shown in the **Connected** state when at least one BGP peer is reachable, regardless of the provisioning status with your cloud provider.

BGP establishment is the sole indicator of site connectivity. BGP also allows for determining routing exchange and tunnel failover.

**To configure the BGP settings for the** **Cloud Interconnect** **site:**

1. Configure the same settings in the BGP tab as in the Cloud Interconnect site configuration. For each circuit, go to **Site Configuration > BGP** and click **New**.
2. Under ASN Settings configure the Cato ASN as the value of your choice (make sure it matches the Peer ASN previously configured on the GCP VLAN Attachment configuration page)
3. Configure the Peer ASN as **16550**. This is a reserved ASN notation used by GCP for VLAN Attachment circuits.
4. Under **IP** settings configure the **Peer** IP. This is the same IP as configured in the Cloud Interconnect settings as **Site**. (This IP represents the cloud provider peer IP.)

The **Cato** IP is automatically selected based on the **Cloud Interconnect** settings.

| ![image10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474216403229.png) |
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

![BGP_Policy_options.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474216429981.png)
6. Configure the **Additional Settings** for the BGP routes:

| ![image12.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474211716893.png) |
| --- |
  1. MD5 – An additional layer of security. This field is mandatory for Cloud Interconnect.
  2. Metric – Peer priority may be changed.

The expected configuration profile is to set a better metric for the primary peer than the secondary peer.
  3. **Hold time** and **Keepalive interval** values.
  4. **Track > Email Notification** – Optional alerts for BGP connectivity changes.
7. Click **Apply**.

The Cloud Interconnect site is configured. Verify that the site is working correctly, see below [Monitoring and Testing Connectivity for the Cloud Interconnect Site](/v1/docs/cloud-interconnect-for-gcp-public-cloud#monitoring-and-testing-connectivity-for-the-cloud-interconnect-site).

#### Sample BGP Policy for Cloud Interconnect Site

See the following example of two peers in the supported Active-Passive configuration with Cato. (Primary peer metric is 90, secondary peer metric is 100)

| ![image13.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202182685.png) |
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

| ![image16.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202223389.png) |
| --- |

This is an example of an email notification for LAN Monitoring:

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474241178653.png)

### BGP Status

In Site Configuration > BGP, the **Show BGP Status** confirms the connectivity of each circuit.

The status outputs granular information on the subnets learned, advertised, and additional data on the BGP peers.

Sample of BGP status output:

| ![image15.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202265501.png) |
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

![BGPemail.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474228647325.png)

### Routing Table

The Monitoring > Routing Table screen shows all routes of your account including dynamic routes.

The routing table can be used to determine which tunnel, primary or secondary, is responsible for adverting these routes based on the Next Hop, PoP and Tunnel Metric.

Routes originating from BGP appear as a **Dynamic** routing type. Routes from the Passive circuit’s peer appear as greyed out. The point-to-point subnets of both circuits appear as a **Static** routing type on the routing table.

For example, the following dynamic route 172.29.0.0/24 is advertised from the New York PoP and has a metric of 5 (highest) which is the primary and currently active tunnel.

The same route is advertised by the secondary tunnel on Ashburn PoP as well with a lower metric of 10.

In case the secondary tunnel on Ashburn PoP would become the active tunnel, the routing table would adjust accordingly for this route.

| ![image18.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202308125.png) |
| --- |

The BGP peers are **Static** and have their own routing table entry. This peers server as the **Next Hop** for the **Dynamic** BGP routes advertised behind them. Similarly as other routes, Metric information can be discerned to understand which peer is currently active with a higher metric and through which Cato PoP location.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474194505373.png)

### Events

In the **Site Monitoring > Events** screen, Cato aggregates all logged events related to the site.

Key events can be used to analyze a timeline of events such as. You can filter the relevant Events using the following event sub-types:

- **BGP Session** – Notify of BGP session establishment or disconnection. An identified reason for disconnection can be inspected in the expanded event log. (Under the ‘+’ icon)
- **BGP Routing** – BGP route changes such as addition or removal of new routes from the BGP peer.
- **LAN Monitoring** – These events are logged as part of the LAN Monitoring setup you configured. If LAN Monitoring is not set these events would not be logged.

![BGPevent.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474194523293.png)

### Site Network Analytics

Site analytics lets you monitor the site’s traffic and throughput and includes these dashboards:

- **Network Analytics** – Analyze connectivity state changes, number of **Flows**, **Hosts** and **Throughput**.

It is important to remember the Cloud Interconnect site connectivity is based on the BGP peers. If both BGP peers are unreachable, the site is considered **Disconnected**.

![xconn-mbps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474225723165.png)
- **Events** - Site events feed.
- **Application Analytics** - This dashboard dissects hosts throughput and application usage. It is possible to add filters such as IP/host, Application, Category, etc...

![AppAnalytics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474202391837.png)
- **Priority Analyzer** - This dashboard allows analyzing QoS distribution over time. (read more about [Priority Analyzer](/v1/docs/analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer))
- **Known Hosts** – A real-time dashboard for hosts behind the site. IP, OS type and Host Activity are among the data points available per host.

![knownHosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474216720157.png)
- **Real Time** - This dashboard allows for real-time monitoring of active hosts, throughput, top applications, active QoS and more.

![RealTime.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474194596125.png)

## Cloud Interconnect Limitations with GCP

The following is a highlight list of limitations to consider before setting up an GCP Cloud Interconnect site:

- GCP assigns the peering routing IPs for the GCP router and the Cato peer automatically. This can't be modified.
- Bandwidth capacity is assigned from the service provider (e.g. Megaport) and cannot be modified in the GCP console. If a bandwidth change is required, please contact the Cato sales team to update and reflect the new bandwidth value.
- A network VPC is attached to a new Interconnect upon creation and cannot be modified. To change the network the Interconnect must be re-created.
- IPv6 routes exchange is not supported by Interconnect.

You may read more on GCP’s [official Interconnect documentation](https://cloud.google.com/network-connectivity/docs/interconnect/support/faq).
