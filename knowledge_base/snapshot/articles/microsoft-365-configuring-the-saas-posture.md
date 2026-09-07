---
title: "Microsoft 365: Configuring the SaaS Posture"
slug: "microsoft-365-configuring-the-saas-posture"
updated: 2026-08-05T08:48:12Z
published: 2026-08-05T08:48:12Z
canonical: "knowledge.catonetworks.com/microsoft-365-configuring-the-saas-posture"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft 365: Configuring the SaaS Posture

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Create the MS Tenant Integration (if you do not have this already configured)
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the Microsoft 365 Integration

To configure the integrations, create an API app.

### Prerequisites

- You must have one of these licenses:
  - Microsoft 365 E3
  - Microsoft 365 E3 license with E5 Compliance add-on
  - Microsoft 365 E3 license with E5 eDiscovery and Audit add-on
  - Office 365 E5 license

### Step 1: Create the MS Tenant Integration

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

**To create the MS Tenant integration:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(19).png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(20).png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. Select **SaaS Posture**.
6. Select the **Microsoft Primary Tenant** that was created in Step 1.
7. (Optional) Add a description.
8. Click **Save**.

The CMA connects to the vendor
9. Click **Authorize**.
10. A Microsoft permissions screen will appear.
11. Review the requested permissions and click **Accept.**

The app is visible on the **Integrated Apps** table with a **Connected** status.
