---
title: "Cato Cloud Thresholds and Limits"
slug: "cato-cloud-thresholds-and-limits"
status: "update"
updated: 2026-09-03T07:52:58Z
published: 2026-09-03T07:52:58Z
canonical: "knowledge.catonetworks.com/cato-cloud-thresholds-and-limits"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Cloud Thresholds and Limits

This article provides a list of the main default thresholds and limitations for various features and capabilities available for use in the Cato Cloud.

These limits are designed to support the Cato best practices to ensure the reliability and performance of the service. If there is a requirement to increase a threshold or limit, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

For more information about API limits, see [Understanding Cato API Rate Limiting](/v1/docs/understanding-cato-api-rate-limiting).

For more about working with PoPs located in China, see [Understanding Cato Networking in China](/v1/docs/understanding-cato-networking-in-china).

## Event Thresholds and Limits

### Event Limits

| **Feature** | **Limit** |
| --- | --- |
| Event | 2,500,000 events/hour* |
| Events CSV export | 250,000 events per export |
| eventsFeed API | see [Understanding Cato API Rate Limiting](/v1/docs/understanding-cato-api-rate-limiting) |

*Dependent on DPA agreement:

- For accounts operating under DPA 2021, the Event limit is 2,500,000 events/hour per event sub-type.
- DPA 2023 includes a bundled Event limit of 2,500,000 events/hour which can be extended by licensing additional Data Units (each Data Unit provides 2,500,000 events/hour). For more information, see [Guide to Cato Data Lake](/v1/docs/guide-to-cato-data-lake).

### Event Discovery Search

The Event Discovery tool allows admins to search and analyze the account events for a maximum time frame of 3 months. The Usage Analytics tool for exploring and analyzing usage statistics supports a maximum time frame of 31 Days

## Alert Limits

### Alert Limits per Alert Type

| **Limit** | **Alert Type** |
| --- | --- |
| 50 alerts per hour per alert sub-type | All alert types not specified below (default) |
| 2000 alerts per hour per alert sub-type | - SESSION_PASSIVE_DISCONNECTED - SESSION_PASSIVE_CONNECTED - SESSION_DISCONNECTED - SESSION_CONNECTED - XDR_NOTIFICATION |

## Supported Encryption Algorithms Based on IPsec Site Bandwidth

For IPsec sites with bandwidth of 100Mbps or more, use only the AES 128 GCM-16 or AES 256 GCM-16 algorithms. Use AES CBC algorithms only on sites with bandwidth less than 100Mbps.

These guidelines reflect that GCM encryption is more efficient and scalable than CBC, enabling better performance and reliability for high-throughput encrypted traffic in the Cato Cloud.

## Supported Throughput for Cato Sites

The Cato Cloud supports site throughput of up to 10Gbps for WAN and Internet links on the X1700B Socket and Cloud Interconnect, which is immediately available in [many PoP locations](/v1/docs/pop-locations-supporting-10gbps).

This section shows the details for the supported throughput for WAN and Internet traffic of different site types.

### Throughput for the Socket Sites

The maximum supported throughput for the Socket Next Gen LAN Firewall (LAN FW) and LAN Threat Prevention (IPS) is based on an app-mix of TCP and UDP applications defined by Cato. For each of the following scenarios, we note the bandwidth in packets per second (PPS) for packets of the sizes shown in the column headers.

| **Model** | **LAN Firewall L4** **(1,450b)** | **LAN Firewall L7** **(1,450b)** | **LAN Threat Prevention (IPS)** **(1,450b)** | **Internet** **(1,300b)** |
| --- | --- | --- | --- | --- |
| **X1500A** | 960 Mbps (70K pps) | 625 Mbps (52K pps) | 625 Mbps (48K pps) | 435 Mbps (56.5K pps) |
| **X1500B** | 2.0 Gbps (320K pps) | 2.0 Gbps (180K pps) | 1.9 Gbps (180K pps) | 1.5 Gbps (200K pps) |
| **X1500C** | 2.0 Gbps (560K pps) | 2.0 Gbps (440K pps) | 2.0 Gbps (440K pps) | 2.0 Gbps (440K pps) |
| **X1600** | 7.87 Gbps (440K pps) | 7.87 Gbps (280K pps) | 3.1 Gbps (280K pps) | 1.88 Gbps (240K pps) |
| **X1700A** | 8.5 Gbps (875K pps) | 8.1 Gbps (835K pps) | 8.1 Gbps (835K pps) | 5.33 Gbps (760K pps) |
| **X1700B** | 12.4 Gbps (1,085K pps) | 11.2 Gbps (1,030K pps) | 10.7 Gbps (990K pps) | 10.2 Gbps (935K pps) |
| **X1700C** | 15.4 Gbps (1,500K pps) | 15.4 Gbps (1,500K pps) | 15.35 Gbps (1,385K pps) | 20.0 Gbps (1,530K pps) |

> [!NOTE]
> Note:
> 
> Performance and throughput are measured under ideal testing conditions based on 1500 packet MTU.

### Throughput for vSocket Sites

- Virtual Sockets (vSockets)
  - Azure:
    - 2 NIC - up to 1 Gbps
    - 3 NIC with accelerated networking - up to 2Gbps
  - Google Cloud Platform (GCP): Up to 2 Gbps
  - Amazon Web Services (AWS) and VMware ESXi: Actual throughput will depend on various factors, including the instance type, network configuration, and environmental conditions in the specific deployment

### Throughput for IPsec and Cloud Interconnect Sites

- Cloud Interconnect: Up to 10Gbps
- IPsec sites
  - IPsec IKEv1 (Cato-initiated): Up to 3 Gbps
  - IPsec IKEv2: Up to 3 Gbps

## Transaction Processing Latency

Transaction processing latency measures the time from when the Cato Single Pass Cloud Engine (SPACE) receives network data packets for a transaction until the complete transaction is received by the client or host. This latency can be up to 10 milliseconds for both decrypted and non-decrypted transactions of up to 1MB of data.

## Cato SDP Client

### Supported Throughput for Cato SDP Clients

The throughput for Cato SDP Clients is influenced by various factors, such as the device's hardware, operating system, system resources, and Internet connectivity. The encryption and encapsulation between the SDP Client and the Cato Cloud may add an overhead of up to 20% of the throughput.

There are some Cato PoP locations where each Client is limited to a maximum throughput. Specifically, throughput for Cato Clients connecting to PoPs located in China and Vietnam is limited to 20Mbps.
