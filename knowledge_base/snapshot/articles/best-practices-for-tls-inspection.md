---
title: "Best Practices for TLS Inspection"
slug: "best-practices-for-tls-inspection"
tags: ["Best Practices", "Internet Security"]
updated: 2026-06-22T09:27:06Z
published: 2026-06-22T09:27:06Z
canonical: "knowledge.catonetworks.com/best-practices-for-tls-inspection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices for TLS Inspection

## Overview of TLS Inspection

The majority of Internet traffic is encrypted over HTTPS, however malware uses HTTPS as an evasive technique. These kinds of threats can cause damage to your organization data.

Cato Networks provides Transport Layer Security (TLS) inspection for WAN and Internet HTTPS traffic. Cato supports TLS versions 1.1, 1.2, and 1.3. When TLS inspection is activated, the Cato PoPs decrypt the HTTPS traffic and inspect it for malicious content. We recommend that you use TLS inspection for Cato’s threat protection services such as Intrusion Prevention System (IPS), Anti-Malware and Managed Threat Detection and Response (MDR).

This article explains how TLS Inspection provides protection against these kinds of threats and describes best practices for threat protections and TLS traffic.

> [!NOTE]
> Note:
> 
> Due to issues related to certificate pinning, TLS Inspection isn't supported for Android devices.

## Enabling TLS Inspection

Use the Cato Management Application to enable TLS inspection for the entire account. As part of implementing TLS Inspection, you must install the Cato certificate as a root certificate on the end-user hosts and devices. Use the TLS Inspection policy to define rules to inspect or bypass traffic from TLS inspection. When the TLS Inspection is enabled for your account, the out of the box policy is to inspect all HTTPS traffic by default.

### Decrypting Traffic with Cato Certificate

When a client (for example, a web browser) connects to a server, the PoP sends Cato’s certificate to the browser as part of the TLS negotiation. For the client to verify that this certificate is signed by a trusted CA, you must install Cato’s certificate on all of your clients and devices. The certificate is available for download from the Cato Management Application or from the [Client download portal](https://clientdownload.catonetworks.com/). Then the PoP can decrypt the HTTPS traffic and inspect it to detect if there are any security threats.

Installing Cato’s certificate also allows you to use Cato’s block page for HTTPS websites. If TLS traffic is blocked by URL Filtering or Internet Firewall rules, the Cato certificate allows access to Cato’s block page. TLS Inspection isn’t required to block access to HTTPS websites, but if the Cato certificate isn’t installed on your users’ computer, a certificate warning is prompted instead of Cato’s block page. Therefore, we recommend that you install Cato’s certificate on the client devices. For more about the certificate and block pages, see [Certificate Warnings with Blocked HTTPS Websites](/v1/docs/certificate-warnings-with-blocked-https-websites).

### Excluding Items from TLS Inspection

You can exclude specific items from TLS inspection using the unified TLS inspection window. This can include services or destinations that are considered legitimate or trusted. For more about excluding traffic from TLS inspection, see [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account).

**Notes**:

- TLS inspection is bypassed for Android, Linux, and unidentified operating systems. Event logs for these operating systems include the **OS Type** as:
  - OS_ANDROID
  - OS_LINUX
  - OS_UNKNOWN
- Enabling TLS inspection activates the TCP acceleration feature for all TLS traffic. When the TCP acceleration is activated, the PoPs act as proxy servers to inspect the traffic for malicious files and threats. For more information about TCP acceleration, see [Explaining the Cato TCP Acceleration and Best Practices](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices).

## Best Practices for TLS Inspection

### Enabling TLS Inspection to Improve Security

Cato Networks highly recommends that you enable TLS inspection for your account. If you want the full protection of Cato’s advanced security and detection services, it’s important to know that some of these service capabilities can only inspect un-encrypted data. For example, if you don’t use TLS inspection, it reduces the efficiency of security services such as MDR which uses an Automated Threat Hunting System.

Another example is the IPS service that uses signatures-based detection. When TLS inspection is activated, the IPS can apply deep packet inspection and allows additional capabilities on the range of security signatures. And so, it provides better protection for your network.

### How to Handle Applications that Use Certificate Pinning?

Some sites and applications use certificate pinning for security reasons. Certificate pinning forces the client to use a specific certificate to prevent man-in-the-middle attacks. These applications don’t work when the TLS inspection is activated. Therefore, you must add them as a bypass rule within the TLS inspection policy window.

For more information regarding configuring TLS inspection, see [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account).
