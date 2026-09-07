---
title: "Action Required: Review Internet Firewall and Application Control Policies for Changes to Yahoo Applications"
slug: "action-required-review-internet-firewall-application-control-policies"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/action-required-review-internet-firewall-application-control-policies"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Required: Review Internet Firewall and Application Control Policies for Changes to Yahoo Applications

In the [App Catalog](/v1/docs/using-the-app-catalog), there are multiple Yahoo apps. Starting from January 18, 2026, we are making a change to the Yahoo General app so that it now also includes the Yahoo Mail app. This change means that the Yahoo Mail app can be applied to a rule:

- Within the Yahoo General app
- Within the General category (contains over 1000 apps)
- As a standalone app (Yahoo Mail)

This update changes how the Internet Firewall and Application Control policies are applied to traffic for rules that contain the Yahoo General app or the General category.

To ensure the Yahoo Mail app is controlled to meet your requirements, you must update rules in your [Internet Firewall](/v1/docs/managing-the-internet-firewall-policy) or [Application Control Policy](/v1/docs/managing-the-application-control-policy) after January 18, 2026.

## What is Changing?

Starting from January 18, 2026:

- The Yahoo Mail app will be included within the Yahoo General app and the General category
  - Any rule that includes the Yahoo General app or the General category will also apply to the Yahoo Mail app
- You can still create a rule for only the Yahoo Mail app
  - These rules will only apply to Yahoo Mail traffic and not other Yahoo General domains
  - These rules must be a higher priority than any rule containing the Yahoo General app or the General category

## What is the Impact to my Account?

You need to review the Internet Firewall or Application Control policies and identify rules that contain:

1. The Yahoo General app - starting from January 18, 2026, this rule will be applied to the Yahoo Mail app
2. The General category - starting from January 18, 2026, this rule will be applied to the Yahoo Mail app

If you have a rule that contains the Yahoo Mail app that is lower-priority than either of these two rules:

- The higher-priority rule containing the Yahoo General app or General category will be applied first
- This means that the action for the lower-priority rule with the Yahoo Mail app will be ignored

For example, in the scenario below, the Yahoo Mail app will be blocked by rule number 2, even though rule 3 allows it: ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/0517cd84-4bf5-2c9c-56cb-48a853f50c7d.png)

## What Updates do I Need to Make to My Account?

If you want Yahoo Mail to behave differently from the Yahoo General app or the General category:

- Adjust your Internet Firewall or Application Control rules so that any rule containing Yahoo Mail is placed above:
  - Rules that contain Yahoo General, and/or
  - Rules that use the General category

This ensures the Yahoo Mail app matches the intended rule before the broader Yahoo General or General category rules take effect.

## Who can I Contact If I have any Questions?

Please use the [Cato Knowledge AI assistant](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.catonetworks.com%2Fhc%2Fen-us%2Farticles%2F24202009938077-Understanding-Cato-s-Knowledge-Base-AI-Assistant&amp;data=05%7C02%7Cyaakov.simon%40catonetworks.com%7C61561874b4c04ae2166308ddc205e382%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638880052726478094%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=kGPEWXBsuZ4iSKsSp1QeRk29uKK8cPSLSVGOV2GQ1TI%3D&amp;reserved=0) in the CMA to answer questions about configuring Internet Firewall or Application Control rules.

For information about the change to app behavior, please contact the [Support team](https://support.catonetworks.com/hc/en-us/requests/new).
