# Support SLA Policy (synthetic, for this exercise)

SLA clocks start at ticket creation and run in business hours (Mon-Fri 08:00-18:00 in the
customer's primary region) except for P1, which runs 24x7. "First response" means a
substantive, ticket-specific reply - not an auto-acknowledgement.

## Response and resolution targets

| Priority | Definition | First response (Premium) | First response (Standard) | Resolution target |
|---|---|---|---|---|
| P1 | Sev-1: full outage, multi-site regional outage, security incident | 15 min (24x7) | 15 min (24x7) | 4 hours |
| P2 | Site down, HA failed, production tunnel down, business-critical app blocked | 1 hour | 4 hours | 1 business day |
| P3 | Degraded service, single-user/app issues, billing disputes | 4 business hours | 8 business hours | 3 business days |
| P4 | Questions, how-to, non-urgent configuration | 8 business hours | 2 business days | 5 business days |

In addition to the table: performance complaints (product area `performance`) on Premium
accounts must receive a substantive response within 8 business hours even when filed as P4.

## Update cadence
- P1: customer update every 30 minutes until mitigated (see POL-SEV1).
- P2: every 4 business hours.
- P3/P4: on every state change.

## Clock rules
- `pending customer` pauses the resolution clock; the first-response clock never pauses.
- `pending approval` (human gate) does NOT pause any clock - approval latency is the
  desk's problem, not the customer's.
- Reopened tickets resume the original clock; they do not start a new one.

## Breach consequences
Breaches on P1/P2 create qualifying events for the credit process in POL-CREDIT and must be
listed in the daily operations report.
