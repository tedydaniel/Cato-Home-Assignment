---
title: "Product Update - Feb. 12th, 2024"
slug: "product-update-feb-12th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-feb-12th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Feb. 12th, 2024

## New Features & Enhancements

- **New X1600 LTE Socket**: We are introducing a new [X1600 Socket model with embedded LTE](/v1/docs/cato-socket-deployment-guides-and-data-sheets) (4G) connectivity. You can use the LTE link as a backup, or for active WAN connectivity in rural areas.
  - The LTE links support the following:
    - 150 Mbps upstream and 600 Mbps downstream throughput
    - Dual SIM standby
  - The X1600 LTE Socket supports the same wired throughput as the X1600 base model
  - Socket v20 is the minimum version
- **Announcing New Site Throughput Up to 10 Gbps:** We improved the infrastructure of the Cato Cloud to support up to 10 Gbps throughput per site. These are the types of sites that can provide this throughput:
  - X1700 Socket sites
  - Cross Connect sites
- **XDR Stories for Cato Endpoint Protection Alerts:** You can now review stories for Cato Endpoint Protection (EPP) alerts in the XDR Stories Workbench. An EPP story correlates data from all [EPP alerts](/v1/docs/cato-endpoint-protection-epp-configuring-the-xops-integration) that occurred on the same device within a 24-hour period. This lets Cato EPP customers conduct threat investigations in a unified platform extending into both the network and the endpoint.
  - Stories for Cato EPP alerts incorporate data such as:
    - Threat name
    - Remediation status
    - Relevant file names
  - Available with an EPP license for all XDR tiers
- **Introducing Socket v20:** We are starting the gradual rollout for Socket version 20. This version includes security enhancements, and the firmware for new features. In the coming weeks we will update the Cato Cloud and release the following features:
  - **Synthetic Probe Monitoring:** Synthetic probes let you proactively check the status of the apps for Internet breakout and the Cato tunnel. You can easily identify issues originating with your ISP, or a misconfiguration for a specific app with high latency due to QoS priority configuration
  - **Port and Transport Level Metrics for Sites**: We are introducing a new section in the [Network Analytics](/v1/docs/showing-the-site-network-analytics) page that provides visibility into physical port metrics, with a breakdown by Transport Types (Cato, Local Breakout, Off-Cloud, LAN, Alt. WAN) and Socket interface
- **Introducing Exact Data Matching for DLP:** [Exact Data Matching](/v1/docs/working-with-exact-data-matching-edm-for-dlp) (EDM) finds specific sensitive data values that are important to the organization, rather than matching general data patterns. For example, instead of blocking transfer of all credit card data, you can import a structured data set of your customers' credit card data, and block only that data set. Tailoring EDM to your DLP policies, can significantly reduce false positives and increase admin productivity.
  - When you import data sets, all data is hashed prior to import, and no unhashed sensitive data is imported or stored
- **Seamlessly Connect your Cloud Tenants to Cato**: We added a turnkey provisioning configuration that is designed to swiftly connect your cloud resources to the Cato PoP location.
  - Available for Cross Connect sites
  - Supported Cloud Providers: AWS DirectConnect, Azure ExpressRoute, GCP InterConnect, Oracle FastConnect
- **New Connectors for SaaS Security API:** We added connectors to monitor data for these platforms:
  - **Salesforce:** Monitor reports exported from your [Salesforce account](/v1/docs/salesforce-configuring-the-data-protection-api-connector) for sensitive data, compliance violations, and more. For example, identify when a Salesforce user exports a report containing credit card details
  - **ServiceNow:** Monitor tables and data in your [ServiceNow tenants](/v1/docs/servicenow-configuring-the-data-protection-api-connector). For example, identify when a user uploads sensitive data into a ServiceNow ticket or attachment
- **Public vSocket Image for Deploying Azure Marketplace vSockets:** The Cato virtual Socket (vSocket) image is now publicly available for [vSockets in the Azure Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace). This enhancement significantly simplifies the process of deploying a vSocket to a site.
- **Visibility for Entra ID Anomalies:** We enhanced the [Cloud Activity Dashboard](https://support.catonetworks.com/hc/en-us/articles/15931659820445-Using-the-Cloud-Activity-Dashboard) to show anomalous sign-ins in your Entra ID tenant. A new widget summarizes these risky user sign-ins, such as sign-ins from a malware-linked IP address, an unusual location, a suspicious browser, and more.
  - The new widget requires setting up a [connector for Microsoft Entra ID Protection](/v1/docs/configuring-the-microsoft-entra-id-protection-connector-for-sign-in-anomaly-data)
- **Enforce Different Security Polices When a User Connects Behind a Site or Remotely:** You can enforce different security policy rules when a user connects remotely with the Client or behind a site. For example, you can allow a user to only access sensitive information behind a site, but not when working remotely.
  - This can be included in [Internet Firewall](/v1/docs/managing-the-internet-firewall-policy), [WAN Firewall](/v1/docs/managing-the-wan-firewall-policy), and [TLS Inspection](/v1/docs/adding-device-conditions-for-tls-inspection) policies
  - This new option is not included in policies by default. To include this configuration in a policy, add the device’s **Connection Origin**
- **More Effective DLP Data Detection with ML Data Classifiers:** We’re introducing machine learning (ML) based data classifiers trained to identify different types of sensitive documents. Using an advanced data science similarity model, the [ML classifiers](/v1/docs/creating-dlp-content-profiles) offer better adaptability and accuracy in detecting sensitive data, as they can dynamically learn and evolve based on changing data patterns. The new ML classifiers provide comprehensive detection for medical records, tax forms, patent documents, resumes, immigration forms, and more.

## Cato SDP Client Releases

- **Windows Client v5.10:** Over the next few weeks, we will start the rollout of Windows Client v5.10. This version contains:
  - **User Notifications for CASB and DLP:** The device displays a notification to the user when their activity is blocked by [App Control](/v1/docs/managing-the-application-control-policy) or [Data Control](/v1/docs/creating-the-data-control-policy) rules. This educates the user about which app was blocked and why.
  - Improved Client messages for failed upgrades and token expiration
  - Stability enhancements, including Pre-login mode
  - Bug fixes

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
