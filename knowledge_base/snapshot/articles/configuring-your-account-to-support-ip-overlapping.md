---
title: "Configuring Your Account to Support IP Overlapping"
slug: "configuring-your-account-to-support-ip-overlapping"
updated: 2026-08-11T12:34:24Z
published: 2026-08-11T12:34:24Z
canonical: "knowledge.catonetworks.com/configuring-your-account-to-support-ip-overlapping"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Your Account to Support IP Overlapping

## Overview of IP Overlapping and the Cato Cloud

There are several deployment scenarios where it is necessary to use overlapping IP addresses in your account. The IP Overlapping feature provides greater flexibility in network design and enables your account to route traffic to sites with overlapping IP addresses.

The routing decision is based on the shortest IP range.

## Requirements for IP Overlapping

Make sure that the account meets the following requirements before you enable IP Overlapping:

- You can only enable IP Overlapping on an account that does NOT use Static Range Translation
- One range must be smaller and fully contained within the other range
- All Sockets in the account must be version 6.1 and higher
- Make sure that each site has a unique IP address for the Native Range. You cannot duplicate an IP address between different sites
- The [IP range for remote access users](/v1/docs/ip-allocation-policy-for-remote-users) or the Cato system range can't be contained within an overlapping range

The default Cato system range is 10.254.254.0/24

## Enabling IP Overlapping for the Account

Use the **System Settings** window to enable the IP Overlapping feature for the account.

> [!NOTE]
> IMPORTANT!
> 
> Enabling the IP Overlapping feature is a permanent change for the account. After you enable this feature, to disable it please contact Support.

**To enable IP Overlapping for the account:**

1. From the navigation menu, select **Resources > System Settings**.
2. In the **IP Overlapping** section, select **Enable IP Overlapping between sites**.
3. Click **Save**. IP Overlapping is enabled for your account.

### Example of IP Overlapping Between Sites

The following list shows an example of sites with IP Overlapping.

- New York City: 10.0.0.0/16 (10.0.0.0 - 10.0.255.255)
- Frankfurt: 10.0.0.0/24 (10.0.0.0 - 10.0.0.255)
- London: 10.0.1.0/24 (10.0.1.0 - 10.0.1.255)
