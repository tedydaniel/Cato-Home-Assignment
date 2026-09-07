---
title: "Investigating AI Security App Events"
slug: "investigating-ai-security-app-events"
updated: 2026-07-20T06:10:35Z
published: 2026-07-20T06:10:35Z
canonical: "knowledge.catonetworks.com/investigating-ai-security-app-events"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Investigating AI Security App Events

This article explains how to investigate AI Security for Apps events by using the `invocation_id` from a Cato event to fetch invocation details from the Cato public API.

## Overview

When a Guard policy protecting one of your Homegrown Agents takes action on an interaction, Cato generates an event with the event type `AI Security` and the sub-type `Application Runtime Protection`. The event includes metadata such as the matched Guard, rule, action, detectors, and `invocation_id`.

The event doesn't include LLM prompts, responses, or raw message data. To investigate the interaction, use the `invocation_id` from the event to query the Cato public API and retrieve the invocation details, including sensitive content if your API key has the required RBAC permissions.

You can forward these events to SIEMs, data lakes, and other external systems with Event Integrations. You can also review invocations directly in the Cato Management Application (CMA) from **AI Security for Apps > Interaction Explorer**.

## Event and API Investigation Flow

The investigation flow is:

1. A Guard policy takes action on an interaction, and Cato generates an `Application Runtime Protection` event.
2. The event is forwarded to your SIEM or third-party application through an Event Integration. The event is also visible on the Events page in the CMA.
3. You review the event and copy the `invocation_id`.
4. You query the Cato public API with the `invocation_id` to retrieve the invocation metadata and, if authorized, the prompt and response data.

Note: What the CMA calls a Homegrown Agent is referred to as an application in the event. For example, the `application_id` field identifies the Homegrown Agent the Guard is protecting.

## Forwarding Events to SIEMs and Third-Party Applications

Event Integrations automatically forward Cato events to external platforms and storage destinations, such as Amazon S3, Azure Storage, CrowdStrike, Microsoft Sentinel, and Splunk. Use them to retain, monitor, and analyze AI Security for Apps events without manual exports or polling.

AI Security for Apps events with the event type `AI Security` and sub-type `Application Runtime Protection` are forwarded the same way as other Cato events.

## Application Runtime Protection Event Fields

Each `Application Runtime Protection` event describes a single Guard policy decision. The example below shows the structure of the event:

```json
{
  "event_type": "AI Security",
  "event_sub_type": "Application Runtime Protection",
  "event_count": 1,
  "event_id": "ee3ac03332b7c",
  "time": 1782808925461,
  "time_str": "2026-06-30T08:42:05Z",
  "account_id": "123",
  "account_name": "ACME",
  "guard_id": "cccccccc-bbbb-aaaa-dddd-ffffffffffff",
  "guard_name": "Production ChatBot",
  "rule_id": "4502893254224071709",
  "rule_name": "Block PII in prompts",
  "action": "Anonymize",
  "detectors": [
    "DETECTOR_1",
    "DETECTOR_2"
  ],
  "application_id": "cccccccc-bbbb-aaaa-dddd-ffffffffffff",
  "cato_app": "cccccccc-bbbb-aaaa-dddd-ffffffffffff",
  "is_cloud_app": false,
  "is_sanctioned_app": false,
  "invocation_id": "cccccccc-bbbb-aaaa-dddd-ffffffffffff",
  "session_id": "cccccccc-bbbb-aaaa-dddd-ffffffffffff"
}
```

### Key fields

| Field | Description |
|---|---|
| `event_type` / `event_sub_type` | Always `AI Security` / `Application Runtime Protection` for these events. Use these fields to filter in your integration or on the Events page. |
| `time` / `time_str` | When the interaction was intercepted, as an epoch timestamp and an ISO-8601 UTC string. |
| `guard_id` / `guard_name` | The Guard that protected the application and produced the decision. |
| `rule_id` / `rule_name` | The specific Guard policy rule that matched. |
| `action` | The enforcement outcome, such as `Anonymize`, `Block`, or `Monitor`. |
| `detectors` | The detectors that fired for this interaction, such as a PII detector. |
| `application_id` | The Homegrown Agent the Guard is protecting. This is referred to as an application in the event. |
| `invocation_id` | Identifies the specific interaction and is used to fetch the full invocation, including the LLM prompt and response, through the API. |
| `session_id` | Groups invocations that belong to the same conversation session. |

Note: The event may also include the fields `cato_app`, `is_cloud_app`, and `is_sanctioned_app`. These fields aren't relevant to AI Security for Apps investigations and are planned to be removed in a future release.

## Why Events Don't Include LLM Data

Application Runtime Protection events don't include prompts, responses, or raw message data. These events are often forwarded to third-party platforms and retained outside Cato, so excluding sensitive interaction content reduces data exposure and keeps event volume predictable.

To review the underlying interaction, query the Cato public API with the `invocation_id`. Access to sensitive content requires the **AI Security > AI Security for Apps > Read Sensitive Content** RBAC permission.

## Fetching Invocation Details with the API

To retrieve the full details of an invocation, query the Cato public GraphQL API using the `invocation_id` from the event. For the API endpoint, authentication, and general usage, see the Cato API documentation.

### Query

```graphql
query GetInvocation($accountId: ID!, $id: ID!) {
  aiSecurity(accountId: $accountId) {
    apps {
      invocation(input: { id: $id }) {
        id
        sessionId
        timestamp
        tokenCount
        guard {
          id
          name
        }
        action
        data {
          message {
            role
            content {
              text
            }
          }
        }
      }
    }
  }
}
```

### Variables

```json
{
  "accountId": "1234",
  "id": "cccccccc-bbbb-aaaa-dddd-ffffffffffff"
}
```

| Variable | Type | Description |
|---|---|---|
| `accountId` | `ID!` | Your Cato account ID. Scopes the query to a single account. This matches the `account_id` field in the event. |
| `id` | `ID!` | The invocation to fetch. Use the `invocation_id` from the event. |

### Response fields

| Path | Type | Description |
|---|---|---|
| `...invocation.id` | `ID!` | Globally unique invocation ID. |
| `.sessionId` | `ID` | Groups invocations from the same conversation session. `null` if not tracked. |
| `.timestamp` | `DateTime!` | UTC time the invocation was intercepted. |
| `.tokenCount` | `Int` | Total tokens for the invocation. |
| `.guard.id` / `.guard.name` | `ID` / `String` | The Guard that received the invocation. The Guard can be `null` if the invocation isn't associated with a Guard. |
| `.action` | `Enum!` | Enforcement outcome. API values are uppercase enum values, such as `BLOCK`, `ANONYMIZE`, `MONITOR`, or `NONE`. Event values may use display formatting, such as `Anonymize`. |
| `.data.message[]` | `[InvocationMessage!]` | The chat messages for the invocation. Each message has a `role` (`USER`, `ASSISTANT`, `TOOL_CALL`, `TOOL_MESSAGE`, or a custom role) and `content[]`, with each content item containing a `text` field. This field can include sensitive prompt and response content and is gated behind an additional RBAC permission. |

## Access Control

Access to invocation data is controlled by two RBAC permissions:

- Metadata access: To get any response at all, including invocation metadata such as ID, timestamp, Guard, action, and token count, the API key requires the **AI Security > AI Security for Apps > Interaction Explorer** permission. Without this permission, the query returns an authorization error.
- Sensitive content access: The `data` field, which can include sensitive prompt and response content, is additionally protected by the **AI Security > AI Security for Apps > Read Sensitive Content** RBAC permission on the API key. This keeps sensitive interaction content restricted to authorized users.
