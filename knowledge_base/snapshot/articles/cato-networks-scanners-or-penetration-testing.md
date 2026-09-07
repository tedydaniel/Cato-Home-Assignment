---
title: "Cato Networks Scanners or Penetration Testing"
slug: "cato-networks-scanners-or-penetration-testing"
updated: 2026-08-16T10:35:16Z
published: 2026-08-16T10:35:16Z
canonical: "knowledge.catonetworks.com/cato-networks-scanners-or-penetration-testing"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Networks Scanners or Penetration Testing

## Preparing for a Penetration Test with Cato

This article explains the requirements for a penetration test based on the Cato Networks Terms of Use (TOU) - [https://www.catonetworks.com/msa/](https://www.catonetworks.com/msa/).

Every customer planning to conduct any kind of security activity such as penetration testing or running scanners must submit a **Penetration Test Request** ticket to initiate the request. In addition, provide the following details before actually running the tests, this is to ensure no impact to Cato's service we provide to our customers nor to avoid violating the terms of use.

**Note:** DDOS or stress testing is not part of the penetration test.

## Submitting a Request for a Penetration Test

**To submit a request for a penetration test:**

1. Open a ticket from the AI Workspace in the Cato Management Application (show me the [page](https://externallink.cc.catonetworks.com/#/account/me/aiWorkspace?support)).
2. Enter the following details:

- **Category:** Penetration Test Request
- **Priority:** Medium
- **Subject:** Description of the test
- **Description:** Please provide information on what is planned to be scanned or what vulnerabilities are planned to be checked
- **Source IPs:** IP addresses of the Scanners/Pentest machines/hosts. **Note:** The following IPs are restricted and can’t be used for a penetration test:
  - 10.x.x.x
  - 172.16–31.x.x
  - 192.168.x.x
- **Destination IPs:** [Cato-assigned IP addresses](/v1/docs/allocating-ip-addresses-for-the-account) that are relevant
- **Start Date** and **End Date** for the test, make sure that the Start Date is the current date or a future date
- **Tools and versions that will be used during the test:** List all the tools and their versions to be used to conduct the test

## Allowlisting IPS for the Penetration Test

If IPS is enabled on your account with the Block action, use the IPS Policy **Allow List** to allow the following signatures:

- cid_scan_attack_tools_inbound
- cid_scan_attack_tools_wanbound
- cid_scan_attack_tools_outbound

For more information, see [Allowlisting IPS Signatures](/v1/docs/allowlisting-ips-signatures).

After you complete the tests, remember to disable or delete the signatures from the IPS Policy **Allow List**.

## DNS Traffic with Penetration Testing

Penetration testing may detect that UDP Port 53 (DNS traffic) is open on a PoP in the Cato Cloud. The DNS service on the PoPs uses this port only to allow Sockets and SDP Clients to determine the closest available PoP. The PoP DNS service does not provide any other DNS functionality over UDP Port 53.
