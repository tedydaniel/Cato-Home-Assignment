---
title: "Configuring a Forward Proxy (EA)"
slug: "configuring-a-forward-proxy"
updated: 2026-08-19T12:28:16Z
published: 2026-08-19T12:28:16Z
canonical: "knowledge.catonetworks.com/configuring-a-forward-proxy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a Forward Proxy (EA)

> [!NOTE]
> **Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information about enabling the feature, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

Forward Proxy lets you connect your existing forward proxy deployment to Cato AI Security. If your organization already uses a forward proxy to communicate with external vendors, you can continue using that network architecture instead of redesigning it. You define a forward proxy in Cato, and your existing proxy forwards supported AI traffic to Cato for inspection and enforcement.

Cato assigns a dedicated endpoint and port for each account. Your existing forward proxy sends traffic to that endpoint, and Cato forwards authorized traffic to AI Security.

To configure the forward proxy to work with ZScaler, see [this](/v1/docs/configuring-zscaler-to-work-with-cato-forward-proxy) knowledge base article.

## How the Forward Proxy Works

Forward Proxy is an account-level entity in the CMA. When you enable the feature, Cato generates a dedicated proxy endpoint for your account that includes:

- FQDN
- Port

For example, samplefqdn.fwdproxy.catonetworks.net:8337

Your existing forward proxy sends HTTP CONNECT traffic to the Cato endpoint. Cato accepts only authorized traffic and then forwards it to AI Security.

Cato validates traffic based on:

- Source IP address
- Supported destination
- User identity information in the request header

## Use Case

As a security admin, your organization already uses a proxy, such as Zscaler, to route traffic to external vendors. You want to connect that traffic to Cato AI Security without changing your existing network architecture.

You create a Forward Proxy in the CMA and add the public source IP addresses used by your organization's proxy. After you enable the feature, Cato generates a dedicated endpoint and port for your account. You then configure your existing proxy to forward supported AI traffic to that Cato endpoint.

When traffic reaches Cato, it validates the source, destination, and user identity information before forwarding authorized traffic to AI Security. This workflow lets you continue using your current proxy deployment while sending supported AI traffic to Cato AI Security for inspection and enforcement.

## Limitations

- Only one Forward Proxy is supported per account
- You can't choose the proxy endpoint or port because Cato assigns them automatically
- If you disable and then re-enable the feature, Cato doesn't guarantee that you will receive the same endpoint and port
- A maximum of 1,000 source IPs is supported
- The following source IPs are blocked and can't be configured:
  - 0.0.0.0/0 ::1/128
  - 127.0.0.0/8
  - ::/0
  - ::1/128

## Configure a Forward Proxy

![forward_proxy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34983920924317(1).png)

**To configure a forward proxy:**

1. Navigate to **Network > Forward Proxy**.
2. Under **Source** , add at least 1 IP address or range, and click **Apply**.
3. In the upper right-hand corner of the screen, enable the Forward Proxy feature. This is only possible once you've defined at least one IP address or range.

Once you enable the feature, the **Proxy Port** and **Proxy Endpoint** are generated.

**Note:** If you disable the feature, the port and endpoint are released and upon re-enabling the feature, a new port and endpoint will be generated.
4. Copy the values of the **Proxy Port** and **Proxy Endpoint** to your current proxy to ensure that traffic is routed from the current proxy to your account's Forward Proxy.
5. Configure the **User Format**, if applicable.
