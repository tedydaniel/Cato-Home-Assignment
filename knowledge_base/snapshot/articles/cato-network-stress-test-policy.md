---
title: "Cato Network Stress Test Policy"
slug: "cato-network-stress-test-policy"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/cato-network-stress-test-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Network Stress Test Policy

## Overview

Cato lets you perform controlled, high-volume network stress tests against your environment without disrupting other customers. To protect the shared Cato Cloud, you must request approval before conducting such tests.

The Cato Cloud is a multi-tenant platform with resources shared across all customers. To avoid impacting other accounts and customers, you must receive approval from Cato before performing a network stress test. The results of a network stress test help you validate capacity planning, performance, and resilience.

## What is a Network Stress Test?

A network stress test generates large volumes of legitimate traffic to a specific, intended target in your environment. Common use cases include:

- Performance validation
- Gameday exercises
- Load verification

A stress test is **not** a DDoS test. Packet floods, amplification/reflection attacks, or attempts to overwhelm infrastructure are prohibited.

## Preparing for a Network Stress Test

Every customer planning to conduct any kind of network stress test must coordinate this via the Support team at least 30 days before the test. In addition, provide the following details before actually running the tests, to ensure no impact to Cato's service we provide to our customers, nor to avoid violating the terms of use.

Unauthorized stress tests are not permitted and may be blocked.

1. **Site details**: Location, connection type, date/time/time zone
2. **WAN setup**: Number of WAN links, bandwidth per link (Active/Active, at least two interfaces), trial license bandwidth, expected commercial license bandwidth
3. **Traffic generation**: Tool used, description of the test, test goals/success criteria (with numbers), packets per second (PPS), connections per second (CPS), number of simulated hosts (for sites above 3 Gbps, simulate more than 1000 hosts)
4. **Traffic profile**: Protocols (HTTP, HTTPS, SMB, voice/audio, DNS, UDP, TCP), other protocols if applicable
5. **Traffic type**: Internet-bound, WAN-bound, or blend
6. **Destination site**: Location, connection type, last-mile links
7. **Packet and policy details**: Expected packet size distribution, policies under test (Network Rules, Internet/WAN firewall, TLS Inspection, IPS, Application Control/DLP, etc.)
8. **Event settings**: Relevant event configurations for the test
