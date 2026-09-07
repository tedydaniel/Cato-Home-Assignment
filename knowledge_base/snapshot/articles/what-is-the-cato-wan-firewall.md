---
title: "What is the Cato WAN Firewall?"
slug: "what-is-the-cato-wan-firewall"
updated: 2026-08-18T07:18:24Z
published: 2026-08-18T07:18:24Z
canonical: "knowledge.catonetworks.com/what-is-the-cato-wan-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Cato WAN Firewall?

This article provides background information about the WAN firewall for your account.

For more information about working with the WAN firewall, see [Managing the WAN Firewall Policy](/v1/docs/managing-the-wan-firewall-policy).

## Overview of the Cato WAN Firewall

The WAN firewall in the Cato Cloud controls access to objects and entities in your Wide Area Network (WAN). Configure the WAN firewall rulebase to create a secure access control policy and protect the network.

The WAN firewall is part of the Next Gen Firewall (NGFW) that is integrated into the Cato Cloud and lets you create rules to prevent unauthorized access to the network. The WAN firewall uses a whitelist approach, and there is a default ANY-ANY block rule to drop all connections that are not explicitly allowed in the rulebase.

Use the rules to configure the firewall to inspect all connections and only allow the ones that match its configured settings. The firewall uses an ordered rulebase. This means that it starts inspecting the connection and checks to see if it matches the first rule. If not, then it continues to sequentially apply each rule to the connection until a rule matches the connection.

The WAN firewall also includes full layer 7 functionality with User Awareness, allowing zero trust access policies to specific applications on the WAN.

### Use Case - Only Allowing Approved Video Conferencing Device Manufacturers

A security admin receives a task to review the security posture of the meeting rooms in the site for the London branch office. The admin goes to the [Device Inventory](/v1/docs/what-is-device-inventory) page, filters for **Field - Device Type**, **Operator - In**, **Value - Video Conferencing**, and sees all the video conferencing devices in the London site. The admin realizes that there are video conferencing devices from several different manufacturers, and this does not meet the organizational security policy. The IT team already has an IoT security license and creates new rules in the WAN and Internet firewall policies with **Device Attribute** settings that only allow the two approved manufacturers for the video conferencing devices. Some of the video conferencing devices in the London site will no longer work because they are blocked by the firewall policies until they can be replaced with new devices from the approved manufacturers.

### Understanding Autonomous Firewall Insights

![WAN_firewall.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26771719231901(1).png)

The **WAN Autonomous Firewall Insights** are a list of [Posture checks](/v1/docs/reviewing-posture-checks-for-your-account) that evaluate your WAN Firewall policy and show how they comply with Cato’s recommendations. Following these recommendations optimizes your firewall configurations and improves security posture.

There are two types of insights:

- Star icon (powered by AI): Enabled rules in your WAN Firewall policy are automatically analyzed by Artificial Intelligence (AI) to detect issues, for example, rules that can be discarded or modified, such as:
  - **Temporary Rule:** Introduced as a short-term solution to address an immediate need. These rules are mostly created to function temporarily while a proper or permanent solution is being deployed or developed.
  - **Testing Rule:** Rules explicitly created for validating, debugging, or experimenting with a specific feature or scenario.
  - **Expired Rule** or **Rule with Future Expiration Date:** Rules created to address a specific need and have a desirable cutoff date that has already passed or that has not yet been reached or cannot be proven/evaluated.
  - **Over Permissive Rules:** Rules that may be overly permissive based on users, hosts, apps, or protocols defined for the rule. This insight uses topological heuristics and indicates that we recommend that you remove the extra items from the rule to better adhere to your zero trust strategy.

For example: restrict user access only to **sampleAdmin**, conditioned by a specific zero trust [Device Posture profile](/v1/docs/creating-device-posture-profiles-and-device-checks), limit application to only **RDP**, and restrict protocol to only **TCP**.
  - **Unused Rule:** Identifies firewall rules with an Allow action that have not generated any events in the past 60 days
- **Configuration-based:** The configurations and settings in your Internet Firewall policy are to ensure they follow best practices.

### Working with the WAN Firewall Configuration Wizard

The WAN Firewall Configuration Wizard autonomously reviews your policy using these checks and insights. When a check fails, you can review and update your policy directly in the Wizard without editing individual rules. This helps you stay secure while simplifying policy management. For more information, see [Using the Configuration Wizard](/v1/docs/using-the-configuration-wizard).

### Anti-Spoofing Protections in the Cato Firewall

One of the basic functionalities of an NGFW is to protect against anti-spoofing attacks. The security engines in the Cato Cloud implicitly drop any connection where the source IP is outside the scope of the configured entity (such as site, network range, device, or user). This blocks anti-spoofing attacks and prevents violations of the configured logical topology.

### Working with Ordered Rules

The WAN firewall inspects connections sequentially and checks to see if the connection matches a rule. The final rule in the rulebase is a default ANY-ANY block rule - so if a connection does not match a rule, then it is blocked by the final default rule. A strong access control policy contains firewall rules that allow specific connections and traffic in the WAN.

You can review the default rule settings in the **Default Rules** section at the end of the rulebase. These rule settings can't be edited.

Rules that are at the top of the rulebase have a higher priority because they are applied to connections before the rules lower down in the rulebase. For example, if a connection matches rule #3, the action is applied to the connection, and the firewall stops inspecting it. The firewall does not continue to apply rules #4 and below to the connection. You can increase the efficiency of the WAN firewall and give a high priority to rules that match the largest number of connections.

### Working with Multiple Objects in a Single Rule

When there is a rule with objects in multiple columns, such as an **application** and a **service**, then there is an AND relationship between them. For example, if there is a rule that allows the Backup Services application for port 443, then the traffic is allowed when it matches both the application and the port.

For rules that use multiple objects in a single column, such as more than one **port**, there is an OR relationship between them. For example, if there is a rule that allows access to the mail server for service **SMTP** and ports 25, 265, 587, and 2525, then the traffic is allowed when it matches the SMTP service or any one of the ports.

- **Note:** Each rule can have a maximum of 64 conditions with an AND relationship between them, and a rule's exceptions are included in the rule limit. For example, if there is a rule with two AND conditions (such as a **source** and a **service**), and the rule has 25 exceptions with 3 AND conditions each (such as a **source**, an **app**, and a **service**), then the rule has 77 conditions. This exceeds the supported limit of 64 conditions and the rule might not function properly. However, you can assign more than 64 objects within the same column of a rule, since there is an OR relationship between them. For example, you can assign more than 64 apps in one rule.

### Understanding the Hit Count

The hit count helps you identify unused rules that can be removed from a policy and optimize rule configuration to better match the required traffic scope. The hit count for a rule is based on the number of events generated by the rule. If a rule does not generate events, the hit count is zero.

The hit count contains two numbers:

- The approximate number of events generated by each rule in the policy
- How often the rule is hit relative to other rules (ranked by percentile)

You can quickly identify the rules with the highest and lowest hit count, based on the color of the status bar. This color reflects how often the rule is hit relative to other rules:

- Blue: 0 - 24th percentile
- Green: 25th - 49th percentile
- Orange: 50th - 74th percentile
- Red: 75th -100th percentile

#### Resetting and Refreshing the Hit Counter

![Reset.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33141035526301(1).png)

The hit count values are updated automatically every 24 hours and are based on the past 14 days of traffic. From the three dots at the end of each rule, you can reset or refresh the hit count for up-to-date visibility. This lets you accurately measure rule effectiveness and immediately validate rule activity.

- Resetting the hit counter for a specific firewall rule returns the hit count to 0
- Refreshing the hit counter updates the hit count on demand for all firewall rules

### Policy Revisions and Concurrent Editing by Multiple Admins

The WAN Firewall lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### Configuring the Time Settings for a Rule

You can configure the time settings for a rule so that it is enabled or disabled at a defined date and time. In the **Time** drop-down menu, you can configure the **Daily Schedule** and/or the **Active Period**.

You can configure both of these options so that, for example, the rule is active on weekdays during the month of May 2025. Alternatively, you can configure each option independently to meet your requirements.

#### Understanding the Daily Schedule

The **Daily Schedule** defines the schedule for when the rule is active. If a schedule is configured for a rule, a clock symbol is displayed in the **Action** column.

The options for the **Daily Schedule** are:

- **No time constraint:** There is no schedule for the rule. This is the default behavior of the rules.
- **Limit to working hours:** The rule is active only during the working hours configured in the Cato Management Application. For more about working hours, see [Defining Default Working Hours for the Account](/v1/docs/defining-default-working-hours-for-the-account).
- **Custom:** Select the time of the day and the days of the week when the rule is active. Uncheck the **Recurring** option, and select the **Date** and time setting for the rule.
  - **Recurring:** The time setting will be applied more than once, for example, every Tuesday from 9:00am to 5:00pm.

#### Understanding the Active Period

The **Active Period** defines the date and time period the rule is active in UTC. If the **Effective From** field is not selected, the rule is active immediately after the rule is saved and published.

On the rule table, if an **Active Period** is defined, an hourglass symbol is displayed in the **Action** column. The color of the symbol reflects the status:

- **Black**: The rule is not active and will become active in the future
- **Green**: The rule is active
- **Red**: The rule has expired

## Understanding the Settings for WAN Firewall Rules

This section explains the fields and settings for the rules in the WAN firewall rule base. A thorough understanding of the WAN firewall helps to successfully manage access control for the corporate network.

**Rule Actions**

The following table describes the actions that each firewall rule can apply to the network traffic. For actions that generate events, you can show event logs in **Home > Events**.

| Item | Description |
| --- | --- |
| Allow | Firewall allows matching traffic. |
| Block | Firewall blocks matching traffic. |
| Prompt | Firewall redirects matching traffic to a web page with a message. The user is prompted to decide whether or not to continue. You can customize the prompt web page, see [Customizing the Warning / Block Page](/v1/docs/customizing-the-warning-block-page-branding). The Cato prompt page is an HTML page that uses JavaScript and session cookies to manage user consent. These cookies are domain-specific, temporary, and typically deleted when the browser is closed. Cato currently uses three cookie name prefixes, (`tls_cert_err`, `fw_wan`, and `fw_inet`). Cookie handling and session persistence depend on user settings and behaviour, the browser, and operating system. To review events for when a user chooses to proceed after a prompt page, filter the [Events](/v1/docs/analyzing-events-in-your-network) page to show events with the **Prompt Action** field set with the value **Proceed**. |

### Rulebase Columns

The following table describes each column in the WAN firewall rulebase. When there are multiple columns configured for a rule, then there is an AND relationship between them.

For more about **Source**, **Destination**, **App**, and **Category** items for a rule, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects).

| Item | Description |
| --- | --- |
| # | Shows the priority of the rule in the WAN firewall rule base. - Use the **Rule Order** field to change the priority of the rule. - Use the **Enabled** toggle to enable or disable the rule. The toggle is green ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26771703813405(1).png) when enabled. |
| Name | Enter a **Name** for the rule |
| Source | Source of the traffic for this rule |
| Criteria | [Define conditional access](/v1/docs/adding-device-conditions-to-firewall-rules) based on attributes of the actual device of an end-user or other devices communicating on your network, such as IoT/OT. Options include: - **Device Attributes** - Attributes of devices as identified by the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine - **Platforms** - Device operating system (OS) - **Countries** - Source country for the connection based on the physical location of the device (according to the IP address geo-location) - **Device Posture Profiles** - Device Profiles (configured in Access > Device Posture) - **Origin of the Connection** - The geolocation of the device (remote or behind a site) |
| Direction | Indicates the direction of the rule. Options include: - **To** - This rule allows the traffic in only one direction, **Source** to the **Destination**. For example, site Alpha is allowed to connect to site Bravo, but site Bravo cannot connect with site Alpha. - **Both** - This rule manages traffic in both directions, to and from the **Source** and **Destination**. |
| Destination | Destination of the traffic for this rule |
| App/Category | Only applies to matching objects for the specific applications, categories, and other objects |
| Service/Port | Only applies to traffic that matches the specified services and ports |
| Action | Apply the specified action to traffic that matches the rule For example, when the traffic is blocked, the connection is dropped, and the lower priority rules are not applied to this connection |
| Track | When the rule is matched, an event is generated, or an email notification alert is sent to the specified list |
| Hit Count | The hit count for this rule |
| ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26771719376285(1).png) | Opens a drop-down menu with these options: - **Add Rule Above** - Add a new rule above the selected rule - **Add Rule Below** - Add a new rule below the selected rule - **Duplicate Rule:** Create a new identical rule directly below the original selected rule in the same section - **Move Rule** - Change the priority of the rule by defining a different position for it in the rule order - **Add Exception** - Create a new exception to the selected rule - **Enable/Disable** - When a rule is disabled, the firewall doesn't inspect connections for the settings in the rule - **View Rule Events** - Show the [Events](/v1/docs/analyzing-events-in-your-network) page prefiltered for events related to the rule - **Delete Rule** - Delete the selected rule |

## Related Resources for the WAN Firewall

- For more about the applications and categories, see [Working with Categories](/v1/docs/working-with-categories)
- For more about the settings in the WAN firewall, see [Managing the WAN Firewall Policy](/v1/docs/managing-the-wan-firewall-policy)
