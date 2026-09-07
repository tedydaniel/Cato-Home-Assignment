---
title: "Managing Vulnerabilities for the Cato Socket and Client"
slug: "managing-vulnerabilities-for-the-cato-socket-and-client"
updated: 2026-06-15T09:34:38Z
published: 2026-06-22T09:20:31Z
canonical: "knowledge.catonetworks.com/managing-vulnerabilities-for-the-cato-socket-and-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Vulnerabilities for the Cato Socket and Client

This article discusses how the Cato platform manages vulnerabilities of different severities for the Cato Socket and the Cato Client.

## Overview

Cato continuously monitors vulnerabilities through active participation in security and vulnerability disclosure organizations. As both a member and contributor, Cato receives early notifications about Common Vulnerabilities and Exposures (CVEs) relevant to its products. In parallel, Cato regularly conducts penetration testing, both internally and in collaboration with external experts, to proactively identify potential weaknesses.

Following industry best practices, Cato only publishes CVEs after validating the vulnerability and releasing a new Socket or Client version that contains the fix, regardless of its severity. All Cato CVE advisories include remediation steps in the **What Changes Do I Need to Make** section.

Cato also maintains strict update cycles for third-party libraries, such as OpenSSL, to ensure timely adoption of critical security fixes. When applicable, Cato publishes its own CVEs as part of a transparent and responsible disclosure process.

To receive email notifications when Cato publishes a new security update, please click the **Follow** button in the [Security Announcements section](/v1/docs/security-announcements-1) in the Knowledge Base.

### Example of Publishing a CVE

This section is an example that describes the process for how Cato patches a discovered vulnerability and publishes the CVE.

1. The Cato Application Security team discovers and validates that there is a vulnerability in the Windows Client v5.7.
2. Windows Client RnD team completes development and testing of a new Client v5.7.1 that contains the patch, and releases it to customers.
3. Cato publishes a CVE with details of the vulnerability.

To mitigate potential avenues of attack, Cato only publicly discloses vulnerabilities when protective measures are actively in place.

## Sockets

The Cato Socket uses a proprietary operating system (Socket-OS), which significantly reduces exposure to common open-source vulnerabilities. Cato continuously conducts penetration testing to ensure that the Socket remains a secure and robust platform.

### Socket Patch Management Process

Cato applies patches to Socket devices based on the severity of the identified security issue:

- When a **critical** security issue is discovered:
  - Cato releases an urgent Socket update (usually a minor version) as a managed service that includes patches for critical issues. All Sockets in the customer's account are upgraded automatically. This process includes clear communication and detailed release notes.

**Note:** If the automatic Socket upgrade service is paused, you need to resume the Socket upgrade to receive the newest version with security patches.
- When a **medium** to **low** security issue is discovered:
  - Cato delivers quarterly Socket updates that enhance security with patches for medium to low issues, improve performance, and introduce new features. Regularly updating your Sockets to the newest version helps you maintain a strong security posture across your network.

## Cato Clients

Cato continuously conducts penetration testing to ensure that the [Clients on all platforms](/v1/docs/cato-clients) (Windows, macOS, iOS, Android, Linux, Chromebook), as well as our clientless solutions, remain secure and robust.

### Client Patch Management Process

Cato applies patches to Clients based on the severity of the identified security issue:

- When a **critical** security issue is discovered:
  - Cato releases an urgent Client update with a patch for the critical issue that can be downloaded from the [Access> Client Rollout](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy) page in the Cato Management Application or the [Client download portal](https://clientdownload.catonetworks.com/). This process includes clear communication and detailed release notes.

For Windows, macOS, and Linux, the Client can be rolled out as a managed service, where all Clients in the customer's account are upgraded automatically by Cato Networks. For other operating systems, the Client can be distributed via an MDM or installed manually.
- When a **medium** to **low** security issue is discovered:
  - Cato delivers quarterly Client versions that enhance security with patches for medium to low issues, improve performance, and introduce new features. Regularly updating your Clients to the newest version helps you maintain a strong security posture across your network.

## Related Articles

- [Understanding Cato's Managed Socket Upgrade Service](/v1/docs/understanding-cato-s-managed-socket-upgrade-service)
- [Recommendations for Cato Client Upgrades](/v1/docs/recommendations-for-cato-client-upgrades)
