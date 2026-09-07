---
title: "Remote Internet Security with One-Time Authentication"
slug: "remote-internet-security-with-one-time-authentication"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/remote-internet-security-with-one-time-authentication"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remote Internet Security with One-Time Authentication

This article explains how to use Cato features to provide users with Remote Internet Security with One Time Authentication and secured private access on demand.

## Overview

Cato can provide users with secured remote Internet access after one-time authentication. This means users always have Internet connection and protection with minimal interaction with the Client. Access to your private network (WAN) can be provided on demand.

This is configured by defining the level of authentication users require for secured access to either the Internet or your private network (WAN). For example, you can always allow users to have secured access to the Internet after their initial authentication, but only allow access to your private network (WAN) after a user re-authenticates.

In addition, you can control the user re-authentication experience. A prompt can be displayed to users either before or after the authentication token expires.

### Configurations for Secured Access to the Internet or Private Network (WAN)

Remote Internet Security with One Time Authentication is enabled by defining the user **Confidence Levels** and the level of access (**Action**) in [Client Connectivity Policy](/v1/docs/what-is-the-client-connectivity-policy) rules. The Confidence Level describes how reliable the user's authentication is. The **Action** defines if the user can access the Internet and private network (WAN) or only the Internet.

#### Understanding Confidence Levels

The Confidence Level describes how reliable the user's authentication is. The Confidence Levels are:

- **High:** The user is authenticated to the Client, and the [Cato token](/v1/docs/sso-authentication-for-users-with-cato) is valid
- **Low:** The user has authenticated to the Client, but the Cato token has expired
- **Any:** The user has authenticated to the Client, and the Cato token is either valid or expired

Confidence levels are applied to users after authenticating with any authentication method. The Cato token never expires for users who authenticate with a Username and Password or Registration codes. These users always have a **High** confidence level.

#### Understanding Actions

The **Action** defines the level of access provided to the user. The Actions are:

- **Allow WAN and Internet:** The user has secured Internet access and can access the private network (WAN)

**Note:** This option provides permission for a user to access the private network (WAN). A user's access to the private network (WAN) is dependent on rules in the [WAN Firewall](/v1/docs/managing-the-wan-firewall-policy).
- **Allow Internet only:** The user only has secured Internet access and cannot access the private network (WAN)

Unsupported Client OS and versions triggering this action will be blocked.

**Note:** This option provides permission for a user to access the Internet. A user's access to the Internet is dependent on rules in the [Internet Firewall](/v1/docs/managing-the-internet-firewall-policy).

This Action also includes the option to **Terminate active WAN sessions**. This option applies when a user was previously allowed WAN access under one rule, but their circumstances change and they now match only a rule that allows Internet access. In this case, you can choose whether to terminate the user’s existing WAN sessions.

For example, a user is granted WAN access based on their confidence level. If that condition later changes, such as when the token expires, the user is no longer allowed to access the WAN. This setting determines whether their current WAN sessions are disconnected.
- **Block WAN and Internet:** The user is blocked from accessing the Internet and WAN

Existing WAN sessions are always terminated once a user meets a rule with this action.

### Prerequisites

- Windows Client v5.9 and higher, or macOS Client v5.10 (and higher)
- Users must be assigned an SDP license to have secure internet access
- Users must authenticate and have a valid token at least once for confidence levels to be enforced

## Use Cases

### Use Case - Secured Internet Access After Authenticating Once

A publishing company has sales reps who work remotely that rarely need access to the company WAN.

The company creates these rules for the sales rep user group:

- In their Always-On policy they ensure the Client connects with anyone working remotely
- In the Client Connectivity Policy, they let users with a Low Confidence Level access the Internet

When sales reps arrive at a prospect, they are securely connected to the Internet without any interaction with the Cato Client.

![Low_Confidence_Level.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144793410461.png)

### Use Case - Re-Authentication Always Required

A bank has strict Internet security requirements and needs to always ensure that users remotely accessing the Internet and private network (WAN) are authenticated.

The company creates these rules for all remote users:

- In their Always-On policy to ensure the Client always connects
- In the Client Connectivity Policy, they provide access to the Internet and private network (WAN) to users with a High Confidence level.

When a user connects remotely, they must authenticate before they can access the Internet or private network (WAN).

![High_Confidence.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144767853213.png)

## Configuring Remote Internet Security with One-Time Authentication

Follow these steps to enable Remote Internet Security with One-Time Authentication:

1. Define a rule in your Always-On policy so that the Client always connects to the Cato Cloud protecting users and devices.
2. Define a rule in your Client Connectivity policy that defines the level of access based on the user's **Confidence Level**.
3. Configure how users are prompted to re-authenticate to provide the best experience for your users.

### Step 1: Applying the Always-On Policy to Always Protect Remote Users

The Always-on Policy enhances Internet security by defining rules for when users or User groups always connect to the Cato Cloud. This ensures all traffic goes through a PoP and Cato security engines inspect the traffic to ensure it complies with your security policies.

For more information on how to create a rule in your Always-On policy, see [Protecting Users with Always-On Security](/v1/docs/protecting-users-with-always-on-security).

If you already have a rule for the relevant user groups in your Always-On policy, this step is not required.

### Step 2: Configure Client Connectivity Policy to Provide Access Based on Confidence Level

The Client Connectivity policy secures your network by ensuring devices or users only connect when they comply with the organizational security requirements.

Including the Confidence Level and Actions in a Client Connectivity Policy rule lets you define the access available to users and User groups based on how reliable their authentication is.

For more information on how to manage network access in your Client Connectivity Policy, see [Configuring the Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy).

Client Connectivity Policy rules can only be applied to users with an SDP License.

![CCP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144793446301.png)

**To configure access based on Confidence Level:**

1. From the navigation menu, click **Access > Client Connectivity Policy**.
2. Click **New**. The **New Rule** panel opens.
3. Configure the scope of the rule:
  1. Define the **Confidence Level**
  2. Define the **Action**
4. Click **Apply** and then click **Save**.

> [!NOTE]
> Note:
> 
> As a best practice, create a final rule for any User or Group with a Confidence Level of **Any** and the **Allow Internet** action. This provides any user that has not matched a higher priority rule with secured Internet access.

### Step 3: Define the User Experience for Re-authenticating

You can choose when the Client prompts users to re-authenticate. For example:

- If a user only needs secured Internet access and does not need regular access to your private network (WAN), they do not need to be disturbed by prompts to re-authenticate.
- If a user always needs access to your private network (WAN), they can receive prompts to re-authenticate before and after the authentication token expires so that their access is not blocked.

If you configure **Any** or **Low** confidence level with the action **Allow WAN and Internet**, the user is not prompted to re-authenticate after the token expires, and is granted full access with an expired token. For more information about available authentication methods, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients).

![When_to_Auth.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144745420189.png)

**To define when users are prompted to re-authenticate:**

1. From the navigation menu, click **Access > User Authentication**.
2. Click the **Additional Settings** tab.
3. Choose when users are prompted to re-authenticate.

**Note:** You can choose, one, both, or neither options. If you leave both options unchecked, the user does not receive any prompts to re-authenticate.
4. Click **New**.

## Monitoring the User Confidence Level and Network Access

You can monitor the confidence level of users at any time from the **Access > Users** page. The current confidence level of a user is displayed in the **SDPO Users Activity** tab (the column may be hidden).

An event is also created whenever the Client Connectivity Policy allows a user to connect. For more information, see [Configuring the Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy).

## Understanding the User Experience

The Client displays the level of access permitted to the user based on how reliable their authentication is. Depending on the level of access permitted, Secured Private Access and Secured Internet Access are listed with a check or exclamation mark.

| If the Client has access to both the private network (WAN) and Internet | If the Client only has access to the Internet: ![Internet_Only.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144778680733.jpeg) |
| --- | --- |

![Trust_Level_Client_Auth.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144793614493.jpeg)

## Advanced Configurations

Enabling Remote Internet Security with One Time Authentication has impacts on other features.

### DNS Configuration

The internal DNS for your account are ignored for users granted access only to the Internet.

If a user has only Internet access, the Cato Internet DNS (10.254.254.1) is used as their primary DNS and their secondary DNS is 8.8.8.8.

**Note**: DNS Forward Rules are still applied by default. This behavior can be changed on a per-user or per-account basis. For more information, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

### Office Mode

You can configure users with Always-On enabled to require authentication to Cato when the Client is connected in Office Mode. For more information, see [Protecting Users with Always-On Security](/v1/docs/protecting-users-with-always-on-security).

A user configured in a Client Connectivity Policy rule that allows access to the Internet with a Low Confidence Level (Cato Authentication token expired) does not need to authenticate in Office Mode. The Client Connectivity Policy configuration overrides the Always-On configuration in Office Mode.

### Pre-Login

Pre-Login configurations are not impacted by configurations for Remote Internet Security with One Time Authentication. Before users authenticate, traffic is routed as follows:

- Clients with Always-On enabled are only allowed to connect to resources defined in Allowed Destinations, Internet traffic is blocked.
- Clients without Always-On enabled can connect to resources defined in Allowed Destinations and access unsecured Internet access.

For more information about Pre-Login, see [Using Windows Pre Login and the SDP Client](/v1/docs/using-windows-pre-login-and-the-sdp-client).

### Technical Details

Remote Internet Security with One Time Authentication is enabled using configurations in the [Always-On policy](/v1/docs/protecting-users-with-always-on-security) and the [Client Connectivity Policy](/v1/docs/what-is-the-client-connectivity-policy),

After users authenticate and the authentication token is valid, all traffic passes through the Cato PoP and is inspected by Cato's [security engines](/v1/docs/security) in accordance with your security policies.

After the authentication token expires, you can allow Internet traffic to continue to pass through the Cato PoP. This provides continuous secure Internet access even though the user is unauthenticated. For secured private access, users are still required to re-authenticate to gain access according to your WAN Firewall policy.
