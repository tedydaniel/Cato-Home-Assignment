---
title: "Routing Traffic Through a Site Web Proxy (EA)"
slug: "routing-traffic-through-a-web-proxy"
status: "update"
updated: 2026-09-03T12:43:37Z
published: 2026-09-03T12:43:37Z
canonical: "knowledge.catonetworks.com/routing-traffic-through-a-web-proxy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Routing Traffic Through a Site Web Proxy (EA)

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

## Overview

Site Web Proxy extends Secure Web Gateway (SWG) protection to devices behind a site that cannot install the Cato Client, such as servers, shared kiosks, and OT/IoT devices. You can route HTTPS traffic from these devices to the Cato Cloud for inspection and policy enforcement by configuring the device’s proxy settings, either manually or with a standard PAC file. This lets you apply existing Internet security policies to agentless and unmanaged devices without installing the Client.

With the Site Web Proxy, traffic is processed as follows:

1. **Configure the Device Proxy Settings**: Configure the device to point to the proxy FQDN and port. The recommended method to do this is with a PAC file, although it can also be done manually.
2. **Request is sent to the proxy:** The device sends the request through the Site tunnel to the proxy in the Cato PoP instead of directly to the destination.
3. **(Optional) User is authenticated, and security policies applied:** The proxy instance can support authenticated or unauthenticated traffic. For an authenticated proxy, Kerberos associates the session with a user, and any matching security policies for the user are applied. Unauthenticated proxy instances are also supported for governed Internet access for devices and services that don’t support Kerberos authentication.
4. **(Optional) Traffic inspected:** Based on your security policy configurations, traffic from the device is inspected by Cato’s security engines.
5. **Traffic is forwarded:** The proxy forwards the request to the Internet destination.
6. **The response returns through the proxy:** The session is logged, and the destination’s response is relayed to the device.

Each proxy instance is associated with selected sites or all sites. It uses a unique port and has its own ordered rulebase. Kerberos and no-authentication proxy instances can coexist in your account, however, the Site and Port combination must be unique to each instance.

### Use Case

Company ABC operates in a regulated industry and must inspect outbound web traffic from every device on its network. Its environment includes shared kiosks, production servers, and IoT devices that can’t run the Cato Client.

Company ABC deploys Site Web Proxy and distributes a PAC file to the relevant devices. Devices that support Kerberos use an authenticated proxy instance that associates traffic with the user. Devices that can’t authenticate use a separate no-authentication proxy instance.

Based on the proxy configuration defined in the PAC file, the device's browser sends web traffic to the Site Web Proxy, where the traffic is inspected and the configured Internet security policies are applied. This allows Company ABC to centralize its security and compliance controls without installing the Cato Client on every device.

## Configuring the Site Web Proxy

To configure the Site Web Proxy, you need to:

1. Map user identity attributes for the Cato SCIM Application in Microsoft Entra (Only required for a proxy instance with Authenticated traffic)
2. Create a proxy instance
3. Define the ordered network rules to govern traffic through the proxy
4. Configure the proxy settings of the device

Both authenticated (Kerberos) and unauthenticated proxy instances can coexist in your account. Each proxy instance maintains its own network rule set.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(53).png)

### Step 1: Mapping User Identity Attributes for the Cato SCIM Application

Extend the Entra SCIM provisioning schema to synchronize the following attributes from Microsoft Entra ID into the Cato SCIM application:

- **onPremisesSamAccountName:** The legacy Windows logon name. It is used by Windows authentication and legacy applications that require the sAMAccountName attribute
- **onPremisesDomainName:** The fully qualified domain name (FQDN) of the on-premises Active Directory domain associated with the user account. It is used together with `onPremisesSamAccountName` to identify the user during Kerberos authentication.

> [!NOTE]
> Note:
> 
> - This configuration must be applied before user provisioning begins. If this is not possible, run the synchronization to the Cato SCIM application once the configuration is applied
> - Before editing the schema, it is recommended to save a copy of the JSON document. This allows you to restore the original configuration if an error occurs
> - If you are only configuring proxy instances with unauthenticated traffic, this step is not required
> - The exact names shown in the schema can vary depending on the Microsoft Entra provisioning template version. Use the examples below as references and locate the equivalent Entra source, Cato target, and user-provisioning mapping objects in your schema

**To map user identity attributes:**

1. In the [Entra Admin Center](https://entra.microsoft.com/), navigate to **Enterprise Applications**.
2. Open the **Cato Networks** **SCIM** application.
3. Click on **Provisioning** then **Edit Provisioning**.
4. Expand the **Mapping** section and click **Provision Azure Active Directory Users**, then **Show advanced options**.
5. Click **Review your schema here**. A JSON schema document opens.
6. To expose the Entra source attributes so they can be used in provisioning mappings, using Ctrl+F, search for `"name": "Microsoft Entra ID'`.
7. Identify the `"attributes"` array (directories[] > "Microsoft Entra ID" > objects[] > User > attributes[]), the final attribute object is `onPremisesSecurityIdentifier` .
8. Add a comma after the final attribute and paste the following entries before the closing ]

**Entries to expose the Entra source attributes**

```json
{
  "anchor": false,
  "caseExact": false,
  "defaultValue": null,
  "flowNullValues": false,
  "multivalued": false,
  "mutability": "ReadWrite",
  "name": "onPremisesSamAccountName",
  "required": false,
  "type": "String",
  "apiExpressions": [],
  "metadata": [],
  "referencedObjects": []
},
{
  "anchor": false,
  "caseExact": false,
  "defaultValue": null,
  "flowNullValues": false,
  "multivalued": false,
  "mutability": "ReadWrite",
  "name": "onPremisesDomainName",
  "required": false,
  "type": "String",
  "apiExpressions": [],
  "metadata": [],
  "referencedObjects": []
}
```
9. To add the corresponding target SCIM extension attributes to the Cato SCIM schema, locate the Cato target directory. Search for either `"name": "Cato Networks Provisioning"` or `"name": "CatoNetworks"`. If neither is present, search for `"catonetworks"` and locate the Cato user object’s `attributes` array.
10. Add a comma after the final attribute and paste the following entries before the closing ]

**Entries to add the corresponding target SCIM extension attributes**

```json
{
  "anchor": false,
  "caseExact": false,
  "defaultValue": null,
  "flowNullValues": false,
  "multivalued": false,
  "mutability": "ReadWrite",
  "name": "urn:ietf:params:scim:schemas:extension:catonetworks:2.0:User:sAMAccountName",
  "required": false,
  "type": "String",
  "apiExpressions": [],
  "metadata": [],
  "referencedObjects": []
},
{
  "anchor": false,
  "caseExact": false,
  "defaultValue": null,
  "flowNullValues": false,
  "multivalued": false,
  "mutability": "ReadWrite",
  "name": "urn:ietf:params:scim:schemas:extension:catonetworks:2.0:User:onPremisesDomainName",
  "required": false,
  "type": "String",
  "apiExpressions": [],
  "metadata": [],
  "referencedObjects": []
}
```
11. To create the synchronization mappings between Entra attributes and Cato SCIM attributes, locate the user-provisioning mapping from Microsoft Entra ID to Cato. Search for either `"Provision Azure Active Directory Users"` or `"Provision Microsoft Entra ID Users"`, then find that object’s `attributeMappings` array.
12. At the end of that array, find the last }, add a comma paste the following entries before the closing ]

**Entries to synchronize mapping between Entra and Cato SCIM attributes**

```json
{
  "defaultValue": "",
  "exportMissingReferences": false,
  "flowBehavior": "FlowWhenChanged",
  "flowType": "Always",
  "matchingPriority": 0,
  "targetAttributeName": "urn:ietf:params:scim:schemas:extension:catonetworks:2.0:User:sAMAccountName",
  "source": {
    "expression": "[onPremisesSamAccountName]",
    "name": "onPremisesSamAccountName",
    "type": "Attribute",
    "parameters": []
  }
},
{
  "defaultValue": "",
  "exportMissingReferences": false,
  "flowBehavior": "FlowWhenChanged",
  "flowType": "Always",
  "matchingPriority": 0,
  "targetAttributeName": "urn:ietf:params:scim:schemas:extension:catonetworks:2.0:User:onPremisesDomainName",
  "source": {
    "expression": "[onPremisesDomainName]",
    "name": "onPremisesDomainName",
    "type": "Attribute",
    "parameters": []
  }
}
```
13. Click **Save**. A Schema Text Editor save successful message is displayed. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(74).png)
14. In the Cato Networks SCIM application, click on **Provisioning** then **Edit Provisioning**.
15. Expand the **Mapping** section and click **Provision Azure Active Directory Users**, then **Show advanced options**.
16. After a few minutes, ensure these mappings appear:
  - sAMAccountName → onPremisesSamAccountName
  - onPremisesDomainName → onPremisesDomainName

### Step 2: Creating a Proxy Instance

The proxy instance defines the sites, endpoint, and authentication method. The supported authentication options are:

- **Kerberos:** The proxy authenticates each request against the identity in the device’s Kerberos ticket, tying every session to a specific user. This enables user-based policies to be applied. To use Kerberos authentication, generate a **KEYTAB** file on the Kerberos Key Distribution Center (KDC). The KEYTAB file contains the secrets that allow the Cato PoP to validate Kerberos tickets and verify the user's identity.
- **No Authentication:** The proxy does not apply user authentication. User-based policies are not applied.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image-1783949253027.png)

**To create a proxy instance:**

1. From the navigation menu, select **Resources > Site Web Proxy**.
2. Click **New,** then **New Proxy**.
3. Add a name for the proxy instance and choose the site(s) to associate with the proxy.
4. Enter the FQDN that devices use to connect to the proxy and a port for the proxy instance. **Note:** The **Corresponding IP** is displayed for DNS resolution. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(67).png)
5. Select the **Authentication Method.** ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(68).png)
6. If **Kerberos** is selected as the **Authentication Method**, upload the KEYTAB file. If you are creating an unauthenticated proxy instance, this step is not required.
7. Click **Apply and Create Rule**. The Proxy instance is created.

### Step 3: Defining Network Rules

Once the proxy instance is created, define its network rules. Each rule consists of a source, a destination, and an action. The available actions depend on the **Authentication Method** of the proxy instance.

- A Kerberos proxy instance supports these actions:
  - **Authenticate:** Traffic requires Kerberos authentication
  - **Allow:** Traffic is permitted without authentication. Use an **Allow** rule when specific devices, services, or destinations can bypass authentication. **Allow** rules must be ordered above any **Authenticate** rules **Note:** The **Allow** action refers to Kerberos authentication. Unauthenticated traffic is inspected by security engines and may be blocked by a security policy.
- For an unauthenticated proxy instance, only the Allow action is available

Traffic that doesn’t match a rule in the Site Web Proxy rulebase is blocked by the final system rule.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(55).png)

**To define a network rule:**

1. From the navigation menu, select **Resources > Site Web Proxy**.
2. Click **New,** then **New Proxy Rule**. The **New Proxy Rule** panel opens. **Note:** If you are defining a network rule immediately after creating a proxy instance, the **New Proxy Rule** panel is automatically displayed.
3. Enter a **Name** for the rule, choose the **Proxy** the rule applies to, and choose the **Position** of the rule within the rulebase.
4. Add the **Source** to be enforced by the rule. The supported sources are IP addresses or Network subnets. **Note:** To apply the rule to all Sources, leave this section blank.
5. Define the **Destinations** the rule applies to. **Note:** To apply the rule to all Destinations, leave this section blank.
6. Choose the **Action** that is applied by the rule.
7. Click **Apply**.
8. Click **Publish**.
9. Set the **Site Web Proxy** toggle to **Enabled**.

### Step 4: Configure the Proxy Settings of the Device

Configure the device's proxy settings to send web traffic to the Site Web Proxy. The recommended method is to use a PAC file, though it can also be done manually.

**To configure the proxy settings of the Device:**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(64).png)

1. Configure the FQDN of the device to the Proxy FQDN you configured when you created the Proxy instance. This is listed in the **Proxy FQDN** column of the proxy instance.
2. Configure your DNS server to resolve the FQDN to Cato’s IP address. This is listed in the **Proxy FQDN** column of the proxy instance. By default, the proxy IP address is **10.254.254.7**.

## Known Limitations

- Kerberos authentication is supported with Microsoft Active Directory and Microsoft Azure
- Only HTTPS requests are supported (HTTP is planned to be supported when this feature is release for General Availability)
- To support Remote Browser Isolation (RBI), an additional configuration on the PAC file to skip http://rbi.catonetworks.com from the proxy is required. For more information, see [Configuring the RBI Service for Browsing Sessions](/v1/docs/configuring-the-rbi-service-for-browsing-sessions).
- Site Web Proxy activity is tracked using enriched Internet Firewall events, which identify successful proxy connections. Dedicated Site Web Proxy event types are not currently available
