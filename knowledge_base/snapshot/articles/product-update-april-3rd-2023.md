---
title: "Product Update - April 3rd, 2023"
slug: "product-update-april-3rd-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-april-3rd-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - April 3rd, 2023

## New Features & Enhancements

- **Cato RBI Introduces a New Way to Protect Against Web-Based Threats:** Cato’s [Remote Browser Isolation (RBI)](/v1/docs/securing-browsing-sessions-through-rbi) service provides secure browsing by processing web browsing on a virtualization service and streaming web pages safely to the user's device. All in-browser code is executed remotely and never on the device, keeping it safe from threats such as ransomware and phishing. Instead of blocking websites or showing a warning page, RBI gives admins another option to secure user devices when browsing uncategorized sites.
- **Improved CASB Granularity with Tenant**-**Specific Restrictions:** You can now [restrict access to specific tenants](https://support.catonetworks.com/hc/en-us/articles/10178151671837) as part of our CASB solution. For example, only allow access to enterprise tenants, and users can’t connect to non-business related tenants, such as private email or file sharing. This lets you set access controls and policies for specific tenants within the organization across different cloud applications.
  - The CASB engine enforces the tenant restrictions using header injection for key SaaS applications
- **IPsec IKEv2 Sites Support Devices with Dynamic IP:** You can now establish an [IPsec IKEv2 tunnel between the Cato Cloud and a third-party firewall or router](https://support.catonetworks.com/hc/en-us/articles/9706084661021-Configuring-an-IPsec-IKEv2-Site-for-a-Firewall-Router-with-Dynamic-IP-EA-) operating behind NAT with dynamic public IP address. Cato now supports IPsec IKEv2 connections initiated by the third-party firewall or router.
- **Connect on Boot:** As part of the new [Always-On Policy](/v1/docs/protecting-users-with-always-on-security), we have updated how **Connect on Boot** is configured for Windows Clients.
  - Defining **Connect On Boot** configuration for specific SDP users from the Cato Management Application is no longer supported
  - If **Connect on Boot** is disabled in the Cato Management Application, SDP users can define their own configuration from the Client. For accounts that configured **Connect on Boot** for specific SDP users, we recommend using this setting
  - If **Connect on Boot** is enabled in the Cato Management application, all Clients in your account automatically connect during device boot, SDP users can’t change the behavior in the Client
  - For migrated accounts to the Always-On Policy, see [this article](https://support.catonetworks.com/hc/en-us/articles/9927211182493-Cato-Management-Application-Notification-New-Always-On-Policy) for more information
- **Cato Management Application Enhancements:**
  - You can now edit Data Protection and Threat Protection rules in the [SaaS Security API](/v1/docs/what-is-the-data-protection-api) screen
  - Export all the site data for your account to a CSV file. The new **Export** feature is available in the Network > Sites screen

## Security Updates

- **IPS Signatures:**
  - CVE-2023-23397 - For more information on Cato protection for this threat, see this [blog post](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.catonetworks.com%2Fblog%2Fcato-protects-against-cve-2023-23397-exploits%2F&amp;data=05%7C01%7Cjonathan.rabinowitz%40catonetworks.com%7Cacb7962d1d844644fc8708db305cfc9a%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638156948172551068%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=DXxe%2FWGXHh9I0eI7aq0faTj%2FBiIehRWw82dO2qnQ1MQ%3D&amp;reserved=0)
  - **Ransomware:**
    - CryptoArch (New)
    - Monti (New)
    - RansomHouse (New)
    - Tils (New)
    - BianLian (Enhancement)
    - Clop (Enhancement)
    - Cuba (Enhancement)
    - Lorenz (Enhancement)
    - Makop (Enhancement)
    - Maze (Enhancement)
    - Midas (Enhancement)
    - Target777 (Enhancement)
  - **Malware:**
    - Cobalt Strike (Enhancement)
    - Emotet (Enhancement)
- **Application Database:**
  - Added more than 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog))
  - Easyupload (New)
  - ChatGPT (Enhancement)
  - OpenAI (Enhancement)
  - Rakuten (Enhancement)
- **TLS Inspection:**
  - ChatGPT and OpenAI have been added to global TLS bypass
