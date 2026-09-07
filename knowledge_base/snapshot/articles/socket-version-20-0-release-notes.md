---
title: "Socket Version 20.0 Release Notes"
slug: "socket-version-20-0-release-notes"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-version-20-0-release-notes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Version 20.0 Release Notes

Socket version 20 includes the following features:

- This version also includes the firmware for the following features:
  - **Synthetic Probe Monitoring:** Synthetic probes let you proactively check the status of the apps for Internet breakout and the Cato tunnel. You can easily identify issues originating with your ISP, or a misconfiguration for a specific app with high latency due to QoS priority configuration
  - **Port and Transport Level Metrics for Sites**: We are introducing a new section in the [Network Analytics](/v1/docs/showing-the-site-network-analytics) page that provides visibility into physical port metrics, with a breakdown by Transport Types (Cato, Local Breakout, Off-Cloud, LAN, Alt. WAN) and Socket interface
  - **BGP Protection Mechanism Enhancement:** To guarantee uninterrupted access to Cato's internal servers, we are enhancing the BGP protection mechanism and ensuring that Cato’s system routes are consistently advertised to BGP peers.
    - The ranges include:
      - 10.254.254.1/32
      - 10.254.254.5/32
      - 10.254.254.232/32
      - 10.254.254.12/32
      - 10.254.254.0/24 (Cato's default system range)
    - If you need to disable this default configuration, contact your Cato representative or Support. However, disabling this feature will impact system performance

- v20.0.18221 includes:
  - **AWS vSocket IMDSv2 Support**: To align with AWS best practices, we are introducing support for the IMDSv2 security option for AWS vSocket sites, which employs session-oriented authentication mechanisms.
    - Enabling IMDSv2 support on the EC2 instance doesn't impact the site functionality
- v20.0.18453 includes:
  - Security updates: Update to the OpenSSH version used in the [Socket](https://support.catonetworks.com/hc/en-us/articles/19952349220381).
