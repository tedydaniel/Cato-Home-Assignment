---
title: "Product Update - June 12th, 2023"
slug: "product-update-june-12th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-june-12th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 12th, 2023

## New Features & Enhancements

- **Support for Stronger PSKs for IPsec Sites:** We are enhancing the Pre-Shared Key (PSK) for IPsec sites, and support PSKs of up to 64 characters for IPsec tunnels.
  - Previously PSKs supported up to 32 characters
  - This feature will be gradually released over the next two weeks
- **Enhancement for Cloud App Tenant Control:** To meet enterprise requirements for numerous allowed corporate domains in Header Injection rules, the **Header Value** now supports up to 4K bytes.
  - Previously, the **Header Value** supported up to 1024 bytes

- **Cato Management Application Enhancement:**
  - **New AI Tools Category:** Starting June 25th, you can Use the **AI Tools** system category to easily include the most popular AI apps in networking and security policies, including: ChatGPT, AgentGPT, Google Bard, Elicit AI, MagicPen AI, Poe AI, OpenAI
    - Learn more about the **AI Tools** category in the [Apps Catalog](/v1/docs/using-the-app-catalog)

## PoP Announcements

- **Austin, United States:** A new Cato PoP is now available in Austin
- **Chennai, India**: A new Cato PoP is now available in Chennai
- **Frankfurt, Germany:** A second Cato PoP is now available in Frankfurt
- **Shenzhen, China**: A second Cato PoP is now available in Shenzhen
- **Vancouver, Canada:** A new Cato PoP is now available in Vancouver

## Security Updates

- **Block New TLDs that Pose Security Risks:** Google recently added a number of new top-level domains (TLDs), such as .mov and .zip. Attackers can exploit these new TLDs to distribute malware and carry out phishing attacks. You can use the **Suspicious TLDs** application to control access to new TLDs that present security risks.
  - Learn more about the **Suspicious TLDs** application in the [App Catalog](/v1/docs/using-the-app-catalog)
- **Application Database:**
  - Added many new SaaS applications (you can view the SaaS apps in the [App Catalog](/v1/docs/using-the-app-catalog))
  - New **AI Tools** Category with these applications (starting June 25th):
    - AgentGPT (New)
    - Elicit AI (New)
    - Google Bard (New)
    - MagicPen AI (New)
    - Poe AI (New)
    - ChatGPT (Enhancement)
    - OpenAI (Enhancement)
  - Enhanced these SaaS applications:
    - Anydesk
    - Line Works
    - Naver
- **IPS Signatures:**
  - Ransomware Rancoz (New)
  - Ransomware EXISC (New)
  - Ransomware FAST (New)
  - Ransomware TURKEY (New)
  - Ransomware Cerber (New)
  - Ransomware Devos (New)
  - Ransomware Zhong (New)
  - CVE-2023-21932
  - CVE-2023-27524
  - NMap RDP scanner (New)
- **Suspicious Activity Monitoring:**
  - Wget communicates with low-popularity domain (New)
  - Java download binary (Enhancement)
  - Upload JSP Web Shell (Enhancement)
- **Application Control Policy (CASB):**
  - Google Drive - download (Enhancement)
- **Data Loss Prevention (DLP):**
  - Enhanced support for BMP images
  - Added new LOG file type
- **TLS Inspection:**
  - Onenote – default TLS bypass on native client, default inspection on browsers
