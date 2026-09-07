---
title: "Resolving Issues with LDAP Sync"
slug: "resolving-issues-with-ldap-sync"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/resolving-issues-with-ldap-sync"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Resolving Issues with LDAP Sync

For customers that use LDAP for User Provisioning with their Cato account, this article explains how the LDAP traffic goes over the Internet to the Cato Cloud.

## Overview

When the IdP is syncing over LDAP (such as AD), packets traverse securely from the Cato Cloud to the on-prem or cloud-based server.

The packets are encrypted and then sent from the Cato Management Application to a PoP in the Cato Cloud, and then via Cato's DTLS tunnel to the site where they are decapsulated by the Socket and sent over the LAN. No packet is ever sent over the Internet unencrypted or in an insecure state.

The source IP address of the Cato server for LDAP is a publicly routeable IP address, however only encrypted packets are sent over the Internet.

## Cato's IP Address for LDAP Sync

To identify the Source IP Address for the Cato Management Application, see [Using Cato IP Addresses](https://support.catonetworks.com/hc/en-us/articles/20511945810589) (You must be signed in to view this article)
