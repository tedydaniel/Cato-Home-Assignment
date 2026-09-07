---
title: "Creating User Notification Templates"
slug: "creating-user-notification-templates"
updated: 2026-08-27T10:06:36Z
published: 2026-08-27T10:06:36Z
canonical: "knowledge.catonetworks.com/creating-user-notification-templates"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating User Notification Templates

This article explains how to create User Notification templates that you can apply to security policy rules to provide customized messages when access is blocked or prompted.

## Overview

When traffic matches a security rule with a Notify, Block, or Prompt action, users see a browser or Client notification explaining the reason for enforcement. You can create customized User Notifications that let you explain each policy enforcement rule to users at the moment access is notified, blocked, or prompted. This improves user knowledge and awareness, reduces friction during security actions, and aligns security enforcement with broader business communication goals. Helping reduce confusion and support requests.

### Use Case: Educating Users When Access to Business Applications Is Restricted

Company ABC uses the Internet Firewall to restrict access to Salesforce to a specific group of sales users. Employees outside this group occasionally attempt to access Salesforce and receive a block action. Without context, users are unsure why access is denied and often open support tickets.

The IT team creates a custom user notification template and assigns it to the Internet Firewall rule that blocks Salesforce access. The notification explains that Salesforce is restricted to approved sales users, clarifies that the block is based on company's access policy, and provides a dedicated email address to request access.

As a result, users immediately understand why access to Salesforce is blocked and how to request approval, reducing confusion and frustration. This targeted notification educates employees about the company’s access policy at the moment of enforcement, significantly lowering the number of avoidable helpdesk tickets. For the IT team, this means less time spent on repetitive access requests, more consistent policy communication, and a better overall user experience without compromising security.

## Understanding Available Customizations

The branding of the notification, including the logo, font, and color, can be customized globally across all notifications. For more information, see [Customizing the Warning / Block Page Branding](/v1/docs/customizing-the-warning-block-page-branding).

For each notification template, you can customize the text of the message and for a webpage, decide whether to include additional items. Within the text of the Browser Page you can also add dynamic parameters that update based on the action taken by the user. The supported parameters are {Blocked URL}, {Reason}, {User}, {Host IP}, {Server IP}, {Client IP}, and {Categories}.

### Reporting the Wrong Category

You can decide whether to include a link to allow end users the ability to report a resource being wrongly categorized. For example, they can report that a news website is incorrectly classified as **Social**.

When the user clicks the link to report that a website or application has the wrong category, the Cato Management Application (CMA) generates an **Event Reference ID** , which can be optionally displayed to the end user. In addition, an event is generated for the admins in your account and the Cato Security team. Admins can use the [Events screen](/v1/docs/analyzing-events-in-your-network) to review and analyze these events with the **Event Reference IDs**.

The Cato Security team regularly reviews reported wrong categories and validates that the content for the category is correct. When websites or applications belong to the wrong category, the Cato Security team updates the definition of the category. We recommend that you [override the default category](/v1/docs/overriding-default-domain-categories-for-the-account) for the domain or website.

After a few minutes, the wrong category link is no longer active. Users are able to click the link again after they refresh the webpage.

### Reviewing Warning / Block Page Events

When a Warning or Block page is displayed, an event is generated. To easily find this event, you can choose to display the Event ID on the page. This enables users to provide the Event ID, which you can add to the **Event Reference ID** filter on the **Events** page. For more information, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).

**Note**: The reference ID is only displayed if a category for the domain can be identified.

### Localizing the Page to a Different Language

You can configure the Warning / Block Page to be displayed in different languages. When you configure support for a language, the default text on the page is shown in the target language but this can be customized.

When you define multiple languages for the page, the browser shows the page according to its language preferences. You can choose to set a **Default Language** to display when the preferred browser languages aren't supported, or if the browser has no preferred language configured. For example, an admin defines Chinese, Japanese, and Italian language support, and sets Japanese as the **Default Language**:

- A user whose preferred browser language is Italian sees an Italian message
- A user whose preferred browser languages are Korean and Vietnamese sees the default Japanese message

### Additional Customizations

The template also includes these additional customizations:

- Include a **Powered by Cato Networks** footer in the notification, or override the global branding by customizing the notification background color
- Override the global brand settings for your account. The global brand settings are configured on the **Account > Warning Block** Page. For more information, see [Customizing the Warning / Block Page Branding](/v1/docs/customizing-the-warning-block-page-branding)
- For a Block page, choose to redirect users to an alternative safe page instantly or after a configurable timeframe

## Creating User Notification Templates

You can create multiple User Notification Templates to be applied to different security policy rules to help educate users why their action has been blocked. As you customize the template, you can view a preview of the Client notification and Browser page.

> [!NOTE]
> Note:
> 
> - Client Notifications apply to Application Control (CASB) and DLP rules with a Block or Notify action
> - The Block Page applies to Internet and WAN Firewall, Application Control (CASB), and DLP rules

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(66).png)

**To create User Notification Templates:**

1. From the navigation menu, select **Account > User Notifications**.
2. Click **New**.
  - Use an existing template, e.g. Step Up Re Authenticate

or
  - Click **User Notification**
3. Choose a **Template Name** and select the **Page Type**.
4. Customize the notification as required. To edit the text of the Browse Page, click on the text you want to edit.
5. Click **Save**.

## Adding a User Notification Template to a Security Rule(s)

Once you have created a template you can add it to specific security policy rule(s).

![Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33982722691357.png)

> [!NOTE]
> Note:
> 
> Templates can only be applied to rules with a **Block** or **Notify** action.

**To add a User Notification Template to a security rule:**

- In the **Action > User Notification** section of the rule, in the **Notification Template** drop-down, select the template you want to use.

## Creating AI Security Notification Templates

AI Security rules support two notification types, each with different settings depending on whether the rule blocks access or engages the user before continuing.

### Block Notifications

A block notification is shown to users when a User Access Policy rule blocks access to an AI application. The notification displays a title and description that you configure, and can optionally include an explanation of what was detected. Users see the notification in the browser extension and must acknowledge it with **Got It** before the page closes.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/block AI sec.png)

**To create an AI Security block notification template:**

1. From the navigation menu, select **Account > User Notifications**.
2. Click **New**.
3. Enter a **Template Name**.
4. From the **Policy Type** drop-down menu, select **AI Security Interaction**.
5. From the **Page Type** drop-down menu, select **Block**.
6. Under **Notification Settings**, enter a **Title** and **Description** for the notification message.
7. (Optional) Select **Show detection explanation message** to include details about what triggered the block.
8. Click **Save**.

### Engage Notifications

An engage notification is shown to users when a User Access Policy rule requires them to acknowledge a message before accessing an AI application. The notification presents one or more options, each with a label and an action that determines what happens when the user selects it. You can also control how often the notification appears.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/engage AI sec.png)

**To create an AI Security engage notification template:**

1. From the navigation menu, select **Account > User Notifications**.
2. Click **New**.
3. Enter a **Template Name**.
4. From the **Policy Type** drop-down menu, select **AI Security Access**.
5. From the **Page Type** drop-down menu, select **User Engage**.
6. Under **Notification Settings**, enter a **Title** and **Description** for the notification message.
7. Under **Options**, configure the choices presented to the user. For each option, enter the **Text** label and select the **Action** to apply when the user selects it: **Continue**, **Block**, or **Redirect**. Click **Add Option** to add more choices.
8. From the **Notification Frequency** drop-down menu, select how often the notification is shown to the user.
9. Click **Save**.

## Known Limitation

- User notifications for CASB and DLP events might not be delivered correctly when a third-party NAT or PAT device is located between the user device and the Cato Socket. If reliable CASB or DLP user notifications are required, disable **Office Mode** for the affected users. For more information, see [Configuring Office Mode.](/v1/docs/configuring-office-mode)
- If notifications are suppressed on the device, for example in a Focus or Do not disturb mode, notifications cannot be displayed
