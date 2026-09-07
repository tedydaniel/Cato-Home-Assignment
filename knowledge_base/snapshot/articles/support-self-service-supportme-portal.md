---
title: "Support Self Service | SupportMe Portal"
slug: "support-self-service-supportme-portal"
updated: 2026-08-26T16:36:11Z
published: 2026-08-26T16:36:11Z
canonical: "knowledge.catonetworks.com/support-self-service-supportme-portal"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Support Self Service | SupportMe Portal

## Overview

The 'Support Self Service' (**aka SSS**) platform was set up to facilitate troubleshooting by gathering all relevant information from a PoP perspective (i.e pcaps/connection record) in cases of issues accessing resources via Cato Cloud. Resources can be servers, webpages, databases and so on.

### Support Self Service Modes

- **Local mode** - When the end-user with the issue accessing the SupportMe portal, SSS tool gathers the information from the current PoP the user is connected to and the remote PoP of the destination host/server (1 to 2 PoPs involved in the process)
- **Remote mode** - Mainly in use for IT administrators, running the tool on behalf end users, located remotely. SSS tool collects the information from a remote PoP in Cato cloud where the end user is connected to, managed by the local PoP (where the IT admin is) in a proxy mode (2 to 3 PoPs are involved in the process).

**Note**: When running, only traffic sent to the PoP is captured. Any traffic sent within the LAN or between VLANs will not be recorded.

## How it Works

1. While connected to Cato Cloud - Navigate to [https://supportme.catonetworks.com](https://supportme.catonetworks.com/)
  - If you are unsure how to check that your traffic is routed via Cato Cloud, please contact your network administrator.
  - If you are attempting to replicate a browser-based issue (such as accessing a website), please verify that you are using an Incognito/InPrivate session. This will help capture the full traffic flow, and ensures that local endpoint caching is not being utilised.
  - **If non-default DNS servers are used, please check with the Network Administrator to make sure that there is a DNS record for tunnel-api.catonetworks.com pointing to 10.254.254.3. For accounts that don't use the default reserved system range (10.254.254.0/24), configure this record to point to the x.x.x.7 IP address in the custom system range.**
  - DNS over HTTPS (DoH) is not supported for the SSS tool. You can temporarily disable DoH in the browser first, and then use the SSS tool.
2. Once you are in, you'll have 3 simple steps to follow:
  1. Confirm the auto-populated details are correct and add an email address.

For remote mode (recording on the behalf of a remote user), make sure to change the IP address to be of the remote user.

![image__12_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10719892556701.png)
  2. The next window will ask you for more information:

> [!NOTE]
> Note:
> 
> - You may enter a single IP address/FQDN or a list of comma-separated IP addresess/FQDN into this form. For example” '192.168.0.1,' or 'page.example.com' or '192.168.0.1,192.168.0.2' or 'page.example.com,catonetworks.com'.
> - FQDNs are treated as wildcards on the backend. For example, entering ‘google.com’ will be treated as ‘*.google.com’, meaning it will also cover subdomains such as ‘drive.google.com’

| ![Screen_Shot_2021-03-14_at_16.42.54.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10719907290397.png) |
| --- |
    - Subject: Enter a meaningful subject summarizing your issue.
    - Problem Destination: An FQDN or IP address that you are trying to reach. Please verify that the FQDN/IP address is valid so the traffic capture will work.
    - Description: A full description of what is currently happening and the expected behaviour. If there is an existing ticket open for this issue, please mention the ticket number in the 'Description' box.
3. Follow the Record/Stop/Send steps.

![Screen_Shot_2021-03-14_at_16.45.02.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10719907340701.png)

**Note:** After clicking **Send** - All the recorded traffic on the PoP will be sent to Support, with the relevant reference number.

You'll receive email from our Support system confirming we got the data and proceed from there, together to solve your issue.

![support_self](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10719892725021.png)
