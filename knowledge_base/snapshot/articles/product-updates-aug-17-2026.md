---
title: "Product Updates - Aug. 17, 2026"
slug: "product-updates-aug-17-2026"
updated: 2026-08-18T05:22:52Z
published: 2026-08-18T05:22:52Z
canonical: "knowledge.catonetworks.com/product-updates-aug-17-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - Aug. 17, 2026

## New Features & Enhancements

- **Improved Visibility into Socket Site Throughput and License Usage:** Monitor site-level throughput in relation to your licensed capacity, helping you better [understand and manage](https://knowledge.catonetworks.com/docs/understanding-and-managing-traffic-shaping-for-socket-sites) bandwidth usage.
  - The enhanced Network Analytics page provides real-time visibility into bandwidth utilization and helps identify when traffic approaches or exceeds your licensed limits
  - Supported from Socket v25 and higher
- **Windows Client v6.12.6:** During the week of Aug. 16, 2026, we will begin rolling out the [Windows Client version 6.12.6](https://knowledge.catonetworks.com/docs/summary-of-cato-windows-client-releases). This version includes stability improvements, security updates, and bug fixes.
- **Starting Rollout of Socket v27:** We are starting to gradually roll out [Socket version 27](https://knowledge.catonetworks.com/docs/socket-version-27-0-release-notes) to all customers, including firmware for new features, enhancements, and bug fixes. No customer action is required.
- **Improvement to Automatic Client Upgrades:** To prevent Clients from remaining on outdated versions, Clients upgrade to the latest fully rolled-out version, even when a newer version is in gradual rollout.
  - Previously, if a Client missed an upgrade, for example because the device was offline, it remained on its current version until it was included in the gradual rollout of the newer version
  - Supported for Client upgrade policies set to **Automatic by Cato** (show me the [Client Rollout page](https://externallink.cc.catonetworks.com/#/account/me/ClientRollout))
- **Traffic Direction in AppStats API Includes LANBOUND:** Starting with Socket v27, and as part of a gradual rollout, AppStats API queries can return `LANBOUND` traffic data. To avoid unexpected results in existing reports and integrations, add explicit `traffic_direction` filters to your queries.
  - Applies to sites with Sockets v27 and higher
  - The full set of possible values for `traffic_direction&nbsp;`after this change is: `WANBOUND`, `NO_DIRECTION`, `INBOUND`, `OUTBOUND`, `LANBOUND`
  - Asset Security - Devices license required
- **User Provisioning from Google Workspace:** Provision users and user groups from Google Workspace as an IdP using a Cato connector.
  - Configure the connector in the [Integration Catalog](https://support.catonetworks.com/hc/en-us/articles/15935823855389-Using-the-Integrations-Page)
- **Microsoft Sentinel Connector Updated with Reduced Permission Scope:** The ARM template for Sentinel connector setup follows a least-privilege model, with two custom roles replacing the previous broad workspace-level role and no separate DCE resource required.
  - Existing connectors are not impacted
  - The [integration guide](https://knowledge.catonetworks.com/docs/integrating-cato-events-with-microsoft-sentinel#faq) covers the updated architecture, permission model, and ARM template deployment (show me the [Integrations page](https://externallink.cc.catonetworks.com/#/account/me/integrationsCatalog))
- **Streamlined Penetration Test Requests:** We improved the process for [penetration tests for your account](https://knowledge.catonetworks.com/docs/cato-networks-scanners-or-penetration-testing). Submit requests directly from Support tickets, and the information is sent to the InfoSec GRC team, who will then follow up by email.
  - Select **Penetration Test Request** as the **Category** when opening a ticket
- **Guide to Remediating Security Incidents with Cato APIs:** A [step-by-step Knowledge Base article](https://knowledge.catonetworks.com/docs/remediating-xops-stories-by-api) covers how to automate API-based responses to security events and XOps stories. Use it to extract story data, apply remediation actions such as isolating hosts, blocking IOCs, and quarantining users, and annotate the story with actions taken.
- **Upcoming Stricter Schema Type Validation for Cato API:** From Aug. 30, 2026, the Cato API enforces stricter type validation to align with the documented schema. Review the [Potentially Breaking Changes](https://knowledge.catonetworks.com/docs/cato-api-potentially-breaking-changes-and-eol#20260621-api-id-fields-type-change-from-longinteger-to-string) article to verify your API calls are not impacted.
- **CMA Enhancements:**
  - **Export Reports as CSV:** [Report](https://knowledge.catonetworks.com/docs/cato-reports) data can be exported as CSV files for sharing and offline analysis, either on demand or on a recurring schedule delivered directly to your inbox
  - **Preview User Details from the Users Page:** Clicking a user on the **Users** page to provide a quick summary of key details

### PoP Announcements

- **Paris, FR:** The following ranges are now available for the Paris PoP location:
  - 159.117.245.0/24
  - 159.117.247.0/24
- The following new ranges will soon be available:
  - **Brisbane, AU:** 113.30.139.0/24
  - **Munich, DE:** 159.117.248.0/24
  - **Osaka, JP:** 113.30.141.0/24
  - **Paris, FR:** 159.117.249.0/24
  - **Sao Paulo, BR:** 199.27.57.0/24
- **Upcoming Localized IP Range for Azerbaijan:** The following localized IP range for Azerbaijan (serviced through the Frankfurt PoP location) will soon be available:
  - **AZ:** 209.206.29.128/27

### Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](https://support.catonetworks.com/hc/en-us/articles/7603867737885-Using-the-App-Catalog).
  - New Apps: 36 new apps - Block, Inc., Buzz, Cato Client Software Updates, Cbox Live Chat, ChatApp, ChatCrypt, Cloudcom - SMS Add-on for Google Sheets, Flyzoo, Gadu-Gadu (GG), Google Account, IRCCloud, LaKeel Messenger, Luxchat, Max, Mibbit Web IRC Client, MightyText, Modica Group, Monkey: Random Video Chat, NeWork, Peerly, Pidgin, Prompt.io, RumbleTalk, STORE+, SimSimi, Soprano MEMS (Mobile Enterprise Messaging Suite), Teamwire, Telstra Integrated Messaging, Text-Connect, TextNow, Textmagic, Trillian, Voxer, Wholesale SMS, YouChat, iFlyChat
  - Enhanced Apps:
    - Adobe
      - Updated app domains
    - Articulate
      - Updated app domains
    - Buffer, Inc.
      - Updated app domains
    - Chatwork
      - Updated app domains
    - DCE/RPC
      - Signature Updated
    - Dynatrace LLC
      - Updated app domains
    - Google Applications
      - Removed domain **accounts.google.com**
    - Greenhouse
      - Updated app domains
    - Happy Scribe
      - Updated app domains
    - Harvey Legal AI Platform
      - Updated app domains
    - Hibob
      - Updated app domains
    - Hightail
      - Updated app domains
    - Indeed, Inc.
      - Updated app domains
    - Keihi
      - Updated app domains
    - Le Chat (Mistral AI)
      - Updated app domains
    - Lumin Pdf Corporation
      - Updated app domains
    - Maintainx
      - Updated app domains
    - Microsoft Netlogon
      - Signature Updated
    - MineOS
      - Added domain **saymine.io**
    - MobileIron, Inc.
      - Updated app IPs
    - NewArc.ai
      - Updated app domains
    - Nitro Software, Inc.
      - Updated app domains
    - Notion
      - Updated app domains
    - Pdfescape
      - Updated app domains
    - Pennylane
      - Updated app domains
    - Preply
      - Updated app domains
    - Redis
      - Signature Updated
    - sketchup
      - Updated app domains
    - Smallpdf
      - Updated app domains
    - Sprout Social
      - Updated app domains
    - Synthesia
      - Updated app domains
    - Talkdesk
      - Updated app domains
      - Added domains **mytalkdesk.com**, **mytalkdesk.eu**, **mytalkdeskca.com**, **talkdeskapp.co.uk**, **talkdeskapp.eu**, **talkdeskappca.com**, **talkdeskid.com**, **talkdeskid.eu**, **talkdeskidca.com**
    - Teamtailor
      - Updated app domains
    - TurboScribe
      - Updated app domains
    - Twilio
      - Updated app IPs
    - Workable Software Limited
      - Updated app domains
    - Yodeck
      - Updated app domains
    - Zoom CDN Services
      - Modified name from **Zoom Apps** to **Zoom CDN Services**
  - Category Changes:

The following categories are scheduled for deprecation: "Custom Apps", "Other", "Transportation". All applications previously associated with these categories have already been reassigned to more accurate, active categories. This change applies only to the categories and does not deprecate the applications themselves or affect any other feature.
    - Custom Apps - Deprecated:
      - Removed apps: Accela, Inc., ActiveCampaign, LLC., Airnow PLC, AppDirect, Applied Technologies Internet SAS, AudienceRate Ltd, BILL.COM INC., Balsamiq Studios, LLC, BetterCloud, Inc., BigTime Software, Inc., Buffer, Inc., ClassDojo, Inc, Copper Enterprise, Inc., Deputechnologies Pty Ltd, Dimdata Systems Co., Ltd., Doximity, Inc., Drift.com, Inc., Duolingo, Inc., EasyVista S.A, Engine Yard, Inc., Enko Teknoloji A., Expensify, Inc., Feedly, Inc., Flexera Software LLC, FlowMSP, Inc., FrontApp, Inc., Hootsuite, Humanity.com, Inc., JN PROJECTS Inc., Leadpages, LumApps, Mixpanel, Moxtra, Inc., MuleSoft LLC, ONR Applications, Inc., ProntoForms Corporation, Propertify Inc, Qordoba, Inc., Rafay Systems, Inc., ResponseTap Inc., Sioux High Tech Software Ltd., Snap, Softr Platforms GmbH, SourceCode Technology Holdings, Inc., Sprout Social, Stream.io INC, Trello, Inc., appypie, ascendix, author_it, axosoft, biznessapps, engineerbabu, fieldedge, graphli, inevent, innodemneurosciences, joomla, owncloud, raygun, spruced, tawk.to inc., techdecade, travis_ci, versum, whatfix, yoyogames
    - Other - Deprecated:
      - Removed apps: 2NDSITE Inc., 317 Labs, Inc., 360Learning SA, Accruent, Aerospike, AffectLayer, Inc., Aha, Air Computing Inc., Alfresco Software, Inc., Amplitude, Inc., Aplos Software, LLC, Ask Nicely Holdings Inc., Basecamp LLC, Beekeeper, Belly, BigTime Software, Inc., BirdEye Inc., Bloomerang, Bloomfire, Inc., Bright Pattern, Inc., Brightidea, Bugsnag Inc., BuiltOn AS, Bullhorn Inc., CLARABRIDGE INC, CallRail, Celonis, Chargebee, Inc., Chef Software Inc., Chili Piper, Inc., Chintai Network Services Pte Ltd, Clarizen, Inc., ClassDojo, Inc, Classy Inc., CloudCraze LLC, CoSchedule, LLC, Code42 Software, Inc., Cogito Corporation, Collibra Inc., ConnectAndSell Inc., ConnectWise, LLC, Cosential, Inc., Databox, Inc., Directness BV, Dolado, E2open, Eko Group Holdings Ltd, Engagio Inc., Engine Yard, Inc., Eventbrite, Inc., Expensify, Inc., Fabric, Inc., Flexera Software LLC, FloQast, Inc., Fond, FrontApp, Inc., Fusebill, Fuze, Inc., Greenhouse, Grexit, Inc., Grupo Solin SAS, H20 Capital Innovation, L.P, Help Scout Inc., Helpshift, Inc., Huddle, ISMART SOLULAB LLP, Inner Genius Pvt. Ltd., Insightly, Inc., Intra Links, JN PROJECTS Inc., Jama Software, Inc., Jostle Corporation, Justworks, Inc., Kaseya Limited, Kimble Applications Ltd., Kindful, Kissflow, Kustomer Inc., Le Bihan SA, Leadfeeder Inc., Leadspace, Inc., Lessonly, Inc., Lexos Soluo em Tecnologia, Liferay, Inc., LiquidPlanner, Inc., Listrak, LiveIntent, Inc., LivePerson, Loopio Inc., MariaDB Corporation, Mavenlink, LLC, MeisterLabs GmbH, Mendeley, Mindjet LLC, Moxtra, Inc., Newion Partners BV, Nitro Software, Inc., Octopusapp, Inc., Optimizely, Inc., Outreach Corporation, Pantheon Systems, Inc., Pax8, PayFit SAS, Pipelinersales Corporation, Podium Corp Inc., ProntoForms Corporation, Qordoba, Inc., Quip LLC, Radius Intelligence, Inc., Replicon Inc., Respond Software, Inc., Rokt Pte Ltd., Rubicon Project, Inc., SaaS Labs US, Inc., Salesfusion, Inc., Scoro Software O, Segment.io, Inc., Sendoso, Simply Measured, Inc., Skillshare, Small Improvements Software GmbH, Smartly, Inc., Smartsheet Inc., Social Tables, Inc., Swimm, Targetprocess Inc., TeamSnap, Inc., Terminus Software, Inc., Tradeshift Inc., Trello, Inc., Two Hop Management B.V., UI Flow, Inc., UJET, Inc., UXPin, Upland Software, Inc., User Replay Limited, Valeti App Sistemas SA, Vindicia, Wagepoint Inc., WalkMe, Incorporated, Wix.com Limited, WizRocket Inc, Workfront, Wrike, X Co, Yaydoo, Inc., Yext, Inc., Zapproved LLC, ZigZag Global Ltd, activeimpactinvestments, aderant, agilecrm, appointy, ariba, bitsofgold, bombora, breega, callbox, changepoint, clicktime, cohere, confirmit, conquer, doodle, drupal, dubber, easyprojects, eclipse, educba, evite, fishbowlinventory, formstack, g20vc, happyfox, hipeople, hornbill, hubstaff, iWave Information Systems Inc., intapp, ipower, jobdiva, leadforensics, manageengine, meistertask, mitel, motivosity, nextmatter, nwea, plasticspot, primevp, projectorpsa, salkantay, sellercloud, sellsy, smartdraw, snapengage, sumtotalsystems, sutisoft, thelabz, trueconf, unanet, valideffect, whatfix, xmind, zoho
    - Transportation - Deprecated:
      - Removed apps: Anvyl, Inc., Arena Solutions, Inc., Coupa, DEEM, INC., DriverDoc, E2open, Frank Subscription, LLC, Kissflow, LOB.COM, INC., Naver Map, Newlinks (Beijing) Technology Co., Ltd, Onfleet, Inc., RoboticWares Private Limited, Teamflow, LLC, Tradeshift Inc., Valeti App Sistemas SA, Vendorflow, Inc., Vroozi, Inc., Yaydoo, Inc., dealersocket, experlogix, graphli, mixtelematics, otonomi, salkantay, smedia, transoftsolutions
    - Computers and Technology:
      - Added app: AudienceRate Ltd
  - These are the updates for Socket apps, from Socket v25
    - Added 2 apps
      - Cato Client Software Updates supported for domains based
      - Talkdesk supported for domains based
    - Modified 1 apps
      - Twilio - Modified app IPs
- **Application Control Policy**
  - Granular App: Otter.AI
    - Login (New)
    - 3rd Party Login - Microsoft/Google/Apple (New)
    - Conversation (New)
    - Share (New)
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](https://support.catonetworks.com/hc/en-us/articles/10055007301149).
  - CVE-2021-30118 (New)
  - CVE-2022-48164 (New)
  - CVE-2022-48166 (New)
  - CVE-2023-2780 (New)
  - CVE-2023-30145 (New)
  - CVE-2023-49294 (New)
  - CVE-2023-6977 (New)
  - CVE-2024-25608 (New)
  - CVE-2024-2928 (New)
  - CVE-2024-3848 (New)
  - CVE-2024-38653 (New)
  - CVE-2025-0520 (New)
  - CVE-2025-10353 (New)
  - CVE-2025-32101 (New)
  - CVE-2025-49002 (New)
  - CVE-2025-49533 (New)
  - CVE-2025-54068 (New)
  - CVE-2025-67038 (New)
  - CVE-2026-20253 (New)
  - CVE-2026-3055 (New)
  - CVE-2026-56188 (New)
  - CVE-2026-58531 (New)
  - CVE-2026-9198 (New)
- **Dynamic Prevention**

For the full control list, please refer to the Threat Catalog on CMA.
  - Detected Source IP Downloading Dual-Use Tools, Limiting Lateral Movement, Discovery, Command and Control and Data Exfiltration (New) - Added 84 new controls
  - Detected Source IP Downloading Archive From Low-Reputation Server, Limiting Command and Control, Data Exfiltration and Discovery (New) - Added 62 new controls
  - Detected Source IP Downloading Executable From Low-Reputation Server, Limiting Command and Control, Data Exfiltration and Discovery (New) - Added 65 new controls
  - Detected Source IP Accessing Low-Reputation FTP Servers, Limiting Command and Control, Data Exfiltration and Discovery (New) - Added 70 new controls
- **DLP**
  - Telephone numbers [South Korea] CCL (Enhancement)
- **Asset Management**
  - Added more than 1300 new devices
- **TLS Inspection**
  - Apple Networking Domain bypass (New)
  - Puppet bypass (New)
- **XDR Indications of Attack**
  - Threat Prevention
    - Periodic Non-Browser TI Communication (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](https://support.catonetworks.com/hc/en-us/sections/24373046669085-Application-Control-via-API-with-App-Activities)
  - Azure AD | Anomalies
    - (Enhancement) - New SaaS Alerts for high-privilege OAuth admin consent, service-principal credential creation, external guest invitations, and domain federation configuration
  - GitHub | Anomalies
    - (Enhancement) - New/refined SaaS Alerts for project made public, self-hosted runner registration, audit-log streaming tampering, and new app installations
  - SharePoint | Anomalies
    - (Enhancement) - Site-admin-added SaaS Alert now excludes Teams app-only provisioning to cut false positives
  - Box | Anomalies
    - (Enhancement) - Added vendor policy to alert data and enriched actor/target detail in alert descriptions
  - Box | Activity
    - (Enhancement)
  - ChatGPT | Activity
    - (Enhancement)
  - Egnyte | Activity
    - (Enhancement)
  - Citrix ShareFile | Activity
    - (Enhancement)
  - Microsoft Exchange | Activity
    - (Enhancement)
  - Microsoft Office | Email Security
    - (Enhancement)

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://knowledge.catonetworks.com/docs/understanding-rollout-to-the-cato-cloud). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
