---
title: "SDP Client Silently Upgraded Even Though Policy was Changed to Managed Upgrade"
slug: "sdp-client-silently-upgraded-even-though-policy-was-changed-to-managed-upgrade"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/sdp-client-silently-upgraded-even-though-policy-was-changed-to-managed-upgrade"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SDP Client Silently Upgraded Even Though Policy was Changed to Managed Upgrade

## Question

Why were SDP clients silent upgraded even though the upgrade policy was changed to Managed Upgrade?

## Answer

The reason could be due to the SDP client hasn't connected in a while and is still holding on to the old upgrade policy which it downloaded from the CMA before the upgrade policy was changed. For e.g., when the old upgrade policy was set to 'Automatic Silent Upgrade', and the administrator recently changed the upgrade policy to 'Managed Upgrade', if the SDP client didn't connect after the policy was changed, it will still be configured with the old policy of 'Automatic Silent Upgrade'. When the new version is available, the SDP client will be upgraded automatically (even though it remains disconnected).

To confirm if this is the case, we can check on the following registry key.

`Computer\HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\LastUser\UpgradeMode`

0 - Managed Upgrade

1 - Automatic Silent Upgrade

2 - User Upgrade

## Workarounds

1. Get the users to connect their SDP Client to retrieve the latest upgrade policy
2. In the event that step 1 is not feasible, for e.g. there are a lot of disconnected users, then make use of GPO to change the registry value to match the latest upgrade policy
