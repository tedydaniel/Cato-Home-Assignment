---
title: "Product Update - May 6th, 2024"
slug: "product-update-may-6th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-may-6th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 6th, 2024

## New Features & Enhancements

- **New EPP Agent v1.1**: From May 5th, 2024, we are starting to roll out the Endpoint Protection (EPP) Agent version 1.1. This version contains:
  - **New** ​**​Protection Engine​**​: The new Anti Exploit engine uses machine learning to protect against threats that attack software vulnerabilities.
    - This new engine is in addition to the two existing [protection engines](/v1/docs/configuring-endpoint-protection)
    - Examples of attack techniques that are protected against include:
      - Privilege escalation
      - Process introspection
      - LSASS credential dumping
  - ​**​Automated Check for Other EPP Products​**​: Cato's EPP Agent cannot effectively protect an endpoint if another EPP solution is running. To ensure it can protect the endpoint, the Agent now automatically checks if another EPP solution is installed.
  - ​**​Uninstall and Delete the Agent in One Action:​**​ You can now [uninstall the Agent](/v1/docs/installing-the-cato-epp-solution) from an endpoint and delete it from your account in one action.
    - Previously uninstalling the Agent and deleting the Agent had to be done separately
    - If required, you can still uninstall the Agent from an endpoint without deleting it from your account

- **New SaaS Security API Connector forGitHub:** We added a [connector for GitHub](/v1/docs/github-configuring-the-data-protection-api-connector) that lets you scan the commits that users push to a GitHub repository to identify sensitive data.
  - Scan commits for all repositories or select specific ones
  - Events include a link to the diff comparison for the commit
- **Client Notifications for Application Control Policies:** For improved user experience, you can enable Client notifications to inform users when they are blocked by a [CASB](/v1/docs/managing-the-application-control-policy) or [DLP](/v1/docs/creating-the-data-control-policy) rule in the Cato Management Application.
  - Supported for Windows Client v5.10 and higher
- **Video Updates Moving to Cato Academy:** Starting from June 1st, 2024, all videos for feature updates will only be available in the [Product Updates](https://academy.catonetworks.com/page/product-updates) section at the Cato Academy. The videos in the Knowledge Base will be archived and unavailable after June 1st.
  - Bookmark the [Product Updates](https://academy.catonetworks.com/page/product-updates) section in the Cato Academy so you can easily see the latest videos for new features

Go to the [Cato Product Roadmap](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D2a7169d7d3%26e%3D2b9a2985a2&amp;data=05%7C02%7Cjonathan.rabinowitz%40catonetworks.com%7C98971ce7aae549a4ee1c08dc64642750%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638495628531686831%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&amp;sdata=H1v1TGT3zsRpHAGgTb2rp1Tm9Ulx5Cx5REZMJwfwq5o%3D&amp;reserved=0) in the Knowledge Base to follow the status of upcoming features and enhancements.

## PoP Announcements

**Osaka, JP:** A new IP range is now available in the Osaka PoP location - 202.75.243.0/24

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
