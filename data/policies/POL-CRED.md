# POL-CRED: Credential hygiene in support conversations (internal policy)

**Owner:** Security & Trust | **Last updated:** 2026-02-18

If a customer pastes an API key, IPsec pre-shared key, RADIUS secret, SCIM token, or any password
into a conversation or ticket, treat it as compromised:
1. Redact the value from the transcript, the ticket record and all traces immediately.
2. Advise immediate rotation and confirm rotation before closing.
3. Never quote the credential back to the customer, even partially, and never "confirm whether it
   matches" what is configured on the Cato side.

IPsec PSKs may be up to 64 characters (see "Cato IPsec Guide: IKEv1 vs IKEv2"); rotating a PSK
means re-entering it on both peers and reconnecting the tunnel.
