# Evaluation answers

Generated through the same conversation and graph path as the chat UI.

## Q01
What is the effective MTU over the Socket-to-PoP DTLS tunnel, and what does the Socket do with an oversized WAN packet that has the DF bit set?

For the Socket-to-PoP DTLS tunnel, the effective MTU is reduced by DTLS overhead to 1383 bytes. If the DF bit is set and a WAN packet exceeds the effective MTU, the Socket sends an ICMP Fragmentation Needed message back to the sender with the acceptable MTU size. If DF is not set, the Socket fragments the oversized WAN packet and the PoP reassembles it before forwarding. If you want, I can also summarize how this behaves when multiple active WAN links are present.

### Citations
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — Behavior for Do Not Fragment (DF) Setting (WAN Interfaces)
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — MTU Behavior with Multiple Active WAN Links
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — Overview
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — Socket LAN Ports and Jumbo Frames

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Behavior for Do Not Fragment (DF) Setting (WAN Interfaces) (score: 0.03639344262295082)
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — MTU Behavior with Multiple Active WAN Links (score: 0.031988636363636365)
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Overview (score: 0.030418470418470418)
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket LAN Ports and Jumbo Frames (score: 0.03039344262295082)

Latency: 9521.1 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q02
Do Cato Sockets support jumbo frames on LAN ports? What happens to a 9000-byte frame received on a LAN port?

Cato doesn’t support jumbo frames on Socket LAN ports. If the Socket receives a packet larger than 1500 bytes on a LAN port, it checks the DF bit: if DF is not set, the Socket accepts and fragments the packet; if DF is set, it drops the packet and sends an ICMP Fragmentation Needed message back to the sender. The same knowledge also notes that the Socket LAN Firewall inspects and enforces traffic policies on packets traversing the Socket LAN interfaces. 

### Citations
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — Socket LAN Ports and Jumbo Frames
- https://knowledge.catonetworks.com/docs/what-are-cato-sockets.md — What are Cato Sockets — Socket Next Gen LAN Firewall
- https://knowledge.catonetworks.com/docs/understanding-cato-sockets.md — What are Cato Sockets — Socket Next Gen LAN Firewall
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — Overview
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — Behavior for Do Not Fragment (DF) Setting (WAN Interfaces)

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket LAN Ports and Jumbo Frames (score: 0.03275707898658718)
- https://knowledge.catonetworks.com/docs/what-are-cato-sockets.md — Socket Next Gen LAN Firewall (score: 0.02471590909090909)
- https://knowledge.catonetworks.com/docs/understanding-cato-sockets.md — Socket Next Gen LAN Firewall (score: 0.024475524475524476)
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Overview (score: 0.026129032258064518)
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Behavior for Do Not Fragment (DF) Setting (WAN Interfaces) (score: 0.023373015873015872)

Latency: 7747.7 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q03
A Socket site has two active WAN links with discovered MTUs of 1450 and 1383 bytes. Which MTU is used downstream, and do passive links affect it?

For Socket sites with multiple active WAN links, the PoP uses the lowest discovered MTU across all downstream tunnels, and the Socket uses the smallest MTU among active links for the upstream tunnel. Passive WAN links do not influence the MTU used for active tunnels. If you’re asking about a specific site, please share whether it is Active/Active or Active/Passive.

### Citations
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — MTU Behavior with Multiple Active WAN Links
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Cato Socket Link SLA Architecture — Active/Active Site Behavior
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Cato Socket Link SLA Architecture — Active/Passive Site Behavior
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Socket MTU and DTLS Tunnels — Configuring the MTU for a Specific Socket Site
- https://knowledge.catonetworks.com/docs/configuring-sites-with-cato-sockets.md — Configuring Sites with Cato Sockets — Configuring Primary and Secondary Connections
- https://knowledge.catonetworks.com/docs/performance-issues-for-socket-sites-troubleshooting.md — Performance Issues for Socket Sites Troubleshooting — Troubleshooting the Issue

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — MTU Behavior with Multiple Active WAN Links (score: 0.034393442622950826)
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Active/Active Site Behavior (score: 0.030129032258064514)
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Active/Passive Site Behavior (score: 0.028925373134328358)
- https://knowledge.catonetworks.com/docs/socket-mtu-and-dtls-tunnels.md — Configuring the MTU for a Specific Socket Site (score: 0.027038123167155426)
- https://knowledge.catonetworks.com/docs/configuring-sites-with-cato-sockets.md — Configuring Primary and Secondary Connections (score: 0.026060606060606062)
- https://knowledge.catonetworks.com/docs/performance-issues-for-socket-sites-troubleshooting.md — Troubleshooting the Issue (score: 0.027513513513513513)

Latency: 7582.9 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q04
What are the default BGP Hold Time and keep-alive interval for a Cato site, and what happens if the two neighbors are configured with different Hold Times?

The validated documentation shows that for BGP neighbors in Cato, the default Metric is 100, and Hold Time and Keep-alive Interval are configurable advanced settings. For a redundant GCP VPN setup, the documented example uses a Hold Time of 30 and Keep-alive of 10 for faster convergence, and it also notes that the primary and backup peers use different metrics (100 and 110). I could not verify any specific documented behavior for how Cato handles neighbors with differing Hold Times beyond these configuration details. If you want, I can help confirm whether you mean Socket, IPsec, or GCP VPN BGP behavior.

### Citations
- https://knowledge.catonetworks.com/docs/setting-up-redundant-vpn-tunnels-to-google-cloud-platform-gcp.md — Setting Up Redundant VPN Tunnels to Google Cloud Platform (GCP) — Overview
- https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors-for-a-cato-socket.md — Configuring BGP Neighbors for a Cato Socket — Overview
- https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors-for-an-ipsec-connection.md — Configuring BGP Neighbors for an IPsec Connection — Overview
- https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors-for-a-cato-socket.md — Configuring BGP Neighbors for a Cato Socket — Defining a BGP Neighbor
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Configuring BFD for BGP Neighbors — Understanding BFD for BGP Enabled Sites

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/setting-up-redundant-vpn-tunnels-to-google-cloud-platform-gcp.md — Overview (score: 0.03639344262295082)
- https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors-for-a-cato-socket.md — Overview (score: 0.033125)
- https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors-for-an-ipsec-connection.md — Overview (score: 0.03288461538461539)
- https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors-for-a-cato-socket.md — Defining a BGP Neighbor (score: 0.024415584415584418)
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Understanding BFD for BGP Enabled Sites (score: 0.028174603174603175)

Latency: 7421.0 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q05
How many BGP routes can a Socket accept from a neighbor before the session is affected, and what are the two recommended ways to reduce the advertised routes?

Cato’s default limit is 1024 received prefixes from each BGP neighbor. To reduce the number of advertised routes, the knowledge base recommends summarizing internal prefixes into aggregated routes and applying route filtering to exclude infrastructure, transit, or other non-WAN-relevant prefixes. If the route count still exceeds 1024 after those steps, please contact Cato Support for further assistance.

### Citations
- https://knowledge.catonetworks.com/docs/using-bgp-in-the-cato-cloud.md — Using BGP in the Cato Cloud — Known Limitations
- https://knowledge.catonetworks.com/docs/bgp.md — Using BGP in the Cato Cloud — Known Limitations
- https://knowledge.catonetworks.com/docs/site-routing.md — Using BGP in the Cato Cloud — Known Limitations
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Understanding BGP Configuration Changes for Socket Sites — Understanding BGP Reset Behavior
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Understanding BGP Configuration Changes for Socket Sites — Fallback Behavior for Unsupported Peer Capabilities
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Understanding BGP Configuration Changes for Socket Sites — Overview
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-prefix-exhaustion.md — XOps Network Playbook - BGP Prefix Exhaustion — Step 2 - Reduce the number of advertised routes
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-prefix-exhaustion.md — XOps Network Playbook - BGP Prefix Exhaustion — Overview
- https://knowledge.catonetworks.com/docs/recovery-mechanisms-for-cato-site-types.md — Recovery Mechanisms for Cato Site Types — Routing Resiliency with BGP

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/using-bgp-in-the-cato-cloud.md — Known Limitations (score: 0.026153846153846153)
- https://knowledge.catonetworks.com/docs/bgp.md — Known Limitations (score: 0.02592074592074592)
- https://knowledge.catonetworks.com/docs/site-routing.md — Known Limitations (score: 0.025694603903559127)
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Understanding BGP Reset Behavior (score: 0.025261984392419175)
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Fallback Behavior for Unsupported Peer Capabilities (score: 0.025054945054945054)
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Overview (score: 0.024965920155793575)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-prefix-exhaustion.md — Step 2 - Reduce the number of advertised routes (score: 0.03139344262295082)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-prefix-exhaustion.md — Overview (score: 0.029492753623188407)
- https://knowledge.catonetworks.com/docs/recovery-mechanisms-for-cato-site-types.md — Routing Resiliency with BGP (score: 0.027425373134328357)

Latency: 8225.0 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q06
Which prerequisites and limits apply to BGP summary routes on Socket sites?

For Socket sites, BGP summary routes are supported on Sockets v19.x and higher, and the CIDR range for a summary route must be between /8 and /30. The available evidence also notes that a summary route is advertised only as long as at least one more specific route exists in the Socket or PoP routing table; otherwise, it is withdrawn. I can’t verify any additional prerequisites or limits beyond that from the supplied evidence.

### Citations
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Understanding BGP Configuration Changes for Socket Sites — Related Articles
- https://knowledge.catonetworks.com/docs/working-with-bgp-summary-routes.md — Working with BGP Summary Routes — Overview
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Understanding BGP Configuration Changes for Socket Sites — BGP Reset Behavior by Configuration Change
- https://knowledge.catonetworks.com/docs/product-update-oct-30th-2023.md — Product Update - Oct. 30th, 2023 — New Features & Enhancements
- https://knowledge.catonetworks.com/docs/working-with-bgp-summary-routes.md — Working with BGP Summary Routes — Understanding BGP Summary Routes

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — Related Articles (score: 0.03139344262295082)
- https://knowledge.catonetworks.com/docs/working-with-bgp-summary-routes.md — Overview (score: 0.030625)
- https://knowledge.catonetworks.com/docs/understanding-bgp-configuration-changes-for-socket-sites.md — BGP Reset Behavior by Configuration Change (score: 0.028888888888888888)
- https://knowledge.catonetworks.com/docs/product-update-oct-30th-2023.md — New Features & Enhancements (score: 0.029910714285714287)
- https://knowledge.catonetworks.com/docs/working-with-bgp-summary-routes.md — Understanding BGP Summary Routes (score: 0.030625)

Latency: 8096.4 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q07
What are the default BFD timers Cato recommends for an IPsec site versus a Cloud Interconnect site, and what must you do after changing BFD timers?

For IPsec sites, the knowledge base says the default BFD values are 1000 ms transmit, 1000 ms receive, and multiplier 5, and that these are generally optimal for BFD performance over an internet connection. It also says BFD interval settings must be between 100 and 1800 ms, and that after modifying BFD timers you should disable and then re-enable the BFD session for the changes to take effect. For BGP over Direct Connect, AWS defines the default BFD value as 300 ms with a multiplier of 3. If you want, I can also summarize the recommended guidance by site type in one short table.

### Citations
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Configuring BFD for BGP Neighbors — Understanding BFD for BGP Enabled Sites
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Configuring BFD for BGP Neighbors — Overview
- https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors-for-an-ipsec-connection.md — Configuring BGP Neighbors for an IPsec Connection — Overview
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev2-sites.md — Configuring IPsec IKEv2 Sites — Configuring the IPsec IKEv2 Settings
- https://knowledge.catonetworks.com/docs/product-update-jan-22nd-2024.md — Product Update - Jan. 22nd, 2024 — New Features & Enhancements
- https://knowledge.catonetworks.com/docs/product-update-mar-18th-2024.md — Product Update - Mar. 18th, 2024 — New Features & Enhancements
- https://knowledge.catonetworks.com/docs/product-update-feb-26th-2024.md — Product Update - Feb. 26th, 2024 — New Features & Enhancements

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Understanding BFD for BGP Enabled Sites (score: 0.027038123167155426)
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Overview (score: 0.02653409090909091)
- https://knowledge.catonetworks.com/docs/configuring-bgp-neighbors-for-an-ipsec-connection.md — Overview (score: 0.022657342657342656)
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev2-sites.md — Configuring the IPsec IKEv2 Settings (score: 0.024797979797979798)
- https://knowledge.catonetworks.com/docs/product-update-jan-22nd-2024.md — New Features & Enhancements (score: 0.02439344262295082)
- https://knowledge.catonetworks.com/docs/product-update-mar-18th-2024.md — New Features & Enhancements (score: 0.023873015873015872)
- https://knowledge.catonetworks.com/docs/product-update-feb-26th-2024.md — New Features & Enhancements (score: 0.022129032258064514)

Latency: 8015.1 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q08
On which site types does Cato support active BFD for BGP neighbors, and which UDP port does multi-hop BFD use?

Cato supports BFD in asynchronous mode, and BFD can be configured for BGP neighbors in the Cato Management Application and on the remote peer. The documentation says BFD can use single-hop or multi-hop mode, with transmit/receive intervals and a multiplier used to determine detection time. I could not verify any UDP port usage details from the provided evidence. If you want, I can help check whether your question is about BFD mode, timing settings, or a specific site type.

### Citations
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Configuring BFD for BGP Neighbors — Understanding BFD for BGP Enabled Sites
- https://knowledge.catonetworks.com/docs/recovery-mechanisms-for-cato-site-types.md — Recovery Mechanisms for Cato Site Types — Routing Resiliency with BGP
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Configuring BFD for BGP Neighbors — Overview
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Configuring BFD for BGP Neighbors — Configuring BFD for a site

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Understanding BFD for BGP Enabled Sites (score: 0.04644175180169478)
- https://knowledge.catonetworks.com/docs/recovery-mechanisms-for-cato-site-types.md — Routing Resiliency with BGP (score: 0.031948998178506376)
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Overview (score: 0.029841269841269842)
- https://knowledge.catonetworks.com/docs/configuring-bfd-for-bgp-neighbors.md — Configuring BFD for a site (score: 0.02744360902255639)

Latency: 7858.4 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q09
A BGP session shows Disconnected. Which CMA views does the playbook use to find the disconnect reason and to verify the route table?

For diagnosing a BGP session disconnect, the knowledge article points to the site’s BGP page in CMA (Network > Sites > {site name} > Site Configuration > BGP) to use **Show BGP Status** for the real-time session state. It also says to check **Monitoring > Routing Table** and filter by the site name to verify whether DYNAMIC routes are present or missing. The playbook also mentions Stories Workbench with the Network XDR preset for **BGP session disconnected** stories, and the Events page can show a BGP Session event with Action **Disconnected** or **Established**. If you want, I can narrow this to the exact view to use for confirming whether routes are being learned from BGP peers.

### Citations
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-session-disconnected.md — XOps Network Playbook - BGP Session Disconnected — Step 1 - Verifying that the BGP Session is Disconnected
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-session-disconnected.md — XOps Network Playbook - BGP Session Disconnected — Step 3 - Verifying that the BGP Disconnected Status is resolved
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-session-disconnected.md — XOps Network Playbook - BGP Session Disconnected — Overview
- https://knowledge.catonetworks.com/docs/access-to-internal-resources-troubleshooting.md — Access to Internal Resources Troubleshooting — Resolving Discovered Issues

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-session-disconnected.md — Step 1 - Verifying that the BGP Session is Disconnected (score: 0.030418470418470418)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-session-disconnected.md — Step 3 - Verifying that the BGP Disconnected Status is resolved (score: 0.0294708276797829)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-bgp-session-disconnected.md — Overview (score: 0.027878787878787878)
- https://knowledge.catonetworks.com/docs/access-to-internal-resources-troubleshooting.md — Resolving Discovered Issues (score: 0.02608450704225352)

Latency: 7687.5 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q10
An IPsec IKEv2 site logs NO_PROPOSAL_CHOSEN. What does it mean and how do you find exactly which parameters are being proposed?

NO_PROPOSAL_CHOSEN in IKEv2 indicates a mismatch in the security association parameters, such as algorithms or DH group. For IKEv2 sites, the knowledge base says to review the site’s IPsec tab, especially the Init and Auth Message Parameters, and adjust them to match the firewall settings. If you need to confirm exactly which parameters Cato is proposing, download the PCAP file and inspect the IKEv2 proposal details in the packet capture. I can also help if you want to focus on IKEv1 or IKEv2 specifically.

### Citations
- https://knowledge.catonetworks.com/docs/cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels.md — Cato Cloud to Cisco IOS/IOS-XE via HA IPSec Tunnels — Creating an HA IPsec Site for Your Account with Cisco IOS/IOS-XE Devices
- https://knowledge.catonetworks.com/docs/cato-cloud-to-fortigate-via-ha-ipsec-tunnels.md — Cato Cloud to FortiGate via HA IPSec Tunnels — IKEv2 Site – Configuring Cato IPsec IKEv2 Responder-Only with FortiGate
- https://knowledge.catonetworks.com/docs/recommendations-for-ipsec-connections.md — Recommendations for IPsec Connections — Best Practices for IPsec Connections
- https://knowledge.catonetworks.com/docs/working-with-advanced-configuration-for-the-account.md — Working with Advanced Configuration for the Account — IKEv2 Sites Sending a Single TS per Payload
- https://knowledge.catonetworks.com/docs/ipsec-site-connectivity-troubleshooting.md — IPsec Site Connectivity Troubleshooting — Troubleshooting the Issue
- https://knowledge.catonetworks.com/docs/xops-network-playbooks-1.md — XOps Network Playbook - IPsec Phase2 Failure — Step 2 - Resolving Discovered Issues
- https://knowledge.catonetworks.com/docs/xops-playbooks-1.md — XOps Network Playbook - IPsec Phase2 Failure — Step 2 - Resolving Discovered Issues

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels.md — Creating an HA IPsec Site for Your Account with Cisco IOS/IOS-XE Devices (score: 0.02750455373406193)
- https://knowledge.catonetworks.com/docs/cato-cloud-to-fortigate-via-ha-ipsec-tunnels.md — IKEv2 Site – Configuring Cato IPsec IKEv2 Responder-Only with FortiGate (score: 0.025816993464052286)
- https://knowledge.catonetworks.com/docs/recommendations-for-ipsec-connections.md — Best Practices for IPsec Connections (score: 0.025282331511839708)
- https://knowledge.catonetworks.com/docs/working-with-advanced-configuration-for-the-account.md — IKEv2 Sites Sending a Single TS per Payload (score: 0.021388888888888888)
- https://knowledge.catonetworks.com/docs/ipsec-site-connectivity-troubleshooting.md — Troubleshooting the Issue (score: 0.021013513513513514)
- https://knowledge.catonetworks.com/docs/xops-network-playbooks-1.md — Step 2 - Resolving Discovered Issues (score: 0.028174603174603175)
- https://knowledge.catonetworks.com/docs/xops-playbooks-1.md — Step 2 - Resolving Discovered Issues (score: 0.027984344422700588)

Latency: 8059.0 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q11
Why does a Cisco ASA return TS_UNACCEPTABLE to a Cato IPsec proposal, and how can it be fixed?

TS_UNACCEPTABLE can occur when Cato proposes multiple traffic selectors in a child SA and a third-party device, such as a Cisco ASA, only supports a single TS per child SA. The knowledge base says you can enable the setting to send a single TS per payload for an account or a specific IPsec IKEv2 site under Site Configuration > Advanced Configuration. For Cisco Meraki route-based tunnels with VPN health check enabled, the health-check probe can also trigger TS_UNACCEPTABLE; the documented self-service workaround is to switch to policy-based IPsec. If you want, I can help identify which of these scenarios matches your setup.

### Citations
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev2-sites.md — Configuring IPsec IKEv2 Sites — Sending a Single Traffic Selector for IKEv2 Sites
- https://knowledge.catonetworks.com/docs/working-with-advanced-configuration-for-the-account.md — Working with Advanced Configuration for the Account — IKEv2 Sites Sending a Single TS per Payload
- https://knowledge.catonetworks.com/docs/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check.md — IPsec Tunnel Fails to Establish with TS_UNACCEPTABLE When Meraki VPN Health Check Is Enabled — Issue
- https://knowledge.catonetworks.com/docs/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check.md — IPsec Tunnel Fails to Establish with TS_UNACCEPTABLE When Meraki VPN Health Check Is Enabled — Solution
- https://knowledge.catonetworks.com/docs/xops-network-playbook-ipsec-phase2-failure.md — XOps Network Playbook - IPsec Phase2 Failure — Step 2 - Resolving Discovered Issues
- https://knowledge.catonetworks.com/docs/xops-network-playbooks-1.md — XOps Network Playbook - IPsec Phase2 Failure — Step 2 - Resolving Discovered Issues
- https://knowledge.catonetworks.com/docs/xops-playbooks-1.md — XOps Network Playbook - IPsec Phase2 Failure — Step 2 - Resolving Discovered Issues

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev2-sites.md — Sending a Single Traffic Selector for IKEv2 Sites (score: 0.049906956136464335)
- https://knowledge.catonetworks.com/docs/working-with-advanced-configuration-for-the-account.md — IKEv2 Sites Sending a Single TS per Payload (score: 0.03205128205128205)
- https://knowledge.catonetworks.com/docs/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check.md — Issue (score: 0.028484848484848484)
- https://knowledge.catonetworks.com/docs/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check.md — Solution (score: 0.024964871194379394)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-ipsec-phase2-failure.md — Step 2 - Resolving Discovered Issues (score: 0.029492753623188407)
- https://knowledge.catonetworks.com/docs/xops-network-playbooks-1.md — Step 2 - Resolving Discovered Issues (score: 0.029285714285714283)
- https://knowledge.catonetworks.com/docs/xops-playbooks-1.md — Step 2 - Resolving Discovered Issues (score: 0.029084507042253523)

Latency: 7625.7 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q12
Which IPsec encryption algorithms does Cato recommend for sites with 100 Mbps or more, and why?

For IPsec sites with bandwidth of 100 Mbps or more, the documented recommendation is to use only AES 128 GCM-16 or AES 256 GCM-16. AES CBC algorithms are documented for sites with bandwidth less than 100 Mbps. The guidance says GCM is more efficient and scalable than CBC for high-throughput encrypted traffic in the Cato Cloud.

### Citations
- https://knowledge.catonetworks.com/docs/cato-networks-information.md — Cato Cloud Thresholds and Limits — Supported Encryption Algorithms Based on IPsec Site Bandwidth
- https://knowledge.catonetworks.com/docs/cato-cloud-thresholds-and-limits.md — Cato Cloud Thresholds and Limits — Supported Encryption Algorithms Based on IPsec Site Bandwidth
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev2-sites.md — Configuring IPsec IKEv2 Sites — Overview

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/cato-networks-information.md — Supported Encryption Algorithms Based on IPsec Site Bandwidth (score: 0.0341712204007286)
- https://knowledge.catonetworks.com/docs/cato-cloud-thresholds-and-limits.md — Supported Encryption Algorithms Based on IPsec Site Bandwidth (score: 0.0339068100358423)
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev2-sites.md — Overview (score: 0.03365079365079365)

Latency: 7451.0 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q13
Why does Cato recommend selecting 'Initiate connection by Cato' for IKEv2 sites?

The recommended IKEv2 setting is to keep the default Initiate Connection by Cato enabled, because the Cato Cloud initiates the IPsec connection and this minimizes downtime. The docs also note that this default is strongly recommended for IKEv2 sites. If you want, I can also summarize when Cato recommends Automatic for the IKEv2 Init and Auth parameters.

### Citations
- https://knowledge.catonetworks.com/docs/cato-ipsec-guide-ikev1-vs-ikev2.md — Cato IPsec Guide: IKEv1 vs IKEv2 — IPsec Site Best Practices - Migrating to IKEv2
- https://knowledge.catonetworks.com/docs/configuring-sites-with-ipsec-connections.md — Configuring Sites with IPsec Connections — Configuring IKEv2 Settings
- https://knowledge.catonetworks.com/docs/ipsec-sites.md — Configuring Sites with IPsec Connections — Configuring IKEv2 Settings

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/cato-ipsec-guide-ikev1-vs-ikev2.md — IPsec Site Best Practices - Migrating to IKEv2 (score: 0.047557603686635946)
- https://knowledge.catonetworks.com/docs/configuring-sites-with-ipsec-connections.md — Configuring IKEv2 Settings (score: 0.04392998306041784)
- https://knowledge.catonetworks.com/docs/ipsec-sites.md — Configuring IKEv2 Settings (score: 0.04349680170575693)

Latency: 8711.1 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q14
What is the maximum length of the IPsec pre-shared key, and what is lost when a site's Connection Type is changed from IKEv1 to IKEv2?

We could verify that Cato documentation includes IKEv1 and IKEv2 site setup guidance, and that IPsec IKEv2 examples use primary and secondary pre-shared keys. The evidence does not state a maximum pre-shared key length. It also shows that for IPsec IKEv1, the connection type is Cato-initiated, while IKEv2 guidance recommends selecting “Initiate connection by Cato” in some examples. If you want, I can help verify a specific question about IKEv1 vs IKEv2 behavior or PSK handling from the documentation.

### Citations
- https://knowledge.catonetworks.com/docs/cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels.md — Cato Cloud to Cisco IOS/IOS-XE via HA IPSec Tunnels — Creating an HA IPsec Site for Your Account with Cisco IOS/IOS-XE Devices
- https://knowledge.catonetworks.com/docs/sample-procedure-adding-a-site-with-ipsec-ikev2.md — Sample Procedure - Adding a Site with IPsec IKEv2 — Overview
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev2-sites.md — Configuring IPsec IKEv2 Sites — Overview
- https://knowledge.catonetworks.com/docs/selecting-the-connection-type-for-a-site.md — Selecting the Connection Type for a Site — Overview
- https://knowledge.catonetworks.com/docs/cato-ipsec-guide-ikev1-vs-ikev2.md — Cato IPsec Guide: IKEv1 vs IKEv2 — IPsec Site Best Practices - Migrating to IKEv2
- https://knowledge.catonetworks.com/docs/configuring-sites-with-ipsec-connections.md — Configuring Sites with IPsec Connections — Selecting the IPsec IKEv1 Connection Type
- https://knowledge.catonetworks.com/docs/sample-procedure-adding-a-site-with-ipsec-ikev1.md — Sample Procedure - Adding a Site with IPsec IKEv1 — Example of Creating a New IPsec IKEv1Site

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels.md — Creating an HA IPsec Site for Your Account with Cisco IOS/IOS-XE Devices (score: 0.029705882352941176)
- https://knowledge.catonetworks.com/docs/sample-procedure-adding-a-site-with-ipsec-ikev2.md — Overview (score: 0.029084507042253523)
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev2-sites.md — Overview (score: 0.028373015873015873)
- https://knowledge.catonetworks.com/docs/selecting-the-connection-type-for-a-site.md — Overview (score: 0.026262626262626265)
- https://knowledge.catonetworks.com/docs/cato-ipsec-guide-ikev1-vs-ikev2.md — IPsec Site Best Practices - Migrating to IKEv2 (score: 0.024273504273504276)
- https://knowledge.catonetworks.com/docs/configuring-sites-with-ipsec-connections.md — Selecting the IPsec IKEv1 Connection Type (score: 0.023594771241830063)
- https://knowledge.catonetworks.com/docs/sample-procedure-adding-a-site-with-ipsec-ikev1.md — Example of Creating a New IPsec IKEv1Site (score: 0.02722222222222222)

Latency: 7679.6 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q15
A tunnel to Azure comes up but fails at rekey. What Azure behaviour around PFS/DH groups explains this?

The available documentation confirms that Azure handles PFS differently depending on whether it is the initiator or responder for a Child SA (ESP SA): when Azure is the initiator, it does not send a DH group by default, and when it is the responder, it accepts a DH group from the peer. The knowledge base also notes that cloud vendor IPsec settings can be incompatible and should match the Cato IPsec site settings. I can’t verify from the supplied evidence whether your specific tunnel rekey issue is caused by this behavior or by a different Azure configuration. If you’d like, please share whether Azure is acting as initiator or responder during the rekey.

### Citations
- https://knowledge.catonetworks.com/docs/cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels.md — Cato Cloud to Cisco IOS/IOS-XE via HA IPSec Tunnels — Creating an HA IPsec Site for Your Account with Cisco IOS/IOS-XE Devices
- https://knowledge.catonetworks.com/docs/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check.md — IPsec Tunnel Fails to Establish with TS_UNACCEPTABLE When Meraki VPN Health Check Is Enabled — Solution
- https://knowledge.catonetworks.com/docs/settings-that-can-be-modified-by-cato-support.md — Settings That Can be Modified by Cato Support — IPsec
- https://knowledge.catonetworks.com/docs/recommendations-for-ipsec-connections.md — Recommendations for IPsec Connections — Best Practices for IPsec Connections
- https://knowledge.catonetworks.com/docs/setting-up-a-cato-ipsec-tunnel-to-your-azure-virtual-network-gateway.md — Setting up a Cato IPsec Tunnel to Your Azure Virtual Network Gateway — Creating Active-Active Tunnels between the Virtual Network Gateway and the Cato PoP
- https://knowledge.catonetworks.com/docs/setting-up-redundant-vpn-tunnels-to-google-cloud-platform-gcp.md — Setting Up Redundant VPN Tunnels to Google Cloud Platform (GCP) — Overview
- https://knowledge.catonetworks.com/docs/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check.md — IPsec Tunnel Fails to Establish with TS_UNACCEPTABLE When Meraki VPN Health Check Is Enabled — Environment

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels.md — Creating an HA IPsec Site for Your Account with Cisco IOS/IOS-XE Devices (score: 0.0264957264957265)
- https://knowledge.catonetworks.com/docs/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check.md — Solution (score: 0.023814262023217247)
- https://knowledge.catonetworks.com/docs/settings-that-can-be-modified-by-cato-support.md — IPsec (score: 0.023060109289617485)
- https://knowledge.catonetworks.com/docs/recommendations-for-ipsec-connections.md — Best Practices for IPsec Connections (score: 0.028125)
- https://knowledge.catonetworks.com/docs/setting-up-a-cato-ipsec-tunnel-to-your-azure-virtual-network-gateway.md — Creating Active-Active Tunnels between the Virtual Network Gateway and the Cato PoP (score: 0.021785714285714283)
- https://knowledge.catonetworks.com/docs/setting-up-redundant-vpn-tunnels-to-google-cloud-platform-gcp.md — Overview (score: 0.0211986301369863)
- https://knowledge.catonetworks.com/docs/ipsec-tunnel-fails-to-establish-with-ts-unacceptable-meraki-vpn-health-check.md — Environment (score: 0.020069444444444445)

Latency: 7697.1 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q16
What are the requirements for enabling IP Overlapping between sites, and what is the default Cato system range?

For IP Overlapping, the account must not use Static Range Translation, one range must be smaller and fully contained within the other, all Sockets must be version 6.1 or higher, and each site must have a unique Native Range IP address. The Cato system range or the IP range for remote access users cannot be contained within an overlapping range, and the default Cato system range is 10.254.254.0/24. If you want to change the System Range, the documentation says to reach out to Cato Support.

### Citations
- https://knowledge.catonetworks.com/docs/configuring-your-account-to-support-ip-overlapping.md — Configuring Your Account to Support IP Overlapping — Requirements for IP Overlapping
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev1-sites.md — Configuring IPsec IKEv1 Sites — Overview of IPsec IKEv1 Connections
- https://knowledge.catonetworks.com/docs/configuring-network-ranges-for-a-site.md — Configuring Network Ranges for a Site — Creating a Network Range for a Local Network
- https://knowledge.catonetworks.com/docs/working-with-the-cato-system-range.md — Working with the Cato System Range — Reserved IPs in The System Range
- https://knowledge.catonetworks.com/docs/preparing-to-install-the-cato-client.md — Preparing to Install the Cato Client — Prerequisites for Installing the Cato Client
- https://knowledge.catonetworks.com/docs/working-with-the-cato-system-range.md — Working with the Cato System Range — Changing The System Range

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/configuring-your-account-to-support-ip-overlapping.md — Requirements for IP Overlapping (score: 0.05278688524590164)
- https://knowledge.catonetworks.com/docs/configuring-ipsec-ikev1-sites.md — Overview of IPsec IKEv1 Connections (score: 0.027425373134328357)
- https://knowledge.catonetworks.com/docs/configuring-network-ranges-for-a-site.md — Creating a Network Range for a Local Network (score: 0.026992753623188405)
- https://knowledge.catonetworks.com/docs/working-with-the-cato-system-range.md — Reserved IPs in The System Range (score: 0.030414746543778803)
- https://knowledge.catonetworks.com/docs/preparing-to-install-the-cato-client.md — Prerequisites for Installing the Cato Client (score: 0.026813186813186812)
- https://knowledge.catonetworks.com/docs/working-with-the-cato-system-range.md — Changing The System Range (score: 0.032393442622950824)

Latency: 7476.4 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q17
Which alternate UDP port can DTLS tunnels use, when is it recommended, and what are the version prerequisites?

Cato recommends configuring UDP port 1337 as the preferred DTLS port for Socket sites and Client users located in China, because UDP 443 can experience connectivity issues such as packet loss. By default, DTLS uses UDP 443 and falls back to 1337 when issues are experienced; for the alternate-port setting, 443 becomes the fallback. The available evidence does not mention any version prerequisites for this setting. If you want, I can also summarize where this setting is configured in System Settings.

### Citations
- https://knowledge.catonetworks.com/docs/understanding-cato-networking-in-china.md — Understanding Cato Networking in China — UDP Port 1337 for China Socket and Client DTLS Traffic
- https://knowledge.catonetworks.com/docs/using-an-alternate-udp-port-for-socket-and-client-dtls-traffic.md — Using an Alternate UDP Port for Socket and Client DTLS Traffic — Overview
- https://knowledge.catonetworks.com/docs/configuring-a-different-udp-port-for-the-cato-client.md — Configuring a Different UDP Port for the Cato Client — Overview
- https://knowledge.catonetworks.com/docs/using-an-alternate-udp-port-for-socket-and-client-dtls-traffic.md — Using an Alternate UDP Port for Socket and Client DTLS Traffic — Configuring the Alternate DTLS UDP Port
- https://knowledge.catonetworks.com/docs/socket-site-is-disconnected-with-lte-5g-providers.md — Socket Site is Disconnected with LTE/5G Providers — Solution

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/understanding-cato-networking-in-china.md — UDP Port 1337 for China Socket and Client DTLS Traffic (score: 0.029726775956284153)
- https://knowledge.catonetworks.com/docs/using-an-alternate-udp-port-for-socket-and-client-dtls-traffic.md — Overview (score: 0.029462365591397848)
- https://knowledge.catonetworks.com/docs/configuring-a-different-udp-port-for-the-cato-client.md — Overview (score: 0.024761904761904763)
- https://knowledge.catonetworks.com/docs/using-an-alternate-udp-port-for-socket-and-client-dtls-traffic.md — Configuring the Alternate DTLS UDP Port (score: 0.027220026350461134)
- https://knowledge.catonetworks.com/docs/socket-site-is-disconnected-with-lte-5g-providers.md — Solution (score: 0.027205882352941177)

Latency: 7482.1 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q18
Why might throughput drop for a Socket placed behind a third-party firewall, and what is the recommended fix?

The documentation says reduced throughput for a Cato Socket or VPN Client can be caused by a third-party firewall with UDP Flooding protection, which may limit traffic sent over Cato DTLS tunnels. Cato recommends disabling UDP Flooding protection in the firewall and running a speed test to compare the impact on throughput. If you want, I can help summarize the relevant troubleshooting step for your firewall model.

### Citations
- https://knowledge.catonetworks.com/docs/performance-troubleshooting-socket-behind-a-third-party-firewall.md — Performance Troubleshooting: Socket Behind a Third-Party Firewall — Solution
- https://knowledge.catonetworks.com/docs/performance-troubleshooting-socket-behind-a-third-party-firewall.md — Performance Troubleshooting: Socket Behind a Third-Party Firewall — Challenge
- https://knowledge.catonetworks.com/docs/cato-networks-information.md — Cato Cloud Thresholds and Limits — Supported Throughput for Cato Sites
- https://knowledge.catonetworks.com/docs/what-is-the-cato-firewall.md — What is the Cato Firewall — Overview
- https://knowledge.catonetworks.com/docs/performance-issues-for-socket-sites-troubleshooting.md — Performance Issues for Socket Sites Troubleshooting — Possible Causes

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/performance-troubleshooting-socket-behind-a-third-party-firewall.md — Solution (score: 0.029726775956284153)
- https://knowledge.catonetworks.com/docs/performance-troubleshooting-socket-behind-a-third-party-firewall.md — Challenge (score: 0.029462365591397848)
- https://knowledge.catonetworks.com/docs/cato-networks-information.md — Supported Throughput for Cato Sites (score: 0.022291666666666668)
- https://knowledge.catonetworks.com/docs/what-is-the-cato-firewall.md — Overview (score: 0.026060606060606062)
- https://knowledge.catonetworks.com/docs/performance-issues-for-socket-sites-troubleshooting.md — Possible Causes (score: 0.023174603174603174)

Latency: 7041.3 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q19
How does the secondary Socket decide to take over in a Socket HA pair, and what does it do right after taking over?

Manual Socket HA failover can be triggered from the CMA to temporarily fail a site over to the Secondary Socket and validate that HA is configured and responsive. The documented flow is that the CMA tells the Primary Socket to stop sending VRRP packets, the Secondary Socket detects the failure and becomes Master, and after about 120 seconds the CMA shows the expected status update. I can also confirm that failover can occur automatically if the Primary Socket fails, loses power, loses VRRP connectivity for more than three seconds, or has no Internet connectivity for more than ten seconds. If you want, I can verify the exact post-takeover status messages or where to view HA status in CMA.

### Citations
- https://knowledge.catonetworks.com/docs/manually-activate-socket-ha-failover.md — Manually Activate Socket HA Failover — Overview
- https://knowledge.catonetworks.com/docs/what-is-socket-ha.md — What is Socket HA — Failover Conditions for Socket High Availability
- https://knowledge.catonetworks.com/docs/socket-ha-status-troubleshooting.md — Socket HA Status Troubleshooting — Troubleshooting the Issue
- https://knowledge.catonetworks.com/docs/what-is-socket-ha.md — What is Socket HA — Monitoring Socket High Availability

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/manually-activate-socket-ha-failover.md — Overview (score: 0.027031963470319633)
- https://knowledge.catonetworks.com/docs/what-is-socket-ha.md — Failover Conditions for Socket High Availability (score: 0.026736111111111113)
- https://knowledge.catonetworks.com/docs/socket-ha-status-troubleshooting.md — Troubleshooting the Issue (score: 0.026262626262626265)
- https://knowledge.catonetworks.com/docs/what-is-socket-ha.md — Monitoring Socket High Availability (score: 0.02388888888888889)

Latency: 7914.3 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q20
What is an HA split-brain condition, how do you recognise it in CMA, and which Socket carries traffic while it lasts?

Cato HA for Sockets is designed for resiliency through active/active links, active/passive links, or an active/standby pair of two Sockets. The available evidence says a split-brain condition occurs when both vSockets take the Master role, often because HA keepalive messages do not reach the secondary vSocket or because the vSockets are on different firmware versions. In Azure, the evidence says CMA shows HA Status as Not Ready in a split-brain scenario, and it is recommended to check both vSockets’ WebUI pages to confirm their HA status; in AWS, the evidence calls out checking LAN connectivity, NSG rules on UDP/20480, different LAN subnets, and packet captures to see whether keepalives reach the secondary vSocket. I can’t verify from the evidence exactly how split-brain is represented in every CMA view, so if you want, please share whether this is AWS or Azure and which CMA screen you are seeing.

### Citations
- https://knowledge.catonetworks.com/docs/what-are-cato-sockets.md — What are Cato Sockets — High Availability
- https://knowledge.catonetworks.com/docs/understanding-cato-sockets.md — What are Cato Sockets — High Availability
- https://knowledge.catonetworks.com/docs/cato-sockets.md — What are Cato Sockets — High Availability
- https://knowledge.catonetworks.com/docs/aws-ha-vsocket-troubleshooting.md — AWS HA vSocket Troubleshooting — Troubleshooting the Issue
- https://knowledge.catonetworks.com/docs/azure-ha-vsocket-troubleshooting.md — Azure HA vSocket Troubleshooting — Troubleshooting the Issue
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Cato Socket Link SLA Architecture — Active/Active Site Behavior
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Cato Socket Link SLA Architecture — Overview

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/what-are-cato-sockets.md — High Availability (score: 0.025219941348973606)
- https://knowledge.catonetworks.com/docs/understanding-cato-sockets.md — High Availability (score: 0.024963924963924963)
- https://knowledge.catonetworks.com/docs/cato-sockets.md — High Availability (score: 0.02471590909090909)
- https://knowledge.catonetworks.com/docs/aws-ha-vsocket-troubleshooting.md — Troubleshooting the Issue (score: 0.029069069069069073)
- https://knowledge.catonetworks.com/docs/azure-ha-vsocket-troubleshooting.md — Troubleshooting the Issue (score: 0.02393162393162393)
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Active/Active Site Behavior (score: 0.020069444444444445)
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Overview (score: 0.027826086956521737)

Latency: 8494.1 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q21
Can an X1600 and an X1600 LTE Socket form an HA pair? What about X1500 and X1500B?

Cato supports Socket HA for physical Socket sites, AWS vSocket sites, and Azure vSocket sites. The available evidence also states that Socket HA sites can use two Sockets with the same Socket type, but the excerpt does not list the full set of compatible model pairings. If you share the exact Socket models you want to pair, I can verify whether that combination is documented.

### Citations
- https://knowledge.catonetworks.com/docs/what-is-socket-ha.md — What is Socket HA — Overview of Socket High Availability for a Site
- https://knowledge.catonetworks.com/docs/cato-socket-connection-prerequisites-and-known-limitations.md — Cato Socket Connection Prerequisites and Known Limitations — Socket Known Limitations
- https://knowledge.catonetworks.com/docs/configuring-and-monitoring-socket-wi-fi-networks.md — Configuring and Monitoring Socket Wi-Fi Networks — Overview
- https://knowledge.catonetworks.com/docs/socket-x1500-deployment-guide.md — Socket X1500 Deployment Guide — Additional Resources
- https://knowledge.catonetworks.com/docs/hardware.md — Hardware — Cato Sockets
- https://knowledge.catonetworks.com/docs/configuring-sites-with-cato-sockets.md — Configuring Sites with Cato Sockets — Overview
- https://knowledge.catonetworks.com/docs/what-are-cato-sockets.md — What are Cato Sockets — High Availability
- https://knowledge.catonetworks.com/docs/understanding-cato-sockets.md — What are Cato Sockets — High Availability

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/what-is-socket-ha.md — Overview of Socket High Availability for a Site (score: 0.029444444444444447)
- https://knowledge.catonetworks.com/docs/cato-socket-connection-prerequisites-and-known-limitations.md — Socket Known Limitations (score: 0.027826086956521737)
- https://knowledge.catonetworks.com/docs/configuring-and-monitoring-socket-wi-fi-networks.md — Overview (score: 0.02750455373406193)
- https://knowledge.catonetworks.com/docs/socket-x1500-deployment-guide.md — Additional Resources (score: 0.02750455373406193)
- https://knowledge.catonetworks.com/docs/hardware.md — Cato Sockets (score: 0.025816993464052286)
- https://knowledge.catonetworks.com/docs/configuring-sites-with-cato-sockets.md — Overview (score: 0.025017921146953406)
- https://knowledge.catonetworks.com/docs/what-are-cato-sockets.md — High Availability (score: 0.028129032258064516)
- https://knowledge.catonetworks.com/docs/understanding-cato-sockets.md — High Availability (score: 0.027873015873015872)

Latency: 7608.4 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q22
What are the prerequisites for triggering a manual HA failover from CMA, and what status is expected about two minutes later?

To manually activate Socket HA failover, go to Socket > Actions > Activate Manual HA Failover, then wait approximately 120 seconds and refresh the Socket page to verify the new status. The documented guidance says this should show the Secondary Socket as active, and it also notes to ensure onsite Socket personnel are available before performing the failover. It further warns not to use manual HA failover for Socket maintenance because that can create a split-brain issue. If you want, I can also summarize the documented steps to return control to the Primary Socket.

### Citations
- https://knowledge.catonetworks.com/docs/manually-activate-socket-ha-failover.md — Manually Activate Socket HA Failover — Overview
- https://knowledge.catonetworks.com/docs/xops-network-playbook-ha-status-is-not-ready.md — XOps Network Playbook - HA Status Is Not Ready — Step 1 - Verifying that HA Status is Not Ready
- https://knowledge.catonetworks.com/docs/aws-ha-vsocket-troubleshooting.md — AWS HA vSocket Troubleshooting — Symptoms
- https://knowledge.catonetworks.com/docs/manually-activate-socket-ha-failover.md — Manually Activate Socket HA Failover — Activating Manual HA Failover
- https://knowledge.catonetworks.com/docs/aws-ha-vsocket-troubleshooting.md — AWS HA vSocket Troubleshooting — Troubleshooting the Issue
- https://knowledge.catonetworks.com/docs/manually-activate-socket-ha-failover.md — Manually Activate Socket HA Failover — Reverting to the Primary Socket

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/manually-activate-socket-ha-failover.md — Overview (score: 0.02885630498533724)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-ha-status-is-not-ready.md — Step 1 - Verifying that HA Status is Not Ready (score: 0.022657342657342656)
- https://knowledge.catonetworks.com/docs/aws-ha-vsocket-troubleshooting.md — Symptoms (score: 0.022424242424242423)
- https://knowledge.catonetworks.com/docs/manually-activate-socket-ha-failover.md — Activating Manual HA Failover (score: 0.025873015873015874)
- https://knowledge.catonetworks.com/docs/aws-ha-vsocket-troubleshooting.md — Troubleshooting the Issue (score: 0.024925373134328358)
- https://knowledge.catonetworks.com/docs/manually-activate-socket-ha-failover.md — Reverting to the Primary Socket (score: 0.02603648424543947)

Latency: 8205.7 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q23
Which conditions generate an 'HA Not Ready' connectivity event, and when is 'HA Ready' generated afterwards?

According to the documentation, an HA Not Ready connectivity event can be generated when both Sockets in an HA configuration report as the primary Socket for 30 seconds. An HA Ready event is generated when one Socket reports as primary and the other as secondary for 30 seconds after an HA Not Ready event. The HA status is also described as Not Ready when the site has incompatible Socket versions, a Socket is disconnected, or there is an HA keepalive failure. If you want, I can also summarize the related HA status conditions from the Socket HA and connectivity status articles.

### Citations
- https://knowledge.catonetworks.com/docs/monitoring-your-site-with-connectivity-events.md — Monitoring Your Site with Connectivity Events — Overview of Connectivity Events
- https://knowledge.catonetworks.com/docs/xops-network-playbook-ha-status-is-not-ready.md — XOps Network Playbook - HA Status Is Not Ready — Step 1 - Verifying that HA Status is Not Ready
- https://knowledge.catonetworks.com/docs/what-is-socket-ha.md — What is Socket HA — Understanding Socket High Availability and Failover
- https://knowledge.catonetworks.com/docs/connectivity-statuses-for-cato-sites.md — Connectivity Statuses for Cato Sites — Socket Site Connectivity Statuses
- https://knowledge.catonetworks.com/docs/xops-network-playbook-ha-status-is-not-ready.md — XOps Network Playbook - HA Status Is Not Ready — Overview
- https://knowledge.catonetworks.com/docs/socket-ha-status-troubleshooting.md — Socket HA Status Troubleshooting — Troubleshooting the Issue

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/monitoring-your-site-with-connectivity-events.md — Overview of Connectivity Events (score: 0.029211087420042643)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-ha-status-is-not-ready.md — Step 1 - Verifying that HA Status is Not Ready (score: 0.024444444444444442)
- https://knowledge.catonetworks.com/docs/what-is-socket-ha.md — Understanding Socket High Availability and Failover (score: 0.02424908424908425)
- https://knowledge.catonetworks.com/docs/connectivity-statuses-for-cato-sites.md — Socket Site Connectivity Statuses (score: 0.027984344422700588)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-ha-status-is-not-ready.md — Overview (score: 0.026813186813186812)
- https://knowledge.catonetworks.com/docs/socket-ha-status-troubleshooting.md — Troubleshooting the Issue (score: 0.02632034632034632)

Latency: 7777.8 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q24
After how long is a 'Disconnected' connectivity event generated for an active link, and after how long is 'Connected' generated?

For Socket sites, a Connected event is generated after a tunnel has been connected to the PoP for 30 seconds and the link role is Active. A Disconnected event is generated if the Active link’s tunnel to the PoP is disconnected for more than 2.5 minutes, and if the tunnel reconnects within 2.5 minutes, a Reconnected event is generated instead. The connectivity status can also show Connected or Degraded depending on the site type and the conditions listed in the documentation. If you want, I can help clarify the behavior for Socket, IPsec, or Cloud Interconnect sites specifically.

### Citations
- https://knowledge.catonetworks.com/docs/monitoring-your-site-with-connectivity-events.md — Monitoring Your Site with Connectivity Events — Overview of Connectivity Events
- https://knowledge.catonetworks.com/docs/connectivity-statuses-for-cato-sites.md — Connectivity Statuses for Cato Sites — Socket Site Connectivity Statuses
- https://knowledge.catonetworks.com/docs/understanding-socket-connectivity-event-message-fields.md — Understanding Socket Connectivity Event Message Fields — Overview
- https://knowledge.catonetworks.com/docs/connectivity-statuses-for-cato-sites.md — Connectivity Statuses for Cato Sites — Cloud Interconnect Site Connectivity Statuses
- https://knowledge.catonetworks.com/docs/connectivity-statuses-for-cato-sites.md — Connectivity Statuses for Cato Sites — IPsec Site Connectivity Statuses
- https://knowledge.catonetworks.com/docs/socket-site-tunnel-connectivity-troubleshooting.md — Socket Site Tunnel Connectivity Troubleshooting — Troubleshooting the Issue

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/monitoring-your-site-with-connectivity-events.md — Overview of Connectivity Events (score: 0.027203682393555813)
- https://knowledge.catonetworks.com/docs/connectivity-statuses-for-cato-sites.md — Socket Site Connectivity Statuses (score: 0.025219941348973606)
- https://knowledge.catonetworks.com/docs/understanding-socket-connectivity-event-message-fields.md — Overview (score: 0.02499359795134443)
- https://knowledge.catonetworks.com/docs/connectivity-statuses-for-cato-sites.md — Cloud Interconnect Site Connectivity Statuses (score: 0.026782106782106782)
- https://knowledge.catonetworks.com/docs/connectivity-statuses-for-cato-sites.md — IPsec Site Connectivity Statuses (score: 0.02653409090909091)
- https://knowledge.catonetworks.com/docs/socket-site-tunnel-connectivity-troubleshooting.md — Troubleshooting the Issue (score: 0.026491228070175437)

Latency: 7709.5 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q25
When all active links have unacceptable SLA, how does the Socket evaluate moving to another PoP, and how long does the evaluation take?

When the Socket determines that all active links do not meet the SLA over the evaluation time range, this is considered an unacceptable SLA and the Socket automatically takes remediation actions. Depending on the link configuration and Connection SLA settings, it can activate a lower-precedence passive link, or if none of the links meet the acceptable thresholds, connect all links to a different PoP. The available evidence does not specify the exact evaluation duration or timing for that decision. If you want, I can help verify whether you’re asking about active/passive or active/active site behavior.

### Citations
- https://knowledge.catonetworks.com/docs/understanding-acceptable-and-unacceptable-sla-for-sites.md — Understanding Acceptable and Unacceptable SLA for Sites — Operating with Unacceptable SLA
- https://knowledge.catonetworks.com/docs/understanding-acceptable-and-unacceptable-sla-for-sites.md — Understanding Acceptable and Unacceptable SLA for Sites — Operating within Acceptable SLA
- https://knowledge.catonetworks.com/docs/configuring-the-connection-sla-settings-for-active-active-socket-sites.md — Configuring the Connection SLA Settings for Active/Active Socket Sites — How Traffic Distribution Works for Active/Active Sites (Default Behavior)
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Cato Socket Link SLA Architecture — Active/Passive Link Evaluation with Smart SLA
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Cato Socket Link SLA Architecture — Active/Active Site Behavior
- https://knowledge.catonetworks.com/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites.md — Configuring the Connection SLA Settings for Active/Passive Socket Sites — Overview
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Cato Socket Link SLA Architecture — Active/Passive Site Behavior

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/understanding-acceptable-and-unacceptable-sla-for-sites.md — Operating with Unacceptable SLA (score: 0.02760683760683761)
- https://knowledge.catonetworks.com/docs/understanding-acceptable-and-unacceptable-sla-for-sites.md — Operating within Acceptable SLA (score: 0.024285714285714285)
- https://knowledge.catonetworks.com/docs/configuring-the-connection-sla-settings-for-active-active-socket-sites.md — How Traffic Distribution Works for Active/Active Sites (Default Behavior) (score: 0.024040404040404043)
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Active/Passive Link Evaluation with Smart SLA (score: 0.02779569892473118)
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Active/Active Site Behavior (score: 0.02639344262295082)
- https://knowledge.catonetworks.com/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites.md — Overview (score: 0.026159420289855073)
- https://knowledge.catonetworks.com/docs/cato-socket-link-sla-architecture.md — Active/Passive Site Behavior (score: 0.027417840375586852)

Latency: 8143.3 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q26
What does Last Mile Monitoring probe by default, how many probes can a rule carry, and what is the default probe interval?

The documentation says Last Mile Monitoring Probes monitor last-mile ISP link quality, and by default Cato measures the ISP links to facebook.com, google.com, and amazon.com. It also says you can configure custom websites for Internet and WAN traffic, and assign up to 5 probes for each rule. I couldn’t verify any default probe interval or additional limits from the provided evidence. If you want, I can help check whether you’re asking about the default destinations, the per-rule probe limit, or another setting.

### Citations
- https://knowledge.catonetworks.com/docs/last-mile-monitoring-probes-and-connectivity.md — Last Mile Monitoring Probes and Connectivity — Overview
- https://knowledge.catonetworks.com/docs/generating-a-last-mile-link-report.md — Generating Last Mile Link Reports — Understanding the Last Mile Link Report
- https://knowledge.catonetworks.com/docs/last-mile-monitoring-probes-and-connectivity.md — Last Mile Monitoring Probes and Connectivity — Enabling the Last Mile Monitoring Probes Policy
- https://knowledge.catonetworks.com/docs/last-mile-monitoring-probes-and-connectivity.md — Last Mile Monitoring Probes and Connectivity — Configuring the Last Mile Monitoring Probe Policy

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/last-mile-monitoring-probes-and-connectivity.md — Overview (score: 0.032393442622950824)
- https://knowledge.catonetworks.com/docs/generating-a-last-mile-link-report.md — Understanding the Last Mile Link Report (score: 0.027888888888888887)
- https://knowledge.catonetworks.com/docs/last-mile-monitoring-probes-and-connectivity.md — Enabling the Last Mile Monitoring Probes Policy (score: 0.027873015873015872)
- https://knowledge.catonetworks.com/docs/last-mile-monitoring-probes-and-connectivity.md — Configuring the Last Mile Monitoring Probe Policy (score: 0.026129032258064518)

Latency: 7680.6 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q27
Which KPIs can a Link Quality rule monitor, and what should you export from a Link Quality SLA story to raise a case with the ISP?

Cato Link Quality rules can monitor Packet Loss, Jitter, Latency, and Congestion, and a Last-Mile Quality event is generated when configured thresholds are exceeded. For a Link Quality SLA story, the validated guidance says to use the Actions menu and export data to the ISP template, selecting the relevant incident time range and link; the export includes Traceroute and ICMP/Ping results to help investigate last-mile issues and share with an ISP. I can’t verify any other export contents beyond Traceroute and ICMP/Ping from the supplied evidence. If you want, I can help map these fields to the specific story you’re looking at.

### Citations
- https://knowledge.catonetworks.com/docs/xops-network-playbook-link-quality-sla.md — XOps Network Playbook - Link Quality SLA — Overview
- https://knowledge.catonetworks.com/docs/working-with-link-health-rules.md — Working with Link Health Rules — Overview
- https://knowledge.catonetworks.com/docs/last-mile-monitoring-probes-and-connectivity.md — Last Mile Monitoring Probes and Connectivity — Overview
- https://knowledge.catonetworks.com/docs/xops-network-playbook-link-quality-sla.md — XOps Network Playbook - Link Quality SLA — (Optional) Step 2 - Review Ping & Traceroute data
- https://knowledge.catonetworks.com/docs/retrieving-diagnostic-data-with-site-operations-story-actions.md — Retrieving Diagnostic Data with Site Operations Story Actions — Retrieving and Exporting Traceroute and ICMP Results
- https://knowledge.catonetworks.com/docs/xops-network-playbook-link-quality-sla.md — XOps Network Playbook - Link Quality SLA — Raising cases to Cato Support
- https://knowledge.catonetworks.com/docs/xops-network-playbook-link-quality-sla.md — XOps Network Playbook - Link Quality SLA — Step 1 - Verifying the Link Quality Is Impacted

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/xops-network-playbook-link-quality-sla.md — Overview (score: 0.04893312516263336)
- https://knowledge.catonetworks.com/docs/working-with-link-health-rules.md — Overview (score: 0.03229166666666666)
- https://knowledge.catonetworks.com/docs/last-mile-monitoring-probes-and-connectivity.md — Overview (score: 0.02761904761904762)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-link-quality-sla.md — (Optional) Step 2 - Review Ping & Traceroute data (score: 0.0483424408014572)
- https://knowledge.catonetworks.com/docs/retrieving-diagnostic-data-with-site-operations-story-actions.md — Retrieving and Exporting Traceroute and ICMP Results (score: 0.031684587813620074)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-link-quality-sla.md — Raising cases to Cato Support (score: 0.02639344262295082)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-link-quality-sla.md — Step 1 - Verifying the Link Quality Is Impacted (score: 0.02608450704225352)

Latency: 7972.0 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q28
After a Socket upgrade the site is down and events show 'No open tunnel after grace time'. How long is the grace period, and what must be done before rebooting the Socket?

The documented grace period for the Socket Upgrade period is 17 minutes, and events with the message “No open tunnel after grace time” indicate the Socket was reported offline after that period ended. The troubleshooting guidance says to collect console logs before rebooting the Socket whenever possible, because logs on physical Sockets are lost after reboot and are crucial for root cause analysis. If the tunnel still fails to establish or the Socket becomes inaccessible after an upgrade, the documented next step is to reboot it. If you want, I can also summarize the recommended event filters and recovery sequence from the upgrade troubleshooting article.

### Citations
- https://knowledge.catonetworks.com/docs/xops-network-playbook-socket-offline-after-upgrade.md — XOps Network Playbook - Socket Offline After Upgrade — Step 1 - verify that the Site is Disconnected
- https://knowledge.catonetworks.com/docs/socket-upgrade-failure-troubleshooting.md — Socket Upgrade Failure Troubleshooting — Resolving Discovered Issues
- https://knowledge.catonetworks.com/docs/socket-upgrade-failure-troubleshooting.md — Socket Upgrade Failure Troubleshooting — Troubleshooting Socket Upgrade Failure
- https://knowledge.catonetworks.com/docs/managing-sockets.md — Managing Sockets — Managing Cato Sockets for a Site
- https://knowledge.catonetworks.com/docs/socket-sites.md — Managing Sockets — Managing Cato Sockets for a Site
- https://knowledge.catonetworks.com/docs/cato-socket-connection-prerequisites-and-known-limitations.md — Cato Socket Connection Prerequisites and Known Limitations — Socket Connection Prerequisites
- https://knowledge.catonetworks.com/docs/xops-network-playbook-socket-offline-after-upgrade.md — XOps Network Playbook - Socket Offline After Upgrade — Step 3 - Resolving Socket Inaccessible after an upgrade

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/xops-network-playbook-socket-offline-after-upgrade.md — Step 1 - verify that the Site is Disconnected (score: 0.03333333333333333)
- https://knowledge.catonetworks.com/docs/socket-upgrade-failure-troubleshooting.md — Resolving Discovered Issues (score: 0.02770334928229665)
- https://knowledge.catonetworks.com/docs/socket-upgrade-failure-troubleshooting.md — Troubleshooting Socket Upgrade Failure (score: 0.027433155080213906)
- https://knowledge.catonetworks.com/docs/managing-sockets.md — Managing Cato Sockets for a Site (score: 0.025157894736842105)
- https://knowledge.catonetworks.com/docs/socket-sites.md — Managing Cato Sockets for a Site (score: 0.024987012987012988)
- https://knowledge.catonetworks.com/docs/cato-socket-connection-prerequisites-and-known-limitations.md — Socket Connection Prerequisites (score: 0.026129032258064518)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-socket-offline-after-upgrade.md — Step 3 - Resolving Socket Inaccessible after an upgrade (score: 0.024658227848101268)

Latency: 7879.1 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q29
What connectivity requirement about upstream TLS inspection applies to Socket upgrades, and which ports must be connected for a gradual upgrade on an X1700?

The documentation says Socket upgrades require connectivity to specific Socket ports to the Cato Cloud, otherwise the new version may not install correctly and the Socket can roll back. It also says HTTPS traffic from the Socket’s WAN IP must be excluded from upstream SSL/TLS inspection, or the upgrade process fails. For X1700 Sockets, ports 1, 2-8, and add-on ports can be assigned to Cato, LAN, VRRP, or alternative WAN depending on the configuration, but I can’t verify a single required port list for your exact gradual-upgrade scenario from the evidence provided. If you want, share the exact X1700 model and which ports are currently assigned so I can narrow it down.

### Citations
- https://knowledge.catonetworks.com/docs/connectivity-requirements-for-socket-upgrades.md — Connectivity Requirements for Socket Upgrades — Overview
- https://knowledge.catonetworks.com/docs/socket-version-24-0-release-notes.md — Socket Version 24.0 Release Notes — Known Limitations
- https://knowledge.catonetworks.com/docs/product-update-feb-12th-2024.md — Product Update - Feb. 12th, 2024 — New Features & Enhancements
- https://knowledge.catonetworks.com/docs/exchanging-socket-ports.md — Exchanging Socket Ports — Socket Ports Destinations for the X1700 Socket
- https://knowledge.catonetworks.com/docs/how-to-change-the-socket-model-for-a-site.md — How to Change the Socket Model for a Site — Mapping the Socket Ports
- https://knowledge.catonetworks.com/docs/tls-inspection-troubleshooting.md — TLS Inspection Troubleshooting — Troubleshooting Common Issues
- https://knowledge.catonetworks.com/docs/features-troubleshooting-1.md — TLS Inspection Troubleshooting — Troubleshooting Common Issues

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/connectivity-requirements-for-socket-upgrades.md — Overview (score: 0.0339068100358423)
- https://knowledge.catonetworks.com/docs/socket-version-24-0-release-notes.md — Known Limitations (score: 0.024761904761904763)
- https://knowledge.catonetworks.com/docs/product-update-feb-12th-2024.md — New Features & Enhancements (score: 0.02277777777777778)
- https://knowledge.catonetworks.com/docs/exchanging-socket-ports.md — Socket Ports Destinations for the X1700 Socket (score: 0.02639344262295082)
- https://knowledge.catonetworks.com/docs/how-to-change-the-socket-model-for-a-site.md — Mapping the Socket Ports (score: 0.024492753623188406)
- https://knowledge.catonetworks.com/docs/tls-inspection-troubleshooting.md — Troubleshooting Common Issues (score: 0.023157894736842106)
- https://knowledge.catonetworks.com/docs/features-troubleshooting-1.md — Troubleshooting Common Issues (score: 0.022987012987012986)

Latency: 8015.8 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q30
A pinned banking app breaks with TLS inspection on. What does Cato recommend, and which operating systems are bypassed from TLS inspection automatically?

Cato recommends enabling TLS inspection for better security coverage, but some applications using certificate pinning, strict TLS validation, or mutual TLS may not work with inspection enabled. The documentation also says TLS inspection is bypassed for Android, Linux, and unidentified operating systems. If you’re asking about a specific app or device type, please share which one so I can verify whether an exclusion or bypass is documented.

### Citations
- https://knowledge.catonetworks.com/docs/tls-inspection-troubleshooting.md — TLS Inspection Troubleshooting — Troubleshooting Common Issues
- https://knowledge.catonetworks.com/docs/features-troubleshooting-1.md — TLS Inspection Troubleshooting — Troubleshooting Common Issues
- https://knowledge.catonetworks.com/docs/security-troubleshooting.md — TLS Inspection Troubleshooting — Troubleshooting Common Issues
- https://knowledge.catonetworks.com/docs/best-practices-for-tls-inspection.md — Best Practices for TLS Inspection — Enabling TLS Inspection
- https://knowledge.catonetworks.com/docs/features-troubleshooting-1.md — TLS Inspection Troubleshooting — Possible Causes
- https://knowledge.catonetworks.com/docs/fixing-tls-inspection-issues-for-claude-code.md — Fixing TLS inspection Issues for Claude Code — Issue
- https://knowledge.catonetworks.com/docs/best-practices-for-tls-inspection.md — Best Practices for TLS Inspection — Best Practices for TLS Inspection

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/tls-inspection-troubleshooting.md — Troubleshooting Common Issues (score: 0.025714285714285717)
- https://knowledge.catonetworks.com/docs/features-troubleshooting-1.md — Troubleshooting Common Issues (score: 0.02554778554778555)
- https://knowledge.catonetworks.com/docs/security-troubleshooting.md — Troubleshooting Common Issues (score: 0.025385500575373993)
- https://knowledge.catonetworks.com/docs/best-practices-for-tls-inspection.md — Enabling TLS Inspection (score: 0.026658227848101262)
- https://knowledge.catonetworks.com/docs/features-troubleshooting-1.md — Possible Causes (score: 0.0245)
- https://knowledge.catonetworks.com/docs/fixing-tls-inspection-issues-for-claude-code.md — Issue (score: 0.024129032258064516)
- https://knowledge.catonetworks.com/docs/best-practices-for-tls-inspection.md — Best Practices for TLS Inspection (score: 0.027625)

Latency: 7934.7 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q31
Users see certificate warnings when opening blocked HTTPS sites even though TLS inspection is disabled. Why, and what fixes it?

Cato can still serve block pages for blocked HTTPS websites even when TLS Inspection is disabled, and that can cause browser certificate warnings if the Cato Certificate is not installed on the device or browser. The docs also note that traffic matching a Firewall rule with Prompt or Block can trigger this behavior, and an untrusted or self-signed certificate may be blocked even though TLS Inspection is disabled. If you want, I can help verify whether the site is being blocked by a policy rule or whether the Cato Certificate is missing.

### Citations
- https://knowledge.catonetworks.com/docs/certificate-warnings-with-blocked-https-websites.md — Certificate Warnings with Blocked HTTPS Websites — Overview
- https://knowledge.catonetworks.com/docs/accessing-an-untrusted-website-is-blocked-even-though-tls-inspection-is-disabled.md — Accessing An Untrusted Website Is Blocked Even Though TLS Inspection Is Disabled — Troubleshooting
- https://knowledge.catonetworks.com/docs/getting-started-with-cato-certificates.md — Getting Started with Cato Certificates — Cato TLS Inspection Certificate
- https://knowledge.catonetworks.com/docs/tls-inspection-troubleshooting.md — TLS Inspection Troubleshooting — Symptoms
- https://knowledge.catonetworks.com/docs/accessing-an-untrusted-website-is-blocked-even-though-tls-inspection-is-disabled.md — Accessing An Untrusted Website Is Blocked Even Though TLS Inspection Is Disabled — Issue

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/certificate-warnings-with-blocked-https-websites.md — Overview (score: 0.03538461538461539)
- https://knowledge.catonetworks.com/docs/accessing-an-untrusted-website-is-blocked-even-though-tls-inspection-is-disabled.md — Troubleshooting (score: 0.03187301587301587)
- https://knowledge.catonetworks.com/docs/getting-started-with-cato-certificates.md — Cato TLS Inspection Certificate (score: 0.031625)
- https://knowledge.catonetworks.com/docs/tls-inspection-troubleshooting.md — Symptoms (score: 0.0285)
- https://knowledge.catonetworks.com/docs/accessing-an-untrusted-website-is-blocked-even-though-tls-inspection-is-disabled.md — Issue (score: 0.029726775956284153)

Latency: 8544.4 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q32
How do IPS allowlist rules differ from firewall rules in matching, and how can a rule be created directly from a block event?

IPS allowlist rules are used to make the IPS engine ignore matching traffic for IPS block actions, and you can also create one directly from an IPS block event in Home > Events. The Internet Firewall is a separate rule base with Allow, Block, and Prompt actions, and it evaluates traffic sequentially. Based on the evidence, I can verify the distinction between IPS allowlisting and firewall rules, but I cannot verify whether a specific rule should be created in your case without the event or policy details. If you’d like, share whether the traffic is blocked by an IPS signature or by the Internet Firewall.

### Citations
- https://knowledge.catonetworks.com/docs/allowlisting-ips-signatures.md — Allowlisting IPS Signatures — Overview of IPS Allowlisting
- https://knowledge.catonetworks.com/docs/internet-firewall.md — What is the Cato Internet Firewall? — Understanding the Settings for Internet Firewall Rules
- https://knowledge.catonetworks.com/docs/cato-firewalls.md — What is the Cato Internet Firewall? — Understanding the Settings for Internet Firewall Rules
- https://knowledge.catonetworks.com/docs/dns-security.md — Customizing the DNS Protections for IPS — Allowlisting DNS Traffic
- https://knowledge.catonetworks.com/docs/customizing-the-dns-protections-for-ips.md — Customizing the DNS Protections for IPS — Allowlisting DNS Traffic
- https://knowledge.catonetworks.com/docs/allowlisting-ips-signatures.md — Allowlisting IPS Signatures — Creating an IPS Allowlist Rule from a Block Event
- https://knowledge.catonetworks.com/docs/enabling-and-working-with-anti-malware-and-ips.md — Enabling and Working with Anti-Malware and IPS — Best Practice
- https://knowledge.catonetworks.com/docs/recommendations-for-internet-and-wan-firewall-policies.md — Recommendations for Internet and WAN Firewall Policies — Overview
- https://knowledge.catonetworks.com/docs/internet-firewall.md — What is the Cato Internet Firewall? — Overview

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/allowlisting-ips-signatures.md — Overview of IPS Allowlisting (score: 0.028157894736842104)
- https://knowledge.catonetworks.com/docs/internet-firewall.md — Understanding the Settings for Internet Firewall Rules (score: 0.027884615384615386)
- https://knowledge.catonetworks.com/docs/cato-firewalls.md — Understanding the Settings for Internet Firewall Rules (score: 0.027651515151515153)
- https://knowledge.catonetworks.com/docs/dns-security.md — Allowlisting DNS Traffic (score: 0.05062178588125292)
- https://knowledge.catonetworks.com/docs/customizing-the-dns-protections-for-ips.md — Allowlisting DNS Traffic (score: 0.05057889822595705)
- https://knowledge.catonetworks.com/docs/allowlisting-ips-signatures.md — Creating an IPS Allowlist Rule from a Block Event (score: 0.03362903225806452)
- https://knowledge.catonetworks.com/docs/enabling-and-working-with-anti-malware-and-ips.md — Best Practice (score: 0.033893442622950826)
- https://knowledge.catonetworks.com/docs/recommendations-for-internet-and-wan-firewall-policies.md — Overview (score: 0.028157894736842104)
- https://knowledge.catonetworks.com/docs/internet-firewall.md — Overview (score: 0.025384615384615387)

Latency: 8987.6 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q33
How many egress public IPs are included in an account's default license, and what does Cato recommend for VoIP egress rules?

By default, Cato accounts include three Cato-allocated public IPs, and the license view shows these as Licensed, Used, and Unused. For egress rules using static public IPs, the docs note that the default license for each account includes 3 unique IPs that can be used by any PoP. For VoIP traffic, Cato recommends configuring only one egress IP address and enabling the Preferred IP for SIP Traffic advanced setting to keep the same egress IP. If you want, I can help clarify whether you’re asking about the available licensed IPs or the recommended VoIP rule setup.

### Citations
- https://knowledge.catonetworks.com/docs/cato-licenses.md — Working with Cato License Types — Understanding the IPs Section
- https://knowledge.catonetworks.com/docs/account-information.md — Working with Cato License Types — Understanding the IPs Section
- https://knowledge.catonetworks.com/docs/working-with-cato-license-types.md — Working with Cato License Types — Understanding the IPs Section
- https://knowledge.catonetworks.com/docs/network-rule-evaluation-troubleshooting.md — Network Rule Evaluation Troubleshooting — Troubleshooting the Issue
- https://knowledge.catonetworks.com/docs/how-to-configure-a-network-rule-to-egress-traffic.md — How to Configure a Network Rule to Egress Traffic — Best Practices for Egressing Traffic
- https://knowledge.catonetworks.com/docs/how-to-configure-a-network-rule-to-egress-traffic.md — How to Configure a Network Rule to Egress Traffic — Troubleshooting Egressing Traffic with Network Rules
- https://knowledge.catonetworks.com/docs/how-to-configure-a-network-rule-to-egress-traffic.md — How to Configure a Network Rule to Egress Traffic — Configuring a Network Rule to Egress Traffic
- https://knowledge.catonetworks.com/docs/what-is-cato-sd-wan.md — What is Cato SD-WAN — Path Selection and Optimization Policies

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/cato-licenses.md — Understanding the IPs Section (score: 0.02839344262295082)
- https://knowledge.catonetworks.com/docs/account-information.md — Understanding the IPs Section (score: 0.028129032258064516)
- https://knowledge.catonetworks.com/docs/working-with-cato-license-types.md — Understanding the IPs Section (score: 0.027873015873015872)
- https://knowledge.catonetworks.com/docs/network-rule-evaluation-troubleshooting.md — Troubleshooting the Issue (score: 0.029670329670329672)
- https://knowledge.catonetworks.com/docs/how-to-configure-a-network-rule-to-egress-traffic.md — Best Practices for Egressing Traffic (score: 0.027053571428571427)
- https://knowledge.catonetworks.com/docs/how-to-configure-a-network-rule-to-egress-traffic.md — Troubleshooting Egressing Traffic with Network Rules (score: 0.026353944562899786)
- https://knowledge.catonetworks.com/docs/how-to-configure-a-network-rule-to-egress-traffic.md — Configuring a Network Rule to Egress Traffic (score: 0.027205882352941177)
- https://knowledge.catonetworks.com/docs/what-is-cato-sd-wan.md — Path Selection and Optimization Policies (score: 0.02548701298701299)

Latency: 9725.6 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q34
How long is a Cato MFA token valid, and when does Cato ask for the code again on a trusted device?

I can confirm that the available evidence includes internal guidance for MFA resets and full admin lockout recovery, but it does not verify how Cato MFA token validity or trusted-device re-prompt behavior works. The evidence points to a public KB article titled "How Cato MFA and Expiration Mechanism Works," but the article content itself is not provided here. If you want, I can help check whether you’re asking about token expiration, trusted-device persistence, or both.

### Citations
- policy://POL-IDV — POL-IDV: Identity verification for MFA resets and admin access recovery (internal policy) — Full admin lockout
- policy://POL-IDV — POL-IDV: Identity verification for MFA resets and admin access recovery (internal policy) — Procedure (after verification)
- policy://POL-CREDIT — POL-CREDIT: SLA credits, refunds, and billing disputes (internal policy) — Process

### Top retrieved chunks
- policy://POL-IDV — Full admin lockout (score: 0.10750000000000001)
- policy://POL-IDV — Procedure (after verification) (score: 0.10250000000000001)
- policy://POL-CREDIT — Process (score: 0.055)

Latency: 8048.6 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`

## Q35
Scheduled SCIM provisioning failed overnight. What are the playbook's three troubleshooting moves?

The SCIM troubleshooting playbook describes SCIM as a push-based provisioning mechanism to Cato Management Application and notes it supports Azure, Okta, and One Login. For a failed SCIM sync, it recommends reviewing whether maintenance activity coincided with the sync time and checking recent configuration changes in the Audit Trail, especially Domain model changes. If the playbook does not resolve the issue, the documentation says to submit a Support ticket and include the troubleshooting steps already taken. If helpful, I can narrow this down for Azure, Okta, or One Login.

### Citations
- https://knowledge.catonetworks.com/docs/xops-network-playbook-scim-provisioning-failed.md — XOps Network Playbook - SCIM Provisioning Failed — Raising Cases to Cato Support
- https://knowledge.catonetworks.com/docs/features-troubleshooting.md — SCIM Sync and Provisioning Troubleshooting — Troubleshooting the Issue
- https://knowledge.catonetworks.com/docs/scim-sync-and-provisioning-troubleshooting.md — SCIM Sync and Provisioning Troubleshooting — Troubleshooting the Issue
- https://knowledge.catonetworks.com/docs/xops-network-playbook-scim-provisioning-failed.md — XOps Network Playbook - SCIM Provisioning Failed — Step 2 - Troubleshooting SCIM Sync Failure
- https://knowledge.catonetworks.com/docs/access-troubleshooting.md — SCIM Sync and Provisioning Troubleshooting — Overview
- https://knowledge.catonetworks.com/docs/features-troubleshooting.md — SCIM Sync and Provisioning Troubleshooting — Overview
- https://knowledge.catonetworks.com/docs/scim-sync-and-provisioning-troubleshooting.md — SCIM Sync and Provisioning Troubleshooting — Overview

### Top retrieved chunks
- https://knowledge.catonetworks.com/docs/xops-network-playbook-scim-provisioning-failed.md — Raising Cases to Cato Support (score: 0.03276785714285714)
- https://knowledge.catonetworks.com/docs/features-troubleshooting.md — Troubleshooting the Issue (score: 0.03229437229437229)
- https://knowledge.catonetworks.com/docs/scim-sync-and-provisioning-troubleshooting.md — Troubleshooting the Issue (score: 0.0320682302771855)
- https://knowledge.catonetworks.com/docs/xops-network-playbook-scim-provisioning-failed.md — Step 2 - Troubleshooting SCIM Sync Failure (score: 0.03142857142857143)
- https://knowledge.catonetworks.com/docs/access-troubleshooting.md — Overview (score: 0.02782201405152225)
- https://knowledge.catonetworks.com/docs/features-troubleshooting.md — Overview (score: 0.030679156908665108)
- https://knowledge.catonetworks.com/docs/scim-sync-and-provisioning-troubleshooting.md — Overview (score: 0.03015873015873016)

Latency: 9489.1 ms
Token cost: recorded by LangSmith when configured
KB snapshot date: see `knowledge_base/snapshot/manifest.json`
