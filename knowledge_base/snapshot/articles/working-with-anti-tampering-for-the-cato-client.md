---
title: "Working with Anti-Tampering for the Cato Client"
slug: "working-with-anti-tampering-for-the-cato-client"
updated: 2026-08-23T12:43:50Z
published: 2026-08-23T12:43:50Z
canonical: "knowledge.catonetworks.com/working-with-anti-tampering-for-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Anti-Tampering for the Cato Client

This article provides information about the Anti Tampering mechanism for the Cato Client for Windows.

> [!NOTE]
> Note:
> 
> Available from Windows Client v5.14 and higher. In addition, Windows Client 5.14 installs an additional driver to support Anti-Tampering. This driver is not loaded unless you enable Anti-Tampering.

## Overview

Anti-tampering prevents users from making changes to the Cato Client, that you, as an administrator, do not want them to make. For example, a user might try to disable certain global settings that an admin configured or try to force the Client's process or service to stop. Tampering is usually done for one of the following reasons:

- Malicious actors who want to disable various defense mechanisms so they can carry out their attacks.
- Employees who do not like the limitations imposed by admins and are looking to circumvent those.

Anti-tampering protects the various resources on the hosts from any attempt to alter or disable these defense mechanisms, even if the user has local admin privileges.

### What Does Anti-Tampering Prevent

Anti-Tampering prevents unauthorized modifications of the Client. When Anti-Tampering is enabled, users cannot do the following:

- Edit the Cato Client registry entry
- Modify or create files and directories under:
  - C:\Program Files (x86)\Cato Networks\Cato Client
  - C:\ProgramData\CatoNetworks
- Upgrade or uninstall the Cato Client

Users can contact their admins to receive a code to temporarily disable the different protections.

- To disable Anti-Tampering protection to make changes to the operating system, e.g. edit the registry or uninstall an application, see [Protecting Users with Always-On Security](/v1/docs/protecting-users-with-always-on-security).
- To disable Anti-Tamper protection to enable you to upgrade the Windows Client, respectively, see [Disabling Anti-Tampering Protection to Enable Client Upgrades](/v1/docs/working-with-anti-tampering-for-the-cato-client#disabling-antitampering-protection-to-enable-client-upgrades). (You do not need to disable Anti-Tamper protection if your Clients are automatically upgraded using the [Cato upgrade service](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy))
- To disable Anti-Tamper protection to uninstall the Client, see [Disabling Anti-Tampering Protection to Enable Client Uninstall](/v1/docs/working-with-anti-tampering-for-the-cato-client#disabling-antitampering-protection-to-enable-client-uninstall)

### Use Case

When Anti-Tampering is enforced, users cannot uninstall the Client. However, when the admin wants to uninstall several clients at the same time, it's not possible to ask the admin to bypass each host individually. Instead, they can use the one code for all Clients, which is valid for 2 weeks.

## Disabling Anti-Tampering Protection to Enable Client Upgrades

As part of the Anti-Tampering protections, when Anti-Tampering is enabled, by design, the Client can't be upgraded. To enable an upgrade either manually or using an MDM, there is a specific bypass code that is not connected to disabling Anti-Tampering for the configured duration. You do not need to disable Anti-Tamper protection if your Clients are automatically upgraded using the [Cato upgrade service](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy).

**To disable Anti-Tampering for Client upgrades:**

1. Navigate to **Access > Client Rollout**.
2. Under the relevant client operating system version, copy the **Upgrade code**. If the upgrade policy for that operating system is set to **Managed by the admin**, copy the code to your MDM, or provide the code to a specific user for a manual upgrade.

## Disabling Anti-Tampering Protection to Enable Client Uninstall

As part of the Anti-Tampering protections, when Anti-Tampering is enabled, the Client can't be uninstalled. To enable admins to uninstall the Client either manually or using an MDM, there is a specific bypass code that is not connected to disabling Anti-Tampering for the configured duration.

If you’re not sure if a specific Client has Anti-Tampering enabled, you can still insert the code – if Anti-Tampering is not enabled, the upgrade will still work.

**To disable Anti-Tampering to uninstall the Client:**

1. Navigate to **Access > Client Access**.
2. Under the **Client Uninstall Code** section, copy the **bypass code** to your MDM, or provide the code to a specific user for a manual uninstall.

## Configuring Exclusions for Anti-Tampering

In specific, controlled scenarios, you may need to allow trusted tools or workflows to interact with protected components. Anti-tampering exclusions let you explicitly allow these actions without disabling anti-tampering entirely, helping you maintain protection while avoiding operational disruption.

You should use anti-tampering exclusions sparingly and only for well-understood, validated use cases, because overly broad exclusions weaken your security posture.

### Use Case

ABC Company uses several endpoint management and security tools that need to interact with protected endpoint components as part of normal operations. For example, the IT team uses a trusted software deployment tool to install updates and perform maintenance on managed endpoints.

When anti-tampering is enabled, these tools attempt to modify protected services and files, and their actions are blocked. This prevents the updates from completing successfully and causes operational disruption.

To address this, the IT team creates a targeted anti-tampering exclusion for the specific trusted process used by the deployment tool. The exclusion allows the tool to perform the required actions, while anti-tampering continues to protect all other components and processes on the endpoint.

### Configuring Exclusions

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(189).png)

**To configure an Anti-Tamper exclusion:**

1. From the navigation menu, select **Access > Always-On Policy** and click the **Anti Tamper Exclusions** tab.
2. Click **New** and configure the following:
  - Name and description of the rule
  - Under Users/Groups, define who the rule applies to
  - Under **Objects**, configure the:
    - **Path** - Select what you are excluding (for example, a process or file path)
    - **(Optional)** Enable **Verify Signature** for the process. This is recommended for security best practices
      - **Thumbprint Hash** - Enter the exact hash for the process
3. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
4. Click **Publish**. A confirmation window opens, click **Publish**.
