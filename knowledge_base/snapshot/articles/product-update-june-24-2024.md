---
title: "Product Update - June 24, 2024"
slug: "product-update-june-24-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-june-24-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 24, 2024

## New Features & Enhancements

- **Cato XDR Enhancements:**
  - **New Related Stories View Provides Better Context for XDR Investigations:** For improved efficiency for analysts, we added a new view in the [drill-down page](/v1/docs/drilling-down-and-analyzing-xops-security-stories) for XDR Security stories where you can quickly review similar stories and stories with the same source.
    - This view provides better context for the investigation and shows key details for each related story, such as the story Indication, Source, Criticality, and Targets it has in common with the story being investigated.
  - **Mute Network Stories in XDR:** The XDR Mute Stories policy now provides the ability to filter out Network stories from the Stories Workbench.
  - **Enhancement for Security Mute Stories Rules:** You can now use **Global Range** and **Interface Subnet** objects defined for your account in [Mute Stories rules](/v1/docs/muting-xops-stories). For example, this can help you focus on important stories by preventing the generation of stories based on traffic from a guest VLAN you defined with a specific IP range.
    - Available for Threat Prevention and Threat Hunting stories
- **Revoke a Remote User Session to Mitigate Security Risks:** To increase control of access to your network, you can now force a remote user to reauthenticate by [revoking their session](/v1/docs/revoking-a-remote-user-session) across all devices. Users cannot access your network until they reauthenticate to establish a new session.
  - Revoking sessions helps prevent unauthorized access due to a stolen device, compromised accounts, employee terminations, and more
  - Supported for all authentication methods, IdPs, and all Client versions
- **Customize Branding for the Cato Management Application:** You can apply your company branding and custom Knowledge Base and Support links to the [Cato Management Application](/v1/docs/customizing-the-cma). The new Management Application page complements the existing branding experience for emails, firewall block pages, and the Cato Client.
  - All branding pages are now conveniently located under the new Administration > Branding section
- **Enhancement for App Analytics:** We have added new data to increase the visibility of [App usage](/v1/docs/understanding-app-analytics) in your network.
  - You can now filter by traffic direction (Inbound, Outbound, or WANbound) to categorize the data for deeper analysis
  - New **Users** tab displays all user activity regardless of the user location. For example, for users that both connect remotely and from behind a site, all their activity is unified into a single row on the table
  - New **Sources** tab displays the IP address of the source that initiated the connection
- **Enhancements to the Domain Lookup Page:** We improved the [Domain Lookup page](/v1/docs/identifying-the-category-for-a-domain) for better usability, including:
  - Clearer indication of which categories can be edited when you want to [override default domain categories](/v1/docs/overriding-default-domain-categories-for-the-account)
  - More intuitive display of the domain **Popularity** and **Malicious Score**

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

## PoP Announcements

**New Localized IP Range for Slovenia:** A new localized IP range for Slovenia (serviced through the Prague PoP location) is now available - 209.206.3.128/25

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Malware RadX RAT-Checkin Communication (New)
    - Malware WhiteSnake Stealer-Communication (New)
    - Ransomware 0day (Enhancement)
    - Ransomware AzzaSec (Enhancement)
    - Ransomware Banta (Enhancement)
    - Ransomware BOMBO (Enhancement)
    - Ransomware Cebrc (Enhancement)
    - Ransomware Chaddad (Enhancement)
    - Ransomware DORRA (New)
    - Ransomware Dtbc (Enhancement)
    - Ransomware FUNNY (Enhancement)
    - Ransomware Geometrical (Enhancement)
    - Ransomware GhostHacker (Enhancement)
    - Ransomware Gtsc (New)
    - Ransomware Harma (Enhancement)
    - Ransomware Jerd (New)
    - Ransomware Jinwooks (Enhancement)
    - Ransomware Lexus (Enhancement)
    - Ransomware Malware Mage (New)
    - Ransomware ONION (Enhancement)
    - Ransomware payB (Enhancement)
    - Ransomware POLSAT (Enhancement)
    - Ransomware Rapax (Enhancement)
    - Ransomware Run (New)
    - Ransomware Stop/Djvu (Enhancement)
    - Ransomware SYSDF (Enhancement)
    - Ransomware Tutu (Enhancement)
    - Ransomware WSHLP (New)
    - Ransomware Xcss (New)
    - Ransomware xDec (Enhancement)
    - Ransomware Xtbl (New)
    - CVE-2020-25858 (New)
    - CVE-2014-100005 (New)
    - CVE-2018-10143 (New)
    - CVE-2021-32819 (New)
    - CVE-2022-26833 (New)
    - CVE-2022-29517 (New)
    - CVE-2024-24919 (Enhancement)
    - CVE-2024-25600 (New)
    - CVE-2024-28253 (New)
    - CVE-2024-28255 (New)
    - CVE-2024-28847 (New)
    - CVE-2024-28848 (Enhancement)
    - CVE-2024-30044 (New)
    - CVE-2024-30050 (New)
    - CVE-2024-3116 (New)
    - CVE-2024-4323 (New)
    - CVE-2024-4358 (Enhancement)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Suspicious Bot Activity (Enhancement)
      - Suspicious Scanning Tool Download (Enhancement)
      - Exploitation Attempt (Enhancement)
      - Suspicious Tool Download (Enhancement)
    - Threat Prevention:
      - Suspicious WebAssembly Download (Enhancement)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - AnyDesk Lateral Transfer over SMB (New)
    - AnyDesk Download (Enhancement)
    - LNK File Download over WebDAV (New)
    - SimpleHelp Downloading (New)
- **Apps Catalog:**
  - Added over 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Surfshark VPN (New)
    - Zoho (Enhancement)
    - Zoho Mail (New)
    - VPN Unlimited (New)
    - Splashtop (Enhancement)
    - ExpressVPN (Enhancement)
    - Lightway (ExpressVPN proprietary protocol) (New)
- **Application Control (CASB and DLP):**
  - Enhanced granular actions for the following apps:
    - Instagram - Comment, Follow, Login, Login with Facebook, Send File, Upload Post, Upload Video
    - Webex - Download
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT
      - Payment Terminal
        - Castles Technology (Enhancement)
        - Ingenico (Enhancement)
      - Printer
        - Xerox (Enhancement)
        - Smart TV
        - Samsung (Enhancement)
      - VoIP
        - Avaya (Enhancement)
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Polycom (Enhancement)
        - Ubiquiti (Enhancement)
    - Networking
      - Network Appliance
        - Aruba Networks (Enhancement)
    - Mobile
      - Mobile Phone
        - Redmi (Enhancement)
        - Samsung (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
