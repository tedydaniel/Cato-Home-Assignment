---
title: "Routing with the Cato Client (Split Tunnel Policy)"
slug: "routing-with-the-cato-client-split-tunnel-policy"
updated: 2026-09-02T06:22:28Z
published: 2026-09-02T06:22:28Z
canonical: "knowledge.catonetworks.com/routing-with-the-cato-client-split-tunnel-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Routing with the Cato Client (Split Tunnel Policy)

This article explains how to centrally manage Cato Client traffic routing rules with the Split Tunnel policy.

## Overview

The Split Tunnel policy gives you granular control over how the Cato Client routes remote user traffic. By default, the Client routes traffic through the tunnel to the Cato Cloud to benefit from full security inspection and enforcement, and path optimization over the Cato backbone. However, there may be situations that require adaptive routing, for example, for optimizing the performance of real-time media services or when running alongside third-party vendors.

Use the Split Tunnel Policy to define how the Client routes traffic: to bypass the tunnel and route directly to the Internet destination or inside the tunnel for inspection.

When users are behind a Cato site, traffic routing depends on whether the Client is in Office Mode:

- In Office Mode, the user is treated as behind the site, and traffic is routed according to the Network Rule policy
- When the Client is not in Office Mode, the user is treated as a remote user, and the Split Tunnel policy controls how the Client routes the traffic

### Split Tunnel Rule Settings

Rules are matched based on multiple criteria, including user identity, geolocation, operating system, and Source Network. You can define either inclusive or exception-based rules. For example:

- Identity - Apply routing rules selectively to specific users or user groups
- Device - Select which OS and countries the routing rules apply to
- Source Network - Route traffic based on [managed or unmanaged](/v1/docs/working-with-managed-networks) networks

The Routing Configuration supports:

- User traffic:
  - Forward all traffic to the Cato Cloud, with specific exclusions for internal applications or vendor-hosted resources
  - Route only selected traffic as part of displacing legacy VPN solutions
  - Route only web-bound traffic through the Cato Cloud while allowing other traffic to exit locally
- DNS traffic:
  - Support DNS resolving by a local DNS server for specified domains

For more about DNS and Cato Clients, see [DNS Relay](/v1/docs/working-with-the-dns-relay-service).
  - Support local DNS resolution for domains required by a third-party VPN to prevent DNS conflicts

This level of control allows you to optimize security coverage while minimizing latency and preserving direct access to trusted resources.

### Prerequisites

The following features are currently available only with Windows Client v5.16 and higher

- DNS Exclusions
  - Ensure that the following are allowed access in your local firewall:
    - the IP address 127.0.0.253
    - the Cato Networks DNS service
    - the DNS relay process, dns-relay.exe
- Web-only routing
  - Ensure that the Cato Client has write permissions on the system PAC file

### Policy Revisions and Concurrent Editing by Multiple Admins

The Split Tunnel policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

## Use Cases

### Cato Internet Security with Remote Private Access

ABC Company provisions the Cato Client for their users with Always-on enabled. This means they are connected even when in the office behind their third-party vendor. As the admin, you are confident that traffic for your internal applications is secured by the third-party vendor and is excluded from the Cato Cloud for users in the office. All other traffic is sent to the Cato Cloud for security.

![split_tunnel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33817956480029.png)

You configure two rules in the Split Tunnel Policy to implement this behavior:

![managed_network_exclude.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33817956500381.png)

- Rule 1 is for user traffic that originates from behind **Any Managed Network**, for all ports and protocols. Excluded DNS and Destinations are defined. This excludes the traffic from being routed to the Cato Cloud.
- Rule 2 is for user traffic that originates from behind **Any Unmanaged Network**, for all ports and protocols. There are no exclusions, this traffic is routed to the Cato Cloud.

### Lightweight Internet Security

ABC Company is looking for Cato to only secure web traffic towards SaaS applications and the public Internet. This requires Cato to co-exist with the third-party vendors when users connect from managed and unmanaged networks. This is a lightweight mode that is appropriate for gradually onboarding from a proxy-based architecture to Cato.

**Note:** 3rd party VPNs that comply with Cato's prerequisites should not be interrupted by the Cato Client for Windows in Web-only mode.

![Diagram2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33814614059421.png)

You create a rule in the Split Tunnel Policy that sends all web traffic to the Cato Cloud, and all other traffic is sent through the managed network.

## Configuring the Split Tunnel Policy

The Split Tunnel Policy is an ordered rule base that sequentially checks if a rule is met. When a user meets a rule, the traffic routing settings based on that rule are applied. If no rule is met, traffic is routed through the Cato Cloud, and LAN access is allowed.

The Split Tunnel policy is only applied when the users are connecting via the Client. However, in office mode, the Client detects the Cato site, and the site configuration determines which traffic is steered to the Cato Cloud.

To include IP ranges that are exceptions to the Split Tunnel settings, add the IP ranges to a [Global IP Range](/v1/docs/using-ip-ranges-in-policies) entity.

For more information, see [Including and Excluding Traffic for the Split Tunnel Policy](/v1/docs/including-and-excluding-traffic-for-the-split-tunnel-policy).

**Note:** When Windows SMB Multichannel is enabled on a device, SMB traffic may bypass the Split Tunnel policy and use the Cato tunnel, even when the SMB destination is excluded by the policy.

![Split_Tunnel_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33814614089245.png)

### High-Level Overview of Split Tunnel Policy

These are the settings you can define for the rules in the Split Tunnel policy:

1. General settings (ie. Name, Description).
2. Who the rule applies to ( **Users & Groups**, **Platforms**, **Countries**, and **Source Network**).
3. The scope of traffic to which the rule applies, for example, all traffic or web-only
4. The routing policy for the scope of traffic.

### Creating a Basic Split Tunnel Rule

This section explains how to configure a basic rule in the Split Tunnel policy. It assumes you want to route almost all traffic to the Cato Cloud.

**To configure the Split Tunnel Policy:**

1. From the navigation menu, click **Access > Split Tunnel Policy**.
2. Click **New**.

The **New Split Tunnel Policy Rule** panel opens.
3. Configure the following **General** settings:

Make sure to **Enable** the rule for it to be applied
  - Name
  - Description
  - Position
4. Define to whom the rule applies by defining the:
  - Users and User Groups
  - Platforms
  - Countries
5. Under **Configuration**, configure the following:
  - In the **Select Connection Mode** section, select the scope of the traffic to be included in this rule.
  - Under **Routing Policy**, determine how the scope is routed. Options include
    - **Route all traffic to Cato**: Traffic is routed through the Cato Cloud. You can define exceptions to be routed directly to the Internet.
    - **Route only selected to Cato**: Traffic directly accesses the Internet and bypasses the Cato Cloud. You can define traffic that is included in the tunnel and routed to the Cato Cloud. Blocking outbound LAN access conflicts with this option and cannot be selected.
    - **End-user defined**: Users are able to upload a text file to the Client to configure which traffic is routed through the Cato Cloud and which traffic is excluded from the Cato Cloud. Blocking outbound LAN access cannot be selected with this option.
  - Under **Destination Exclusions**, configure an app, domain, FQDN, or IP range to which the routing policy doesn't apply
6. Determine whether to allow or block **LAN Access**

To avoid traffic routing conflicts between subnets with the same IP address, in the event of a conflict, you can block outbound LAN access. With this option, all traffic is routed to the Cato Cloud, providing increased security. The Client is blocked from connecting to a LAN host in the remote user's home network.
7. Click **Apply**.
8. Repeat steps 2-5 for each rule in the Split Tunnel Policy.
9. Enable the **Split Tunnel Policy** and then click **Save**.

The slider is green when the rule is enabled, and gray when the rule is disabled.

### Customize the Source Network

When creating a Split Tunnel rule, you can determine different routing policies based on the source network, ie, whether it is [managed or unmanaged](urn:resource:component:190799).

When traffic is on an unmanaged network, it will always first go through Cato. For traffic on managed networks, you can determine if the traffic is routed through Cato or directly to the destination.

**Note:** You must enable and configure [managed networks](urn:resource:component:190799) to apply the rules accordingly.

**To customize the source network:**

1. From the navigation menu, click **Access > Split Tunnel Policy**.
2. Create a new rule and configure the settings in steps 2-4 [above](/v1/docs/routing-with-the-cato-client-split-tunnel-policy#h_01KTR7THW0N171NC09AASKR5AK).
3. Under the **Source Network** section, determine if this rule applies to:
  - All networks
  - All unmanaged networks
  - All managed networks
4. Define the connection mode, routing policy, and destinations that are excluded in steps 5-7 [above](/v1/docs/routing-with-the-cato-client-split-tunnel-policy#h_01KTR7THW0N171NC09AASKR5AK).

## Limitations

When working with Web-Only mode in the Split Tunnel Policy, RBI is not supported.

## Using the Cato Client with Microsoft Defender

The Microsoft Defender 'Isolate' feature requires you to send traffic directly to the Windows Defender Cloud IP addresses. By default, the Cato Client sends traffic through the Cato network adapter. However, Microsoft Defender expects the traffic to originate from the Microsoft Defender Adapter, causing a communication failure between Microsoft Defender and Windows Defender Cloud.

To configure Microsoft Defender to work with the Cato Client, define a rule in the Split Tunnel policy to send traffic to the [Microsoft Defender addresses](https://learn.microsoft.com/en-us/defender-cloud-apps/network-requirements).

## User-Defined Split Tunnel Settings

You can let users configure Split Tunnel settings in the Client. Users can upload files with the IP ranges that are included or excluded from the tunnel.

**Note:** This option is not recommended for production environments and should only be used in exceptional cases where centralized policy control is not required.

**To define the IP ranges for Split Tunnel Settings in the Client:**

1. Create a text file with the IP addresses to route through or excluded from the encrypted tunnel.

You can configure the following rules within the text file:

You can use a slash **(/)** or semicolon **(;)** for comments.
  - **Include**: Traffic to the IP range is routed through the encrypted tunnel. All other traffic is routed directly to the Internet. In the text file, add the list of IP address and netmask to route through the encrypted tunnel as follows:

```plaintext
/comment
include
<IP>,<netmask>
<IP>,<netmask>
```

For example:

```plaintext
/splittunnel
include
198.51.100.0,255.255.255.255
```
  - **Exclude**: Traffic to the IP range is routed directly to the Internet. All other traffic is routed through the encrypted tunnel. In the text file, add the list of IP address and netmask to route directing to the Internet as follows:

```plaintext
;comment
exclude
<IP>,<netmask>
<IP>,<netmask>
```

For example:

```plaintext
/splittunnel
exclude
198.51.100.0,255.255.255.255
```
2. On the Windows Client, on the **Settings** screen, click **Upload File** and upload the text file.

On the macOS Client, on the **Settings** screen, select **Split Tunnel Enabled**.
3. On the Windows Client, on the **Settings** screen, select Enable split tunnel.

On the macOS Client, click **Upload Split Tunnel Configuration** and upload the text file.
