---
title: "Cato Client Last-Mile Support for IPv6"
slug: "cato-client-last-mile-support-for-ipv6"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/cato-client-last-mile-support-for-ipv6"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Client Last-Mile Support for IPv6

This article provides information about the Cato Client supporting IPv6 traffic.

## Overview

The Cato Client supports connecting to the Cato Cloud through ISPs that provide last-mile IPv6-only connections. This ensures compatibility with modern networking standards. The Client also supports last-mile connections in dual-stack environments, where IPv4 is disabled.

The Client requires NAT64 to translate IPv6 addresses to IPv4 addresses. The NAT64 prefix within an IPv6 address is collected by the Client allowing it to connect to the Cato Cloud. This means that the Client can only use IPv6 addresses when it is connected to a NAT64 environment.

For monitoring and troubleshooting purposes, the IPv6 address appears on the **Statistics** page in the Client.

### Prerequisites

- Supported on these Client versions:
  - Windows Client v5.11 and higher
  - macOS Client v5.7 and higher
  - iOS Client v5.4 and higher
- NAT64 is implemented

### Known Limitations

- In dual-stack environments where IPv4 is blocked, the Time-to-Connect can be up to 12 seconds
- The macOS Client does not support IPv6 in a captive portal
