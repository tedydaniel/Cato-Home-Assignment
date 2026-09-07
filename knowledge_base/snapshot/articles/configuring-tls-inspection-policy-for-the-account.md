---
title: "Configuring TLS Inspection Policy for the Account"
slug: "configuring-tls-inspection-policy-for-the-account"
updated: 2026-08-23T12:53:01Z
published: 2026-08-23T12:53:01Z
canonical: "knowledge.catonetworks.com/configuring-tls-inspection-policy-for-the-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring TLS Inspection Policy for the Account

This article discusses how to configure and customize the TLS Inspection policy to meet the specific requirements of your network.

## Overview of the Cato TLS Inspection Policy

Today most network traffic is encrypted (TLS, HTTPS), which often minimizes the benefit of scanning traffic with IPS, Internet firewall, Application Control Policy, and Anti-Malware traffic. If the traffic contains malicious content, it is also encrypted and the Cato security engines can't inspect or scan it.

When you enable TLS Inspection for your account, Cato securely decrypts traffic that passes through a PoP and the Cato security engines inspect it for malware and scan downloaded files. If the content of the traffic is confirmed as safe, Cato then re-encrypts the traffic and forwards it to the destination. However, if the content contains actual or suspected malware, then the Cato security engines block the traffic.

You can choose to use the default Cato policy that inspects all traffic. You can also create specific TLS Inspection rules that define which traffic is inspected and which traffic bypasses TLS Inspection.

![tlsinspection.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468554386589(1).png)

> [!NOTE]
> Note:
> 
> By default, TLS Inspection is bypassed for these operating systems:
> 
> - Android (due to issues related to certificate pinning)
> - Linux
> - Unknown operating systems

### Cato Default Bypass Rules for Applications

Cato includes several applications in an implicit bypass rule that are automatically excluded from TLS Inspection. For a list of these applications, see below [Default Bypass Rules](/v1/docs/configuring-tls-inspection-policy-for-the-account#h_01K74C0WN796838Y6JAVCH1PAN).

### Latency for TLS Inspection

Some minimal latency is expected at the initial connection due to the TCP and TLS handshakes that occur before data can flow to the appropriate network or security engine in the PoP. This latency is up to 10 milliseconds per packet.

### Working with an Ordered TLS Inspection Rule Base

The TLS Inspection engine inspects connections sequentially, and checks to see if the connection matches a rule. The final rule in the rule base is a default implicit ANY - ANY Inspect rule - so if a connection does NOT match a rule, then it is automatically inspected.

You can review the default rule settings in the **Default Rules** section at the end of the rulebase. The rule settings can't be edited except for the Untrusted Server Certificate action. For more about the Untrusted Server Certificate action, see below [Adding Rules to Customize the TLS Inspection Policy](/docs/configuring-tls-inspection-policy-for-the-account#UUID-a3b5b8ee-0328-fa47-fd6d-785d2094331c_N1713360059811).

Rules that are at the top of the rule base have a higher priority because they are applied to connections before the rules lower down in the rule base. For example, if a connection matches on rule #2, the action for this rule is applied to the connection and the TLS Inspection engine stops applying the policy to this connection. This means that rules #3 and below aren't applied to the connection.

### Policy Revisions and Concurrent Editing by Multiple Admins

The TLS Inspection Policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### RBAC for Policy Management

The TLS Inspection policy supports configuration of sub-policies that let you assign RBAC for a set of rules to give admins autonomy over the areas they’re responsible for, while preserving centralized control and security boundaries. For more information see [Configuring RBAC for Policy Management](/v1/docs/configuring-rbac-for-policy-management).

### Working with the TLS Inspection Configuration Wizard

The TLS Inspection Configuration Wizard autonomously reviews your policy using these checks and insights. When a check fails, you can review and update your policy directly in the Wizard without editing individual rules. This helps you stay secure while simplifying policy management. For more information, see [Using the Configuration Wizard](/v1/docs/using-the-configuration-wizard).

## Understanding the TLS Inspection Policy

Use the **TLS Inspection Policy** page to configure the TLS Inspection policy for all traffic in your account.

**Working with Multiple Items**

When there are multiple items in a **Source**, or a **What** field, such as two groups or categories, then there is an OR relationship between these items.

![multi-tlsrules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468566932125(1).png)

**Installing the Cato Root Certificate on End-user Devices**

The Cato root certificate must be installed as a trusted certificate on every device and computer that connects to the Cato Cloud. For more information about installing the Cato certificate, see [Installing the Root Certificate for TLS Inspection](/v1/docs/installing-the-root-certificate-for-tls-inspection).

- The Cato certificate can't be installed on most embedded operating systems (OS), therefore many devices using embedded OS lose connectivity when TLS Inspection is enabled. For more about which OS Cato supports for TLS Inspection, see [Best Practices for TLS Inspection](/v1/docs/best-practices-for-tls-inspection).

### Enforcing TLS Versions and Cipher Suites

By default, all TLS versions and cipher suites are allowed. To block outdated and insecure TLS versions or prevent the use of weak cipher suites in encrypted traffic the TLS Inspection policy can enforce the minimum TLS protocol versions and cipher suite strength for traffic in your account.

Cipher suite configuration options are divided into three levels, based on Mozilla’s recommended settings. Some TLS versions are not compatible with certain levels. For more information and a list of cipher suites in each level, see the [Mozilla documentation](https://wiki.mozilla.org/Security/Server_Side_TLS).

### Blocking QUIC and GQUIC Traffic for TLS Inspection

QUIC and GQUIC are transport protocols developed by Google that don't operate over TCP connections, and traffic using these protocols can't be inspected by the TLS Inspection service. Therefore we recommend that accounts that enable TLS Inspection block QUIC and GQUIC traffic using Internet Firewall rules. The rules that block this traffic force the flow to only connect using protocols that can be inspected by the TLS Inspection service. If you allow traffic using the QUIC and GQUIC protocols, the flows can't be inspected and are unnecessarily blocked.

The first time you enable the TLS Inspection policy, rules to block QUIC and GQUIC traffic are automatically added to the Internet Firewall policy. If the Internet Firewall policy already blocks QUIC traffic so that it can be correctly inspected, then no new rules are added.

For more about QUIC and GQUIC traffic, see [Internet and WAN Firewall Policies – Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies).

## Configuring the TLS Inspection Policy

When you configure the TLS Inspection policy, you can enable the default Cato TLS Inspection policy or customize the policy by adding your own rules.

### Using the Default TLS Inspection Policy

The default Cato TLS Inspection policy inspects all traffic (except for the applications that are automatically bypassed). You can use the default policy by enabling TLS Inspection and there is no need to add any rules to the policy.

There is a final implicit rule that matches all traffic with the **Inspect** action.

**To use the default Cato TLS Inspection policy:**

1. From the navigation menu, click **Security > TLS Inspection**.
2. Click the **Enable TLS Inspection** slider.
3. Click **Save**. TLS inspection is enabled using the default policy.

### Adding Rules to Customize the TLS Inspection Policy

You can customize the TLS Inspection policy to only inspect the specific traffic types according to the needs of your organization. Add rules to the policy with **Inspect** and **Bypass** actions to define which traffic is decrypted and inspected.

- Create rules with the **Inspect** action to define the traffic that the Cato Cloud inspects for suspicious and malicious content.
- Create rules with the **Bypass** action to exclude specific traffic from the Cato TLS inspection engines. For example, you can add a bypass rule for the RingCentral application to exclude RingCentral traffic from TLS Inspection.

When creating rules, use **Source** and **What** to define the scope of the TLS traffic and **Action** to configure whether the rule inspects or bypasses traffic. Make sure that the bypass rule has a higher priority (closer to the top of the rulebase) than an inspect rule that matches the same traffic. Traffic that matches a TLS Inspection bypass rule is also excluded from security scans by the Anti-Malware engines.

When you configure a rule with the **Inspect** action, you also must define the behavior for how the rule handles untrusted server certificates.

![TLSi_Untrusted_Cert_New.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468519172125(1).png)

These are the options for this setting:

- **Allow** - The traffic is allowed to the site with an untrusted certificate, and inspected (this is the default setting).
- **Prompt** - The users are shown a prompt asking them to confirm that they want to continue and go to the site with an untrusted certificate. If the user continues to the site, the traffic is inspected
- **Block** - Traffic to the site with an untrusted certificate is blocked

> [!NOTE]
> Note:
> 
> For applications that use certificate pinning to prevent TLS inspection, add them to a bypass rule so they will function correctly for the end users.

**To add rules to the TLS inspection policy:**

1. From the navigation menu, click **Security > TLS Inspection**.
2. Click **New**.
3. Enter a **Name** for the rule.
4. Use the **Enabled** toggle to enable or disable the rule.

The toggle is green ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468519203613(1).png) when enabled.
5. Configure the **Rule Order** for this rule.
6. Expand **Source** and select the source type.
  - Select the type (for example: Host, Network Interface, IP, Any). The default value is **Any**.
  - When needed, select a specific object from the drop-down list for that type.
7. In the **Criteria** section, configure the **Platforms**, **Countries**, **Device Posture Profiles** , and **Connection Origin** required to match this rule.

For more about Device Conditions, see [Adding Device Conditions for TLS Inspection](/v1/docs/adding-device-conditions-for-tls-inspection).
8. Define the **Destination** the rule applies to. For example, a service, an application, a custom or predefined category.
9. Choose the minimum **TLS Version and Cipher Suites**.

**Note**: Some TLS versions are incompatible with cipher suite levels. For more information, see [Enforcing TLS Versions and Cipher Suites](/v1/docs/configuring-tls-inspection-policy-for-the-account#h_01K74C0WN6GF1E35Q3V7EZ8W9W)
10. Configure the **Action** by selecting **Inspect** or **Bypass**.
  - If you select **Inspect**, from the **Untrusted Server Certificates** drop-down menu, select the action for traffic with problematic certificates: **Allow**, **Block**, or **Prompt**. The default value is **Allow**.
11. Click **Apply**.
12. Click **Save**. The TLS Inspection rule is saved in the rulebase.

## Default Bypass Rules

Cato manages default TLS Inspection rules that bypass specific apps, operating systems, and clients that may cause issues. These rules are positioned at the top of the rulebase and can't be edited. To help you plan and make decisions for the TLS Inspection policy, you can view the settings for these rules in the **Default Bypass Rules** section.

When there are multiple items in the What field, such as an Application and FQDN, then there is an AND relationship between these items.

![TLSi_Default_Bypass_Rules.png](https://support.catonetworks.com/hc/article_attachments/27468554647325)

## Related Resources

- [Best Practices for TLS Inspection](/v1/docs/best-practices-for-tls-inspection)
- [Supported TLS Cipher Suites for Cato TLS Inspection](/v1/docs/supported-tls-cipher-suites-for-cato-tls-inspection)
