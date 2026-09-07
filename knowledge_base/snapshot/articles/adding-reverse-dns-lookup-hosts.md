---
title: "Adding Reverse DNS Lookup Hosts"
slug: "adding-reverse-dns-lookup-hosts"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/adding-reverse-dns-lookup-hosts"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Reverse DNS Lookup Hosts

This article discusses how to add IP addresses for Reverse DNS lookup for User Awareness.

## Overview

The Cato Cloud uses several methods to help User Awareness accurately match a user with their IP address. These include DHCP, NetBIOS on your LAN, and reverse DNS lookup.

To enable reverse DNS lookup for the Domain Controller (DC), add the associated DNS server in the **Reverse DNS Lookup Hosts** section.

![dnslookup.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218203522333.png)

> [!NOTE]
> Note:
> 
> The reverse DNS lookup feature is applicable only for DNS servers that can reply with PTR records.

This feature is designed to work with accounts that have User Awareness enabled.

**To add a reverse DNS lookup host:**

1. From the navigation menu, select **Access > User Awareness**.
2. Click the **Reverse DNS Lookup Hosts** section or tab.
3. Enter the IP address for the DNS server for the DC.
4. Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218203581469.png). The IP address for the DNS server is added.
5. **Optional:** Add additional IP addresses as needed.
6. Click **Save**. The reverse DNS lookup hosts are saved.

**To delete a reverse DNS lookup host:**

1. From the navigation menu, select **Access > User Awareness**.
2. Click the **Reverse DNS Lookup Hosts** section or tab.
3. Click ![Delete.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218232169629.svg-xml) next to the IP address to delete. The IP address is removed.
4. Click **Save**. The reverse DNS lookup host IP address is deleted.
