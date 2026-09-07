---
title: "Controlling Access to Private Apps Through RBI"
slug: "controlling-access-to-private-apps-through-rbi"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/controlling-access-to-private-apps-through-rbi"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Controlling Access to Private Apps Through RBI

## Overview

Remote Browser Isolation (RBI) provides controlled access to private applications hosted in the Browser Application Portal. RBI controls which users can access private apps while preventing data exposure and blocking risky file uploads, protecting internal resources. By isolating sessions and enforcing strict data-handling controls, such as blocking downloads, copy/paste, and file transfers, RBI reduces the risk of malware propagation, lateral movement, and data leakage.

Cato secures access to private apps by creating an RBI session when accessing the [Browser Application Portal](/v1/docs/browser-application-portal-overview-securing-remote-access-to-applications) which has access to both the Internet and WAN network. This ensures that access to the private app, and any user actions within it, are controlled through the isolated browser.

## Configuring Secure Access to Private Apps

You can secure access to private apps through RBI by:

1. Enabling the Applications Portal and Browser Application Policy
2. Create an Internal Application for your private app
3. Enabling the [RBI service](/v1/docs/configuring-the-rbi-service-for-browsing-sessions)
4. Create a custom category for the Applications Portal
5. Creating an Internet Firewall rule for the Browser Application Portal with the RBI Action

### Step 1: Enabling the Applications Portal and Browser Application Policy

The Application Portal provides users with secure browser-based access to cloud and private apps. For more information on how to enable the Applications Portal, see [Configuring the Browser Access Portal](/v1/docs/configuring-the-browser-access-portal).

The Browser Access policy gives you granular control over which users in your account can access specific browser-based applications.. For more information on how to create your Browser Application Policy, see [Defining the Browser Access Policy](/v1/docs/defining-the-browser-access-policy).

### Step 2: Create an Internal Application

To secure access to a private app, add it as an Internal Application in the Applications Portal. For more information, see [Managing Applications for the Browser Access Portal](/v1/docs/managing-applications-for-the-browser-access-portal).

### Step 3: Enable the RBI Service

Customize RBI session settings to control which actions users can perform in private applications. For more information, see [Configuring the RBI Service for Secure Web Browsing](/v1/docs/configuring-the-rbi-service-for-browsing-sessions).

### Step 4: Create a Custom Category for the Applications Portal

Categories are global objects that you can use to customize the Networking, WAN, and Internet firewall rules to meet the specific needs of your network. Create a custom category for the Applications Portal, which you can then use in an Internet Firewall rule. For more information, see [Working with Categories](/v1/docs/working-with-categories).

![Categories.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31524641481245.png)

### Step 5: Creating an Internet Firewall Rule

Create an Internet Firewall rule with the Custom Category created in step 4 and an RBI Action. In this rule, you can define the users, devices, or other criteria that you want to be able to access the private app through RBI. For example, a user on a device without an Endpoint protection solution installed can only access an internal HR web portal through RBI. This isolates the session so the user can view data but cannot download, copy, or interact directly with the private network. For more information, see [Managing the Internet Firewall Policy](/v1/docs/managing-the-internet-firewall-policy).

![FWrule4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31524654528797.png)

## Traffic Flow for Accessing Private Apps Through RBI

Traffic from the user’s device is routed through the Cato Cloud, which automatically initiates an RBI session. The RBI service then connects to the Application Portal, which provides secure access to private applications hosted on the WAN.

## Known Limitations

- Users configured to access a private app through RBI must open the entire Browser Application Portal through an RBI session. All apps within the portal will open in the same session.
