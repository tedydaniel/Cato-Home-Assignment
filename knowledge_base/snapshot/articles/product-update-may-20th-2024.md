---
title: "Product Update - May 20th, 2024"
slug: "product-update-may-20th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-may-20th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 20th, 2024

## New Features & Enhancements

- **Manually Upgrade Sockets to a Newer Version**: We're introducing an option to [manually start the Socket upgrade process](/v1/docs/manually-upgrading-a-socket) and install a Socket firmware version. This can help when an upgrade was skipped because the Socket was disconnected during the maintenance window, or for any other reason.
- **Simplified Removal of Users and User Groups From Your Account:** You can now delete a [user](/v1/docs/working-with-users) or [user group](/v1/docs/working-with-user-and-system-groups) even if they are included in a policy. After being deleted, they are removed from the Users or User Groups pages and can no longer connect with the Cato Client or have a policy applied.
  - Users or user groups are still visible in a policy and marked as deleted, for example, **John Doe (Deleted)**
  - Previously, users or user groups could not be deleted when included in a policy
- **Improved Monitoring of Sanctioned Apps:** To better manage cloud app ecosystems, customers can now include their known business applications in the **Sanctioned Apps Category**. This lets you filter to see analytics specifically for sanctioned apps.
  - The [App Analytics](/v1/docs/understanding-app-analytics) and [Experience Monitoring](/v1/docs/what-is-cato-experience-monitoring) pages can be filtered for sanctioned apps
  - For customers with a CASB license:
    - The **Sanctioned Apps Category** can be configured in [Application Control rules](/v1/docs/managing-the-application-control-policy)
    - The [Cloud Apps Dashboard](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D523e7ad8e0%26e%3D2b9a2985a2&amp;data=05%7C02%7Cjonathan.rabinowitz%40catonetworks.com%7Ce62910fbea5b44669e3b08dc74ea212d%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638513796137572509%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&amp;sdata=Vo%2FpovVBHTjuopUUXZ%2BxGcOxWeW65ou7a4rw03JYvLA%3D&amp;reserved=0) can be filtered for sanctioned apps
  - The **Sanctioned Apps Category** is configured in the Assets > Categories page
  - Previously, the category was available only with a CASB license

Go to the [Cato Product Roadmap](https://support.catonetworks.com/hc/en-us/articles/14517158733853) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Malware AlphaCrypt-CnC Beacon (New)
    - Malware DuckTail APT-CnC communication (New)
    - Malware Lumma Stealer-CnC (New)
    - Malware PrivateLoader-CNC Communication (New)
    - Ransomware ATCK (New)
    - Ransomware BlackSkull (New)
    - Ransomware DumbStackz (Enhancement)
    - Ransomware KUZA (Enhancement)
    - Ransomware Mallox (Enhancement)
    - Ransomware Ncov (Enhancement)
    - Ransomware Robaj (Enhancement)
    - Ransomware SHINRA (Enhancement)
    - Ransomware Stop/Djvu (Enhancement)
    - Ransomware Tuborg (Enhancement)
    - Ransomware Virus (MedusaLocker) (Enhancement)
    - Ransomware Wormhole (Enhancement)
    - Ransomware xDec (Enhancement)CVE-2022-38108 (New)
    - CVE-2020-4000 (New)
    - CVE-2021-21345 (New)
    - CVE-2021-21480 (New)
    - CVE-2022-29847 (New)
    - CVE-2022-44373 (New)
    - CVE-2023-32985 (New)
    - CVE-2023-34993 (New)
    - CVE-2023-37569 (New)
    - CVE-2023-44353 (New)
    - CVE-2023-48782 (New)
    - CVE-2023-6019 (New)
    - CVE-2023-6184 (New)
    - CVE-2024-1212 (Enhancement)
    - CVE-2024-26212 (New)
    - CVE-2024-3272 (New)
    - Generic Directory Traversal - HTTP (Enhancement)
    - PetitPotam - Active Directory Certificate Services (ADCS) NTLM Authentication (New)
- **Detection & Response**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Suspicious Bot Activity(Pastebin) (Enhancement)
      - Suspicious DNS Traffic (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
