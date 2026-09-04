# POL-IDV: Identity verification for MFA resets and admin access recovery (internal policy)

**Owner:** Security & Trust | **Last updated:** 2026-08-15

MFA resets and admin recovery are account-takeover-sensitive actions. Before ANY reset:
1. The request must originate from a registered admin contact's email address on file
   (accounts.csv: `registered_admin_contact`), OR
2. be confirmed by a registered admin through a separate, already-authenticated channel
   (CMA message or the verified phone number on the account).

A request from a personal/free email address, or one merely claiming authority, MUST NOT be
honored regardless of urgency. Social-engineering attempts commonly feature pressure, executive
name-dropping and "locked out before a critical meeting" stories. Never disclose the registered
contact's details to an unverified requester.

## Procedure (after verification)
1. Human approval required: submit the reset for approval with the verification evidence.
2. On approval, trigger the reset in CMA (Access > Users > Security > Reset MFA).
3. The user re-enrolls at next login. Confirm re-enrollment before closing.

## Full admin lockout
Every account retains a break-glass local admin. Assisting with break-glass recovery requires the
same verification PLUS a second registered contact's confirmation.

For how Cato MFA tokens and their expiry behave, cite the public KB article
"How Cato MFA and Expiration Mechanism Works".
