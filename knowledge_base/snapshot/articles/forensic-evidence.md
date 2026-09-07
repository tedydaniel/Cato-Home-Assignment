---
title: "Investigating DLP Violations with Forensic Evidence"
slug: "investigating-dlp-violations-with-forensic-evidence"
updated: 2026-09-06T13:27:04Z
published: 2026-09-06T13:27:04Z
canonical: "knowledge.catonetworks.com/investigating-dlp-violations-with-forensic-evidence"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Investigating DLP Violations with Forensic Evidence

This article explains how to view forensic evidence from DLP policy violation events.

## Overview

To investigate DLP policy violations, you can securely view the violation evidence directly in the Cato Management Application (CMA). This allows security teams to quickly understand the context of an incident, assess potential data exposure, validate false positives, and fine-tune DLP policies with confidence.

When a DLP policy event is generated, the evidence files are encrypted and sent to a configured secure storage destination. To minimize data exposure and ensure compliance with regulatory requirements, these files can only be viewed on request by admins with the relevant permissions.

**Note**: Image file types are not supported

### Use Case: Investigating PII Exposed via Slack

A sales representative needs to process a refund to a customer. They send a Slack message to their manager to approve the refund that includes the customer's address. A DLP rule configured to detect PII identifies the customer's address, blocks the message, and triggers an event. The Slack messages are encrypted and stored securely in an Amazon S3 bucket as evidence.

A security analyst, with permission to view forensic evidence, starts to investigate the event. As part of the investigation, they securely view the Slack conversation and confirm that PII data was exposed.

By confirming with certainty that a policy violation has taken place, the security analyst can contact the employees involved and educate them about the company's data protection policy.

## Enabling the Viewing of Forensic Evidence

To enable forensic evidence to be viewed, you need to:

1. Enable your preferred option for the secure storage of the evidence
2. Configure forensic evidence settings
3. Provide permissions for Admin that can view the evidence

### Step 1: Enabling the Secured Storage of Evidence

Forensic evidence is stored externally to Cato in a storage destination that you choose. To enable evidence storage, you must create an integration between Cato and the supported storage service. This integration allows Cato to securely write encrypted evidence files when a DLP policy is triggered in your designated storage. For step-by-step instructions on configuring the integration, see the link below. The supported storage services are:

- [Amazon S3](/v1/docs/amazon-s3-configuring-the-forensic-storage-connector)
- [Google Cloud](/v1/docs/google-cloud-configuring-the-forensic-storage-connector)
- [Azure Blob Storage](/v1/docs/azure-blob-storage-configuring-the-forensic-storage-connector)

### Step 2: Configure Forensic Evidence Settings

To start storing forensic evidence, you need to enable the feature in the CMA. You can also choose to only display a snippet of the evidence or allow the original file to be stored and available for download during an investigation.

**Note**: All forensic evidence is always encrypted, it is not possible to uncheck the **Encrypt evidence stored in the configured destination** checkbox

![Forensics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33222703990301.png)

**To configure forensic evidence:**

1. From the navigation menu, click **Security > Data Types & Profiles**.
2. On the **Settings** tab, enable the **Store DLP Evidence** toggle.
3. To allow the original evidence file to be downloaded from an event, select the **Store original files upon match** checkbox. If this option is not checked, only a snippet of the evidence is available during an investigation.
4. Choose the location for the evidence to be stored.
5. Click **Save**.

### Step 3: Provide Permissions for Admin

Only Admins with the **DLP Forensics** permission are able to view forensic evidence within an event. You can add this permission to existing custom roles or create a new custom role and apply it to the relevant admin. For more information on Roles & Permissions, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

![Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33981408011293.png)

## Viewing Forensic Evidence

Forensic evidence is available from the **Data Incident** panel, available from the event that was generated after a DLP rule was violated.

**Note**: After an event is generated, it may take a few minutes for the file to be available for download.

![DLP_Draw.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33222710342301.png)

**To view forensic evidence:**

1. From the navigation menu, click **Security > Data Protection** to view the **Data Protection Dashboard**.
2. In the **Top Violating Rule**, click on the rule you want to investigate.

The Events page is displayed with a predefined filter of the events generated by this rule. For more information, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).
3. Expand the event and in the **Evidence** field, click **View forensics**.

![View_Forensics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33981398388637.png)The **Data Incident** panel opens.
4. In the **Forensics** section, click **View Evidence** , and in the pop-up box, click **Confirm**.

![Event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33222713405597.png)

The forensic evidence is displayed in the snippet. To access the full file click **Download File**. This option is grayed out if the **Store original files upon match** checkbox was unchecked in Step 2.

![Evidence.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33981421717917.png)
