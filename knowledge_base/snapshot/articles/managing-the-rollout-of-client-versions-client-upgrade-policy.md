---
title: "Managing the Rollout of Client Versions (Client Upgrade Policy)"
slug: "managing-the-rollout-of-client-versions-client-upgrade-policy"
updated: 2026-08-31T13:57:20Z
published: 2026-08-31T13:57:20Z
canonical: "knowledge.catonetworks.com/managing-the-rollout-of-client-versions-client-upgrade-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing the Rollout of Client Versions (Client Upgrade Policy)

Cato regularly releases new Cato Client versions that support new features and also connectivity or performance enhancements. This article explains how to manage upgrading Clients to the newest version with the Client Rollout page in the Cato Management Application (CMA).

## Overview

When Cato releases a new Windows, macOS, or Linux Client version, you can manage how the version is rolled out to users in your organization. For each OS, you can define the Client upgrade policy to either use the Cato Upgrade service to automatically manage the rollout or update Clients with an MDM or manually.

The Cato upgrade service provides additional control and visibility of a version rollout within your account. You can choose the user experience to determine if a notification is displayed. For additional testing, you can define which users are the first to receive the newest version. For example, you can choose to begin the rollout of a new version with the IT team to run further tests. If you would like to receive the latest Client version sooner, open a Support ticket. For more information, see [Best Practices for Cato Client Upgrades](/v1/docs/recommendations-for-cato-client-upgrades).

Once the rollout has begun, you can monitor the progress and, if necessary, pause and resume the rollout at any time. After a rollout is paused, the Cato Upgrade service doesn't upgrade any additional Clients to the new version until the rollout is resumed or another Client version is released.

## Understanding the Cato Client Upgrade Policy

The Client receives the upgrade policy settings when it is connected to the Cato Cloud. This means that the first time that you install the Client on a device, it only receives the upgrade settings after it connects to the Cato Cloud.

Choose one of the following policies for updates to the Clients:

- **Automatic by Cato** - The Cato upgrade service deploys the new Client version to users. When a new Client version is available, it is gradually rolled out to users in your account. Cato continually monitors the new versions to quickly identify any issues. The **Mode** defines the user experience:
  - **Silent Mode** - The end user can’t control the Client installation, and it is automatically upgraded to the newest version. When the Client is upgrading, if the Client is connected to the Cato cloud, a notification is shown to the end user. This explains that during the upgrade, the Client disconnects from the Cato Cloud and then reconnects after the upgrade is complete.
    - For macOS Clients, the OS opens a window and requires the end user to authenticate to the computer to install the new Client version
  - **User Managed Mode** - When a new Client update is available, the end user receives a notification. They can choose to install the new Client immediately or at a later time. A reminder notification is shown every 12 hours.
- **Managed by Admin** - Cato does not automatically upgrade the Client and Administrators can decide how Client upgrades are managed. You could use MDM software or manually install the Client on a device. The end users don't receive any notifications from Cato.

> [!NOTE]
> Notes:
> 
> - Users do not need admin permissions on the computer to upgrade the Windows Client
> - For Windows Clients, the Automatic Silent Upgrade and Managed Upgrade options, the Client requires access to the %TEMP% directory for the local user
> - A restrictive GPO policy may block the installation of the Cato Adapter during the installation or upgrade process of the Cato Client. To ensure the Client upgrades successfully, configure the GPO policy to permit the installation of the Cato Adapter.

## Configuring the Cato Client Upgrade Policy

Select the upgrade option for each operating system used in your account.

**To configure the Cato Client upgrade policy:**

1. From the navigation menu, click **Access > Client Rollout**.
2. Click the **Upgrade Policy** tab.
3. Choose the **Client Upgrade Policy** for each operating system.
4. If you selected an **Automatic by Cato** upgrade policy, choose the **Mode**.
5. Click **Save**.

### Defining the Pilot Group for Upgrades Managed by Cato

With the **Automatic by Cato** upgrade policy, you can choose to begin the rollout of a new version with the **Pilot Group**. These are the first users who automatically receive the new Client before it is rolled out to the rest of your account. This lets you evaluate new features with a controlled group of users.

> [!NOTE]
> Note:
> 
> The Pilot Group is available only for the Cato Client.

After 1-2 weeks, the upgrade rollout continues with other users, or you can pause the rollout. A notification is shown in the Cato Management Application when the rollout starts for the **Pilot Group**. For more information about the stages of the Client rollout, see [Understanding who the Newest Version is Available to](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy#h_01JPJ9TNQ5EDWWAZHR4M1A7VTC).

> [!NOTE]
> Note:
> 
> The length of time the rollout stays with the Pilot Group is an estimate and maybe impacted by the GA deployment lifecycle. Gradual Rollout stage may start even if not all users in the Pilot Group have received the update.

![Upgrade_Test_Users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25828704101021(1).png)

**To define the Pilot Group for Automatic by Cato Upgrades:**

1. From the navigation menu, click **Access > Client Rollout**.
2. In the **Upgrade Policy** tab, make sure that **Automatic by Cato** is selected.
3. Click the **Pilot Group** tab.
4. Select the users to add to the **Pilot Group**
5. Click **Save**.

The selected users are added to the **Pilot Group**.

## Overview of the Rollout Status Screen

![2023-04-18_18-10-23.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25828680283677(1).png)

Each operating system used in your account has a widget for the newest Client version and a progress bar that shows how far the rollout has progressed.

The progress bar shows the progress of the new Client rollout. To view data on the users that have the newest Client version installed on their device, click the **More Info** dropdown and select **View upgraded users**. This opens the **Users** screen with predefined filters. For more information on the User Dashboard, see [Using the Access Overview Page](/v1/docs/using-the-access-overview-page).

### Use Case

To provide maximum security for users, Company ABC manages its Client upgrades with Automatic Silent Upgrades. On May 10, a new Windows Client is available. On the same day, the IT department plans a major system upgrade. To reduce the risk of multiple upgrades on the same day, the rollout of the new Windows Client is paused. No users will receive the new Windows Client on May 10.

After the system upgrade is successfully deployed, the IT department downloads the new Windows Client for testing. The Client passes all tests and the rollout of the new Client is resumed. The IT department is able to monitor the progress of the rollout from the Pilot Group to all users to ensure the Client upgrade is successful.

### Prerequisites

- To download the newest Client version for testing, allowlist the following URL for all security endpoint software and solutions, go to the [Client Download portal](https://clientdownload.catonetworks.com/)

### Testing the Newest Client Version

You can download the newest Client version for testing from the Cato Management Application. The following file formats are available:

| Client Type | Supported File Formats |
| --- | --- |
| Windows | exe, msi |
| macOS | pkg |
| Linux | rpm, deb |

**To test the newest Client version:**

1. From the navigation menu, click **Access > Client Rollout**.
2. Click the **Rollout Status** tab.
3. From **Download Client**, choose the file type you want to download.

The newest Client is downloaded to your device.

### Monitoring the Progress of the Rollout

You can view which users the newest Client version has been made available to and view which users have the newest version installed. Once a new version is made available to a user, the version is only installed once the device is turned on and connected to the Internet.

#### Understanding Who the Newest Version is Available to

For automatic upgrades, once the rollout of a new Client version begins, you can monitor who the new version has been made available to. From the **Access > Client Rollout** page, on the **Rollout Status** tab, you can who the newest version is available to:

- **Available to Pilot Group:** The newest version is only available to your Pilot Group
- **Gradual Rollout:** Rollout to users outside of the Pilot Group has begun
- **Available to all Users:** Gradual Rollout is complete, and the new version is available to all users. Users without a ZTNA license need to be connected behind a site to receive the upgrade

The newest Client version is uploaded to the [Client Download portal](https://clientdownload.catonetworks.com/) when the majority of customers are using that version.

#### Viewing Users who Installed the Newest Version

You can add predefined filters to the **Remote User Dashboard** to view the users who have the newest Client version installed on their device.

**To view users who installed the newest version:**

1. From the navigation menu, click **Access > Client Rollout**.
2. Click the **Rollout Status** tab.
3. From the **More Info** dropdown, select **View upgraded users**.

The **Users** screen is displayed with a predefined filter for the newest Client version.

### Pausing the Rollout of the Newest Client Version

For **Automatic by Cato** upgrades, you can pause the automatic rollout of the newest Client version.

In rare cases where Cato identifies an issue with a Client version during rollout, Cato may pause the rollout. When a Client rollout is paused by Cato, a notification banner appears on the Client Rollout page. When Cato pauses the rollout, no action is required by you, and Cato removes the banner when the rollout resumes. Sometimes, this may be a newer Client version.

**To pause the rollout:**

1. From the navigation menu, click **Access > Client Rollout**.
2. Click the **Rollout Status** tab.
3. Click **Pause Rollout**.

The rollout is paused until you click **Resume Rollout** or a new Client version is released. When you resume a paused rollout, it’s possible that the new version will be rolled out to many users at the same time. For example, you paused the rollout on Oct 10 when the new version was installed for 10% of the users. When you resume the rollout on Oct 25, 80% of the remaining users will be upgraded on that same day.

## Checking for a New Version

After the Client connects to the Cato Cloud for the first time, these are the conditions for the Client to check for a new version:

- Windows Clients
  - The device is powered on and connected to the Internet
- macOS Clients
  - The user is logged in to the computer
  - The Client app is open and running, but it isn't required to be connected to the Cato Cloud
- Linux Clients
  - The device is powered on and connected to the Internet

If an automatic upgrade fails, the Windows Client does not attempt to upgrade again to the same version. A new version must be released before the Client attempts to upgrade. The macOS Client re-attempts to install the new version.

Clients only attempt to upgrade to the latest version. If a Client is several versions behind, it does not upgrade to a previous version that was completely rolled out to the account.

## Sample Upgrade Workflows for Users

This section shows sample workflows of the user experience for each of the upgrade options.

### Sample Automatic by Cato - Silent Mode Workflow

1. A new version of the Cato Client is released.
2. The user logs in to the computer and opens the Cato Client.
3. The Cato Client automatically downloads the new version and then installs the new version.

The user is disconnected from the secure tunnel during the upgrade.

For Windows, the installation file is downloaded to the `%TEMP%` directory.
4. When the installation is completed, the Client behavior is:
  - For Windows - when the client completes the upgrade, the Client opens and the user needs to manually connect. If Always-on is enabled, the Client reconnects
  - For macOS - the Client automatically restarts, and if the Client was connected to the secure tunnel before the upgrade process, it then reconnects

### Sample Automatic by Cato - User Managed Mode Workflow

- A new version of the Cato Client is released
- The user logs in to the computer and opens the Cato Client.
- The user sees a notification in the Cato Client that there is a new version.
- The user can choose to download and install the new version or continue using the older version.
- If the user doesn't install the new version, the Cato Client periodically shows reminders to the user that a new version is available.

Users can also choose to upgrade at any time and click **Upgrade Now** in the appropriate section of the Client:
  - Windows - **Support** tab
  - macOS - **About** tab

### Sample Managed by Admin Upgrade Workflow

1. A new version of the Cato Client is released.
2. The admin chooses when to use the MDM to push the new Cato Client version to the users.
3. The user logs in to the computer and opens the Cato Client.
4. The new version is installed, and the Client behavior is:
  - For Windows - the end user can start the updated Cato Client
  - For macOS - the Client automatically restarts, and if the Client was connected to the secure tunnel before the upgrade process, it then reconnects
