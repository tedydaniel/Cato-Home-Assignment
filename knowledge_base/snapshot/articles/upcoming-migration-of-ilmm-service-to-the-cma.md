---
title: "Upcoming Migration of ILMM Service to the CMA"
slug: "upcoming-migration-of-ilmm-service-to-the-cma"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/upcoming-migration-of-ilmm-service-to-the-cma"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upcoming Migration of ILMM Service to the CMA

Cato is integrating the Intelligent Last Mile Monitoring (ILMM) service into the XDR ecosystem. This will let ILMM customers benefit from enhanced control and deeper insights by using the XDR capabilities in the Cato Management Application (CMA).

These enhancements require configuration changes to your account. This notification details the required changes, which will be implemented by Cato with no need for customer action.

The migration for the relevant accounts will take place over several weeks and Cato will start the migration rollout on May 5, 2025.

## What are the Changes to My Account?

In the next few weeks, the ILMM service will be managed completely through the CMA instead of using separate tools.

Cato will implement the following configuration changes to enable this enhancement:

- **Last Mile Link Report** - Cato will configure the settings in the [Reports](/v1/docs/cato-reports) page to generate a **Last Mile Link** report that replaces the current ILMM report. To configure the recipients for this report, a new mailing list will be created in the [Mailing List](/v1/docs/working-with-mailing-lists) page containing the email addresses of the parties that currently receive the ILMM report.
- **Response Policy Rules and New Webhook Integration** - To enable integration of your CMA account with the ticketing service for ILMM, Cato will configure the following:
  - A [Response Policy](/v1/docs/creating-the-response-policy-for-xops-stories) rule for the **Network XDR** producer with a trigger of **Story Created**
  - A Response Policy rule for the **Network XDR** producer with a trigger of **Story Updated**
  - A new [Webhook integration](/v1/docs/sending-cma-notifications-via-webhooks) in the Subscriptions page for Cato’s Zendesk ticketing system. Both of the above Response Policy rules will be configured to send a notification to this integration
- **Link Quality Health Rule** - The ILMM service requires specific settings configured in a rule in the [Quality Health Rule](/v1/docs/working-with-link-health-rules) page. The default rule that is configured for new accounts meets these requirements, however some accounts don’t have this rule configured. Therefore Cato will perform the following:
  - For accounts with the default rule configured - no change will be made
  - For accounts with no Quality Health Rules configured - Cato will add the default rule
  - For accounts with existing rules but without the default rule - Cato will add a new rule
- **Mute Stories Rules** - The current ILMM [Scheduled Maintenance](/v1/docs/managing-ilmm-for-your-account) page will soon be deprecated and fully replaced by the [Mute Stories policy](/v1/docs/muting-xops-stories). Mute Stories rules can be defined to avoid creating alerts during planned maintenance windows. Cato will configure the following:
  - A Mute Stories rule to mute alerts for IPsec, vSocket, and Cloud Interconnect sites, as these sites are currently not supported by the ILMM service.
  - During the migration process, Cato will configure a Mute Stories rule whenever we detect an existing planned maintenance window to ensure the maintenance windows are migrated as required. Going forward, we recommend that admins create additional Mute Stories rules for new and upcoming planned maintenance windows.

> [!NOTE]
> Note:
> 
> Do not change any of these settings. Any alteration of these configurations may prevent the ILMM service from functioning.

## Do I Need to Make Any Changes?

No. Cato will make all the required changes.

## What is the Impact on the Account?

There is no impact to the functionality of your account. Cato will update your account to ensure that the ILMM service is integrated with Cato XDR without impact to the Cato service.

## Who Do I Talk to If I Have Questions?

Please contact your Cato account representative or [Support](https://support.catonetworks.com/hc/en-us/requests/new).
