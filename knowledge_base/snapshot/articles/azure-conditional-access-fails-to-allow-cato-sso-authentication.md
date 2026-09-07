---
title: "Azure Conditional Access Fails to Allow Cato SSO Authentication"
slug: "azure-conditional-access-fails-to-allow-cato-sso-authentication"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/azure-conditional-access-fails-to-allow-cato-sso-authentication"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Conditional Access Fails to Allow Cato SSO Authentication

## Issue

When implementing Azure Conditional Access for the Cato Portal application to restrict Single Sign-On (SSO), the Cato Client shows the error message "You cannot access this right now" due to the Conditional Access policy not meeting the configured requirements.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/15888902442909.png)

## Environment

- Azure SSO is configured as the authentication method in CMA.
- Azure Conditional Access applies to restrict source IP addresses (location) or the Cato Portal application.
- Both embedded or external browsers.

## Troubleshooting

These steps can be followed to troubleshoot SSO issues related to Azure Conditional Access:

1. Understand the [SSO Process Flows for Initial Authentication](/v1/docs/sso-authentication-for-users-with-cato) for SSO authentication:
  - During the initial Cato Client connection, SSO authentication occurs directly between the Client and the IdP outside the tunnel. Azure will see the Client's ISP IP address in the authentication request.
  - In cases where Always-On is enabled for the user or when SSO re-authentication takes place after the IdP token expires, SSO authentication between the Client and the IdP occurs inside the tunnel via the PoP. Azure will see the Cato PoP IP address in the authentication request.
2. Access Azure Sign-in logs under Conditional Access to analyze Failure events. The logs will include the client's source IP address for each authentication attempt. Use the 'show details' option under the Conditional Access tab for further insights into the failure. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/15889184458013.png)
3. Verify the Conditional Access Policy configuration, including the Cato Portal application and the Cato PoP IP range as excluded items. You may want to verify that the Policy is correctly configured and that it allows the correct source IP addresses and application for SSO authentication to be successful.
4. It may be possible that the Cato Portal application isn't detected correctly by the Conditional Access policy due to permission restrictions with Microsoft Azure. If that is the case, you will see a successful authentication followed by a failure as shown below. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/15889137886237.png)

## Solution

If the Conditional Access Policy includes location (user's source IP address), define the IP address or IP range based on the Always-On configuration of the user:

- Users with Always-On disabled (on-demand) will use the client's ISP IP address during authentication and the PoP's IP address for re-authentication (IdP token expires while the tunnel is up).
- Users with Always-On enabled will use the client's ISP IP address only during the initial authentication (after Cato install) and the PoP's IP address for subsequent authentication requests and re-authentication requests (IdP token expires while the tunnel is up).
- For Always-On users, the initial authentication (after Cato install) can also be forced to use the Cato tunnel by enabling the *InitialAlwaysOn* registry key as explained in [Installing Windows Clients and Always-On](/v1/docs/protecting-users-with-always-on-security).

If the Conditional Access Policy includes a block-all policy excluding the Cato Portal application, go to the Single Sign-On page in CMA and click **Microsoft Credentials,** which will prompt for admin credentials to perform consent with Azure again.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19794816508701.png)
