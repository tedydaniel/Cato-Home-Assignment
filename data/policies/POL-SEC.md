# POL-SEC: Security verdicts, IPS exceptions, and what support may change (internal policy)

**Owner:** Security Operations | **Last updated:** 2026-08-05

- Support may create narrowly scoped IPS allowlist rules (specific signature + destination +
  source scope) for suspected false positives, following the public KB procedure "Allowlisting
  IPS Signatures". Every exception gets a 30-day expiry and a follow-up date on the ticket, and a
  false-positive report is filed with Security Research (turnaround 2 business days).
- Support NEVER disables IPS, Anti-Malware or TLS Inspection globally, or sets an engine to
  monitor-only, as a workaround on a production account.
- Overriding an Anti-Malware / C2 / threat-reputation verdict is NOT a support decision: escalate
  to the security team with the event IDs. Customer assurance ("it's our red team tool") is not
  sufficient evidence.
- TLS inspection issues with pinned applications are solved with a narrow bypass rule, never by
  disabling inspection (see "Best Practices for TLS Inspection").
