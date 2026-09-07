---
title: "Inspecting WebSockets in Cato Cloud"
slug: "inspecting-websockets-in-cato-cloud"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/inspecting-websockets-in-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Inspecting WebSockets in Cato Cloud

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

Modern enterprise applications increasingly rely on WebSocket (WS) communication instead of traditional HTTP request/response models. Platforms such as Slack, Microsoft Teams, Zoom, and AI services like ChatGPT and Copilot use WebSockets to enable real-time, bidirectional communication over a single persistent connection.

This shift introduces a critical visibility and security gap: traditional inspection techniques that focus on HTTP traffic cannot analyze WebSocket payloads once the connection is established.

Cato Cloud addresses this challenge with deep WebSocket inspection, enabling full visibility and enforcement across CASB, DLP, and AI security use cases.

## Key Benefits

- Full application-layer visibility across modern apps
- Accurate policy enforcement for SaaS and AI services
- Enhanced DLP capabilities for real-time data protection
- Improved compliance posture with complete audit logs
- Elimination of WebSocket blind spots

## Use Cases

### AI Security (AI Firewall)

AI applications rely heavily on WebSocket streaming.

Without inspection:

- Prompts and responses are invisible
- Sensitive data (PII, source code) may leak undetected

With inspection:

- Full visibility into prompts and responses
- Ability to detect:
  - Data leakage
  - Policy violations
  - Malicious or unsafe AI outputs

### CASB Enforcement

Modern SaaS platforms use WebSockets for core actions.

Without inspection:

- Only connection-level visibility (e.g., “connected to Slack”)
- No ability to distinguish user actions

With inspection:

- Granular activity detection:
  - File uploads/downloads
  - Message posting
  - Data sharing
- Policy enforcement per action (e.g., block sensitive uploads)

### Visibility, Logging, and Compliance

Without WebSocket parsing:

- Missing application-layer logs
- Incomplete SIEM data
- DLP and audit failures

With parsing:

- Full event reconstruction
- Accurate audit trails
- Compliance-ready logging

## Why WebSocket Inspection is Required

After an initial HTTP upgrade handshake, WebSocket connections carry application data as a continuous stream of framed messages. These messages:

- Are not visible to standard HTTP inspection engines
- May contain structured or unstructured data (JSON, binary, proprietary formats)
- Can include sensitive information such as:
  - User-generated content
  - File transfers
  - AI prompts and responses

Without proper parsing, security engines only see metadata (e.g., IPs, ports, TLS session) and lose all application-layer context.

### Challenges in Inspecting WebSockets

WebSocket inspection is complex due to protocol characteristics:

- Frame fragmentation – messages can be split across multiple frames
- Masking – client-to-server payloads are obfuscated
- Multiplexing – multiple logical messages may share a connection
- Protocol variability – payloads may use JSON, GraphQL, MessagePack, or proprietary formats

Effective inspection requires full parsing, reassembly, and decoding before any security analysis can occur.

## How the Cato Cloud Inspects WebSockets

The Cato Cloud performs inline WebSocket inspection at wire speed using a multi-layer approach:

1. Frame-Level Parsing
  - Are not visible to standard HTTP inspection engines
  - May contain structured or unstructured data (JSON, binary, proprietary formats)
  - Can include sensitive information such as:
    - User-generated content
    - File transfers
    - AI prompts and responses
2. Protocol-Aware Decoding
  - Identifies application protocols (e.g., JSON, GraphQL)
  - Extracts structured data fields
3. Event Extraction
  - Converts messages into meaningful security events, such as:
    - User actions
    - Data transfers
    - AI interactions
4. Engine Integration
  - Sends parsed data to:
    - CASB policies
    - DLP inspection
    - AI Firewall analysis
