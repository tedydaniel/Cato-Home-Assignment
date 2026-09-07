---
title: "Client Lifecycle Management"
slug: "client-lifecycle-management"
updated: 2026-06-24T08:44:57Z
published: 2026-06-24T08:44:57Z
canonical: "knowledge.catonetworks.com/client-lifecycle-management"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Client Lifecycle Management

Cato regularly releases new Client versions that support new features and also connectivity or performance enhancements. There are different upgrade options that you can select for your account to best meet the requirements of your organization.

## Client Upgrade Options

The Client Upgrade Policy screen lets you defines how the Windows and macOS Clients for SDP users are upgraded to the new version. Admin permissions are not required to update the Client to a new version.

These are the upgrade options:

- Automatic Silent Upgrade - The Client upgrade process is managed by Cato's upgrade service and the device automatically downloads and installs the update. The new version is gradually rolled out to the Clients in your account (see below [Gradual Client Roll-out for the Cato Upgrade Service](/v1/docs/client-lifecycle-management#gradual-client-rollout-for-the-cato-upgrade-service)). When the Client is upgrading, a notification is shown to the user indicating that an upgrade is in process.

![Notification.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275609888285.png)
- User Upgrade - The SDP users are responsible for deciding when to upgrade to the new Client version on the device. When a new version is available, the Client automatically shows a notification to users. They can choose when to click **Update Now** in the Client to download and install the new version.
- Managed Upgrade - For organizations that used a third-party solution to manage installing and upgrading Clients, the admin decides when to push the new version to the devices.

For more information about the Client upgrade options, see [Managing the Rollout of Client Versions (Client Upgrade Policy)](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy).

## Gradual Client Roll-out for the Cato Upgrade Service

For accounts that use the Cato upgrade service to upgrade Clients in their account, the Cato upgrade service manages the gradual roll-out to devices in the account. The goal of gradual roll-out is to provide the best end-user experience for remote devices. Cato continually monitors the new Client versions and can quickly stop deploying the new version, remediate any issues and then continue the roll-out with a new Client that includes the necessary fixes.

Cato has several roll-out phases which occur over the time period of a few weeks. SDP users are gradually upgraded to minimize any negative impacts of the Client upgrade.

## End of Support Policy for Cato Clients

Cato supports multiple versions of the Client for each operating system (OS). At some point, new features and security updates for the newest Client may be incompatible with an older version and that version is declared as End of Support (EoS). When Cato announces that a Client version is EoS, we recommend that you upgrade those Clients in your organization to the newest version.

When a vendor announces that an operating system (OS) is declared EoL, for example Windows 7, Cato will announce when the hosts or devices that are still using that version are no longer supported for the Client.

For more about the EoL policy, see [End of Support (EoS) Policy for Cato Clients](/v1/docs/end-of-support-eos-policy-for-cato-clients).

For more about the minimum supported device OS and version, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).
