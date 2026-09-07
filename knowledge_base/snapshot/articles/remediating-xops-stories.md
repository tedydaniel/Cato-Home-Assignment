---
title: "Remediating XOps Stories and Security Events with Cato APIs"
slug: "remediating-xops-stories-by-api"
updated: 2026-08-13T08:04:16Z
published: 2026-08-13T08:04:16Z
canonical: "knowledge.catonetworks.com/remediating-xops-stories-by-api"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Remediating XOps Stories and Security Events with Cato APIs

This step-by-step guide covers how to automate API-based responses to security events and XOps stories.

Use it to extract story data, apply remediation actions such as isolating hosts, blocking IOCs, and quarantining users, and annotate the story with actions taken.

## 1. API Access & Prerequisites

| **Item** | **Value** |
| --- | --- |
| Endpoint | `https://api.catonetworks.com/api/v1/graphql2` **Note:** Endpoint format varies by CMA region prefix (e.g. [api.us1.catonetworks.com](http://api.us1.catonetworks.com)). Learn more [here](/v1/docs/what-is-the-cato-api). |
| Auth header | `x-api-key: &lt;key&gt;` |
| Content-Type | `application/json` |
| Method | POST (every call, queries and mutations) |
| accountId | You can find this in the CMA (Administration > General Info) |
| Key type | Service Principal (Resources > Service API Keys) **Note:** Learn more about Service Principal keys, key rotation, and IP restrictions [here](/v1/docs/generating-api-keys-for-the-cato-api). |
| Required permissions | - Internet Firewall - WAN Firewall - Client Connectivity - Containers - Users (Viewer for lookups) - Stories (Editor). Required for `addStoryComment` in [Annotating the Story](/v1/docs/remediating-xops-stories-by-api#6-annotating-the-story), below |
| Store API credentials securely for use in the scripts on this page | Create a secure header file named `headers.txt` to store your API credentials safely: ```bash echo "x-api-key: YOUR_API_KEY" > headers.txt echo "Content-Type: application/json" >> headers.txt chmod 600 headers.txt ``` **Note:** Running commands with raw secrets in terminal history can leak credentials. We recommend using environment files like this as a standard best practice. |

### 1.1 HTTP Request Pattern

Every Cato API call follows the same shape: POST to `/api/v1/graphql2` with a JSON body containing `query` and `variables`. Identical pattern for queries and mutations.

**Generic curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "<GraphQL operation as string>",
    "variables": { ... }
  }'
```

**Generic raw HTTP**

```http
POST /api/v1/graphql2 HTTP/1.1
Host: api.catonetworks.com
x-api-key: <your_api_key>
Content-Type: application/json
Content-Length: <byte_count>

{ "query": "<GraphQL operation>", "variables": { ... } }
```

**Generic success response**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "data": {
    "<root_field>": { /* operation-specific fields */ }
  }
}
```

**Generic error response (GraphQL validation)**

```http
HTTP/1.1 200 OK   # GraphQL returns 200 even on validation errors
Content-Type: application/json

{
  "errors": [
    {
      "message": "Variable '$accountId' of required type 'ID!' was not provided.",
      "locations": [{ "line": 1, "column": 7 }],
      "extensions": { "code": "GRAPHQL_VALIDATION_FAILED" }
    }
  ],
  "data": null
}
```

GraphQL returns HTTP 200 even when the operation fails. The error is in `errors[]` in the body. Integration steps must check `errors[]` before processing `data`.

### 1.2 Pre-Production Validation Checklist

| **#** | **Validation step** |
| --- | --- |
| 1 | Generate a dedicated Service Principal API key (**do not reuse admin keys**) |
| 2 | Restrict the API key to your SIEM source IPs |
| 3 | Test every mutation in the GraphQL Playground against your account, as explained [here](/v1/docs/connecting-to-the-cato-api-from-the-graphql-playground) |
| 4 | Confirm response shapes match what your SIEM Parse JSON steps expect |
| 5 | Run a full enforcement-to-reversal cycle for each remediation action in test |
| 6 | Verify CMA audit trail reflects every test action |

## 2. Extracting Remediation Data

Two integration paths feed the same [remediation mutations](/v1/docs/remediating-xops-stories-by-api#5-remediation-mutations-per-alert). Which one you use depends on your Cato licenses:

### 2.1 Choosing an Integration Path

| Path | When to use | Signal source | Correlation |
| --- | --- | --- | --- |
| Story-based (XOps) | Account has an XDR/XOps license and Stories Workbench is populated | `xdr.stories()` query OR `eventsFeed` with `event_type = Detection and Response`. | Cato pre-correlates producers into stories. Entities live in `incident.entities[]` |
| Event-based (non-XOps) | Account does not have XOps and the SIEM receives raw security verdicts and performs its own correlation | `eventsFeed` with `event_type = Securit` | SIEM (or SOAR playbook) correlates. Entities live in the flat `fieldsMap` |

### 2.2 Story-Based Extraction (XOps)

Story data reaches your platform via two paths: (1) `xdr.stories()` query for direct pull; (2) `eventsFeed` query with the full story JSON in `additional_data`.

> [!NOTE]
> Note
> 
> Learn more about XOps and the Stories Workbench [here](/v1/docs/welcome-to-the-cato-xops-service).
> 
> Learn more about how to configure the response policy to generate events for eventsFeed, [here](/v1/docs/creating-the-response-policy-for-xops-stories).

#### 2.2.1 Pull Stories via xdr.stories()

**GraphQL operation**

```graphql
query GetStories($accountId: ID!) {
  xdr(accountID: $accountId) {
    stories(input: {
      paging: { limit: 50, from: 0 }
      filter: [{
        timeFrame: { time: "last.P7D" }   # REQUIRED
        status:    { in: [Open] }
        severity:  { in: [High, Medium] }
      }]
      sort: [{ fieldName: criticality, order: desc }]
    }) {
      paging { total }
      items {
        id
        createdAt
        updatedAt
        incident {
          producerType
          indication
          criticality
          sourceIp
          firstSignal
          lastSignal
          user { id name }
          site { id name }
          entities { type role ref { id name } }
        }
      }
    }
  }
}
```

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  --data-binary @get_stories.json
```

**Success response (illustrative)**

```http
HTTP/1.1 200 OK

{
  "data": {
    "xdr": {
      "stories": {
        "paging": { "total": 47 },
        "items": [
          {
            "id": "sty_01HX9F8K7M2QXAZB3VR4PQYNTC",
            "createdAt": "2026-06-27T14:22:11Z",
            "updatedAt": "2026-06-27T14:38:42Z",
            "incident": {
              "producerType": "ThreatPrevention",
              "indication": "Ransomware Communication",
              "criticality": 9,
              "sourceIp": "10.1.2.50",
              "firstSignal": "2026-06-27T14:22:11Z",
              "lastSignal":  "2026-06-27T14:38:42Z",
              "user": { "id": "usr_8K2QXA3VR4PQYNTC", "name": "jane.doe@example.com" },
              "site": { "id": "ste_2QXA3VR4PQYNTC", "name": "HQ-Site" },
              "entities": [
                { "type": "ip",     "role": "target", "ref": { "id": "ip_x1", "name": "203.0.113.5" } },
                { "type": "domain", "role": "target", "ref": { "id": "d_x2",  "name": "malicious.example.com" } },
                { "type": "host",   "role": "source", "ref": { "id": "h_x3",  "name": "WIN-LAPTOP-23" } }
              ]
            }
          }
        ]
      }
    }
  }
}
```

**Error response (missing required timeFrame)**

```json
{
  "errors": [
    {
      "message": "Field 'StoryFilterInput.timeFrame' of required type 'TimeFrameInput!' was not provided.",
      "locations": [{ "line": 4, "column": 15 }],
      "extensions": { "code": "GRAPHQL_VALIDATION_FAILED" }
    }
  ],
  "data": null
}
```

#### 2.2.2 Key Story Fields for Remediation

| **JSONPath** | **Type** | **Remediation use** |
| --- | --- | --- |
| `items[].id` | String | Story ID. For `addStoryComment`, audit correlation. |
| `items[].incident.sourceIp` | String | Host/device source IP. Use for Isolate Host. |
| `items[].incident.user.id` | String | Cato user entity ID. Pass directly to user mutations. |
| `items[].incident.user.name` | String | Username/email. Use only if `.user.id` absent. |
| `items[].incident.entities[]` | Array | IOCs, hosts, users. Filter by `.type`. |
| `entities[type=ip].ref.name` | String | IOC IP value → BlockListIps. |
| `entities[type=domain].ref.name` | String | IOC domain value → BlockListUrls. |
| `items[].incident.producerType` | Enum | `ThreatPrevention`, `ThreatHunt`, `AnomalyStats`, `AnomalyEvents`. |
| `items[].incident.criticality` | Int (1–10) | Auto-remediation threshold. |

#### 2.2.3 Polling XOps Events via eventsFeed

> [!NOTE]
> Note:
> 
> Learn more about setup and integration patterns for eventsFeed, [here](/v1/docs/cato-api-eventsfeed-large-scale-event-monitoring).

**GraphQL operation**

```graphql
query FetchXOpsEvents($accountId: ID!, $marker: String) {
  eventsFeed(
    accountIDs: [$accountId]
    marker: $marker
    filters: [{ fieldName: event_type, operator: is, values: ["Detection and Response"] }]
  ) {
    marker
    fetchedCount
    accounts { id records { fieldsMap } }
  }
}
```

**Success response**

```json
{
  "data": {
    "eventsFeed": {
      "marker": "W3siVG9waWMiOi4uLn0=","fetchedCount": 1,
      "accounts": [
        {
          "id": "YOUR_ACCOUNT_ID",
          "records": [
            {
              "fieldsMap": {
                "event_type":     "Detection and Response",
                "event_sub_type": "Threat Prevention",
                "story_id":       "sty_01HX9F8K7M2QXAZB3VR4PQYNTC",
                "src_ip":         "10.1.2.50",
                "user_name":      "jane.doe@example.com",
                "severity":       "High",
                "additional_data": "{ \"id\": \"sty_01HX...\", \"incident\": { ... } }"
              }
            }
          ]
        }
      ]
    }
  }
}
```

#### 2.2.4 Parsing the Event Record

The full story payload is in `additional_data` as a JSON string. Parse it separately from the flat `fieldsMap` keys.

| You need | JSONPath | Notes |
| --- | --- | --- |
| user entity ID | `$.incident.user.id` | Direct (no user lookup needed) |
| username (fallback) | `$.incident.user.name` | Use only if `.user.id` absent (see [Resolving a User Entity ID (Fallback)](/v1/docs/remediating-xops-stories-by-api#3-resolving-a-user-entity-id-fallback), below) |
| host IP | `$.incident.sourceIp` | For Isolate Host |
| IOC IPs (array) | `$.incident.entities[?(@.type=='ip')].ref.name` | For Block IOC IP |
| IOC domains (array) | `$.incident.entities[?(@.type=='domain')].ref.name` | For Block IOC Domain |
| producer enum | `$.incident.producerType` | PascalCase routing key |
| criticality | `$.incident.criticality` | Auto-remediation threshold |

#### 2.2.5 jq Examples

```bash
# Extract user.id
jq -r '.data.eventsFeed.accounts[].records[].fieldsMap.additional_data
        | fromjson | .incident.user.id // empty' response.json

# All IOC IPs
jq -r '.data.eventsFeed.accounts[].records[].fieldsMap.additional_data
        | fromjson | .incident.entities[]
        | select(.type == "ip") | .ref.name' response.json

# All IOC domains
jq -r '.data.eventsFeed.accounts[].records[].fieldsMap.additional_data
        | fromjson | .incident.entities[]
        | select(.type == "domain" or .type == "url") | .ref.name' response.json
```

---

### 2.3 Event-based Extraction (non-XOps)

Non-XOps customers subscribe to `eventsFeed` and filter on `event_type = "Security"`. Each event carries a single verdict from one enforcement point — IPS signature match, Anti-Malware scan, Threat Prevention DNS/URL match, Application Control decision, or DNS Protection lookup. Entities are in the flat `fieldsMap`; there is no `additional_data` story JSON to parse. Correlation and dedup are the SIEM/SOAR’s responsibility.

#### 2.3.1 Polling Security Events via eventsFeed

**GraphQL operation**

```graphql
query FetchSecurityEvents($accountId: ID!, $marker: String) {
  eventsFeed(
    accountIDs: [$accountId]
    marker: $marker
    filters: [{ fieldName: event_type, operator: is, values: ["Security"] }]
  ) {
    marker
    fetchedCount
    accounts { id records { fieldsMap } }
  }
}
```

To narrow to specific producers, add a second filter clause on `event_sub_type`:

```graphql
filters: [
  { fieldName: event_type,     operator: is, values: ["Security"] }
  { fieldName: event_sub_type, operator: is, values: ["IPS", "Anti Malware", "Threat Prevention"] }
]
```

**Success response (illustrative — Anti-Malware verdict)**

```json
{
  "data": {
    "eventsFeed": {
      "marker": "W3siVG9waWMiOi4uLn0=",
  "fetchedCount": 1,
      "accounts": [
        {
          "id": "YOUR_ACCOUNT_ID",
          "records": [
            {
              "fieldsMap": {
                "event_type":     "Security",
                "event_sub_type": "Anti Malware",
                "action":         "Block",
                "src_ip":         "10.1.2.50",
                "dest_ip":        "203.0.113.5",
                "user_name":      "jane.doe@example.com",
                "domain_name":    "malicious.example.com",
                "threat_name":    "Trojan.Generic.KX",
                "severity":       "High",
                "rule_name":      "Anti-Malware Default"
              }
            }
          ]
        }
      ]
    }
  }
}
```

Field names vary by sub_type. All fieldsMap keys in this section were verified against the `EventFieldName` schema enum, but the `event_type` and `event_sub_type` string values (e.g. `"Security"`, `"Anti Malware"`) are runtime values and should be confirmed against a live sample from your account (Events Discovery page in the CMA). Spelling/spacing on `"Anti Malware"` vs `"Anti-Malware"` in particular is worth a spot-check before wiring the parser.

#### 2.3.2 Key Event Fields for Remediation

| **You need** | **fieldsMap key** | **Notes / used by** |
| --- | --- | --- |
| host IP (source) | `src_ip` | For [Isolate Host](/v1/docs/remediating-xops-stories-by-api#52-isolate-host). |
| username | `user_name` | Resolve to `user.id` via [Resolving a User Entity ID](/v1/docs/remediating-xops-stories-by-api#3-resolving-a-user-entity-id-fallback), then used with [Isolate User](/v1/docs/remediating-xops-stories-by-api#51-isolate-user). |
| user ID (if present) | `user_id` | Some sub_types include it directly. If this is already populated, you can ignore the section [Resolving a User Entity ID](/v1/docs/remediating-xops-stories-by-api#3-resolving-a-user-entity-id-fallback). |
| IOC IP (destination) | `dest_ip` | For [Block IOC, IP Address](/v1/docs/remediating-xops-stories-by-api#53-block-ioc-—-ip-address). Only when the verdict indicates outbound C2/IOC traffic. Do not blocklist legitimate destinations. |
| IOC domain | `domain_name` | For [Block IOC, Domain](/v1/docs/remediating-xops-stories-by-api#54-block-ioc-—-domain-fqdn). Also `dest_domain`, or parse hostname from `url` / `full_path_url`. |
| producer | `event_sub_type` | Routing key: `IPS`, `Anti Malware`, `Threat Prevention`, `Application Control`, `DNS Protection`. |
| verdict | `action` | `Block` \| `Alert` \| `Allow`. Only remediate on `Block` / `Alert`. |
| severity | `severity` | Auto-remediation threshold. |
| threat name | `threat_name` | For [SIEM-side audit record](/v1/docs/remediating-xops-stories-by-api#234-siemside-audit-record1). |
| rule | `rule_name` | Which Cato policy fired. Useful for audit and dedup. |

#### 2.3.3 Sub-type → Remediation Action

Not every security verdict maps to every remediation mutation action. Suggested mapping:

| **event_sub_type** | **Isolate Host** | **Isolate User** | **Block IOC IP** | **Block IOC Domain** |
| --- | --- | --- | --- | --- |
| IPS | ✅ repeat offender | ⚠️ policy-dependent | ✅ external attacker src | — |
| Anti Malware | ✅ infected host | ✅ user’s device | ✅ C2 dest | ✅ C2 domain |
| Threat Prevention | ⚠️ policy-dependent | ⚠️ policy-dependent | ✅ | ✅ |
| Application Control | — usually alert-only | ⚠️ policy-dependent | — | ⚠️ risky-app domain |
| DNS Protection | ⚠️ repeat lookups | — | — | ✅ malicious FQDN |

Legend: ✅ typical, ⚠️ policy-dependent, — not applicable.

#### 2.3.4 SIEM-side Audit Record

Log the remediation locally so the SOC has an audit trail. Suggested minimum shape:

```json
{
  "timestamp":       "2026-08-12T14:38:42Z",
  "cato_event_id":   "<fieldsMap.event_id or SIEM-assigned>",
  "event_sub_type":  "Anti Malware",
  "action_taken":    "block_ioc_ip",
  "entity":          "203.0.113.5",
  "cato_rule_id":    "IFW_BLOCK_IOC_IPS_RULE_ID",
  "api_status":      "SUCCESS",
  "operator":        "SOAR-playbook-v3"
}
```

#### 2.3.5 jq Examples

```bash
# All source IPs from Security events (candidates for Isolate Host)
jq -r '.data.eventsFeed.accounts[].records[].fieldsMap
        | select(.event_type == "Security")
        | .src_ip // empty' response.json

# IOC destination IPs from Anti-Malware blocks
jq -r '.data.eventsFeed.accounts[].records[].fieldsMap
        | select(.event_sub_type == "Anti Malware" and .action == "Block")
        | .dest_ip // empty' response.json

# Malicious FQDNs from DNS Protection
jq -r '.data.eventsFeed.accounts[].records[].fieldsMap
        | select(.event_sub_type == "DNS Protection")
        | .domain_name // empty' response.json
```

### 2.4 Shared: Entity → Remediation Mutations Action Mapping

The [remediation mutation](/v1/docs/remediating-xops-stories-by-api#5-remediation-mutations-per-alert) targets are identical whether entities came from a story or a flat event (see [Choosing an Integration Path](/v1/docs/remediating-xops-stories-by-api#21-choosing-an-integration-path)).

Pass the extracted values directly into the [remediation mutation](/v1/docs/remediating-xops-stories-by-api#5-remediation-mutations-per-alert) inputs.

| **Extracted entity** | **Story path** | **Event path** | **Remediation Mutation action** |
| --- | --- | --- | --- |
| host IP | `$.incident.sourceIp` | `fieldsMap.src_ip` | [Isolate Host](/v1/docs/remediating-xops-stories-by-api#52-isolate-host) |
| user ID | `$.incident.user.id` | `fieldsMap.user_id` (fallback: resolve `fieldsMap.user_name` via [Resolving a User Entity ID](/v1/docs/remediating-xops-stories-by-api#3-resolving-a-user-entity-id-fallback)) | [Isolate User](/v1/docs/remediating-xops-stories-by-api#51-isolate-user) |
| IOC IP(s) | `$.incident.entities[?(@.type=='ip')].ref.name` | `fieldsMap.dest_ip` | [Block IOC, IP Address](/v1/docs/remediating-xops-stories-by-api#53-block-ioc-—-ip-address) |
| IOC domain(s) | `$.incident.entities[?(@.type=='domain')].ref.name` | `fieldsMap.domain_name` (also `dest_domain`; parse from `url` / `full_path_url`) | [Block IOC, Domain](/v1/docs/remediating-xops-stories-by-api#54-block-ioc-—-domain-fqdn) |
| story ID | `$.id` | *(N/A — use* [*SIEM audit record*](/v1/docs/remediating-xops-stories-by-api#234-siemside-audit-record1)*)* | [Annotate Story](/v1/docs/remediating-xops-stories-by-api#6-annotating-the-story) |

## 3. Resolving a User Entity ID (Fallback)

If `incident.user.id` is populated, pass it directly to user mutations. Use `user.userList` only when a username/email is the only identifier available.

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "query LookupUser($accountId: ID!, $search: String!) {
               user(accountId: $accountId) {
                 userList(input: {
                   filter: { searchTerm: { search: $search } }
                   paging:  { limit: 5, from: 0 }
                 }) {
                   items { id email userPrincipalName firstName lastName }
                   pageInfo { total }
                 }
               } }",
    "variables": { "accountId": "YOUR_ACCOUNT_ID", "search": "jane.doe@example.com" }
  }'
```

`searchTerm.search` performs a free-text search across UPN and email. For an exact-email lookup use `filter: { email: [{ ... }] }` (see `EmailFilterInput`).

**Success response**

```json
{
  "data": {
    "user": {
      "userList": {
        "items": [
          {
            "id": "usr_8K2QXA3VR4PQYNTC",
            "email": "jane.doe@example.com",
            "userPrincipalName": "jane.doe@example.com",
            "firstName": "Jane",
            "lastName": "Doe"
          }
        ],
        "pageInfo": { "total": 1 }
      }
    }
  }
}
```

---

## 4. One-Time Setup (Per Account)

Run these mutations **once per account**. After publishing, no further policy changes are required for per-alert actions. The [remediation mutations](/v1/docs/remediating-xops-stories-by-api#5-remediation-mutations-per-alert) described below only *update* the rules created here.

> [!NOTE]
> Note:
> 
> Learn more about Container structure, use cases, and enforcement model, [here](/v1/docs/integrating-custom-ioc-lists-with-containers).
> 
> Learn more about Client Connectivity Policy (used by Quarantine User), [here](/v1/docs/configuring-the-client-connectivity-policy).
> 
> Learn more about Firewall rule ordering and best practices, [here](/v1/docs/recommendations-for-internet-and-wan-firewall-policies).

### 4.1 Object Map

| **Object** | **Name** | **Used by** |
| --- | --- | --- |
| IP Container | `BlockListIps` | [Block IOC IP](/v1/docs/remediating-xops-stories-by-api#53-block-ioc-—-ip-address) - IFW BLOCK rule *destination* |
| FQDN Container | `BlockListUrls` | [Block IOC Domain](/v1/docs/remediating-xops-stories-by-api#54-block-ioc-—-domain-fqdn) - IFW BLOCK rule *destination* |
| IFW rule | `XOps - Block IOC IPs` | Destination refs `BlockListIps` container |
| IFW rule | `XOps - Block IOC Domains` | Destination refs `BlockListUrls` container |
| IFW rule | `XOps - Isolate Host` | [Source-IP list](/v1/docs/remediating-xops-stories-by-api#52-isolate-host); appends host IPs |
| WAN FW rule | `XOps - Isolate Host (WAN)` | [Source-IP list](/v1/docs/remediating-xops-stories-by-api#52-isolate-host); appends host IPs |
| Client Connectivity rule | `XOps - Block Quarantined Users` | [Source-user list](/v1/docs/remediating-xops-stories-by-api#512-quarantine-user-persistent); appends user IDs |

Store the six returned IDs (2 container IDs and 4 rule IDs) in your credential vault. The [per-alert mutations](/v1/docs/remediating-xops-stories-by-api#5-remediation-mutations-per-alert) reference them by ID.

### 4.2 Create the IP/FQDN Containers

Same mutation shape (`createFromList`) for both; only the input variables change. Containers require at least one seed value at creation (RFC 5737 documentation IP `192.0.2.1` is a safe placeholder; `example.com` for FQDN).

**curl — BlockListIps**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation CreateIpContainer($accountId: ID!, $input: CreateIpAddressRangeContainerFromListInput!) {
               container(accountId: $accountId) { ipAddressRange { createFromList(input: $input) {
                 container { id name size } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "name": "BlockListIps",
        "description": "IOC IPs - Internet FW destination",
        "values": [{ "from": "192.0.2.1", "to": "192.0.2.1" }]
      }
    }
  }'
```

**Success response**

```json
{
  "data": {
    "container": {
      "ipAddressRange": {
        "createFromList": {
          "container": { "id": "cnt_1A2B3C", "name": "BlockListIps", "size": 1 }
        }
      }
    }
  }
}
```

**curl — BlockListUrls**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation CreateFqdnContainer($accountId: ID!, $input: CreateFqdnContainerFromListInput!) {
               container(accountId: $accountId) { fqdn { createFromList(input: $input) {
                 container { id name size } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "name": "BlockListUrls",
        "description": "IOC domains - Internet FW destination",
        "values": ["example.com"]
      }
    }
  }'
```

### 4.3 Create Internet Firewall BLOCK Rules

Three rules at `FIRST_IN_POLICY`:

- Rules 1 and 2 reference the containers in their destination
- Rule 3 (Isolate Host) uses `source.ip` empty at creation

The [Isolate Host mutation](/v1/docs/remediating-xops-stories-by-api#52-isolate-host) appends host IPs at alert time. (Use `source.ip` for single addresses. The API's `source.ipRange` validator rejects `{from:X, to:X}` even when the values are equal. Reserve `source.ipRange` for actual multi-address ranges.)

**curl — Rule 1: Block IOC IPs**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation AddIfwRule($accountId: ID!, $input: InternetFirewallAddRuleInput!) {
               policy(accountId: $accountId) { internetFirewall { addRule(input: $input) {
                 status errors { errorMessage errorCode } rule { rule { id name } } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "at": { "position": "FIRST_IN_POLICY" },
        "rule": {
          "name": "XOps - Block IOC IPs",
          "enabled": true,
          "action": "BLOCK",
          "source": {},
          "destination": {
            "containers": {
              "ipAddressRangeContainer": [{ "by": "NAME", "input": "BlockListIps" }]
            }
          },
          "tracking": { "event": { "enabled": true } }
        }
      }
    }
  }'
```

**Success response**

```json
{
  "data": {
    "policy": {
      "internetFirewall": {
        "addRule": {
          "status": "SUCCESS",
          "errors": [],
          "rule": { "rule": { "id": "rul_XK7M2Q", "name": "XOps - Block IOC IPs" } }
        }
      }
    }
  }
}
```

**Rule 2: Block IOC Domains — same mutation, change destination**

```json
"destination": {
  "containers": {
    "fqdnContainer": [{ "by": "NAME", "input": "BlockListUrls" }]
  }
}
```

**Rule 3: Isolate Host — source-IP list, empty at creation**

```json
"source": { "ip": [] },
"destination": {}
```

Store the returned rule IDs as `IFW_ISOLATE_HOST_RULE_ID`, `IFW_BLOCK_IOC_IPS_RULE_ID`, `IFW_BLOCK_IOC_DOMAINS_RULE_ID`.

### 4.4 Create WAN Firewall BLOCK Rule (Host Isolation)

Same shape as IFW Rule 3 above. WAN Firewall source does not support containers: always use direct `ip` (single addresses) or `ipRange` (multi-address ranges).

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation AddWfw($accountId: ID!, $input: WanFirewallAddRuleInput!) {
               policy(accountId: $accountId) { wanFirewall { addRule(input: $input) {
                 status errors { errorMessage errorCode } rule { rule { id name } } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "at": { "position": "FIRST_IN_POLICY" },
        "rule": {
          "name": "XOps - Isolate Host (WAN)",
          "enabled": true,
          "action": "BLOCK",
          "source":      { "ip": [] },
          "destination": {},
          "tracking":    { "event": { "enabled": true } }
        }
      }
    }
  }'
```

Store the returned rule ID as `WAN_ISOLATE_HOST_RULE_ID`.

### 4.5 Create Client Connectivity BLOCK Rule (User Quarantine)

Source-user list, empty at creation. [Quarantine User (Persistent)](/v1/docs/remediating-xops-stories-by-api#512-quarantine-user-persistent) appends offending user IDs at alert time.

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation AddCC($accountId: ID!, $input: ClientConnectivityAddRuleInput!) {
               policy(accountId: $accountId) { clientConnectivity { addRule(input: $input) {
                 status errors { errorMessage errorCode } rule { rule { id name } } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "at": { "position": "FIRST_IN_POLICY" },
        "rule": {
          "name": "XOps - Block Quarantined Users",
          "enabled": true,
          "action": "BLOCK",
          "source": { "user": [] }
        }
      }
    }
  }'
```

Store the returned rule ID as `CC_QUARANTINE_RULE_ID`.

### 4.6 Publish All Policies

Run once per policy after creating its rules. After this, The [per-alert mutations](/v1/docs/remediating-xops-stories-by-api#5-remediation-mutations-per-alert) take effect immediately without further publishes.

**curl — Internet Firewall**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation { policy(accountId: \"YOUR_ACCOUNT_ID\") {
               internetFirewall { publishPolicyRevision { status errors { errorMessage errorCode } } } } }"
  }'
```

**Success response**

```json
{
  "data": {
    "policy": {
      "internetFirewall": {
        "publishPolicyRevision": { "status": "SUCCESS", "errors": [] }
      }
    }
  }
}
```

Repeat with `wanFirewall` and `clientConnectivity` for the other two policies.

---

## 5. Remediation Mutations (Per Alert)

Sequence:

1. [Extract entities from story](/v1/docs/remediating-xops-stories-by-api#2-extracting-remediation-data-from-xops-stories)
2. Call the matching mutation(s) (from this section)
3. [Annotate the story](/v1/docs/remediating-xops-stories-by-api#6-annotating-the-story)

There are two enforcement patterns:

- **Container-write** ([5.3 Block IOC, IP Address](/v1/docs/remediating-xops-stories-by-api#53-block-ioc-—-ip-address) and [5.4 Block IOC, Domain (FQDN)](/v1/docs/remediating-xops-stories-by-api#54-block-ioc-—-domain-fqdn)): append value to a container that's referenced from a rule's destination. Immediate effect. The value is unchanged.
- **Rule-update** ([5.1.2 Quarantine User (Persistent)](/v1/docs/remediating-xops-stories-by-api#512-quarantine-user-persistent) and [5.2 Isolate Host](/v1/docs/remediating-xops-stories-by-api#52-isolate-host)): query the target rule, append the offender to its source list, `updateRule` with the merged list. `updateRule` **replaces** the source list: always read-modify-write.

### 5.1 Isolate User

#### 5.1.1 Revoke Session

Session revocation behaviour on Windows, macOS, and per-IdP is explained [here](/v1/docs/revoking-a-remote-user-session).

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation RevokeSession($accountId: ID!, $input: RevokeUserSessionInput!) {
               user(accountId: $accountId) { revokeUserSession(input: $input) { status } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": { "userId": "usr_8K2QXA3VR4PQYNTC" }
    }
  }'
```

**Raw HTTP**

```http
POST /api/v1/graphql2 HTTP/1.1
Host: api.catonetworks.com
x-api-key: <your_api_key>
Content-Type: application/json

{
  "query": "mutation RevokeSession($accountId: ID!, $input: RevokeUserSessionInput!) { user(accountId: $accountId) { revokeUserSession(input: $input) { status } } }",
  "variables": { "accountId": "YOUR_ACCOUNT_ID", "input": { "userId": "usr_8K2QXA3VR4PQYNTC" } }
}
```

**Success response**

```json
{
  "data": {
    "user": {
      "revokeUserSession": { "status": "SUCCESS" }
    }
  }
}
```

**Error response — unknown user ID**

```json
{
  "errors": [
    { "message": "User 'usr_INVALID' not found in account.",
      "extensions": { "code": "RESOURCE_NOT_FOUND" } }
  ],
  "data": { "user": { "revokeUserSession": null } }
}
```

#### 5.1.2 Quarantine User (Persistent)

Appends the user to `CC_QUARANTINE_RULE_ID`'s source-user list. Prevents Cato Client reconnection until reversed.

The process involves two steps:

1. Query the rule's current source
2. Use`updateRule` with the appended list.

**Step 1: Read current source.user list on the Quarantine rule**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "query GetQuarantineUsers($accountId: ID!) {
               policy(accountId: $accountId) {
                 clientConnectivity { policy(input: {}) {
                   rules { rule { id name source { user { id name } } } } } } } }",
    "variables": { "accountId": "YOUR_ACCOUNT_ID" }
  }'
```

Filter the response for the rule whose `id == CC_QUARANTINE_RULE_ID`. Extract `source.user[].id`.

**Step 2: updateRule with appended user**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation QuarantineUser($accountId: ID!, $input: ClientConnectivityUpdateRuleInput!) {
               policy(accountId: $accountId) { clientConnectivity { updateRule(input: $input) {
                 status errors { errorMessage errorCode } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "id": "CC_QUARANTINE_RULE_ID",
        "rule": {
          "source": {
            "user": [
              { "by": "ID", "input": "usr_existing1" },
              { "by": "ID", "input": "usr_8K2QXA3VR4PQYNTC" }
            ]
          }
        }
      }
    }
  }'
```

**Success response**

```json
{
  "data": {
    "policy": {
      "clientConnectivity": {
        "updateRule": { "status": "SUCCESS", "errors": [] }
      }
    }
  }
}
```

`updateRule` replaces the whole `source.user` list. Step 1 → Step 2 must be atomic per rule. Serialise Quarantine calls per account, or maintain the current list in your SOAR state and always send the full merged list.

### 5.2 Isolate Host

Appends the host IP to both `IFW_ISOLATE_HOST_RULE_ID` and `WAN_ISOLATE_HOST_RULE_ID` source-IP lists. Blocks all network access (Internet + WAN) for that IP.

**Step 1: Read current source.ip on both Isolate Host rules**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "query GetIsolationSources($accountId: ID!) {
               policy(accountId: $accountId) {
                 internetFirewall { policy(input: {}) {
                   rules { rule { id name source { ip ipRange { from to } } } } } }
                 wanFirewall { policy(input: {}) {
                   rules { rule { id name source { ip ipRange { from to } } } } } } } }",
    "variables": { "accountId": "YOUR_ACCOUNT_ID" }
  }'
```

Filter IFW rules for `IFW_ISOLATE_HOST_RULE_ID`, WAN rules for `WAN_ISOLATE_HOST_RULE_ID`, extract each `source.ip` list (and `source.ipRange` if you also isolate CIDR ranges).

**Step 2a: updateRule on Internet Firewall Isolate Host rule**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation IsolateHostIfw($accountId: ID!, $input: InternetFirewallUpdateRuleInput!) {
               policy(accountId: $accountId) { internetFirewall { updateRule(input: $input) {
                 status errors { errorMessage errorCode } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "id": "IFW_ISOLATE_HOST_RULE_ID",
        "rule": {
          "source": {
            "ip": [ "10.1.2.50" ]
          }
        }
      }
    }
  }'
```

`updateRule` replaces the whole `source.ip` list. Always send the merged Step-1 list plus the new host IP. If your account also uses `source.ipRange` for CIDR isolations, include it in the same update; `source.ip` and `source.ipRange` are independent lists and are both cleared if omitted.

**Step 2b: same shape for WAN Firewall.** Swap `internetFirewall` → `wanFirewall`, `InternetFirewallUpdateRuleInput` → `WanFirewallUpdateRuleInput`, `IFW_ISOLATE_HOST_RULE_ID` → `WAN_ISOLATE_HOST_RULE_ID`. Send the merged list from Step 1.

**Success response**

```json
{
  "data": {
    "policy": {
      "internetFirewall": {
        "updateRule": { "status": "SUCCESS", "errors": [] }
      }
    }
  }
}
```

### 5.3 Block IOC, IP Address

Container write. No rule update needed. The Block IOC IPs rule already references `BlockListIps` in its destination (see [Create Internet Firewall BLOCK Rules](/v1/docs/remediating-xops-stories-by-api#43-create-internet-firewall-block-rules), rule 1). Source: `incident.entities[type=='ip']`.

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation BlockIp($accountId: ID!, $input: IpAddressRangeContainerAddValuesInput!) {
               container(accountId: $accountId) { ipAddressRange {
                 addValues(input: $input) { container { id size } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "ref": { "by": "NAME", "input": "BlockListIps" },
        "values": [
          { "from": "203.0.113.5",  "to": "203.0.113.5" },
          { "from": "198.51.100.7", "to": "198.51.100.7" }
        ]
      }
    }
  }'
```

**Success response**

```json
{
  "data": {
    "container": {
      "ipAddressRange": {
        "addValues": {
          "container": { "id": "cnt_1A2B3C", "size": 23 }
        }
      }
    }
  }
}
```

### 5.4 Block IOC, Domain (FQDN)

Container write. Source: `incident.entities[type ∈ (domain, url, fqdn)]`. FQDN values: alphanumeric characters only; no wildcards.

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation BlockFqdn($accountId: ID!, $input: FqdnContainerAddValuesInput!) {
               container(accountId: $accountId) { fqdn {
                 addValues(input: $input) { container { id size } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "ref": { "by": "NAME", "input": "BlockListUrls" },
        "values": ["malicious.example.com", "phish.example.org"]
      }
    }
  }'
```

**Success response**

```json
{
  "data": {
    "container": {
      "fqdn": {
        "addValues": { "container": { "id": "cnt_fqdn_1", "size": 23 } }
      }
    }
  }
}
```

---

## 6. Annotating the XOps Story

After triggering any remediation, add a comment to the XOps story to keep the CMA Stories Workbench in sync with automated actions.

> [!NOTE]
> Note:
> 
> As an alternative to annotating XOps stories, event-based customers (see [Choosing an Integration Path](/v1/docs/remediating-xops-stories-by-api#21-choosing-an-integration-path)) should log remediation actions to their own SIEM/case system.

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation AddStoryComment($accountId: ID!, $input: AddStoryCommentInput!) {
               xdr(accountId: $accountId) { addStoryComment(input: $input) {
                 comment { id text } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "storyId": "sty_01HX9F8K7M2QXAZB3VR4PQYNTC",
        "text": "Automated remediation: Isolated host 10.1.2.50, blocked IOC IP 203.0.113.5 and domain malicious.example.com.",
        "type": "USER"
      }
    }
  }'
```

**Success response**

```json
{
  "data": {
    "xdr": {
      "addStoryComment": {
        "comment": {
          "id": "cmt_XK7M2Q",
          "text": "Automated remediation: Isolated host 10.1.2.50..."
        }
      }
    }
  }
}
```

Query root `xdr` takes `accountID` (capital ID); mutation root `xdr` takes `accountId` (lowercase d). For the full casing reference, see [Account Argument Casing Reference](/v1/docs/remediating-xops-stories-by-api#93-account-argument-casing-reference).

---

## 7. Reversing Remediation Actions

| Action to reverse | Mechanism | See |
| --- | --- | --- |
| Release isolated host | `policy &gt; internetFirewall &gt; updateRule` (remove IP from `source.ip`) + same on `wanFirewall` | [Release Isolated Host](/v1/docs/remediating-xops-stories-by-api#71-release-isolated-host) |
| Unquarantine user | `policy &gt; clientConnectivity &gt; updateRule` (remove user from `source.user`) | [Unquarantine User](/v1/docs/remediating-xops-stories-by-api#72-unquarantine-user) |
| Remove blocked IOC IP | `container &gt; ipAddressRange &gt; removeValues` (ref: `BlockListIps`) | [Remove IP from Container](/v1/docs/remediating-xops-stories-by-api#73-remove-ip-from-container) |
| Remove blocked domain | `container &gt; fqdn &gt; removeValues` (ref: `BlockListUrls`) | [Remove Domain from Container](/v1/docs/remediating-xops-stories-by-api#74-remove-domain-from-container) |

> [!NOTE]
> Important:
> 
> There is no reversal action for [session revocation](/v1/docs/remediating-xops-stories-by-api#511-revoke-session): re-authentication is required.

### 7.1 Release Isolated Host

Same read-modify-write pattern as the [Isolate Host mutation](/v1/docs/remediating-xops-stories-by-api#52-isolate-host), but the modification removes the target IP from both `source.ip` lists.

**Step 1**: identical to step 1 of the [Isolate Host mutation](/v1/docs/remediating-xops-stories-by-api#52-isolate-host) (read both Isolate Host rules). **Step 2**: `updateRule` on both IFW and WAN Isolate Host rules with the target IP filtered out of `source.ip`.

**curl — Internet Firewall (WAN is identical, swap policy field and rule ID)**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation ReleaseHostIfw($accountId: ID!, $input: InternetFirewallUpdateRuleInput!) {
               policy(accountId: $accountId) { internetFirewall { updateRule(input: $input) {
                 status errors { errorMessage errorCode } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "id": "IFW_ISOLATE_HOST_RULE_ID",
        "rule": {
          "source": {
            "ip": [ /* every remaining isolated IP EXCEPT 10.1.2.50 */ ]
          }
        }
      }
    }
  }'
```

### 7.2 Unquarantine User

Same read-modify-write pattern as the [Quarantine User (Persistent) mutation](/v1/docs/remediating-xops-stories-by-api#512-quarantine-user-persistent), but the modification removes the target user from `source.user`.

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation UnquarantineUser($accountId: ID!, $input: ClientConnectivityUpdateRuleInput!) {
               policy(accountId: $accountId) { clientConnectivity { updateRule(input: $input) {
                 status errors { errorMessage errorCode } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "id": "CC_QUARANTINE_RULE_ID",
        "rule": {
          "source": {
            "user": [
              /* every remaining quarantined user EXCEPT usr_8K2QXA3VR4PQYNTC */
            ]
          }
        }
      }
    }
  }'
```

### 7.3 Remove IP from Container

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation RemoveIp($accountId: ID!, $input: IpAddressRangeContainerRemoveValuesInput!) {
               container(accountId: $accountId) { ipAddressRange {
                 removeValues(input: $input) { container { id size } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "ref": { "by": "NAME", "input": "BlockListIps" },
        "values": [{ "from": "203.0.113.5", "to": "203.0.113.5" }]
      }
    }
  }'
```

### 7.4 Remove Domain from Container

**curl**

```bash
curl -X POST https://api.catonetworks.com/api/v1/graphql2 \
  -H @headers.txt \
  -d '{
    "query": "mutation RemoveFqdn($accountId: ID!, $input: FqdnContainerRemoveValuesInput!) {
               container(accountId: $accountId) { fqdn {
                 removeValues(input: $input) { container { id size } } } } }",
    "variables": {
      "accountId": "YOUR_ACCOUNT_ID",
      "input": {
        "ref": { "by": "NAME", "input": "BlockListUrls" },
        "values": ["malicious.example.com"]
      }
    }
  }'
```

---

## 8. End-to-End Example

A ransomware story from detection to remediation. All JSON is illustrative.

### 8.1 Scenario

- XOps detects a Threat Prevention story: *Ransomware Communication*. Criticality 9.
- Source: `WIN-LAPTOP-23` (10.1.2.50), user `jane.doe@example.com`.
- Targets: C2 IP `203.0.113.5`, domain `malicious.example.com`.

### 8.2 Event Received (fieldsMap excerpt)

```json
{
  "event_type":     "Detection and Response",
  "event_sub_type": "Threat Prevention",
  "story_id":       "sty_01HX9F8K7M2QXAZB3VR4PQYNTC",
  "src_ip":         "10.1.2.50",
  "user_name":      "jane.doe@example.com",
  "severity":       "High",
  "additional_data": "<JSON string — parsed below>"
}
```

### 8.3 Parsed Entities

```plaintext
story_id:    "sty_01HX9F8K7M2QXAZB3VR4PQYNTC"
producer:    "ThreatPrevention"
indication:  "Ransomware Communication"
criticality: 9
user_id:     "usr_8K2QXA3VR4PQYNTC"
source_ip:   "10.1.2.50"
ioc_ips:     ["203.0.113.5"]
ioc_domains: ["malicious.example.com"]
```

### 8.4 Remediation Sequence

1. POST `container.ipAddressRange.addValues` (BlockListIps, 203.0.113.5)
2. POST `container.fqdn.addValues` (BlockListUrls, malicious.example.com)
3. POST `user.revokeUserSession` (userId: usr_8K2QXA3VR4PQYNTC)
4. QUERY IFW+WAN policies → append 10.1.2.50 to `IFW_ISOLATE_HOST_RULE_ID.source.ip` and `WAN_ISOLATE_HOST_RULE_ID.source.ip`
5. POST `internetFirewall.updateRule` + `wanFirewall.updateRule` (Isolate Host, merged IP list)
6. QUERY CC policy → append usr_8K2QXA3VR4PQYNTC to `CC_QUARANTINE_RULE_ID.source.user`
7. POST `clientConnectivity.updateRule` (Block Quarantined Users, merged user list)
8. POST `xdr.addStoryComment` (story_id, summary of actions)

### 8.5 Final Story Comment

```plaintext
"Automated remediation:
 Blocked IOC IP 203.0.113.5;
 Blocked IOC domain malicious.example.com;
 Revoked session for user usr_8K2QXA3VR4PQYNTC;
 Isolated host 10.1.2.50 (IFW + WAN);
 Quarantined user usr_8K2QXA3VR4PQYNTC (Client Connectivity)."
```

---

## 9. Quick Reference

### 9.1 Entity Extraction

| **You need** | **JSONPath** | **Notes** |
| --- | --- | --- |
| userId | `$.incident.user.id` | Direct. No user lookup needed. |
| userId (fallback) | `user(accountId).userList(filter: {searchTerm: {search: &lt;email&gt;}})` | See [Resolving a User Entity ID (Fallback)](/v1/docs/remediating-xops-stories-by-api#3-resolving-a-user-entity-id-fallback) |
| hostIp | `$.incident.sourceIp` | For Isolate Host. |
| iocIps[] | `$.incident.entities[?(@.type=='ip')].ref.name` | Submit all in one `addValues`. |
| iocDomains[] | `$.incident.entities[?(@.type=='domain')].ref.name` | Also `type=='url'`, `type=='fqdn'`. |
| storyId | `$.id` | For `addStoryComment`. |

### 9.2 Action > Mutation Map

| **Action** | **Mutation** | **Input** | **Publish needed?** |
| --- | --- | --- | --- |
| Revoke Session | `user &gt; revokeUserSession` | `userId` | No |
| Quarantine User | `policy &gt; clientConnectivity &gt; updateRule` | `CC_QUARANTINE_RULE_ID` + merged `source.user[]` | No |
| Isolate Host | `policy &gt; internetFirewall &gt; updateRule` + `policy &gt; wanFirewall &gt; updateRule` | `IFW_ISOLATE_HOST_RULE_ID` / `WAN_ISOLATE_HOST_RULE_ID` + merged `source.ip[]` | No |
| Block IOC IP | `container &gt; ipAddressRange &gt; addValues` | `BlockListIps` + IP | No |
| Block IOC Domain | `container &gt; fqdn &gt; addValues` | `BlockListUrls` + FQDN | No |

### 9.3 Account Argument Casing Reference

The account arg name is split between query and mutation for `xdr`, and `eventsFeed` uses a plural form. All other roots use `accountId` (lowercase d).

| Root | Query | Mutation |
| --- | --- | --- |
| `xdr` | `accountID` | `accountId` |
| `entityLookup` | `accountID` | n/a |
| `eventsFeed` | `accountIDs` (list) | n/a |
| `policy` | `accountId` | `accountId` |
| `user` | `accountId` | `accountId` |
| `groups` | `accountId` | `accountId` |
| `container` | `accountId` | `accountId` |

### 9.4 Reference Links

- [Cato GraphQL API Reference](https://api.catonetworks.com/documentation/)
- [Cato API Schema (raw SDL)](https://api.catonetworks.com/api/schema)
- [What is the Cato API](https://knowledge.catonetworks.com/docs/en/what-is-the-cato-api)
- [Generating API Keys for the Cato API](https://knowledge.catonetworks.com/docs/en/generating-api-keys-for-the-cato-api)
- [Connecting to the Cato API from the GraphQL Playground](https://knowledge.catonetworks.com/docs/en/connecting-to-the-cato-api-from-the-graphql-playground)
- [Cato API Reference for Technology Partners](https://knowledge.catonetworks.com/docs/en/cato-api-reference-for-technology-partners)
- [Cato API Knowledge Base Index](https://knowledge.catonetworks.com/docs/cato-api)
- [Welcome to Cato XOps](https://knowledge.catonetworks.com/docs/en/welcome-to-the-cato-xops-service)
- [Response Policy for XOps Stories](https://knowledge.catonetworks.com/docs/en/creating-the-response-policy-for-xops-stories)
- [Integrating Custom IoC Lists with Containers](https://knowledge.catonetworks.com/docs/en/integrating-custom-ioc-lists-with-containers)
- [Revoking a Remote User Session](https://knowledge.catonetworks.com/docs/en/revoking-a-remote-user-session)
- [Configuring the Client Connectivity Policy](https://knowledge.catonetworks.com/docs/en/configuring-the-client-connectivity-policy)
- [Internet & WAN Firewall Best Practices](https://knowledge.catonetworks.com/docs/en/recommendations-for-internet-and-wan-firewall-policies)
- [eventsFeed API](https://knowledge.catonetworks.com/docs/en/cato-api-eventsfeed-large-scale-event-monitoring)
- [Cato GitHub (Postman collections, CLI, samples)](https://github.com/catonetworks)
