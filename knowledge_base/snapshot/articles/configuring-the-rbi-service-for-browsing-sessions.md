---
title: "Configuring the RBI Service for Browsing Sessions"
slug: "configuring-the-rbi-service-for-browsing-sessions"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/configuring-the-rbi-service-for-browsing-sessions"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the RBI Service for Browsing Sessions

This article explains how to configure the Remote Browser Isolation (RBI) service to protect against web-based threats.

## Overview

RBI protects devices from web-targeted threats and malicious content that can be embedded in Internet sites and services. RBI runs as an isolated Cato service that emulates browsing activity for users and then streams the emulated traffic to the user device. This keeps the device safe from malware threats by making sure that all in-browser code is executed remotely and never on the device.

For situations where the RBI service can't emulate traffic, you can configure a **Fallback Action** that determines how the traffic is handled. For example, if you temporarily disable the RBI service, or if the service is momentarily unreachable.

For more information about the RBI service, see [Securing Browsing Sessions Through RBI](/v1/docs/securing-browsing-sessions-through-rbi).

**Note:** RBI functionality is not available for Cato PoPs located in China. These PoPs will always apply the **Fallback Action** for the relevant traffic.

### Understanding RBI Profiles

You can customize the security settings for RBI sessions with granular profiles that enable you to configure different browsing isolation settings. These define the actions a user can perform on a site. For example, you can block users from typing or pasting text into web forms, and prevent them from leaking credentials and other sensitive data.

Each RBI Profile contains:

#### Actions To Be Allowed or Blocked

For each profile, you can define the granular actions to Allow or Block:

- Upload - Uploading any file (Uploading using Drag and Drop functionality is not supported)
- Download - Downloading any file
- Printing - Printing web content
- Copy/Paste - Copying data from the site or pasting data into the site
- Typing - Typing text in the site

![Controls.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971832357661.png)

**Note**: RBI restrictions apply only within the isolated browser session. Actions initiated outside the RBI container (e.g., via host browser menus or OS-level shortcuts) bypass RBI controls. To enforce these controls fully, apply browser or endpoint-level policies (e.g., Chrome GPO, DLP tools) alongside RBI configurations.

#### RBI Banner Text

In an RBI session, a banner is displayed to the end user to inform them they are in an RBI session. The branding of this banner can be defined globally across your account. For more information see [Customizing the User Experience](/v1/docs/configuring-the-rbi-service-for-browsing-sessions#customizing-the-user-experience).

In each RBI profile you can override the the text of the banner and create custom text for the profile.

![Banner_text.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971840216221.png)

#### Continuous RBI Sessions

To enhance browsing security and improve end-user experience, you can configure a profile to let users continue browsing to multiple destinations within the same RBI session. This ensures destinations that you define aren't opened in a non-isolated session or in a different RBI session. These are example use cases for continuous RBI sessions:

- Prevent non-isolated browsing to risky domains - Create an extensive domain list using wildcards to ensure the user’s entire browsing session takes place in an isolated environment, even if the user navigates away from Uncategorized or Undefined domains
- Authentication to a site - Configure a list of domains, including all subdomains of a file-sharing app, to let users sign in when they are redirected to a different domain to authenticate

![Continue_browsing.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971817979677.png)

#### Failover Action

The **Fallback Action** defines what happens when the RBI action can't be carried out. In this scenario, you can choose to block the action or display the Prompt page.

![Failover.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971840270109.png)

### Using RBI with the Internet Firewall

RBI sessions are enforced through the Internet Firewall using the RBI action in a rule. When traffic matches the rule, an RBI session starts automatically. By default, the Default RBI profile is applied. You can assign a different RBI profile to meet your security and access requirements.

![FW_RBI.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971850161949.png)

Only rules for application categories **Uncategorized** or **Undefined**, or a **Custom Category**, can be configured for remote browsing. All other traffic is protected by Cato's broad range of additional security services.

**Note:** These are the content types supported by RBI. A Custom Category containing other content types is not supported:

| - Anonymizers - Botnets - Criminal activity - Drugs - Gambling - Hacking - Parked domains - Spyware | - Cheating - Suspected phishing - Suspected malware - Porn - Uncategorized - Undefined - File sharing - Online storage |
| --- | --- |

### Prerequisites for the RBI Service

- Enabling the RBI service requires an RBI license. For more about purchasing the RBI license, please contact your Cato representative.
- TLS Inspection must be enabled for traffic configured for RBI.
- For the RBI service to function properly, the Internet Firewall must allow access to these URLs. If your Internet Firewall has an ANY-ANY Block rule at the bottom, add an explicit rule with higher priority allowing traffic to these URLs:
  - http://securebrowsing.catonetworks.com/
  - https://authentic8.com/
- If you do not use Cato as your [DNS server](/v1/docs/what-is-cato-dns), add a record to your local DNS server for http://rbi.catonetworks.com/ to resolve to 10.254.254.161.

### Known Limitations

- URLs containing fragment identifiers (“#”) are not supported in RBI redirection

## Configuring RBI

This section explains how to configure the RBI service to provide secure web browsing for end-users.

![RBI.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971840309277.png)

This is a sample workflow for implementing RBI:

1. Enable the RBI service
2. Create an RBI Profile
3. Configure an Internet Firewall rule with the **Remote Browsing** action

### Step 1: Enabling and Disabling the RBI Service

When you enable the RBI service, the **Remote Browsing** action for the Internet Firewall is now available, and you can then create rules to direct traffic to the service. By default, RBI is disabled.

**To enable or disable RBI for your account:**

1. From the navigation panel, select **Security > RBI**.
2. Click the slider to enable (green) or disable (gray) the **RBI** service for the account.
3. Click **New**.

### Step 2: Creating an RBI Profile

Each RBI Profile contains granular RBI configurations that can be applied to an Internet Firewall rule.

**To create an RBI profile:**

1. From the navigation panel, select **Security > RBI**.
2. Click **New**.
3. Configure the profile to meet your requirements.
4. Click **Apply**.

### Step 3: Creating an Internet Firewall Rule for Remote Browsing

Use Internet Firewall rules to define when Cato directs traffic to the RBI service. The rules must be configured with the **Application Category** set as **Uncategorized**, **Undefined**, or **Custom Category** with no other apps or categories configured. For more about configuring Internet Firewall rules, see [Managing the Internet Firewall Policy](/v1/docs/managing-the-internet-firewall-policy).

**To create an Internet Firewall rule for remote browsing:**

1. From the navigation menu, select **Security > Internet Firewall**.
2. Click **New**.
3. Enter the **Name** for the rule.
4. Enable or disable the rule using the slider (green is enabled, grey is disabled).
5. Configure the **Rule Order** for this rule.

New rules are added to the bottom of the rulebase. You can change the order in which this rule is applied.
6. Expand **Source** and select the source type.
  - Select the type (for example: Host, Network Interface, IP, User, User Group, Any). The default value is **Any**.
  - When needed, select a specific object from the drop-down list for that type.
7. Expand the **App/Category** section and select **Application Category**.

Select one or more of **Uncategorized**, **Undefined**, or a **Custom Category** from the Application Category drop-down list. When there is more than one **App/Category** object in a rule, there is an OR relationship between them.
8. Set the **Action** for this rule as **Remote Browsing (RBI)** and choose the required profile.
9. **(Optional)** Configure tracking options to generate **Events** and **Send Notification**. The frequency starts counting after the first notification is sent.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.
10. Click **Apply**. The new rule is added to the rulebase.
11. Click **Save**.

The rule is saved.

#### Best Practices for Implementing RBI with the Internet Firewall

We recommend gradually implementing your RBI policy with specific scopes, to avoid potential misconfiguration of policy rules that can result in using RBI for traffic that should have direct access to destinations. These are examples of recommended best practices for implementing RBI.

**Best Practices for Implementing RBI for Uncategorized and Undefined Destinations:**

- If there is already an Internet Firewall rule configured for the application categories **Uncategorized** and **Undefined** :
  1. Start keeping track of events for the configured rule to identify specific **Uncategorized** or **Undefined** destinations that are essential for your users.
  2. Add a higher priority rule with the action **Remote Browsing** defined for a specific scope of essential **Uncategorized** and **Undefined** sites.
- If there is no rule configured for the categories **Uncategorized** and **Undefined**:
  1. Add a rule covering **Uncategorized** and **Undefined** destinations with the action **Allow** or **Prompt**, and set it to track **Events**.
  2. Start keeping track of the events to identify specific **Uncategorized** or **Undefined** destinations that are essential for your users.
  3. Create a higher priority rule with the **Allow** or **Prompt** action, and gradually add the specific essential destinations you identify, until all essential destinations are added.
  4. Set the higher priority rule to the **Remote Browsing** action.
- Since RBI is only supported for browsers, if you are concerned about non-browser traffic to **Uncategorized** and **Undefined** domains, we recommend creating an Internet Firewall **Block** rule for **Uncategorized** and **Undefined** traffic. Position this rule at a lower priority than the RBI rule for these domains.

This secures traffic to these suspicious domains that originates from non-browser clients (for example, cURL scripts).

## Customizing the User Experience

In an isolated RBI session, a banner is displayed to the user. To meet your branding requirements, you can customize the design by changing the global background color, text, and text color.

![167e948476380c.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971785462045.png)

**To customize the user experience:**

1. From the navigation menu, click **Account > RBI Branding**.
2. To change the background color, click on the **Strip Color** and choose a colour.
3. To change the text color, click on the **Text Color** and choose a color.
4. To change the text, click in the **Customize Alert text** and update the text.
5. Click **Save**.

## Reviewing RBI Events

You can review Security events in **Home > Events** and find the logs related to RBI emulation sessions carried out for a connection that matched a firewall rule with the **Remote Browsing** action. These events are labeled with the Sub-Type **Internet Firewall** and the Action **RBI**.

When the RBI session can't be executed and the **Fallback Action** is invoked, the relevant events have the Action **Block** or **Prompt** depending on your configuration.

This is an example of a filter you can create to view events related to RBI:

![RBI_Event_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971785474205.png)

This is an example of an event related to an RBI session:

![RBI_Event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971818090909.png)

## Troubleshooting the RBI Service

You can use the **Administrator RBI Simulator** to help diagnose issues that end-users experience when trying to browse destinations configured for RBI emulation. The utility can help isolate the cause of the issue, and helps you provide useful information to Support to find a resolution.

**Note:** After 5 minutes of inactivity, the RBI session automatically ends and the browser tab closes. To continue browsing, the user must re-open the site in their browser.

### Troubleshooting the RBI Service for a URL

If a user experiences an issue browsing a certain URL, you can generate a test RBI emulation session for the URL with the **Administrator RBI Simulator**. Enter the valid HTTP or HTTPS URL and then follow the resulting link to view the site in an RBI session. The utility sends this traffic directly to the RBI service without passing through the Cato Cloud. This can help determine if a user's issue relates to the RBI service itself, or is caused by other issues such as account configuration or Cato infrastructure connectivity. For example, a user connected to Cato can't browse to an **Uncategorized** website configured for RBI, but the admin is able to reach the site using the utility. This may indicate that the RBI service is functioning properly and the issue is related to connectivity between a PoP and the service.

The **Administrator RBI Simulator** applies the RBI security controls defined in the **RBI Account Preferences**.

After running an RBI session from the utility, you can report the results to Support to help them resolve the issue.

![RBI_Admin_Utility.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971785529757.png)

**To troubleshoot with the Administrator RBI Simulator:**

1. From the navigation panel, select **Security > RBI**.
2. Under **Administrator RBI Simulator**, enter a valid HTTP or HTTPS URL. For example: https://maps.google.com
3. Choose the **Profile** to simulate.
4. Click **Generate**. A URL is created for the RBI session.
5. Click the link next to the URL. The RBI session opens in your default browser.

### Known Limitations

- The RBI service has limited support for localization
