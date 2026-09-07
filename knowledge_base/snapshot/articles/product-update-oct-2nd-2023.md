---
title: "Product Update - Oct. 2nd, 2023"
slug: "product-update-oct-2nd-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-oct-2nd-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Oct. 2nd, 2023

## New Features & Enhancements

- **Introducing the New Cato Learning Center:** We are converging Cato knowledge to a [single location](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings), where you can easily read Knowledge Base articles and Community posts.
  - **Launching the Cato Community:** The [Community](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/community/topics) is the place for our customers and partners to ask questions and start discussions with other community members about the Cato Cloud, share your experiences, learn all about SASE, and provide feedback to Cato.
    - To create or comment on posts, log in to the Community with your Cato Management Application username and password
    - New hierarchy for posts and topics, no previous content was removed
  - **New and Improved Knowledge Base:** We rebuilt the [Knowledge Base](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/categories/4964852963229-Documentation) from the ground up and now it’s easier to read articles and learn about Cato’s service and features.
    - New **Partner Only** section which contains exclusive content for Cato partners and resellers
    - No change to article links or URLs
    - Please share your feedback and comments with us: [productdocs@catonetworks.com](mailto:productdocs@catonetworks.com)
- **New Condition Type in Application Control Rules:** We added support for **Value Sets** so you can group multiple user-defined strings, such as URL paths, for [Application Control](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/articles/13314302436253) rules. This lets you manage extensive activity and Full Path URL polices with fewer rules that are easier to maintain. For example, you can create a **Value Set** that contains a list of URL paths for specific Dropbox folders, and then use it in an Application Control rule for Dropbox.
  - A **Value Set** can include any string values
  - **Value Sets** can be created in the **Edit** panel for a rule, or in the **Value Sets** tab in the [Categories](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/articles/13314286857501) page

## PoP Announcements

**New York, United States:** We added a new range (150.195.207.0/24) to the New York PoP location.

## Security Updates

- **IPS Signatures:** View more details about the IPS Signatures and Protections in the [Threats Catalog](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/articles/10055007301149-Using-the-Threat-Catalog).
  - Ransomware INC (New)
  - Ransomware Key Group (New)
  - Ransomware Kuiper (New)
  - Ransomware NoEscape (New)
  - Ransomware Steloj (New)
  - Ransomware Unlocker (New)
  - Malware DarkGate (New)
  - CVE-2023-36851
  - CVE-2023-36847
  - CVE-2023-36846
  - CVE-2023-36845
  - CVE-2023-36844
  - CVE-2023-35844
  - CVE-2023-33300
  - CVE-2023-33299
  - CVE-2023-32521
  - CVE-2023-28432
  - CVE-2023-27372
  - CVE-2023-26802
  - CVE-2022-28561
  - CVE-2022-26960
  - CVE-2022-24632
  - CVE-2022-24629
  - CVE-2017-8220
  - CVE-2014-8423
- **Suspicious Activity Monitoring:** These protections were added to the [SAM service](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/articles/8065444369693-Monitoring-Suspicious-Activity-with-IPS-SAM-):
  - Commercial VPN access on Inbound
  - Execution of SC to do Lateral Movement
  - Phishing heuristic
- **Apps Catalog:**
  - Added dozens of new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/articles/7603867737885)), including these highlights:
    - Azure Blob (Enhancement)
    - Webex (Enhancement)
    - MullvadVPN (Enhancement)
    - ExpressVPN (Enhancement)
    - PureVPN (Enhancement)
- **Application Control Policy (CASB):**
  - Enhanced granular actions for the following apps:
    - Granular Activity: Zendesk - Login (New)
    - Granular Activity: Atlassian - Login (New)
    - Granular Activity: Dropbox - Upload (Enhancement)
- **Detection and Response:**
  - Threat Hunting IOA signatures:
    - Device Attributes Exfiltration (New)
    - Downloading a Suspicious Script (New)
    - HTA File Found in MS Office (New)
    - PSTools Download Detection (New)
    - Remote PsExec Service Execution (New)
    - SDP File Sharing Application Upstream Bandwidth Anomaly (New)
    - Suspected Exfiltration to Cloud Storage Applications (New)
    - Suspicious Execution - High Risk (New)
    - Suspicious LNK File Download (New)
    - Traffic to an IP address as host name with a redirection (New)
    - Transferring a Suspicious Script (New)
- **Client Classification:**
  - Google Chrome Browser (Enhancement)

## Knowledge Base Updates

- [Quota Exceeded in Cato](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/articles/360014398377)
- [Why Do Primary and Secondary Sockets Reconnect at the Same Time?](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/articles/13825794787101)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings/articles/11968052021277-Understanding-Cato-s-Gradual-Rollout). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
