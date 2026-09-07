---
title: "Recommended DLP Configuration to Monitor AI Apps"
slug: "recommended-dlp-configuration-to-monitor-ai-apps"
tags: ["Best Practices", "CASB", "Internet Security"]
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/recommended-dlp-configuration-to-monitor-ai-apps"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recommended DLP Configuration to Monitor AI Apps

This article lists recommended DLP Rules to create to monitor AI Apps.

## Overview

The Application Control and DLP policy includes pre-defined Cato-recommended rules. Included in these are rules to protect your AI apps. By default, DLP monitors and creates events for the following Data Types being uploaded to GenAI tools:

- PII
- Financial data
- Access keys & tokens
- Legal data

This is available by default for accounts created after March 25, 2025. For accounts created before this date, you can manually create the rules.

## Recommended DLP Configuration

We recommend creating the following DLP profiles and adding them to DLP rules to protect sensitive data while using AI apps. For more information, see [Securing AI App Traffic](/v1/docs/securing-ai-app-traffic).

### DLP Profiles

Create the following DLP Profiles. For more information, see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles).

| Data Profile | Data Type | Content |
| --- | --- | --- |
| PII | Predefined data types | Person identifiers [USA] Credit card numbers - near phrase [Universal] Credit card numbers [Universal] Credit card magnetic track 1 [Universal] Credit card magnetic track 2 [Universal] Driver's licences - DEFAULT [USA] Driver's licences - with phrase [USA] Person identifiers [USA] |
| Finance | Predefined data types | International Securities Identification Number (ISIN) [Universal] CUSIP - ALL [USA] Bank routing numbers [USA] CUSIP - TBA securities [USA] CUSIP - PPN [USA] CUSIP - Fixed income securities [USA] CUSIP - Equity securities [USA] SWIFT bank codes [USA] Bank routing numbers [UK] Unique Tax Reference (UTR) - DEFAULT [UK] Unique Tax Reference (UTR) - weak format [UK] SWIFT bank codes [UK] Bank & card accounts [UK] (RECOMMENDED) Bank & card accounts [USA] (RECOMMENDED) Bank account numbers [USA] Credit card numbers [Universal] |
| Access Keys & Tokens | Predefined data types | Alibaba secret key [Universal] AWS access token [Universal] GCP API key [Universal] Bitbucket client id [Universal] Bitbucket client secret [Universal] Github oauth [Universal] Github pat [Universal] Github refresh token [Universal] Gitlab pat [Universal] Gitlab rrt [Universal] Hashicorp tf API token [Universal] Hashicorp tf password [Universal] Jfrog API key [Universal] Jfrog identity token [Universal] |
| Legal | ML Classifiers | Legal > Agreement Legal > Patent Legal > Court Legal > Power of Attorney |

### DLP Rules

After you create the Data Profiles you can add them to a DLP rule. For an explanation of how to create DLP rules, see [Creating the Data Control Policy](/v1/docs/creating-the-data-control-policy).

| Type | Name | Source | Application (Category) | Criteria | Action |
| --- | --- | --- | --- | --- | --- |
| Data | Monitor PII data uploads | Any | Generative AI Tools | Data Profiles: PII | Monitor/Block (Based on your requirements) |
| Data | Monitor financial data uploads | Any | Generative AI Tools | Data Profiles: Finance | Monitor/Block (Based on your requirements) |
| Data | Monitor Access & Token uploads | Any | Generative AI Tools | Data Profiles: Access Keys & Tokens | Monitor/Block (Based on your requirements) |
| Data | Monitor legal data uploads | Any | Generative AI Tools | Data Profiles: Legal | Monitor/Block (Based on your requirements) |
