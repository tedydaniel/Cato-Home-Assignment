---
title: "Configuring Access Control with MAC Address Authentication"
slug: "configuring-access-control-with-mac-address-authentication"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-access-control-with-mac-address-authentication"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Access Control with MAC Address Authentication

This article describes how to manage network access based on the MAC address of hosts and devices.

## Overview of MAC Address Authentication

You can enable sites with Cato Sockets to provide network access only to hosts and devices based on their MAC addresses. Enter each MAC address in a CSV file that is uploaded to the Cato Authentication Server in the Cato Cloud. The sites only authenticate the devices with MAC addresses that are in this file. All other devices are rejected from connecting to the network. For example, guest users are only allowed access if they are added to the CSV file.

### Using the CSV File

- When you upload a CSV file to the Cato Authentication Server, a log is generated for the [Audit Trail page](/v1/docs/using-the-audit-trail)
- Uploading a new CSV file replaces and overwrites the previous file
- The maximum size for the CSV file is 1 MB
- The maximum number of MAC addresses that are cached in a site is 32,000

## Implementing MAC Address Authentication

You can choose to enable MAC address authentication as a Global Setting for all Socket sites in the account, or only for specific sites.

### Configuring the Global Settings for MAC Address Authentication

This section is a high-level overview that describes how to implement MAC Address Authentication as global setting for all Socket sites in the account.

1. Upload the CSV file with the MAC addresses to the Cato Authentication Server.
2. Configure the authentication time settings.
3. For each site that is NOT performing MAC address authentication, override the global settings for that site and disable the feature.
4. Enable the MAC address authentication global setting for the account.

### Configuring Specific Sites for MAC Address Authentication

This section is a high-level overview of only implementing MAC Address Authentication for specific Socket sites.

1. Upload the CSV file with the MAC addresses to the Cato Authentication Server. This list of MAC addresses is applied to the sites, you can't customize a different list of MAC addresses for each site.
2. Configure the authentication time settings.
3. For each site that is performing MAC address authentication, override the global settings for that site and enable the feature.

Even though the global setting for MAC address authentication is disabled, the CSV file and the authentication time settings are still applied to the enabled sites.

## Configuring MAC Address Authentication for the Account

You can use the **MAC Address Authentication** window to:

- Configure the network access for the entire account based on the MAC addresses
- Manage the time settings for how long each MAC address is authenticated or rejected
- Upload the CSV file that contains the list of MAC addresses that are allowed to connect to the network

> [!NOTE]
> Note:
> 
> If you enable MAC address authentication before you upload the CSV file, then all connections are blocked.

![macauthentication.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33911524304413.jpeg)

**To enable or disable authentication with the MAC address for the entire account:**

1. From the navigation menu, click **Access > MAC Authentication**.
2. Select **Enable MAC authentication control**.

To disable MAC authentication, clear this option.
3. Configure the MAC approval and MAC rejection validation lengths
4. Click **Save**.

### Defining MAC Addresses that are Authenticated

Use the Cato Management Application to upload a CSV file to the Cato Authentication Server that contains all the MAC addresses that are authenticated to access the network. The Socket then pulls this file and compares each connection to the MAC addresses in the CSV file. If the MAC address is listed in the file, then the connection is allowed. Otherwise, the connection is rejected. To update the authenticated MAC addresses, upload a new CSV file to the Cato Authentication Server.

When the **MAC Authentication** window for the Global Settings shows the **No file uploaded** message, then no MAC addresses are allowed. The sites block all network traffic, including Cato Cloud WAN and Internet traffic. We recommend that you upload the CSV file before you enable the MAC address authentication feature.

Each account uses one CSV file for the authenticated MAC addresses for all the sites with Sockets. You can choose to enable or disable individual sites (see below [Disabling a Specific Site from MAC Address Authentication](/v1/docs/configuring-access-control-with-mac-address-authentication#disabling-a-specific-site-from-mac-address-authentication)). The MAC addresses in the CSV file must be in the correct format to upload the file, for example: 00:0a:95:9d:68:16.

The CSV file contains these columns:

- Allowed MAC Address
- Username (optional)
- Comment (optional)

**To define MAC addresses that are allowed to connect to the network:**

1. Prepare the CSV file with the MAC addresses. You can also add usernames and comments.
2. From the navigation menu, click **Access > MAC Authentication**.
3. Select **Enable MAC authentication control**.
4. Click **Upload CSV File**.
5. From the browser pop-up window, select the CSV file. The file is uploaded to the Cato Authentication Server.
6. Click **Save**.

### Downloading the CSV File

The **MAC Address Authentication** window shows the status of the CSV file that is uploaded. It shows the number of MAC addresses in the file and the time stamp of when the file was uploaded.

If the window shows the **No file uploaded** message, then you can download a CSV file that is an empty template for the MAC addresses and other data.

**To download the CSV file from the Cato Management Application:**

1. From the navigation menu, click **Access > MAC Authentication**.
2. Select **Enable MAC authentication control**.
3. Click **Download CSV File**.
4. From the browser pop-up window, select the directory to save the CSV file. The file is downloaded to the directory.

### Defining the Authentication Time Settings

Define the authentication behavior for how long the Cato Authentication Server waits before checking if the specific MAC address is in the CSV file. The **MAC approval is valid for** setting defines the amount of time that the MAC authentication is valid for. For example, if the value of this setting is 12 hours, then a device that was authenticated at 8:00 am is valid until 8:00 pm. After 8:00 pm, when the device tries to connect to the network, the site checks if the specific MAC address is in the CSV file in the Cato Authentication Server.

The **MAC rejection is valid for** setting defines the amount of time that a rejected device waits before trying to authenticate. During this time, the rejection of the MAC address is enforced and the site doesn't compare the device MAC address with the CSV file in the Cato Authentication Server. Afterwards, when the device tries to connect to the network, the Cato Authentication Server compares the specific MAC address with the CSV file. The minimum time value for **MAC rejection is valid for** is **1 hour**.

**To define the MAC approval and rejection settings:**

1. From the navigation menu, click **Access > MAC Authentication**.
2. Select **Enable MAC authentication control**.
3. Set the time amount and value for how long the **MAC approval is valid for**.
4. Set the time amount and value for how long the **MAC rejection is valid for**.
5. Click **Save**.

### Disabling a Specific Site from MAC Address Authentication

You can choose to override the global MAC address authentication settings and disable this feature for specific sites.

**To disable MAC address authentication for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > MAC Authentication**.
3. Select **Override account authentication control**.
4. Make sure that **Enable MAC authentication control** is cleared.

![overrideMAC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33911543614493.png)
5. Click **Save**.

## Enabling MAC Address Authentication for Specific Sites

You can choose to only enable MAC address authentication for specific Socket sites, however, the same list of MAC addresses is applied to all the sites.

Upload the CSV file to the Cato Authentication Server to define the MAC addresses that are allowed to connect for all the sites. Configure the authentication time settings for the entire account. Then, for each site, override the MAC authentication settings for the account and enable MAC address authentication.

![overrideMAC2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33911513765661.png)

> [!NOTE]
> Note:
> 
> In this configuration, you don't enable MAC address authentication for the account, instead only enable the feature for the specific sites.

**To enable MAC address authentication for a site:**

1. From the navigation menu, click **Access > MAC Authentication**.
2. Select **Enable MAC authentication control**.
3. Click **Upload CSV File** to upload the Cato Authentication Server, and define the MAC addresses that are authenticated to the network (see above [Defining MAC Addresses that are Authenticated](/v1/docs/configuring-access-control-with-mac-address-authentication#defining-mac-addresses-that-are-authenticated)).
4. Define the authentication time settings for the account (see above [Defining the Authentication Time Settings](/v1/docs/configuring-access-control-with-mac-address-authentication#defining-the-authentication-time-settings)) and click **Save**.
5. From the navigation menu, click **Network > Sites** and select the site.
6. From the navigation menu, click **Site Configuration > MAC Authentication**.
7. Select **Override account authentication control**.
8. Select **Enable MAC authentication control**.
9. Click **Save**.
