---
title: "XOps Network Playbook - IPsec Phase2 Failure"
slug: "xops-network-playbook-ipsec-phase2-failure"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-ipsec-phase2-failure"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - IPsec Phase2 Failure

This playbook describes steps to resolve issues when a IPSec Phase2 Failure was detected.

## Overview

This playbook explains how to identify when IPSec Phase2 Failure occurred and outlines the steps you can take to this issue.

## Symptoms

- Connectivity loss
- Traffic Disruption

## Step 1 - Verify Failure Occurred

The following are the different ways that a Cato Management Application admin can verify that the IPSec Phase2 Failure occurred.

### Using the Story Drill-down

- Go to the **Stories Workbench** page and set the producer to **Account Operations**, including the filter 'Indication **In** IPsec Phase2 Failure**'.** Adjust the time frame as necessary. ![ipsec-story-drilldown.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33308496358941.jpeg)
- Verify that a story was created as shown below. ![ipsec-story-example.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33308508914461.jpeg)
- Click on the story to drill down into the details. It provides information on the story status, an incident timeline. ![story-drilldown.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33308496359453.jpeg)

### Review Tunnel Timeline

Go to the relevant site, and in the IPSec tab and click on Timeline to download the CSV file. review the file to confirm the story. ![ipsec-csv.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33310816808093.jpeg) In the example above we can see an error **NO_PROPOSAL_CHOSEN** is shown.

## Step 2 - Resolving Discovered Issues

The following shows the different ways that a Cato Management Application admin can resolve discovered issues for IPsec Phase2 Failure.

### No Proposal Chosen

In the Cato Management Application, go to the site’s **IPsec** tab and review the configuration.

- For **IPsec IKEv1 (Cato‑initiated)** tunnels, verify that the **Phase 2 parameters** match the settings on your firewall
- If you need to confirm exactly which parameters Cato is proposing, download the PCAP file and inspect the quick mode message for the **Transform Payload** within the **Proposal Payload**. This will show the encryption, integrity, Authentication selected, and other attributes offered by the initiator ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33460919493789.png)
- **For IPsec IKEv2** – In the Cato Management Application, browse to the site’s IPsec tab and review the **Init** and **Auth Message Parameters**. Adjust the configuration to ensure it matches the settings on your firewall.
- To confirm exactly which parameters are being proposed, download the PCAP file and inspect the **IKE_AUTH** message that contains the **CHILD_SAproposal**. Within the **Security Association** payload, review the **Transform Payload** to see the Encryption, Integrity, PFS (DH group), and other attributes offered by the peer proposing the CHILD_SA. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33463898737053.png)
  - If connection mode is set to Responder Only, reinitiate the session from your firewall post configuration change.

### TS UNACCEPTABLE

In the Cato Management Application, browse to the site IPsec Tab and click on the PCAP button to download the file.

- Review the PCAP file and search for the last Initiator/Responder Response payload for **TS_UNACCEPTABLE.**![ts_unacceptable.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33310816808861.jpeg)
- In the PCAP, review previous **IKE_AUTH_MID** packets for Traffic Selector payload (both Initiator & Responder) and compare the listed IP ranges for the IP ranges listed under the Routing tab in the site IPsec section in the Cato Management Application.
- To resolve the issue either remove or add the required IP ranges.
- When using IPsec with IKEv1, you may encounter an **INVALID ID INFORMATION** message during Phase 2 negotiation. This typically indicates that the two VPN peers are using different IP ranges for the tunnel. Ensuring that both sides define matching local and remote subnets will resolve this issue and allow the connection to establish successfully.

> [!NOTE]
> Note:
> 
> When creating a child SA, Cato sends multiple traffic selectors (TS) in the same TS payload in accordance with RFC 7295. Some third-party solutions, such as Cisco ASAs, only support a single TS in each child SA. A Cisco ASA will send a **TS_UNACCEPTABLE** message in response to a Cato proposal to create a child SA with multiple TS.
> 
> You can configure [your account](/v1/docs/working-with-advanced-configuration-for-the-account) or a specific [IPsec IKEv2 site](/v1/docs/advanced-configurations-for-a-site) to send each TS in a separate packet to support interoperability with these third-party solutions by enabling This configuration under **Site Configuration > Advanced Configuration**.

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
