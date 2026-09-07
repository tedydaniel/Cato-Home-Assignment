---
title: "Allowlisting Processes and URLs for the Cato Client"
slug: "allowlisting-processes-and-urls-for-the-cato-client"
status: "update"
updated: 2026-08-30T06:51:24Z
published: 2026-08-30T06:51:24Z
canonical: "knowledge.catonetworks.com/allowlisting-processes-and-urls-for-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Allowlisting Processes and URLs for the Cato Client

## Overview

To ensure that the Cato Client can communicate with required Cato services and avoid any impact on Client traffic, allowlist the processes and URLs listed in this article in third-party products and services (such as endpoint security products, firewalls, proxies, etc...).

For more information, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## 

### Understanding Regional CMA Domains

Cato operates the Cato Management Application (CMA) in multiple AWS regions to support data sovereignty and residency requirements. Each Cato account is associated with a CMA region, which provides the control-plane services used to manage the account and communicate configuration and other service information to the Cato Client. For more information, see [this article](/v1/docs/welcome-to-the-cma#cma-global-regions-and-data-residency).

Some URLs required by the Client are global and are shared across all CMA regions. Other URLs are region-specific and use a domain associated with the account's CMA region. To simplify configuration, allowlist the global URLs and all the URLs listed for your CMA region. For example, `sso.ias.catonetworks.com` is a global URL, and `auth.jp1.catonetworks.com` is a local URL for the Japan CMA tenant.

**Note:** The CMA region does **not** determine which Cato Cloud PoPs the Client can connect to. By default, Clients can connect to available PoPs across the Cato Cloud independently of the account's CMA region.

## Allowlisting for All Devices

This section lists URLs and processes that you need to allowlist based on the CMA region for your account.

### Allowlisting for EU CMA Region

- **CMA SSO**
  - `auth.catonetworks.com`

- **CMA SSO / ZTNA Client**
  - `sso.ias.catonetworks.com`
- **General**
  - `c-me.catonetworks.net`
  - `v-me.catonetworks.net`
  - `ipv4only.arpa`
- **Network**
  - `network-segmentation.catonetworks.com`
  - `socket-registration.catonetworks.com`
  - `ip2location.catonetworks.com`
- **Captive Portal**
  - `captiveportal.catonetworks.com`
- **PoP Location IP Ranges**
  - For more information, see the [PoP production guide](https://knowledge.catonetworks.com/v1/docs/production-pop-guide)
- **Ports**
  - UDP port 443
  - UDP port 1337
  - TCP port 443
  - TCP port 1337
- **ZTNA Client SSO**
  - `sso.catonetworks.com`
  - `sso.via.catonetworks.com`
  - `vpn.catonetworks.net`
- **ZTNA Client**
  - `tunnel-api.catonetworks.com`

- **ZTNA Client Control Plane**
  - `client-control-plane.catonetworks.com`
  - `client-registration.catonetworks.com`
- **ZTNA Client Telemetry**
  - `client-telemetry.main.prod.k8s.catonet.works`
- **ZTNA Client Download and Upgrade**
  - `cc2.catonetworks.com`
  - `clients.catonetworks.com`
  - `clients.cdn.catonetworks.com`

### Allowlisting for India Region

- **CMA SSO**
  - `auth.in1.catonetworks.com`

- **CMA SSO / ZTNA Client**
  - `sso.ias.catonetworks.com`
- **General**
  - `c-me.catonetworks.net`
  - `v-me.catonetworks.net`
  - `ipv4only.arpa`
- **Network**
  - `network-segmentation.catonetworks.com`
  - `socket-registration.catonetworks.com`
  - `ip2location.catonetworks.com`
- **Captive Portal**
  - `captiveportal.catonetworks.com`
- **PoP Location IP Ranges**
  - For more information, see the [PoP production guide](https://knowledge.catonetworks.com/v1/docs/production-pop-guide)
- **Ports**
  - UDP port 443
  - UDP port 1337
  - TCP port 443
  - TCP port 1337
- **ZTNA Client SSO**
  - `sso.catonetworks.com`
  - `sso.via.catonetworks.com`
  - `vpn.catonetworks.net`
- **ZTNA Client**
  - `tunnel-api.catonetworks.com`

- **ZTNA Client Control Plane**
  - `client-control-plane.in1.catonetworks.com`
  - `client-registration.in1.catonetworks.com`
- **ZTNA Client Telemetry**
  - `client-telemetry.in1.catonetworks.com`
- **ZTNA Client Download and Upgrade**
  - `clients.catonetworks.com`
  - `clients.cdn.catonetworks.com`
  - `client-upgrade.in1.catonetworks.com`

### Allowlisting for Japan Region

- **CMA SSO**
  - `auth.jp1.catonetworks.com`

- **CMA SSO / ZTNA Client**
  - `sso.ias.catonetworks.com`
- **General**
  - `c-me.catonetworks.net`
  - `v-me.catonetworks.net`
  - `ipv4only.arpa`
- **Network**
  - `network-segmentation.catonetworks.com`
  - `socket-registration.catonetworks.com`
  - `ip2location.catonetworks.com`
- **Captive Portal**
  - `captiveportal.catonetworks.com`
- **PoP Location IP Ranges**
  - For more information, see the [PoP production guide](https://knowledge.catonetworks.com/v1/docs/production-pop-guide)
- **Ports**
  - UDP port 443
  - UDP port 1337
  - TCP port 443
  - TCP port 1337
- **ZTNA Client SSO**
  - `sso.catonetworks.com`
  - `sso.via.catonetworks.com`
  - `vpn.catonetworks.net`
- **ZTNA Client**
  - `tunnel-api.catonetworks.com`

- **ZTNA Client Control Plane**
  - `client-control-plane.jp1.catonetworks.com`
  - `client-registration.jp1.catonetworks.com`
- **ZTNA Client Telemetry**
  - `client-telemetry.jp1.catonetworks.com`
- **ZTNA Client Download and Upgrade**
  - `clients.catonetworks.com`
  - `clients.cdn.catonetworks.com`
  - `client-upgrade.jp1.catonetworks.com`

### Allowlisting for US Region

- **CMA SSO**
  - `auth.us1.catonetworks.com`

- **CMA SSO / ZTNA Client**
  - `sso.ias.catonetworks.com`
- **General**
  - `c-me.catonetworks.net`
  - `v-me.catonetworks.net`
  - `ipv4only.arpa`
- **Network**
  - `network-segmentation.catonetworks.com`
  - `socket-registration.catonetworks.com`
  - `ip2location.catonetworks.com`
- **Captive Portal**
  - `captiveportal.catonetworks.com`
- **PoP Location IP Ranges**
  - For more information, see the [PoP production guide](https://knowledge.catonetworks.com/v1/docs/production-pop-guide)
- **Ports**
  - UDP port 443
  - UDP port 1337
  - TCP port 443
  - TCP port 1337
- **ZTNA Client SSO**
  - `sso.catonetworks.com`
  - `sso.via.catonetworks.com`
  - `vpn.catonetworks.net`
- **ZTNA Client**
  - `tunnel-api.catonetworks.com`

- **ZTNA Client Control Plane**
  - `client-control-plane.us1.catonetworks.com`
  - `client-registration.us1.catonetworks.com`
- **ZTNA Client Telemetry**
  - `client-telemetry.us1.catonetworks.com`
- **ZTNA Client Download and Upgrade**
  - `clients.catonetworks.com`
  - `clients.cdn.catonetworks.com`
  - `client-upgrade.us1.catonetworks.com`

## Windows Operating Systems

The following section lists the processes and URLs for all security endpoint software and solutions for endpoints running Windows operating systems.

- CatoClient.exe
- winvpnclient.cli.exe
- login.microsoftonline.com
- CatoUpgradeHelper.exe
- CatoLogCollector.exe
- LogLevelSetup.exe
- CatoClient.exe.config
- wa_3rd_party_host_32.exe
- wa_3rd_party_host_64.exe
- coresvc.exe
- For accounts that use a third-party proxy (for both HTTP and HTTPS):
  - IP - 85.255.31.1
  - URL - sso.ias.catonetworks.com

**Note:** This is only required when using the embedded browser
- msftconnecttest.com

## 

### DNS Relay for Windows Clients

These are the processes and URLs that you need to allowlist for local firewalls with deployments that use [DNS relay](/v1/docs/working-with-the-dns-relay-service).

- IP - 127.0.0.253
- The Cato Networks DNS service
- The DNS relay process dns-relay.exe

## macOS Operating Systems

The following section lists the processes and URLs for all security endpoint software and solutions for endpoints running macOS.

- Exclude the following folder and all its contents:

`/Library/Application Support/CatoNetworks`
- For accounts that use a third-party proxy (for both HTTP and HTTPS):
  - IP - 85.255.31.1
  - `appleiphonecell.com`
- For accounts that have CrowdStrike installed on devices:
  - `/Library/Application\ Support/CatoNetworks/com.catonetworks.mac.CatoClient.helper`
  - `/Library/Application\ Support/CatoNetworks/CatoNetworksUserAgent`
- For accounts that have SentinelOne installed on devices:
  - `/Library/Application Support/CatoNetworks`
- For Captive Portal detection:
  - 1.1.1.1

## Article Changelog

| Date | Description |
| --- | --- |
| Aug 23, 2026 | - Added [Overview](/v1/docs/allowlisting-processes-and-urls-for-the-cato-client#overview) - Separated URLs per CMA region - Added URL for Captive Portal |
