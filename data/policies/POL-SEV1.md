# POL-SEV1: Sev-1 definition and escalation (internal policy)

**Owner:** Incident Management | **Last updated:** 2026-08-20

## Definition
Sev-1: complete loss of connectivity for an entire account, two or more sites down in the same
region simultaneously, a suspected PoP-side outage, or a confirmed security incident. When in
doubt between Sev-1 and Sev-2, page as Sev-1.

## Escalation procedure
1. Acknowledge within 15 minutes with an incident reference.
2. Page the on-call incident commander (human) immediately - a Sev-1 is never handled by
   automation alone. Escalation to a human is mandatory.
3. Check the Cato status page (https://status.catonetworks.com/) and PoP health; if multiple
   accounts show tunnel drops to the same PoP, declare a platform incident and attach all related
   conversations to it.
4. Open a live incident bridge; record the incident ID on every related ticket.
5. Customer updates at least every 30 minutes until mitigated, even if the update is "still
   investigating".

## SLA
Sev-1 response SLA: 15 minutes (all tiers). Resolution target: 4 hours. Qualifying breaches feed
the credit process - see POL-CREDIT after the incident closes.
