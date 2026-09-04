# Telemetry (synthetic CMA data for the demo accounts)

This folder plays the role of the Cato Management Application (CMA) and Socket telemetry that a
support engineer consults instead of asking the customer to look at their own machine. Your agent
must reach it **through tools**, never by pasting the files into the prompt. Timestamps are frozen
around `2026-08-28T17:00:00Z` (use it as "now" during the demo).

| Path | What it is | Suggested tool |
|---|---|---|
| `sites.json` | Site inventory per account: connection type, Socket model/version, HA, WAN links, connected PoP, status, last seen, native range | `get_site_status(site_id)` / `list_sites(customer_id)` |
| `link_quality/<site_id>.csv` | 24 h of per-link last-mile metrics at 5-minute resolution (loss, latency, jitter, throughput) | `get_link_quality(site_id, window)` |
| `events/<site_id>.jsonl` | CMA events: Connectivity, Routing (BGP), IPsec (IKE), Socket upgrade, Security (IPS / Anti-Malware / TLS), Audit | `get_events(site_id, type, window)` |
| `bgp_status/<site_id>.json` | "Show BGP Status" raw output: neighbor state, negotiated timers, routes_count vs limit, last error | `get_bgp_status(site_id)` |
| `ipsec_status/<site_id>.json` | Tunnel status and IKE parameters as configured on the Cato side, plus what the peer proposed (from PCAP) | `get_ipsec_status(site_id)` |
| `clients/<email>.json` | Cato Client diagnostics for a user: version, last error, network conditions (captive portal, UDP/TCP 443 reachability), SCIM provisioning state | `get_client_diagnostics(user_email)` |

Every anomaly in here corresponds to a ticket or scenario. Examples: Munich Bureau (ACC-1008) is
down with the LTE last-resort link showing no carrier; Austin Office (ACC-1007) has a BGP session
flapping with *Hold Timer Expired* and `routes_count` at the 1024 limit; AWS eu-central-1
(ACC-1002) fails IKE with `NO_PROPOSAL_CHOSEN` and the PCAP shows the peer proposing CBC while
Cato is configured for GCM; Denver Clinic (ACC-1009) reported *No open tunnel after grace time*
after a scheduled upgrade; Perth Mine Site (ACC-1010) is HA Not Ready because the two Sockets run
different major versions.

Tool outputs are evidence the agent must cite alongside KB articles, e.g. "Show BGP Status reports
routes_count 1024/1024 [telemetry] — this is the route limit described in the BGP Prefix
Exhaustion playbook [kb:xops-network-playbook-bgp-prefix-exhaustion]".
