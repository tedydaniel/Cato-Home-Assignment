---
title: "Understanding Cato's Managed Socket Upgrade Service"
slug: "understanding-cato-s-managed-socket-upgrade-service"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/understanding-cato-s-managed-socket-upgrade-service"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Cato's Managed Socket Upgrade Service

This article explains the gradual upgrade service for Socket sites.

## Overview of Socket Upgrades

Cato manages the Socket firmware upgrades and version control for Socket sites to make sure that they are running up-to-date versions.

The Socket upgrade service is an automated process that provides all of our customers with the latest firmware. So there's no need for our customers to worry about installing and updating the new versions. The upgrade service ensures minimal impact on the Socket site (if any), and automatic rollback in the rare case that an issue is detected. The newest Socket versions include performance, connectivity, and stability enhancements, and also the latest capabilities and features.

There are situations where the Socket skips an upgrade for a version, for example, because the Socket was not connected to the Cato Cloud during the maintenance window, or there was unstable connectivity. When this happens, you can [manually upgrade](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#manually-upgrade-a-socket) the Socket, however, each Socket that was skipped must be upgraded individually.

**Note:**​​ To minimize operational risk and avoid disruption, Cato pauses automatic Socket upgrades during end-of-quarter periods and major holiday seasons, such as Christmas.

Cato releases three - four major Socket versions each year, and minor upgrades as required. Major versions are whole number increments, such as 17.0 and 18.0, while minor versions are decimal increments, such as 18.3.3 and 18.4.1.

Content for new Socket versions includes:

- Major Socket versions - new features, infrastructure for future features, enhancements, and bug fixes
- Minor Socket versions - bug fixes

### High-Level Overview of Socket Managed Upgrade Service

Cato follows standard industry best practices for cloud-based services and gradually rolls out new Socket versions to customers over several weeks. If an issue is detected, sometimes the rollout is paused until the issue is resolved and a new minor version is released. This pause can introduce an additional delay for some customers to automatically receive the update.

48 hours before Cato is ready to release a new Socket version to an account, an [email notification](/v1/docs/account-level-alerts-and-system-notifications) is sent to the **Socket Upgrade** mailing list, indicating that the Socket sites will be upgraded during the next [Maintenance Window](/v1/docs/configuring-the-socket-upgrade-maintenance-window) configured for the account. The actual time of the upgrade is based on the local time zone where the site is located. Cato also announces the content of the version in the [Socket Release Notes](/v1/docs/socket-release-notes), which is shown in the notification area of the Cato Management Application.

This is a summary of the Socket managed upgrade service process:

1. Cato releases the new Socket version, then the Sockets download the relevant files.
  1. The Socket compares the file hash to validate the file integrity for the new version
  2. If the Socket wasn’t able to download the new version file, during the Maintenance Window it tries again to download the file.
2. The upgrade services start to gradually upgrade Sockets for sites in the Maintenance Window time zone to the new version (see below [Gradually Upgrading Sockets in an Account](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#gradually-upgrading-sockets-in-an-account))
  1. Five Sockets from five different sites are selected for the initial upgrade group.

For Socket HA sites, only the primary Socket is included in the initial upgrade group.
  2. The upgrade service gradually upgrades the initial Sockets one by one, and verifies that each Socket upgrade succeeds and that the service is stable.

If a connectivity or stability issue is detected, the Sockets automatically rolls back to the previous version, and the upgrade process stops for the other sites in the time zone.
  3. After the initial five Sockets successfully upgrade to the new version, the upgrade service continues with the other Sockets in the time zone.
3. Each Socket site upgrades the Sockets as follows (see below [Upgrading a Socket Site to the New Version](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#upgrading-a-socket-site-to-the-new-version)):
  1. The Socket downloads the new version from the upgrade service's secure storage.
  2. The Socket installs the new version and monitors connectivity KPIs to verify that the new version runs correctly on the image.

After the verification completes, a Socket Upgrade event is generated, and an email notification is sent.
  3. In the rare case that there is an issue, the Socket rolls back to the previous version.

## Downloading New Socket Versions

Starting with Socket v18.0, when Cato releases a new Socket version to customers, the Sockets attempt to download the new file regardless of the Maintenance Window. This helps minimize potential upgrade issues during the Maintenance Window, which may result from low bandwidth or network disconnections.

**Note:** For Socket versions lower than v18.0, both downloading the image and upgrading the Socket take place during the Maintenance Window.

## Gradually Upgrading Sockets in an Account

Cato's Socket upgrade service gradually upgrades Sockets to the new version for all sites based on the specific local time zone for the Maintenance Window configured for your account. For example, an account that set the Maintenance Window for 1:00 - 3:00 am on Sundays, all Socket sites that are configured for the US Eastern time zone are upgraded during 1:00 - 3:00 am EST on Sundays.

The goal of a gradual upgrade is to minimize the service impact risk for a single site or for a group of sites, and if there is a significant issue with the new Socket version that impacts connectivity to the Cato Cloud, the upgrade stops automatically. Sockets that can't complete the upgrade automatically roll back to the previous version. For more about Sockets that don't upgrade to the new version, see below [Working with Unsuccessful Socket Upgrades](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#working-with-unsuccessful-socket-upgrades).

For the sites in each Maintenance Window time zone, the gradual upgrade process starts with the upgrade service selecting five Sockets and upgrading them in a Socket by Socket manner. A preference is given to Socket HA sites in each time zone, and only the primary Sockets are included in the initial five Sockets.

**Note:** In case a critical issue is detected that is related to the Socket software upgrade process, the upgrades for all Sockets in the account are skipped (not just for the sites in the Maintenance Window time zone).

If the Socket software upgrade succeeds, then the Cato Management Application continues to upgrade the remaining Sockets in the same time zone for the Maintenance Window. Then the Cato Management Application continues to upgrade the secondary Sockets for HA sites. For more about Socket upgrade and HA sites, see below [Socket HA Upgrade Process](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#socket-ha-upgrade-process).

![gradual_Socket_upgrade.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248028202909.png)

Each Socket takes 17 minutes to complete the upgrade process, during this time period, the Socket downloads the image, verifies and installs the image, performs a fast switch to the new image, and verifies service stability. The actual potential impact on the service is only during the fast switch to the new image, which takes at most a few seconds.

This is a summary of Cato's gradual upgrade for multiple Socket sites in the same time zone:

1. Sockets download new Socket version files once they are released.
2. For each local time zone, based on the Maintenance Window, there are five Socket sites that are selected to initially upgrade to the new version. For example, five different sites in the Eastern time zone for the United States.
3. Each site starts the upgrade process at five minute intervals:
  1. Socket 1 at 0 minutes, Socket 2 waits for 5 minutes, Socket 3 waits for 10 minutes, Socket 4 waits for 15 minutes, and Socket 5 waits for 20 minutes.
  2. From the time that Socket 1 starts the upgrade, it takes Socket 5 37 minutes to complete the upgrade (20 minutes waiting to start the upgrade + 17 minutes for the upgrade process).
  3. If one of the initial five Sockets needs to retry the upgrade process (for example, can't validate the downloaded new image), then the upgrade service for the remaining Sockets starts after 54 minutes.

For more about retrying to upgrade, see below [Socket Upgrade Automatic Retry](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#socket-upgrade-automatic-retry).
4. When the five initial upgrade sites successfully complete the upgrade process, then the other Sockets in the time zone are upgraded to the new Socket version.

## Upgrading a Socket Site to the New Version

This section explains the process to upgrade a single Socket to the new version and verify that it is stable.

![Single_Socket_Upgrade.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248052771997.png)

1. The Socket downloads and installs the new version as follows:
  1. The upgrade service sends an upgrade Socket command to the PoP that the Socket site is connected to. The PoP forwards this command to the Socket.
  2. The Socket downloads the image for the new Socket version from the server for the Cato Management Application, confirms that file hash is correct for the new Socket version.
2. The Socket installs the new image.
3. The Socket switches to the new image.

This process can take a few seconds and during this time there may be an impact to the Cato service for the site.
4. The Socket monitors the stability and connectivity health KPIs for a duration of 10 minutes.
5. 17 minutes after the Socket upgrade process started, the Socket confirms that the new image is stable, and the Cato Management Application server confirms that the Socket successfully upgraded to the new version.
  1. A successful Socket upgrade email notification is sent to the **Socket Upgrade** mailing list, and a notification is shown in the Cato Management Application stating that the Sockets for the site successfully upgraded to the new version.
  2. If the Socket detects a connectivity issue or a health issue related to the new version, it automatically rolls back to the previous version. An email notification is sent to the **Socket Upgrade** mailing list that the Socket did not upgrade to the new version.

### Socket HA Upgrade Process

This section describes the Socket upgrade for sites with a Socket HA configuration. The upgrade process starts with the primary Socket, and only after it is successfully upgraded does the process continue with the secondary Socket.

The entire upgrade process for both Sockets is completed within the duration of the maintenance window.

1. First the primary Socket upgrades to the new version, and confirms that the new version is stable.
2. Then the secondary Socket upgrades to the new version, and confirms that the new version is stable.

The Cato Management Application starts the upgrade process for the secondary Socket only after the primary Socket's upgrade completed successfully and confirmed that the version is stable. In the unlikely scenario there critical issue that impact the primary Socket, then the secondary Socket becomes the active Socket and continues the service for the site.

> [!NOTE]
> Notes:
> 
> - There are rare scenarios where the primary Socket encounters an issue during the upgrade, and then the secondary Socket becomes the active Socket for the site. In these scenarios, the secondary Socket does NOT upgrade to the new version.
>   - If the primary Socket successfully upgrades to the new version, and the secondary Socket can't upgrade to the new version, then the primary Socket remains on the new version. This can mean that the primary and secondary Sockets are running different major versions (see below).
> - If the primary and secondary Sockets are running different major versions, then the HA status for the site is **Not Ready**. For more information, see [What is Socket High Availability (HA)](/v1/docs/what-is-socket-ha).
>   - Socket HA failover takes place even if the Sockets are running different major versions. However, the site might experience functionality issues if the secondary Socket version does not support features that are supported for the primary Socket version.
> 
> For example, if the primary Socket runs version 18.0 and the secondary Socket is running version 15.0, In the case of a failover, features that were released with versions 16 - 18 will not work while the secondary Socket is active.

### Socket Upgrade Automatic Retry

Each Socket upgrade is limited to a duration of 17 minutes. If the Socket can't complete the upgrade and verify that the new version is stable during the time period, then the upgrade service automatically attempts to retry the upgrade as follows. For more information about skipped upgrades, see below [Working with Unsuccessful Socket Upgrades](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#working-with-unsuccessful-socket-upgrades).

When a Socket skips upgrading to a version, a **Socket Upgrade** event is generated with the action **Skipped** and an email notification is sent. For more about Socket Upgrade events, see below [Understanding Events for the Socket Upgrade Status](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#understanding-events-for-the-socket-upgrade-status).

- If the Socket is connected to the Cato Cloud, then the upgrade service tries a second time to upgrade to the new version

If the Socket is unable to upgrade after the second time, then the upgrade service skips this version for the Socket, and will attempt to upgrade to the next version that is released.

For example, the Socket can’t upgrade to v14.2, and attempts to upgrade when v14.3 is released.
- If the Socket isn’t connected to the Cato Cloud, then the upgrade service skips this version for the Socket, and will attempt to upgrade to the next version that is released
- If the Maintenance Window has ended for the site, then the Cato Management Application upgrade service skips this version for the Socket

## Manually Upgrade a Socket

If your Socket was not upgraded as part of the usual maintenance process, you can initiate a manual upgrade. Cato recommends that you keep your Sockets up-to-date and upgrade to the latest Socket version.

You initiate the manual upgrade from the Cato Management Application. For more information, see [Manually Upgrading a Socket](/v1/docs/manually-upgrading-a-socket)

## Pausing Automatic Upgrades for Specific Sockets

You might have certain Sockets that you do not want to automatically upgrade - for example, critical infrastructure or high-volume servers.

> [!NOTE]
> Note:
> 
> Cato recommends that you keep your Sockets up-to-date and upgrade to the latest Socket version.

### Use Case

As a commercial retailer, you have many stores that are connected to the Cato Cloud through different kinds of Sockets. Around the holiday season, you have a high volume of traffic in your stores and your online site and therefore do not want to upgrade the Sockets at this time.

During the holiday season, you can pause the automatic upgrades and resume them when you return to your normal volume.

### Pause and Resume Automatic Upgrades

**To pause automatic upgrades for a specific Socket site:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click **Actions** and select **Pause Automatic Upgrades**.

**To resume automatic upgrades for a specific Socket site:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click **Actions** and select **Unpause Automatic Upgrades**.

## Rescheduling Automatic Upgrades

As part of the Managed Socket Upgrade service, Cato performs the upgrades [gradually](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#gradually-upgrading-sockets-in-an-account). If there is a problem with a specific site, for example, a flapping internet link, the upgrade will fail and all of the sites in your account will not be upgraded.

Starting with Socket v21.1, you can now [pause](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#pausing-automatic-upgrades-for-specific-sockets) the upgrade for the Socket that is experiencing issues, and reschedule the maintenance window for the rest of the sites in your account.

**To reschedule the automatic upgrade maintenance window:**

1. From the navigation menu, select **Resources > System Settings**, and click **Maintenance Window**.
2. Under **Reschedule Maintenance Window**, click **Reschedule**.

The maintenance window is rescheduled to the time defined in the **Socket Maintenance Window** section. You must configure the reschedule at least 48 hours in advance of the upcoming window.

## Understanding Events for the Socket Upgrade Status

When the upgrade process is completed for a Socket, an event with the sub-type **Socket Upgrade** is generated with one of the actions below. For each action, an email notification is sent to the mailing list, and a notification is shown in the Cato Management Application.

| Action | Description |
| --- | --- |
| Succeeded | The Socket successfully upgraded to the new version. |
| Skipped | The upgrade service wasn't able to start the upgrade process for this Socket. For example, the Socket wasn't connected to the network during the Maintenance Window. |
| Failed | The Socket wasn't able to upgrade to the new version, for the first time and for the retry. For example, the Socket wasn't able to verify the file hash of the image. |

## Working with Unsuccessful Socket Upgrades

If a Socket is unable to upgrade to the newest version, these are the recommended next steps:

- Common reasons for an unsuccessful version file download include:
  - Low bandwidth links (less than 1Mbps)
  - LTE links with poor signal strength
- Skipped upgrade - Make sure that the Socket is connected to the Cato Cloud and operating correctly, if yes - then the Socket will upgrade when the next version is released

For more information about preparing a Socket for upgrades, see [Connectivity Requirements for Socket Upgrades](/v1/docs/connectivity-requirements-for-socket-upgrades)
- Failed upgrade - Trigger a [manual upgrade](/v1/docs/manually-upgrading-a-socket) from the Cato Management Application
