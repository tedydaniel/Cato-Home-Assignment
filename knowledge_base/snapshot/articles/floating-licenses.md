---
title: "Floating Licenses"
slug: "floating-licenses"
updated: 2026-08-31T13:24:29Z
published: 2026-08-31T13:24:29Z
canonical: "knowledge.catonetworks.com/floating-licenses"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Floating Licenses

Floating Licenses provide flexibility during the initial deployment phase, allowing customers to begin using licensed services before full license activation. They are billed based on actual used capacity during that period, not on contracted license quantities.

**Ramp-up Period** When a customer purchases licenses with a future service start date, the account enters a Ramp-up Period. The Ramp-up period lasts for up to 12 months or until the service start date of the purchased licenses, whichever occurs first, after which all licenses transition to full activation and enter the **Full Capacity Period**.

**Grace Period**

When moving from trial to commercial, the customer enters the Ramp-Up Period and receives a 14-day grace period. Usage generated during the grace period is not included in Floating measurement.

Following the grace period, usage measurement begins on the next full calendar month. Usage may still be visible in the CMA during the grace period and any partial month that follows; however, that usage is not included in the floating measurement.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/floating_license.png)

## Capacity Measurement During the Ramp-Up Period

During the Ramp-Up Period, usage is measured monthly according to the standard measurement rules for each license type (for example, users, bandwidth, or devices).

The highest measured usage reached to date becomes the billed baseline for the period. If usage decreases in a later month, billing remains based on the highest previously measured value until full activation.

For example, if an account has 40 active licenses at the beginning of August and usage increases to 50 during the month, billing for August is based on 50 licenses.

Similarly, if usage is 1000 users in July and decreases to 750 users in August, billing remains based on 1000 users during the Ramp-Up Period until full activation.

## Billing During the Ramp-Up Period

During the Ramp-Up Period, billing is based on measured used capacity and is charged in arrears according to the agreed billing schedule.

## Over-Usage During the Ramp-Up Period

Over-usage may occur during the Ramp-Up Period and is evaluated based on the same Fair Use rules defined for each license type.

## Adding Licenses during the Ramp-Up Period

Customers may purchase additional licenses or services during the Ramp-Up Period. Additional licenses follow the same Ramp-Up timeline and co-terminate with the account end date.

Purchasing additional licenses does not create a new Ramp-Up Period.

## End of Ramp-Up Period

At the end of the Ramp-Up Period, all licenses transition to full activation.

The month in which the account transitions from the Ramp-Up Period to full activation is measured as a normal commercial month. Usage during that month is included in measurement and over-usage evaluation from the beginning of the calendar month.

Following activation, billing is based on the contracted license quantities, regardless of prior Ramp-Up usage, and standard measurement and over-usage rules apply.

## Measurement During Ramp-Up Period by License Type

| **License** | **Usage Measured During Ramp-Up Period** |
| --- | --- |
| **Base Products** |
| Bandwidth Pool | Monthly P95 bandwidth usage per region group |
| ZTNA User | Monthly distinct authenticated users across all region groups |
| **Premium Security** |
| Advanced Threat Prevention | Billed according to Base Product. Not measured individually |
| Threat Prevention | Billed according to Base Product. Not measured individually |
| Agentic Threat Prevention | Billed according to Base Product. Not measured individually |
| App & Data Security | Billed according to Base Product. Not measured individually |
| CASB | Billed according to Base Product. Not measured individually |
| DLP | Billed according to Base Product. Not measured individually |
| Assets Security | Monthly identified devices per device block. Floating charges apply when the numbed of discovered devices is higher than 50% of the licensed devices |
| AI Security for Users | Not subject to measurement |
| AI Security for Applications | Not subject to measurement |
| EPP | Not subject to measurement |
| **Insights** |
| DEM | Monthly identified users monitored across the Cato Cloud |
| XOps | Billed according to Base Product. Not measured individually |
| **Data Lake Storage** |
| Data Lake | Not subject to measurement |
| **Hardware** |
| Sockets | Deployed Socket units at sites that are actively passing traffic |
| Sockets hardware add-on | Deployed Socket hardware units |
| **Services** |
| Managed Services | - ILMM - Per deployed site - NOCaaS / Hands-Free Management – Active sites which send traffic through Cato Cloud |
| Professional Services | Not subject to measurement |
| Premium Support | Not subject to measurement |
