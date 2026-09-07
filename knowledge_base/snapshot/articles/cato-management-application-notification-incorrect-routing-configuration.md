---
title: "Cato Management Application Notification: Incorrect Routing Configuration in Network Rules"
slug: "cato-management-application-notification-incorrect-routing-configuration"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cato-management-application-notification-incorrect-routing-configuration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Management Application Notification: Incorrect Routing Configuration in Network Rules

## Incorrect Routing Configuration in Network Rules

During a routine review, we discovered that the **Route via** option in Network Rules isn’t configured correctly for some of our customers. We are letting you know that you didn’t define a PoP to egress traffic from, this means that the traffic egresses from whichever PoP that the site is connected to. This is the same behavior as if **Route/NAT** is set to **None**.

Starting on Oct. 15th, 2023, there will be a new in the Cato Management Application to prevent these types of incorrect configurations. Please make sure to edit the relevant rules and remove the Route via configuration or define a PoP location for this option before you can save the rule.

After validation is added, customers with the above configurations will not be able to save any new configurations until they change the rule to resolve the incorrect configuration.

## What Changes Do I Need to Make?

Edit the [Network Rules](/v1/docs/configuring-network-rules) policy and identify the rules where no PoP is defined for the **Route via** method.

To edit the **Routing** option for the rule, make one of the following changes in the **Routing Method** section:

- Set **Route/NAT** to **None**. This is the same behavior as the current setting, and there is no change to behavior in your account.
- Select specified PoP locations for the rule. Traffic matching this rule will start to be routed to egress from the configured PoP locations. **The best practice is to configure at least two PoP locations to egress from**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13939217589533.png)

## Who Do I Talk to If I Have Questions?

Please contact your authorized Cato representative.

## Who Do I Talk to If I Have Technical Issues?

Please reach out to the Cato Support team.
