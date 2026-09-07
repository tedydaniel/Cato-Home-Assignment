---
title: "Cato IPsec Guide: IKEv1 vs IKEv2"
slug: "cato-ipsec-guide-ikev1-vs-ikev2"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/cato-ipsec-guide-ikev1-vs-ikev2"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato IPsec Guide: IKEv1 vs IKEv2

## IPsec Site Best Practices - Migrating to IKEv2

In general, Cato recommends that you use IPsec IKEv2 sites as a best practice. Some of the improvements with IKEv2 are listed below:

1. IKEv2 increases efficiency by reducing the number of messages that must be exchanged to setup a VPN tunnel. Tunnels are setup faster and with less bandwidth.
2. IKEv2 is more reliable. There’s a built-in liveness check in IKEv2 to detect when the tunnel goes down.
3. IKEv2 protects against DoS attacks. Unlike in IKEv1, an IKEv2 responder doesn’t have to perform significant processing until the initiator proves it can receive messages at its advertised IP address.
4. NAT-T is built-in. NAT-T, or NAT Traversal, is required when a VPN endpoint resides behind a router that performs NAT. IPsec tunnels send data using the Encapsulating Security Payload (ESP) which is not compatible with NAT. Therefore, NAT-T is used to encapsulate the ESP packets in UDP which can then be routed over NAT.

For more information on the benefits of using use IPsec IKEv2 sites, see [RFC 4306](https://tools.ietf.org/html/rfc4306).

### Similarities Between IKEv2 and IKEv1

Below is a comparison of strongSwan configurations for IKEv1 and IKEv2 tunnels. [strongSwan](https://www.strongswan.org/) is an open-source IPsec solution for multiple operating systems, including Windows and macOS.

| **IKEv1** | **IKEv2** |
| --- | --- |
| ```plaintext conn cato-vpn auto=add compress=no type=tunnel keyexchange=ikev1 fragmentation=yes forceencaps=yes ike=aes256-sha1-modp1024 esp=aes256-sha1 dpdaction=clear dpddelay=300s rekey=no left=172.16.1.62 leftid=54.183.180.107 leftsubnet=172.16.1.0/24 right=45.62.177.115 rightid=45.62.177.115 rightsubnet=172.17.3.0/24 authby=secret ``` | ```plaintext conn cato-vpn auto=add compress=no type=tunnel keyexchange=ikev2 fragmentation=yes forceencaps=yes ike=aes256-sha1-modp1024 esp=aes256-sha1 dpdaction=clear dpddelay=300s rekey=no left=172.16.1.62 leftid=54.183.180.107 leftsubnet=172.16.1.0/24 right=45.62.177.115 rightid=45.62.177.115 rightsubnet=172.17.3.0/24 authby=secret ``` |

The only difference is a single number. Changing the keyexchange value from ikev1 to ikev2 is enough to convert strongSwan from IKEv1 to IKEv2.

**Note:** You may set the IPSec shared secret (**PSK**) up to 64 characters for both IKEv1 and IKEv2 sites.

### Switching from IKEv1 to IKEv2 in the Cato Management Application

The steps required to migrate from an IKEv1 to IKEv2 tunnel are listed below.

**To migrate a site from an IKEv1 to IKEv2 tunnel:**

1. On the **Network > Sites** screen, select the site you want switch from IKEv1 to IKEv2.
2. On the **Network > Sites > [site name] > Site Configuration > General** screen, in the **Connection Type** dropdown, select **IPsec IKEv2**. The site's **Native Range** and other networks are lost when you change the **Connection Type**.

![360002841277-image-0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248146232861.png)
3. On the **Network > Sites > [site name] > Site Configuration > Networks** screen, enter the **Native Range** and any other remote networks. These are the remote traffic selectors.
4. On the **Network > Sites > [site name] > Site Configuration > IPsec** screen, under the **Primary** section, select the **Cato IP (Egress) IP** and enter the **Site IP** of the remote VPN gateway.

![360002920918-image-1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248160811549.png)
5. Enter the PSK in the **Password** field under **Primary PSK**.

![360002841297-image-2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248135276701.png)
6. Expand the **Routing** section, add the routing option for the site under **Network Ranges**. These should all be networks already configured at other sites connected to Cato or the Cato VPN range.

,.mj
7. Select the **Initiate connection by Cato** checkbox so Cato initiates the VPN connection. This configuration is optional but recommended because the remote VPN gateway may not be configured to initiate the connection.
8. (Optional) Expand the **Init Message Parameters** section, and configure the settings. As most IPsec IKEv2-supporting solutions implement automatic negotiation of the following Init and Auth parameters, Cato recommends setting them to Automatic unless specifically instructed to by your firewall vendor.

You might have noticed that the Init and Auth message parameters are almost identical to the Phase 1 and Phase 2 parameters in IKEv1, but there is both a PRF and Integrity algorithm configuration option in IKEv2. Most vendors do not support different PRF and integrity algorithms, so if in doubt, set them to Automatic or make sure that they’re set to the same value.
9. Click **Save**.

### IKEv2: The Final Frontier

These days, there is really only one reason to party like it’s 1999, or to be precise, 1998, when IKEv1 was first defined by the IETF: if at least one side of the VPN connection is terminating on a legacy device that only supports IKEv1. The major cloud providers (AWS, GCP, Azure, Alibaba Cloud) support IKEv2. So, unless you are connecting to an older VPN endpoint, IKEv2 should be your first choice when setting up VPN tunnels.
