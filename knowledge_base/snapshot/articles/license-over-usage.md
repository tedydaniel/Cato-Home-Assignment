---
title: "License Over-Usage"
slug: "license-over-usage"
updated: 2026-08-31T13:23:20Z
published: 2026-08-31T13:23:20Z
canonical: "knowledge.catonetworks.com/license-over-usage"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# License Over-Usage

Over-usage occurs when the measured usage for a license exceeds the licensed capacity for that license during a calendar month. Usage is measured monthly, and over-usage is evaluated independently for each license.

Unused capacity cannot be transferred between licenses or between region groups to offset over-usage.

When over-usage occurs, the customer must resolve the excess usage by increasing the licensed capacity or as described in the Over-Usage Resolution section of this guide.

When over-usage occurs for Base Products (Bandwidth Pool or ZTNA Users), associated Premium Security and Insights licenses must also be increased accordingly.

## Notification of Over-Usage

When over-usage is detected for a given calendar month, Cato sends a notification to the customer and the partner. Notifications are issued at the end of the calendar month and are sent only for months in which over-usage occurs.

Detailed usage reports and historical visibility for usage measurement and over-usage are available. Customers can configure the notification recipients through the Cato Management Application (CMA).

## Over-Usage Resolution Options

When over-usage is identified, customers have two options to address the excess usage, depending on whether the increased consumption is temporary or ongoing.

**True-Up (One-Time)**

A one-time charge covering the over-usage for the specific month or months in which it occurred. This option is typically used to address short-term or seasonal spikes in usage.

**True-Forward (Expansion)**

An increase in licensed capacity to cover over-usage for the remainder of the current contract term (co-term). The increased licensed quantity must be at least equal to the measured over-usage. Customers can only true-forward a quantity that is at least as large as the over-usage amount.

When choosing True-Forward, the increased licensed capacity applies from the following billing period onward. The month in which the over-usage occurred is not retroactively billed under the True-Forward option.

The applicable pricing and commercial terms for True-Up and True-Forward are defined in the customer’s commercial agreement.

## Over-Usage Evaluation Following Migration from Enforcement License Model

**Note:** Not sure which license model your account uses? See [Identifying your License Model](/v1/docs/identifying-your-license-model).

For customers transitioning from the Enforcement License to the Bursting License, usage measurement and over-usage evaluation begin on the first full calendar month following the migration date.

If a customer migrates during a calendar month, usage generated during the partial month is not included in the measurement or over-usage evaluation. Only usage measured from the first day of the following calendar month is considered.

For example, if an account migrates to the Bursting License on January 5, 2027, usage measurement begins on February 1, 2027, and the first over-usage evaluation is based on February usage.

Usage information may still be visible in the CMA during the partial transition month; however, that period is not included in usage measurement or over-usage evaluation.
