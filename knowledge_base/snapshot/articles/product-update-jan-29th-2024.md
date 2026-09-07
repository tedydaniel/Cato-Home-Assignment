---
title: "Product Update - Jan. 29th, 2024"
slug: "product-update-jan-29th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-jan-29th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Jan. 29th, 2024

## New Features & Enhancements

- **Cato Now Supports Deploying AWS vSockets from the Marketplace:** We added the Cato virtual Socket (vSocket) for the AWS public cloud to the [AWS Marketplace](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace). This enhancement significantly simplifies the deployment process of the vSocket.
  - Supported for single Socket configuration
- **CASB Application Control Enhancement - Control Activities for App Categories:** The [Application Control policy](/v1/docs/managing-the-application-control-policy) now lets you control activities for [categories](/v1/docs/working-with-categories) of apps, in addition to specific apps. This includes both pre-defined system categories and custom categories.
  - For example, you can:
    - Set a rule to block uploads for the File Sharing or Online Storage categories, and the rule automatically updates when new apps are added to the category
    - Define a custom category with apps you want to manage together, and create a single rule that blocks downloads for the category
  - Supported activities include Upload and Download
- **NAT Policy for IPsec and Cross Connect Sites:** A new [site-level NAT policy](/v1/docs/configuring-a-site-level-nat-policy) with granular matching conditions and actions, including DNAT and SNAT. With this policy, you can now integrate with third-party networks (such as contractors) connected over IPsec tunnels or Cross Connects, and require NAT to avoid IP conflicts.
  - Support for Socket sites will be available in the future
- **Manually Override Default Domain Categorization:** Admins can now [override the default category](/v1/docs/overriding-default-domain-categories-for-the-account) for a domain for the account. The category defined by the admin will apply in all account policies. For example, a domain classified as News can be manually reclassified as Social Network.
- **Control Transfer of Specific File Types:** We added [File Type Control](https://support.catonetworks.com/hc/en-us/articles/16378226322717-Creating-File-Control-Rules-in-the-Application-Control-Policy) rules to control uploading and downloading a wide array of file types. This lets you tailor security policies for scenarios such as unauthorized source code transfers or access to Microsoft Office document types.
  - File Type Control rules appear in the [Application Control Policy](/v1/docs/managing-the-application-control-policy)
  - Supports an additional 100 file types not previously supported in Cato DLP
  - File Type Control is included in the CASB license
- **Changes to the License Page:** We are making the following changes to the [Administration > License page](/v1/docs/working-with-cato-license-types), there is no impact to your account.
  - **Bandwidth Tab:** Changing the **Region** column to **License Group**
  - **Users Tab:** Changing the **Zone** column to **License Group**
- **Schedule to Automatically Generate and Send Reports:** We enhanced [Cato’s reports](/v1/docs/reports), and you can automate generating up-to-date reports which can be emailed to recipients.
  - Schedule reports on a daily, weekly, or monthly basis
  - Define the mailing list that receives the reports, or download them directly from the Cato Management Application
  - This feature will be gradually enabled over the next few weeks
- **Send Notifications to ServiceNow, Jira, and Slack:** You can create alert Integrations for [ServiceNow](https://support.catonetworks.com/hc/en-us/articles/16378534226333-Creating-a-ServiceNow-Alert-Integration), [Jira](https://support.catonetworks.com/hc/en-us/articles/16378556700061-Creating-a-Jira-Alert-Integration), and [Slack](https://support.catonetworks.com/hc/en-us/articles/16378566056989-Creating-a-Slack-Alert-Integration) to support alert-based notification and automation flows. The default configuration for each integration is easy to set up and can be customized to meet the specific needs of your organization.
  - This feature will be gradually enabled over the next few weeks
- **Webhooks Support for Alert Notifications:** You can now use [Webhooks](/v1/docs/sending-cma-notifications-via-webhooks) to send alerts to third-party platforms, and create alert-based automation flows. Cato Webhooks provide a high degree of customization, including support for custom headers, and you can customize the message body or use the predefined templates.
  - This feature will be gradually enabled over the next few weeks
- **Subscription Groups for Alert Notifications:** For alerts that you define in the Cato Management Application, create a new [Subscription Group](/v1/docs/creating-subscription-groups) that receives the alert.
  - Subscription Groups contain Mailing Lists and integrations (such as Webhooks and Slack)
  - Previously you were only able to define a Mailing List for alerts
  - This feature will be gradually enabled over the next few weeks
- **New System Notifications Page:** The Administration > System Notifications page is replacing the [Email Notifications page](/v1/docs/account-level-alerts-and-system-notifications). You can choose to send alerts to: Mailing Lists, Integrations, and Subscription Groups.
  - This feature will be gradually enabled over the next few weeks
- **Correlate Different Types of XDR Stories for the Same Source:** You can now see at a glance all the stories related to a source IP, including stories created by different XDR engines. This lets you easily extend your investigation into both the network and endpoint. For example, easily review Threat Prevention and Endpoint Alert stories that were created on the same host.
  - This option is available by selecting **Source IP** in the **Group By** dropdown menu in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

## Video Feature Overviews

- [vSocket Onboarding to AWS Marketplace](https://support.catonetworks.com/hc/en-us/articles/16376617482013)
- [SNAT/DNAT Policy for IPSec and Cross Connect Sites](https://support.catonetworks.com/hc/en-us/articles/16376650010013)
- [Domain Classification Override](https://support.catonetworks.com/hc/en-us/articles/16376514041885)
- [New File Type Control Policy](https://support.catonetworks.com/hc/en-us/articles/16376435491869)
- [Scheduled Reports](https://support.catonetworks.com/hc/en-us/articles/16376390590877)
- [Alerts Integrations](https://support.catonetworks.com/hc/en-us/articles/16376337930141)
- [Webhooks Integration](https://support.catonetworks.com/hc/en-us/articles/16376413709725)
- [XDR for Network Connectivity and Performance Incidents](https://support.catonetworks.com/hc/en-us/articles/16376613563677)
- [XDR - Group Stories by Source IP](https://support.catonetworks.com/hc/en-us/articles/16376534002589)
- [Show Information about Your Cato Management Application Account](https://support.catonetworks.com/hc/en-us/articles/16376331091997)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
