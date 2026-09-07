---
title: "Cloud Interconnect for AWS Public Cloud"
slug: "cloud-interconnect-for-aws-public-cloud"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/cloud-interconnect-for-aws-public-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud Interconnect for AWS Public Cloud

This guide explains how to connect Amazon Web Services (AWS) to the Cato Cloud via Cloud Interconnect.

For more information about Cloud Interconnect sites, see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).

## Overview of Cloud Interconnect for AWS

Cato supports active-passive model only for Cloud Interconnect sites with 2 circuits. BGP is used to exchange the routing information between Cato PoPs and AWS edge routers and also to determine the active acting circuit for the site.

**Best Practice:** Cato recommends connecting two circuits in AWS for resiliency and redundancy scenarios. Single-circuit configurations are also supported.

The diagram below shows the AWS configuration for a Cloud Interconnect site.

![image4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474214481181.png)

- Each VPC has a Virtual Private Gateway that connects to the Direct Connect Gateway using a Virtual Private Gateway Association.
- The Direct Connect Gateway uses a private Virtual Interface to connect to the AWS Direct Connect location.
- There is an AWS Direct Connect connection from the location to the customer data center partner. (such as Equinix)

Depending on the requirements for the AWS data center, it's possible to connect a Transit Gateway instead of a Virtual Private Gateway to the Direct Connect Gateway. For more information, see the AWS documentation about [Transit Gateway Associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html) and [Virtual Private Gateway Associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html).

### Preparing to Create a Cloud Interconnect Site

When you create an AWS Cloud Interconnect site it's necessary to configure settings for your AWS tenant and the Cato Management Application (CMA).

Before you start deploying a Cloud Interconnect site, it is important to verify that the use case for the Primary and Secondary connection is supported by the Cato PoP locations, the cloud providers, and the fabric providers. For more information about preparing for Cloud Interconnect sites, see [Getting Started with Cloud Interconnect Sites](/v1/docs/getting-started-with-cloud-interconnect-sites).

This article assumes that you are creating an HA active-passive Cloud Interconnect site. If you are creating a single-circuit Cloud Interconnect site, please create only one primary Direct Connect Circuit. (Only recommended for testing purposes)

> [!NOTE]
> Note:
> 
> To deploy the Cloud Interconnect site, Cato provides a seamless configuration using some basic credentials, to create the connection with the fabric provider (e.g Equinix). If your use case is not supported through the automated configuration, contact your account representative (PS/SE/CSM) to deploy the connection manually.

For issues you encounter after deploying your Cloud Interconnect site, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

### High-Level Overview of Configuring a Cloud Interconnect Site

![image2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474192602141.png)

This is a high-level overview of the process of configuring Cloud Interconnect for an AWS Cato site:

1. Verify that the use case is supported by the Cato PoP location, the cloud provider, and the fabric provider.
  1. For PoP locations that are immediately available, continue with step 2.
  2. For PoP locations that are available at a future date, wait for Cato to complete the manual backend settings before configuring the Cloud Interconnect site.
2. In the CMA create a new site and choose site type as Cloud Interconnect.
  1. Configure /30 IP subnets for the primary and secondary circuits for the site.
  2. Configure the Bandwidth per circuit.
3. Configure BGP between Cato and AWS:
  1. In AWS - Once provisioned, Accept the Direct Connect circuit peering and configure the same IP subnets as added to the CMA.
  2. In the CMA - Configure BGP peer settings for the primary and secondary circuits. (Cato automatically prefers the primary peer’s metrics)
4. Connect your Direct Connect Gateway to the primary and secondary Direct Connect circuits.
5. Test connectivity with your new site.

Below is a low-level example topology of an Amazon Web Services cloud environment connected to Cato via Cloud Interconnect.:

![image3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474192639005.png)

## Creating the Cloud Interconnect Site

In the CMA, create a new site for the Cloud Interconnect provider.

This article assumes that you are creating an HA Active-Passive Cloud Interconnect site. If you are creating a single-circuit Cloud Interconnect site, please create only one primary Direct Connect Circuit. (Only recommended for testing purposes)

For an AWS Cloud Interconnect site, we recommend that you create the site at the same time that you send the initial request for provisioning. This lets you set up the Cato configuration for this site more quickly.

**To create the** **Cloud Interconnect** **site:**

1. In the CMA, under **Network > Sites**, click **New** to create a new site.
2. Select the **Connection Type** as **Cloud Interconnect** and define the settings for the site.

![image8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474192665885.png)
3. Click **Apply**.
4. Select the new site and go to Site Configuration > Cloud Interconnect and click **New Connection**.

![aws-cross-connect.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200493597.png)
  1. Under **Connection Type**, select **Public Cloud Connection**.
  2. Under **Cloud Provider**, select **AWS Direct Connect** and enter the AWS Account ID.
  3. Under **Cato PoP Location**, select the PoP nearest to the AWS region in which your tenant resides.
  4. Under **Bandwidth**, enter the value that aligns with your Cato license.
  5. Under **Destination Cloud Region**, select the AWS region from which the connection will be made.
  6. Under **Configure Network Settings**, configure the Subnet and peering private IPs.
  7. Click **Apply**.

After the connection is established, navigate to the AWS console.
  8. Under **AWS Direct Connect > Connection**, click **View Details** on the connection you created, and click **Approve**.

Proceed to configure the BGP connection.

![AWS-Cross-Connect-Settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200506525.png)

### Defining the BGP Settings for the Site

This section explains how to define the BGP session in addition to the existing private peering connection.

The Cloud Interconnect site is shown in the **Connected** state when at least one BGP peer is reachable, regardless of the provisioning status with your cloud provider.

BGP establishment is the sole indicator of site connectivity. BGP also allows for determining routing exchange and tunnel failover.

**To configure the BGP settings for the** **Cloud Interconnect** **site:**

1. Configure the same settings in the BGP tab as in the Cloud Interconnect site configuration. For each circuit, go to **Site Configuration > BGP** and click **New**.
2. Under **ASN Settings** configure the **Cato** ASN as the value of your choice (make sure it matches the Peer ASN previously configured on the AWS Virtual Interface configuration page).
3. Configure the **Peer** ASN as your preconfigured private ASN for AWS Direct Connect Gateway.
4. Under **IP** settings configure the **Peer** IP. This is the same IP as configured in the Cloud Interconnect settings as **Site**. (This IP represents the cloud provider peer IP.)

The **Cato** IP is automatically selected based on the **Cloud Interconnect** settings.

| ![image10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200536349.png) |
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

![BGP_Policy_options.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474192763165.png)
6. Configure the **Additional Settings** for the BGP routes:

| ![image12.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474210218397.png) |
| --- |
  1. MD5 – An additional layer of security. This field is mandatory for AWS Direct Connect.

AWS gives you the option to generate your own MD5 value or use their autogenerated MD5 value upon creation of each Virtual Interface.
  2. Metric – Peer priority may be changed.

The expected configuration profile is to have a better metric for the primary peer than the secondary peer.
  3. **Hold time** and **Keepalive interval** values.
  4. **Track > Email Notification** – Optional alerts for BGP connectivity changes.
7. Click **Apply**.

The Cloud Interconnect site is configured. Verify that the site is working correctly, see below [Monitoring and Testing Connectivity for the Cloud Interconnect Site](/v1/docs/cloud-interconnect-for-aws-public-cloud#monitoring-and-testing-connectivity-for-the-cloud-interconnect-site).

#### Sample BGP Policy for Cloud Interconnect Site

See the following example of two peers in the supported Active-Passive configuration with Cato. (Primary peer metric is 90, secondary peer metric is 100)

| ![image13.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200621469.png) |
| --- |

### Cloud Interconnect Site Parameters

After configuring the site, the connection details are available on the Site Configuration > Cloud Interconnect page.

| Column | Description |
| --- | --- |
| Cloud Provider | Provides information about the provider to which you're connected, including: - The region - Account ID - Connection ID |
| Fabric Service | Provides information about the Service Provider to which you're connected, including: - Provider name - VLAN ID - Connection ID - Connection bandwidth |
| PoP Location | Indicates to which PoP you are connected. |
| Network Settings | Provides information about the connection settings behind the tunnel. |
| Connection Status | Provides information about each stage of the connection process. - Connectivity - Indicates if the connection is fully functional. - BGP - Indicates if there is a connection with the BGP peers. This can only occur after a connection to the Cloud Provider and Fabric Service Provider is established. - Cloud Provider - Indicates if a connection to the Cloud Provider is established. - Fabric Service Provider - Indicates if a connection to the Fabric Service Provider is established. |
| Connection | Click **Test Connection** to check the current Connection Status. |

## Configuring the Settings in the AWS Account

This section describes how to configure the settings for an AWS data center so it can connect to the Cloud Interconnect site in your Cato account.

**To configure AWS Direct Connect for the** **Cloud Interconnect** **site:**

1. In AWS, accept the ordered circuits under AWS Direct Connect > Connections. (Once accepted, the connection State appears as **Available**)

![AWS Connections](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474223987869.png)
2. In AWS Direct Connect > Direct Connect Gateways create a new Direct Connect Gateway.
  1. Give it a Name and a private ASN value.

This ASN will be referenced later in the CMA BGP setup as the AWS side.

**Note:** This ASN has to be different than the ASN defined for your Virtual Private Gateway or Transit Gateway.
  2. Select the newly created Direct Connect Gateway and under Gateway Associations click on Associate Gateway.

Here you can select between Virtual Private Gateway(s) or Transit Gateway(s). (Multiple associations are possible but must be of the same gateway type) Allowed Prefixes – If you’d like to customize the prefixes allowed to be advertised to Cato, list them here. Otherwise, leave this field empty.

![image6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474239430173.png)
3. Attach VLAN Interfaces to your Direct Connect gateway: AWS Direct Connect > Virtual Interfaces > Create Virtual Interface.

Here we attach the two provisioned circuits to the Direct Connect gateway.

**Note:** It may take several minutes for the virtual interfaces to change from the Down state to Available.
  1. Select Private or Transit, according to your gateway type.
  2. Give a Name identifier to each Virtual Interface.
  3. In Connection, select each provisioned circuit.
  4. Direct Connect gateway - Select the DCG defined in step #2.
  5. VLAN – Define a unique VLAN for each interface.
  6. BGP ASN – This is the BGP for the Cato side. (One ASN for both circuits)
  7. Your Router Peer IP – A /30 IP representing the Cato peer per circuit
  8. Amazon Router Peer IP – An IP in the same /30 subnet as above per each circuit.
  9. BGP Authentication Key – MD5 authentication layer for each interface. AWS allows you to define the key on your own OR allow AWS to randomly generate a key for you.
  10. Jumbo MTU – Not supported.
4. Once configured, you should have a Direct Connect gateway in the following state with two Virtual Interfaces.

![image7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200733725.png)

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

| ![image16.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474192929821.png) |
| --- |

This is an example of an email notification for LAN Monitoring:

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474192951069.png)

### BGP Status

In Site Configuration > BGP, the **Show BGP Status** confirms the connectivity of each circuit.

The status outputs granular information on the subnets learned, advertised, and additional data on the BGP peers.

Sample of BGP status output:

| ![image15.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200804509.png) |
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

![BGPemail.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200828829.png)

### Routing Table

The Monitoring > Routing Table screen shows all routes of your account including dynamic routes.

The routing table can be used to determine which tunnel, primary or secondary, is responsible for adverting these routes based on the Next Hop, PoP and Tunnel Metric.

Routes originating from BGP appear as a **Dynamic** routing type. Routes from the Passive circuit’s peer appear as greyed out. The point-to-point subnets of both circuits appear as a **Static** routing type on the routing table.

For example, the following dynamic route 172.29.0.0/24 is advertised from the New York PoP and has a metric of 5 (highest) which is the primary and currently active tunnel.

The same route is advertised by the secondary tunnel on Ashburn PoP as well with a lower metric of 10.

In case the secondary tunnel on Ashburn PoP would become the active tunnel, the routing table would adjust accordingly for this route.

| ![image18.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474239635741.png) |
| --- |

The BGP peers are **Static** and have their own routing table entry. This peers server as the **Next Hop** for the **Dynamic** BGP routes advertised behind them. Similarly as other routes, Metric information can be discerned to understand which peer is currently active with a higher metric and through which Cato PoP location.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200890397.png)

### Events

In the **Site Monitoring > Events** screen, Cato aggregates all logged events related to the site.

Key events can be used to analyze a timeline of events such as. You can filter the relevant Events using the following event sub-types:

- **BGP Session** – Notify of BGP session establishment or disconnection. An identified reason for disconnection can be inspected in the expanded event log. (Under the ‘+’ icon)
- **BGP Routing** – BGP route changes such as addition or removal of new routes from the BGP peer.
- **LAN Monitoring** – These events are logged as part of the LAN Monitoring setup you configured. If LAN Monitoring is not set these events would not be logged.

![BGPevent.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474215122973.png)

### Site Network Analytics

Site analytics lets you monitor the site’s traffic and throughput and includes these dashboards:

- **Network Analytics** – Analyze connectivity state changes, number of **Flows**, **Hosts** and **Throughput**.

It is important to remember the Cloud Interconnect site connectivity is based on the BGP peers. If both BGP peers are unreachable, the site is considered **Disconnected**.

![xconn-mbps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474200934557.png)
- **Events** - Site events feed.
- **Application Analytics** - This dashboard dissects hosts throughput and application usage. It is possible to add filters such as IP/host, Application, Category, etc...

![AppAnalytics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474239746717.png)
- **Priority Analyzer** - This dashboard allows analyzing QoS distribution over time. (read more about [Priority Analyzer](/v1/docs/analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer))
- **Known Hosts** – A real-time dashboard for hosts behind the site. IP, OS type and Host Activity are among the data points available per host.

![knownHosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474239778461.png)
- **Real Time** - This dashboard allows for real-time monitoring of active hosts, throughput, top applications, active QoS and more.

![RealTime.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33474193187101.png)

## Cloud Interconnect Limitations with AWS

The following is a highlight list of limitations to consider before setting up an AWS Cloud Interconnect site:

- AWS assigns AWS router IP, Cato peer IP and MD5 key automatically. (You may opt to customize these values manually)
- Direct Connect interfaces may receive up to 100 route advertisements over BGP. (Cato has an option for custom route summarization. If you would like to configure route summarization with BGP, please contact Cato [Support](https://support.catonetworks.com/hc/en-us/requests/new).

You may read more on AWS’s [official Direct Connect documentation](https://aws.amazon.com/directconnect/faqs/).
