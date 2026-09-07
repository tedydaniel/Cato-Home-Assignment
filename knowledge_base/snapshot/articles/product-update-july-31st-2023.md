---
title: "Product Update - July 31st, 2023"
slug: "product-update-july-31st-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-july-31st-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 31st, 2023

## New Features & Enhancements

- **Control and Monitor Automatic Client Rollouts:** Over the next few weeks, we are gradually rolling out the [Client Rollout screen](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy) to provide increased control and visibility of the rollout of Client versions.
  - You can now:
    - View the gradual rollout status of each Client
    - Pause and resume automatic upgrades per OS
    - Set different Client upgrade policies for each OS
    - Easily download the latest version of the Client and view the documentation
  - This screen replaces the **Client Access > Upgrade Policy** screen
- **New Domain Lookup Fields Help Identify Malicious Domains:** To help you assess the security risk of a domain, we added these new fields to the [Domain Lookup](/v1/docs/identifying-the-category-for-a-domain) results:
  - **Malicious Score**: The likelihood that the domain is malicious according to Cato threat intelligence algorithms
  - **Popularity:** How often the domain is visited according to Cato internal data - low popularity domains are generally suspicious
- **New Fields for Security Stories:** We are enriching story data in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench), based on the shared context of other stories in the account. We added these new fields:
  - **Predicted Verdict** and **Predicted Type:** These fields are based on machine learning predictions for the eventual verdict and potential malware type that you may identify. This helps you make an initial assessment of the likelihood if a story is malicious, and to focus your analysis on the most crucial stories
  - **Similar Stories:** A list of stories that helps you get important context for your analysis by showing stories with the same indicator of attack or target
- **Export Network Rules:** You can now export your Network Rules to a CSV file, from the [Network Rules](/v1/docs/configuring-network-rules) screen.

## Knowledge Base Updates

- [Troubleshooting Cato SDP Client Performance Issues](/v1/docs/cato-sdp-client-performance-troubleshooting)
- [Understanding Packet Flow with Cato SPACE Architecture](/v1/docs/understanding-packet-flow-with-cato-space-architecture)
