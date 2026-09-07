---
title: "Certificate Warnings with Blocked HTTPS Websites"
slug: "certificate-warnings-with-blocked-https-websites"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/certificate-warnings-with-blocked-https-websites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Certificate Warnings with Blocked HTTPS Websites

**Summary**

Cato Networks acts as a man-in-the-middle to serve block pages for HTTPS websites even when TLS Inspection is disabled. This means that when browsing to an HTTPS website that is blocked, users will see certificate warnings if the Cato Certificate is not installed on their computer or browser.

The screenshot below shows the warning that Firefox displays when https://facebook.com is blocked and the Cato Certificate is not installed.

| ![115011234585-mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25370703606045.png) |
| --- |

**Solution**

Install the Cato Certificate on users' computers and/or browsers to prevent certificate warnings. For instructions, please refer to our article [How to Install the Cato Certificate](/v1/docs/how-to-install-the-cato-certificate).

The screenshot below shows the block page displayed in Firefox for https://facebook.com after installing the Cato Certificate.

![blocked_FB_example.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25370703678365.png)

**More Details**

When an HTTP website is blocked by policy, Cato is able to generate the block page with an HTTP 403 response following the client's HTTP GET method.

The same method is not possible when an HTTPS website is blocked, however, because all traffic between the client and server is encrypted.

Therefore, in order to serve the block page for HTTPS websites, Cato acts as a man-in-the-middle. Cato is able to detect that an HTTPS website should be blocked prior to the TLS handshake, so it intercepts the Client Hello and completes the TLS handshake with the client. Cato is then able to decrypt the incoming GET request and serve the block page.
