---
title: "Recommendations for Cato Client Upgrades"
slug: "recommendations-for-cato-client-upgrades"
tags: ["Access", "Best Practices", "Clients"]
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/recommendations-for-cato-client-upgrades"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recommendations for Cato Client Upgrades

This article discusses recommendations and best practices for managing Client upgrades for devices in your account.

We recommend that you use the Cato upgrade service to automatically upgrade Clients to the newest version. You can also choose to manually upgrade Clients using an MDM or similar solution.

## What Does it Mean When Cato Announces the Release of a New Version?

Cato announces that a new Client version will soon be released in the Product Update's [Release Notes](https://support.catonetworks.com/hc/en-us/sections/360000462277). Cato follows industry best practices and gradually rolls out a new Client version to customers.

- When the new version is available for your account, an announcement is shown in the Notifications area of the Cato Management Application

![Notification.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218297826717.png)
- When the Client rollout starts for your account, the new Client version is available to download from the Client Rollout page (**Access > Client Rollout**)
- 2 - 4 weeks after the new version is announced in the Release Notes, the Cato upgrade service starts the gradual roll-out (see below). If you would like to receive the latest Client version sooner, open a [Support](https://support.catonetworks.com/hc/en-us/requests/new) ticket.

### What Can I do to Prepare for the New Version

When an upcoming release is announced, here are steps that you can take to prepare:

1. Make sure that your account is using Cato's best practices for upgrading Clients:
  1. To ensure your SDP Clients are running the latest version, set the Client [Upgrade Policy](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy) to **Automatic Silent Upgrade**.

This policy uses the Cato upgrade service to automatically and seamlessly push new Client versions to devices.
  2. To evaluate a new version with specific users before it is rolled out across your account, define the **First Upgraded Users**.

The **First Upgraded Users** receive the latest Client version before the rest of the users in your account. This lets you evaluate the new version on a subset of users, before it is rolled out across your account.
2. Monitor the **First Upgraded Users** for any potential issues. You can identify which users have the last version of the Client from the SDP Users Dashboard. For more information, see [Using the Access Overview Page](/v1/docs/using-the-access-overview-page).

### Gradual Client Roll-out for the Cato Upgrade Service

For accounts that use the Cato upgrade service to upgrade Clients in their account, the Cato upgrade service manages the gradual roll-out to devices in the account. The goal of gradual roll-out is to provide the best end-user experience for remote devices. Cato continually monitors the new Client versions and can quickly stop deploying the new version, remediate any issues and then continue the roll-out with a new Client that includes the necessary fixes.

Cato has several roll-out phases which occur over the time period of a few weeks. SDP users are gradually upgraded to minimize any negative impacts of the Client upgrade.

## Related Resources

- [Managing the Rollout of Client Versions (Client Upgrade Policy)](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy) (also describes **First Upgraded Users**)
- [Client Lifecycle Management](/v1/docs/client-lifecycle-management)
