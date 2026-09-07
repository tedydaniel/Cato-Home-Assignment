---
title: "Dropbox: Configuring the SaaS Posture Integration"
slug: "dropbox-configuring-the-saas-posture-integration"
updated: 2026-09-07T12:40:47Z
published: 2026-09-07T12:40:47Z
canonical: "knowledge.catonetworks.com/dropbox-configuring-the-saas-posture-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dropbox: Configuring the SaaS Posture Integration

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](https://knowledge.catonetworks.com/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Configure the required settings in the SaaS application
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the Dropbox Integration

To configure the Dropbox integration, log in to your Dropbox account and create the connector in the CMA.

### Prerequisites

- A Dropbox team plan
- A Dropbox team admin account
- Third-party connectors for the team must be approved

### Step 1: Log in to Dropbox

Log in to the Dropbox account you would like to integrate with Cato using a team admin user.

#### Step 2: Create the API Connector in the CMA

In a different tab in the same browser, create the API connector in the CMA.

**To create the API connector in the CMA:**

1. In a new tab, open the CMA and from the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. In the **SaaS Application** dropdown, select **Dropbox**.
5. Add a **Name** and **Description**.
6. In the **Capability** drop-down, select **SaaS Posture**.
7. (Optional) Choose to track errors with the integration.
8. Click **Save**. The CMA connects to Dropbox.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(27).png)
9. Click **Authorize**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(28).png)
10. Grant permissions to Cato Networks.
11. The app is visible on the **Integrated Apps** table with a **Connected** status.
