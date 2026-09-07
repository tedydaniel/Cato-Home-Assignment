---
title: "Understanding the JSON Fields for Alert Integrations"
slug: "understanding-the-json-fields-for-alert-integrations"
updated: 2026-07-12T05:07:02Z
published: 2026-07-12T05:07:02Z
canonical: "knowledge.catonetworks.com/understanding-the-json-fields-for-alert-integrations"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding the JSON Fields for Alert Integrations

This table explains the fields that you can add to the JSON template for [webhook integrations](/v1/docs/sending-cma-notifications-via-webhooks).

| Field | Description |
| --- | --- |
| accountId | The Cato account ID is shown in the **Account > Account Info** page |
| accountName | Name for the Cato account in the Cato Management Application (CMA) |
| title | Title of the alert |
| subject | Short summary of the alert |
| alertType | Alert type. Can be used for categorization, such as LIFECYCLE_CHANGED |
| *content* | Free text for the alert content, supported formats are: - Text - contentText - HTML - contentHTML - Markdown - contentMarkdown |
| startDate | Time stamp that the monitored issue started |
| endDate | Time stamp that the monitored issue ended |
| time | Time stamp that the alert was sent |
| ruleId | Unique Cato ID for the policy rule that triggered the alert |
| ruleName | Rule name that triggered the alert |
| policyName | Policy name in the Cato Management Application for the rule |
| siteName | Site name that triggered the alert |
| level | Level or priority of the alert |
| storyId | Unique identifier for the Site Operations story |
| correlationId | Unique identifier used to correlate related events, messages, or operations |
| indication | An indication is a set of actions and behaviors for the Network or Security incident. Each producer has different indications |
| socketInterface | Name in the Cato Management Application for the Socket port (interface) |
| socketInterfaceId | Unique Cato ID for the Socket interface |
| socketRole | For Socket high availability events, indicates whether the Socket is primary or secondary |
| socketSerial | Unique serial number (S/N) of the Socket that generated the connectivity health event |
| socketMacAddress | MAC address of the primary Socket |
| socketDescription | User-defined description of the primary Socket in the Cato Management Application |
| secondarySocketSerial | Unique serial number (S/N) of the secondary (HA) Socket, if applicable |
| secondarySocketMacAddress | MAC address of the secondary (HA) Socket |
| secondarySocketDescription | User-defined description of the secondary Socket in the Cato Management Application |
| storyStatus | Current status of the Site Operations story (for example: OPEN, IN_PROGRESS, RESOLVED) |
| lastIncidentDescription | Description of the most recent incident associated with the Site Operations story |
| ISPName | Name of the ISP related to the Site Operations story |
| managedServiceStatus | Current managed service status |
| lastManagedComment | Most recent comment added by the managed service |
| lastUserComment | Most recent user comment |
| link | Link to the related resource or external reference |
| interactionTopic | Primary topic associated with the interaction |
| interactionSubTopic | Sub-topic associated with the interaction |
| interactionIntent | Intent associated with the interaction |
| action | Action that is relevant to the event type |
| messageId | Unique identifier for the message |
| sessionId | Unique identifier for the session |
| eventId | Unique identifier for the event |
| eventType | Type of event |
| eventSubType | Subtype of the event |
| eventMessage | Message associated with the event |
| eventCount | Number of occurrences for the event |
| severity | Severity level of the event |
| actionsTaken | Actions taken in response to the event |
| networkRule | Network rule associated with the event |
| customCategoryName | Name of the custom category |
| srcIp | Source IP address |
| srcPort | Source port |
| srcSiteId | Unique Cato ID of the source site |
| srcSiteName | Name of the source site |
| srcCountry | Country of the source IP address |
| srcEndpointType | Type of the source endpoint |
| srcIspIp | Public ISP IP address of the source |
| clientIp | Client IP address |
| hostMac | MAC address of the host |
| publicIp | Public IP address |
| subnetName | Name of the subnet |
| destIp | Destination IP address |
| destPort | Destination port |
| destSiteId | Unique Cato ID of the destination site |
| destSiteName | Name of the destination site |
| destCountry | Country of the destination IP address |
| destEndpointType | Type of the destination endpoint |
| destIsSiteOrVpn | Indicates whether the destination is a site or VPN |
| destDomain | Destination domain |
| domainName | Domain name |
| serverIp | Server IP address |
| ipProtocol | IP protocol |
| trafficDirection | Direction of the network traffic |
| popName | Name of the Point of Presence (PoP) |
| linkType | Type of network link |
| tlsInspection | Indicates whether TLS inspection was performed |
| tlsVersion | TLS protocol version |
| tlsRuleName | Name of the TLS inspection rule |
| tlsErrorType | TLS error type |
| userName | User name |
| userId | Unique identifier of the user |
| vpnUserEmail | Email address of the VPN user |
| userRiskLevel | Risk level of the user |
| loggedInUser | Logged-in user |
| userAwarenessMethod | Method used to identify the user |
| isAdmin | Indicates whether the user is an administrator |
| isAdminActivity | Indicates whether the activity was performed by an administrator |
| deviceName | Name of the device |
| deviceType | Type of device |
| deviceOsType | Operating system type of the device |
| osType | Operating system type |
| osVersion | Operating system version |
| hostIp | Host IP address |
| isCompliant | Indicates whether the device is compliant |
| isManaged | Indicates whether the device is managed |
| networkAccess | Network access status |
| devicePostureProfile | Device posture profile |
| applicationName | Name of the application |
| applicationId | Unique identifier of the application |
| applicationType | Type of application |
| applicationRisk | Risk level of the application |
| catoApp | Indicates whether the application is a Cato application |
| categories | Application or URL categories |
| url | URL |
| fullPathUrl | Full URL including the path |
| httpRequestMethod | HTTP request method |
| httpResponseCode | HTTP response code |
| refererUrl | HTTP referrer URL |
| userAgent | User-Agent string |
| threatName | Name of the detected threat |
| threatType | Type of threat |
| threatVerdict | Threat verdict |
| threatConfidence | Confidence level of the threat detection |
| threatScore | Threat score |
| riskLevel | Risk level |
| indicator | Threat indicator |
| signatureId | Signature identifier |
| mitreAttackTactics | MITRE ATT&CK tactics |
| mitreAttackTechniques | MITRE ATT&CK techniques |
| mitreAttackSubtechniques | MITRE ATT&CK sub-techniques |
| detectionName | Name of the detection |
| confidenceLevel | Confidence level |
| criticality | Criticality of the event |
| analystVerdict | Analyst verdict |
| classification | Classification |
| recommendedActions | Recommended actions |
| engineType | Detection engine type |
| fileName | Name of the file |
| fileHash | Hash of the file |
| fileSize | Size of the file |
| fileType | Type of the file |
| fileOperation | File operation |
| filePath | Path of the file |
| fileTopic | File topic |
| fileTopicCategory | File topic category |
| dlpProfiles | DLP profiles |
| dlpScanTypes | DLP scan types |
| matchedDataTypes | Matched data types |
| emailSubject | Email subject |
| initialObjectStatus | Initial object status |
| finalObjectStatus | Final object status |
| dnsQuery | DNS query |
| dnsAnswer | DNS answer |
| dnsRecordType | DNS record type |
| dnsProtectionCategory | DNS protection category |
| tenantName | Name of the tenant |
| tenantId | Unique identifier of the tenant |
| isSanctionedApp | Indicates whether the application is sanctioned |
| outOfBandAccess | Indicates whether access was out-of-band |
| owner | Owner of the object |
| collaborators | Collaborators associated with the object |
| collaboratorName | Name of the collaborator |
| sharingScope | Sharing scope |
| appActivity | Application activity |
| appActivityType | Type of application activity |
| appActivityCategory | Category of application activity |
| objectName | Name of the object |
| objectType | Type of the object |
| vendor | Vendor |
| vendorPolicyName | Name of the vendor policy |
| guardName | Name of the AI guard |
| guardType | Type of AI guard |
| aiAppRiskLevel | Risk level of the AI application |
| providerName | Name of the AI provider |
| resourceName | Name of the resource |
| resourceType | Type of the resource |
| regionName | Name of the region |

## JSON Fields for XOps Site Operations Stories

This table explains the fields for webhooks based on Site Operations stories.

| Field | Description |
| --- | --- |
| lastIncidentDescription | Description of the most recent incident associated with the Site Operations story |
| storyStatus | Current status of the Site Operations story (for example: OPEN, IN_PROGRESS, RESOLVED) |
| ISPName | Name of the ISP related to the Site Operations story |
| socketSerial | Unique serial number (S/N) of the primary Socket involved in the Site Operations story |
| socketMacAddress | MAC address of the primary Socket |
| socketDescription | User-defined description of the primary Socket in the CMA |
| secondarySocketSerial | Unique (S/N) of the secondary (HA) Socket, if applicable |
| secondarySocketMacAddress | MAC address of the secondary (HA) Socket |
| secondarySocketDescription | User-defined description of the secondary Socket in the CMA |
