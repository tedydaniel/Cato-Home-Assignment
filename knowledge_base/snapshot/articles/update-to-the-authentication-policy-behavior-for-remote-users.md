---
title: "Update to the Authentication Policy Behavior for Remote Users"
slug: "update-to-the-authentication-policy-behavior-for-remote-users"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/update-to-the-authentication-policy-behavior-for-remote-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update to the Authentication Policy Behavior for Remote Users

Your account is configured to use Registration Code as the user authentication method for the Cato Client. However, we have identified that some users can still authenticate with their username and password.

On May 24, 2026, we will introduce a fix that enforces authentication by Registration Codes only, as per the original configuration.

After this date, users will only be able to authenticate using a registration code and will no longer be able to authenticate with their username and password.

## What is the Impact to the Account?

After May 24, 2026, users will no longer be able to authenticate to the Client with their username and password. Users who do not have a valid registration code may not be able to authenticate and connect to your network.

## What Action do I Need to Take?

The action required depends on how you want your users to authenticate. If you want users to:

- Authenticate with a Registration Code, and they already have received a code – no action is required.
- Continue authenticating with their username and password, either:
  - Remove registration codes as the method of provisioning users and set your account level Authentication Method to User & Password. This will to apply to all users, for more information, see [Activating Users with a Registration Code](/v1/docs/activating-users-with-a-registration-code) and Configuring the Authentication Policy for Cato Clients
  - Update the authentication settings for specific users. For more information, see [Configuring the Authentication Policy for Cato Clients.](/v1/docs/configuring-the-authentication-policy-for-cato-clients)
  - If you want users to authenticate with registration codes, make sure that users have valid registration codes. For more information, see [Activating Users with a Registration Code.](/v1/docs/activating-users-with-a-registration-code)

## Who do I Talk to If I Have Questions?

Please use the [Cato Knowledge AI assistant](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.catonetworks.com%2Fhc%2Fen-us%2Farticles%2F24202009938077-Understanding-Cato-s-Knowledge-Base-AI-Assistant&amp;data=05%7C02%7Cyaakov.simon%40catonetworks.com%7C61561874b4c04ae2166308ddc205e382%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638880052726478094%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&amp;sdata=kGPEWXBsuZ4iSKsSp1QeRk29uKK8cPSLSVGOV2GQ1TI%3D&amp;reserved=0) in the CMA to answer questions about authenticating to the Client. For other questions, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
