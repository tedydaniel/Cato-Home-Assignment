---
title: "Troubleshooting Support Self Service Portal"
slug: "troubleshooting-support-self-service-portal"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/troubleshooting-support-self-service-portal"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Support Self Service Portal

## Overview

Often, Support asks you to use the [Support Self Service](/v1/docs/support-self-service-supportme-portal) portal to help resolve issues. This article explains how to fix some common errors with this portal.

## Cato Certificate is Missing

If you are using the SDP Client to connect to the Cato Cloud, or connected behind a Socket, the Cato certificate should be installed. When the certificate is missing, the following error is shown:![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29833817333021.png)

To resolve the issue, download the certificate from the [Cato portal](https://clientdownload.catonetworks.com/), and then install the certificate.

## DNS Resolving Issue

If you are using non-Cato DNS servers, please check with the network admin to make sure that there is a DNS record for **tunnel-api.catonetworks.com** pointing to 10.254.254.3. Run the following command to check the DNS record:

```plaintext
 nslookup tunnel-api.catonetworks.com
```

![-zsh-2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/4410249284125.png)

For accounts that don't use the default reserved system range (10.254.254.0/24), configure this record to point to the x.x.x.7 IP address in the [customs system range](/v1/docs/configuring-system-settings-for-the-account).

## Proxy and DNS Security

If you are connected to the Cato Cloud and still see the following screen:![Cato_Self-Service_Portal-2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/4410174384797.png)

Make sure that [DNS security(DoH)](https://support.unlocator.com/article/365-how-to-disable-dns-over-https-on-firefox-and-google-chrome-browsers) is disabled on the browser:![Settings_-_Security.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/4410203640989.png)

Make sure that no proxy is enabled on your browser, for more information, see this [guide](https://www.bitdefender.com/consumer/support/answer/1979/).

## Local Network Permissions

When accessing the Self-Service Portal using Chrome, your device may not be identified if Local Network access is disabled in your browser. To verify this, open the portal, click the site information icon next to the URL in the address bar, and ensure that Local Network is enabled. If you are using Microsoft Edge, make sure that Local Network is set to Allow. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35722503258269.png)
