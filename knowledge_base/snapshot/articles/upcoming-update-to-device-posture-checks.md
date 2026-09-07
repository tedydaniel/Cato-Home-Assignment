---
title: "Upcoming Update to Device Posture Checks"
slug: "upcoming-update-to-device-posture-checks"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/upcoming-update-to-device-posture-checks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upcoming Update to Device Posture Checks

Device Posture checks can run continuously at configured intervals, even before the Client connects. This helps keep device posture data up to date. This feature is currently called Advanced Posture, for more information, see [Client Connectivity Policy - Improved Posture Checks.](/v1/docs/client-connectivity-policy-continuous-posture-checks-check-policy)

Starting August 7, 2026, this configuration will be enabled by default. The checks will run at the recommended interval of every 10 minutes.

Cato will also update the allowed range for continuous posture checks. The minimum interval will be 5 minutes, and the maximum interval will be 1440 minutes (24 hours).

## What is the impact to my Account?

This update helps keep device posture data current and can reduce authentication time for users connecting with the Cato Client.

The following changes will apply to your account:

- For accounts that have not configured device checks to run continuously:
  - Device checks will start to run continuously
  - The periodic posture check interval will be set to the recommended 10 minute cadence
  - If you have changed the periodic check interval, this will be updated to 10 minutes
- For accounts that have configured device checks to run continuously:
  - Accounts with a posture check interval outside the valid range will be updated to 10 minutes
- For all accounts:
  - The Resources > Device Posture > Settings tab will be renamed Check Policy and contain user experience updates and improvements

## What Action Do I Need to Take?

No action is required.

After this change is made, you can configure device checks to not run continuously, although Cato does not recommend it. You can also change the posture check interval to any value within the allowed range.

The recommended posture check interval is 10 minutes.

To update these settings, go to Resources > Device Posture > [Check Policy](/v1/docs/client-connectivity-policy-continuous-posture-checks-check-policy) in the Cato Management Application.

## Who Do I Talk to If I have Questions?

Please use [Cato Ask AI](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.catonetworks.com%2Fhc%2Fen-us%2Farticles%2F24202009938077-Understanding-Cato-s-Knowledge-Base-AI-Assistant&amp;data=05%7C02%7Cyaakov.simon%40catonetworks.com%7C61561874b4c04ae2166308ddc205e382%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638880052726478094%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=kGPEWXBsuZ4iSKsSp1QeRk29uKK8cPSLSVGOV2GQ1TI%3D&amp;reserved=0) in the CMA to answer questions about configuring the Check Policy for [continuous device checks](/v1/docs/client-connectivity-policy-continuous-posture-checks-check-policy).
