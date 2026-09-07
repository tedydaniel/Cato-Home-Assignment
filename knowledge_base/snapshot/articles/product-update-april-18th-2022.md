---
title: "Product Update - April 18th, 2022"
slug: "product-update-april-18th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-april-18th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - April 18th, 2022

## New Features & Enhancements

- **New Cato Knowledge Base Coming Soon:** On April 24, 2022, we are introducing a completely new redesign of the Knowledge Base.
  - On April 24, you may experience some disruption with articles while we are implementing the changes to the production environment
- **Reminder for End-of-Life of the Legacy Cato Management Application:** Starting on April 24, 2022, you will only be able to access the [new Cato Management Application](https://cc.catonetworks.com/#/login). After this date, the legacy Cato Management Application will be end-of-life and no longer available.

## Cato SDP Client Releases

- **Windows Client v5.3:** We are starting the gradual roll-out for the Windows Client version 5.3. This version includes:
  - **Enhanced Reauthentication Experience:** A notification lets users know that the SSO or MFA session will soon expire and allows them to seamlessly reauthenticate. [Read more](/v1/docs/understanding-expiring-session-for-users).
  - For Windows devices with the Intel Killer NICs, Cato recommends that you update to the latest suite. In some tests, this update overcomes the relevant connectivity issues.
  - Bug fixes:
    - Computers recover from sleep mode were unable to connect to the Cato Cloud
    - For Windows Clients with Never-Off enabled and behind a Socket, the user couldn’t use Office Mode to connect
    - Sometimes the Client didn’t reconnect when moving between different networks, such as cellular to WiFi
    - After the MFA session expires, the OS browser didn’t open the authentication page

## Security Updates

- **Cato Cloud Updated for BOD 22-01 CISA Security Recommendations:** Cato continuously monitors the CISA guidelines and recommendations, including the recently released [Binding Operational Directive (BOD) 22-01](https://www.cisa.gov/uscert/ncas/current-activity/2022/03/25/cisa-adds-66-known-exploited-vulnerabilities-catalog). We completed updating the IPS protections to protect against the network-based threats in the Cato Cloud. [Read more about Cato and CISA](https://www.catonetworks.com/blog/how-cato-was-able-to-meet-the-cisa-directive-so-quickly/).
- **IPS Signatures:**
  - Malware - BTCWare (Enhancement)
  - SSH - Brute-force Attempt (Enhancement)
  - CVE-2022-26318
  - CVE-2022-23253
  - CVE-2022-22536
  - CVE-2022-21703
  - CVE-2022-20699
  - CVE-2022-0543
  - CVE-2022-0079
  - CVE-2021-45897
  - CVE-2021-45467
  - CVE-2021-45466
  - CVE-2021-45382
  - CVE-2021-4045
  - CVE-2021-36260
  - CVE-2021-34414
  - CVE-2021-31985
  - CVE-2021-31589
  - CVE-2021-22941
  - CVE-2021-21974
  - CVE-2021-20023
  - CVE-2021-1498
  - CVE-2020-9377
  - CVE-2020-7247
  - CVE-2020-6287
  - CVE-2020-1938
  - CVE-2020-16846
  - CVE-2020-10221
  - CVE-2019-7483
  - CVE-2019-6340
  - CVE-2019-18370
  - CVE-2019-15107
  - CVE-2019-11043
  - CVE-2019-1003030
  - CVE-2018-6961
  - CVE-2018-18325
  - CVE-2018-15811
  - CVE-2018-14839
  - CVE-2018-11138
  - CVE-2018-0125
  - CVE-2017-9822
  - CVE-2017-6334
  - CVE-2017-3881
  - CVE-2017-12617
  - CVE-2016-1555
  - CVE-2016-11021
  - CVE-2016-10174
  - CVE-2016-0752
  - CVE-2015-3035
  - CVE-2015-1187
  - CVE-2014-6287
  - CVE-2014-0130
  - CVE-2013-4810
  - CVE-2013-2729
  - CVE-2013-2465
  - CVE-2013-0632
  - CVE-2012-1823
  - CVE-2010-4345
  - CVE-2010-4344
  - CVE-2009-1151
  - CVE-2005-2773
- **Application Database:**
  - Apple Safe Browsing (New)
  - Craigslist, Inc. (Enhancement)
