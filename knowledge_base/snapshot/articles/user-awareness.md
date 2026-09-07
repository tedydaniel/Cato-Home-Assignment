---
title: "Using Cato Identity Agents for User Awareness"
slug: "using-cato-identity-agents-for-user-awareness"
updated: 2026-08-17T13:50:52Z
published: 2026-08-17T13:50:52Z
canonical: "knowledge.catonetworks.com/using-cato-identity-agents-for-user-awareness"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Cato Identity Agents for User Awareness

## Overview

Knowing the user identity is a key component of Zero Trust Network Architecture (ZTNA) - it is essential to identify the user at any point in time, control user access, and monitor user activity. The Identity Agent for User Awareness identifies users behind a Socket, or in Office Mode. It uses the framework of the Cato Client to get the user information and regularly reports this identity to the PoP (about every 30 seconds). Any change in the IP address is immediately detected and reported.

The Client is installed on the device and runs in the background (without establishing a tunnel), and it provides the Cato Cloud with the user identity.

### Enhanced User Awareness with no ZTNA license

Starting with the following versions, Cato has expanded User Awareness without requiring a ZTNA license. Users can authenticate with the Cato Client while in the office, which creates a Cato token that is used to more accurately identify users for policies and user attribution in DEM and covers all IdPs.

- Cato Client for Windows v5.18 and later
- Cato Client for macOS v5.11 and later

### Prerequisites

The Client prerequisites and requirements for the Identity Agent are based on which IdP is configured for your account and which Client Version you are using.

#### Prerequisites for Enhanced User Awareness with no ZTNA license

|  | Windows Client v5.18 and higher | macOS v5.11 and higher | Linux Clients |
| --- | --- | --- | --- |
| Any supported IdP | Supported with one-time initial authentication | Supported with one-time initial authentication | Not supported |

#### Prerequisites for Linux and Older Windows and macOS Client Versions (Enhanced User Awareness not supported)

|  | Windows Client v5.10 to v5.17 | macOS Client v5.6 to v5.10 | Linux Client v5.2 and higher |
| --- | --- | --- | --- |
| Entra ID with LDAP Entra ID with SCIM Microsoft Intune | Supported | Supported* | Supported* |
| Other IdPs (e.g. Okta) and manually created users | Supported* | Supported* | Supported* |

* Requires a ZTNA license for each user and one-time initial authentication to the Client. For more information, see [Defining Remote Access for Users](/v1/docs/assigning-ztna-licenses-to-users)

## Overview of Implementing Cato's Identity Agent for User Awareness Solution

This is a high-level overview of the process to implement Identity Agent for User Awareness in your account:

1. On the **Access > Directory Services** screen, provision users to your account.
2. After provisioning the users and user groups is completed, create rules and policies that include them.
  1. Install the Client on the devices for the relevant users. Once the user logs in to the device, the Client starts reporting the identity to the Cato Cloud every 30 seconds.
3. For Linux Clients, assign ZTNA licenses to users and user groups. For more information on how to assign ZTNA licenses, see [Defining Remote Access for Users](/v1/docs/assigning-ztna-licenses-to-users).

> [!NOTE]
> **Note:** Cato account licenses use one of two models: **Enforcement** and [**Bursting**](https://knowledge.catonetworks.com/v1/docs/jan-2027-license-bursting-model). Step 3 applies to the Enforcement Model only and is not relevant to the [Bursting Model](/v1/docs/jan-2027-license-bursting-model). Not sure which license model your account uses? See [Identifying your License Model](/v1/docs/identifying-your-license-model).

### Enforcing Policies Based on User Identity

Users or user groups can be added to policies. After Cato has identified the identity of a user, any polices that are configured for the user are enforced both behind a site and remotely.

**Note:** When using Identity Agent, users behind a site are not matched in WAN rules when they are set as the **Destination**.

## Enabling the Identity Agent for User Awareness

Enable your account to identify the provisioned users with Cato's Identity Agent.

![Enable_UA_Agent.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35315692730141.png)

**To enable the identity agent:**

1. From the navigation menu, select **Access > User Awareness**.
2. Select the **Identity Agent** section.
3. Enable the identity agent for your account.

The toggle is green ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35315731491613.png) when enabled.
4. Click **New**.

## Known Limitations

- For devices that use macOS:
  - On macOS Ventura (version 13), after the Client upgrades to the new version, there’s a one-time requirement to reboot the device
  - If you delete a user from the Client, their identity is not reported
- When users are authenticated to the Client, the identity is immediately acquired, and the **Identity Agent report** timestamp in the Client is not relevant.
- For IdPs other than Entra ID:
  - If you delete a user from the Client, their identity is not reported
- User Awareness does not identify disabled users
