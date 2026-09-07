---
title: "Product Update - Aug. 7th, 2023"
slug: "product-update-aug-7th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-aug-7th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Aug. 7th, 2023

## New Features & Enhancements

- **New Policy to Manage DNS Settings for SDP Users**: Over the next few weeks we are gradually rolling out the [DNS Settings Policy](/v1/docs/centralized-management-of-sdp-user-dns-settings-with-the-dns-settings-policy). This policy lets you easily manage custom DNS settings for SDP users and User Groups, for example if they need to use a local private DNS server.
- **Preferred PoP Location Settings and 2nd Tokyo PoP:** In May 2023, Cato launched a second PoP in Tokyo, referred to in the Cato Management Application as **Tokyo_DC2**. This second PoP improved the Cato service scale and resiliency for sites in Japan, and for Tokyo in particular. To benefit from the new PoP we recommend to use the default **Automatic** option for a site’s [Preferred PoP Location settings](/v1/docs/defining-a-preferred-pop-for-a-site). This option allows the Sockets to choose the optimal PoP options for the site for best performance and resiliency.
  - If you have a specific need to configure manual preferred PoP location settings for a site to connect to a PoP in Tokyo, make sure to configure the new **Tokyo_DC2** as the preferred PoP location option. Starting August 6th, 2023, we will temporarily limit the manual configuration options for the primary preferred location to **Tokyo_DC2** only.
  - There’s no impact for existing sites configured with the **Tokyo** PoP as a manual primary preferred PoP location. These sites will continue to use the **Tokyo** PoP option for the primary preferred PoP location.

## Security Updates

- **Application Database:**
  - Added more than 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - StrongDM
- **IPS Signatures:**
  - Malware rueBot (New)
  - Ransomware Underground Team (New)
  - CVE-2023-34960
  - CVE-2023-33246
  - CVE-2023-31689
  - CVE-2023-29357
  - CVE-2023-28343
  - CVE-2023-2825
  - CVE-2023-27997
  - CVE-2023-25135
  - CVE-2020-12641
  - CVE-2015-5317
- **Suspicious Activity Monitoring:**
  - Procdump - Download (New)
  - Execution of Net User Query to Gather Security (New)
  - Executable File Transfer Over SMB With Impersonated Extension (New)
  - Opening Executable in Admin Share (Enhancement)
  - Phishing heuristic (Enhancement)
- **Application Control Policy (CASB):**
  - Enhanced granular actions for the following app:
    - Dropbox: Login

## Knowledge Base Updates

- [Accessing An Untrusted Website Is Blocked Even Though TLS Inspection Is Disabled](/v1/docs/accessing-an-untrusted-website-is-blocked-even-though-tls-inspection-is-disabled)
- [Real-Time Monitoring Shows Imprecise QoS Priority for Traffic](/v1/docs/real-time-monitoring-shows-imprecise-qos-priority-for-traffic)
- [Why Do Connections Destined for the Same Server Receive Different (Block/Allow) Action from Cato?](/v1/docs/traffic-intermittently-fails-to-match-firewall-rules)
- [SSO Authentication for SDP Users with Cato](/v1/docs/sso-authentication-for-users-with-cato)
