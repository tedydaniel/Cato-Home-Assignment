---
title: "Working with Analytics for Specific SDP Users"
slug: "working-with-analytics-for-specific-sdp-users"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/working-with-analytics-for-specific-sdp-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Analytics for Specific SDP Users

This article discusses how to show the analytics for an individual SDP user.

## Understanding the Analytics Screen for Cato Clients

The Client analytics graphs in the User Monitoring > Network Analytics screen display analytics and traffic data for a specific SDP user over the time range. The screen also highlights Cato Client connectivity issues for the user.

Each section shows the analytics graphically. You can also hover and the pop-up shows you the absolute values for the data.

For more about showing analytics for all SDP users in your account, see [Showing User Analytics with SDP Users Overview](/v1/docs/showing-user-analytics-with-sdp-users-overview).

Use the time range filter in the top right corner of the screen to display analytics for a specific duration. You can use one of the predefined time ranges, or customize your own time range. To read more, see [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter).

![Client_Analytics_Graphs.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218298715165.png)

The graphs in this screen show the Client data and analytics for the SDP user (where applicable, the data is based on the duration of the time bucket). Upstream traffic is from the Client to the Cato Cloud, and downstream traffic is from the Cato Cloud to the Client.

- **Max Throughput - Upstream** - The maximum upstream Client throughput
- **Max Throughput - Downstream** - The maximum downstream Client throughput
- **Avg Throughput - Upstream** - The average upstream Client throughput
- **Avg Throughput - Downstream** - The average downstream Client throughput
- **Packet Loss - Upstream** - Packet loss percentage for upstream Client traffic
  - **Client Provider Loss** - Upstream packet loss due to the Internet Service Provider (ISP)

This graph shows data for DTLS tunnels, but not for TCP tunnels
- **Packet Loss - Downstream** - Packet loss percentage for downstream Client traffic
  - **Client Provider Loss** - Downstream packet loss due to the ISP

This graph shows data for DTLS tunnels, but not for TCP tunnels
- **Distance** - The round trip time between the Client and the Cato Cloud

The **Distance** graph indicates when the Client connects to a different PoP in the Cato Cloud.

![Distance_Client_Analytics_Graph.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218310035229.png)
- **Tunnel Age** - The total time that the current DTLS tunnel between the Client and the PoP is connected
