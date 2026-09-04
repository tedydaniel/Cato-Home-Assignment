# POL-CREDIT: SLA credits, refunds, and billing disputes (internal policy)

**Owner:** Support Operations | **Last updated:** 2026-07-08 | **Applies to:** all support agents

- Service credits for SLA breaches are computed per the customer's contract - typically 1/30 of
  the monthly service fee per full day of qualifying outage, capped per contract terms.
- Credits and refunds of ANY amount require human approval: the agent drafts the credit memo and a
  human billing approver must approve before anything is committed or promised to the customer.
- Never state a specific credit amount to the customer before approval. Use: "We have submitted a
  credit request for review; you will receive confirmation within 2 business days."

## Process
1. Verify the claimed outage against Cato incident records (incident ID, affected PoPs or services,
   duration). Customer-reported duration alone is not sufficient evidence.
2. Draft the credit memo: account, period, qualifying incident IDs, computed amount.
3. Submit for approval (approve / edit / reject). The conversation stays in `pending_approval`.
4. On approval, notify the customer and attach the memo. On rejection, communicate the decision
   with the approver's stated reason.

## Out of scope for support
Contract renegotiation, license quantity changes, early termination, and pricing go to the
account manager.
