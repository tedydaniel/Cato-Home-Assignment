---
title: "Cato Management Application Error Codes"
slug: "cato-management-application-error-codes"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cato-management-application-error-codes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Management Application Error Codes

This article shows common error codes which may be displayed when using the Cato Management Application.

| Error code | Error message | Reason | Action Item |
| --- | --- | --- | --- |
| CC-00104 | "Authentication failed - Error CC-00104" | The user's organisation or e-mail address is not recognised by the login domain. | Verify that the User's email is active within your account and that they have typed their address correctly. |
| CC-00105 | "Authentication failed - Error CC-00105" | Two different accounts with the same e-mail address have been found within the same account. | Attempt to identify where the duplicate configuration is, and remove users where required. |
| CC-00107 | "Authentication Failed - Error CC-00107" | Found more than 1 VPN user with the same UPN (UserPrincipalName). | Contact System Administrator |
| CC-00108 | "Authentication failed - Error CC-00108" | SSO is not active for this user (but is active for the account). | Contact your System Administrator to configure SSO for this user. |
| CC-00109 | "Authentication failed - Error CC-00109" | SSO is not active (or configured) for this account. | Contact System Administrator, or configure SSO settings for the account. |
| CC-00110 | "Authentication failed - Error CC-00110" | Could not find a user with this UPN. Possible causes: sync issues, sync from ADFS etc. | Contact System Administrator |
| CC-00111 | "Authentication failed - Error CC-00111" | Generic unexpected SSO Error. | Contact System Administrator |
| CC-00114 | " Google SSO disabled for account - Error CC-00114" | Google SSO is not active (or configured) for this account. | Contact System Administrator |
| CC-00115 | "OneLogin SSO disabled for account - Error CC-00115" | Onelogin SSO is not active (or configured) for this account. | Contact System Administrator |
| CC-00116 | "Okta sso disabled for account - Error CC-00116" | Okta SSO is not active (or configured) for this account. | Contact System Administrator |
| CC-00117 | " Azure SSO disabled for account- Error CC-00117" | Azure SSO is not active (or configured) for this account. | Contact System Administrator |
| CC-00118 | “Mail domain is not valid - Error CC-00118" | Mail domain not valid | Contact System Administrator to enter a valid mail domain |
| CC-00119 | “Authentication failed - Error CC-00119” | The tenant is not configured for Azure SSO | Contact System Administrator |
| CC-00120 | “Authentication failed - Error CC-00120” | More than one Tenant is configured for Azure SSO. | Contact System Administrator |
| CC-00123 | “Authentication failed - Error CC-00123” | No Okta, Google or OneLogin configuration was found for this mail domain | Contact System Administrator |
| CC-00124 | “Authentication failed - Error CC-00124” | More than one okta configuration was found with the same mailSuffix | Contact System Administrator |
| CC-00125 | “Authentication failed - Error CC-00125” | Account not configured with this provider | Contact System Administrator |
| CC-00130 | "Authentication failed - Error CC-00130" | Email configured on multiple accounts with SSO | Contact System Administrator |
| CC-00131 | "Authentication failed - Error CC-00131" | Email does not exist for any VPN user | Validate that the user has entered their login credentials correctly |
| CC-00200 | "Took too long to authenticate with SSO server. Please try again (Error CC-00200)" | The original authorization request cannot be found after receiving the code & state from the external IDP. This is usually caused by the expiration of the original request (or the session) because the user waited too long. | Try to log in again after waiting several minutes. |
| CC-00201 | "There is a problem with the SSO provider ID. Please contact your system admin (Error CC-00201)" | The user that is specified in the client registration parameter of the /authorize request is not found in the Cato Management Application. | Verify the user has been created within CC2 with all expected permissions. |
| CC-00202 | "Authentication failed (Error CC-00202)" | Generic SSO Error | Contact System Administrator |
| CC-00203 | "Authentication failed (Error CC-00203)" | JWT validation is not completing. This can be for reasons such as: - JWT is expired - JWT is used before the defined time - Wrong token issuer - Code/state in authorization response is missing or there is an error parameter in the response | Try login again. If not working, contact your System Administrator |
| CC-00204 | "Authentication failed (Error CC-00204)" | Invalid user info response. It may be caused by: - Missing subject in response - Missing required attributes such as email - The subject is different from the one in the id token | Contact System Administrator |
| CC-00205 | "Authentication failed (Error CC-00205)" | Couldn't parse access token response (unexpected error structure) | Contact System Administrator |
| CC-00206 | "Authentication failed (Error CC-00206) | Received an error when was trying to exchange authentication code for a token | Contact System Administrator |
| CC-00207 | "Authentication failed (Error CC-00207)" | Cannot parse JWT ID token due to invalid claims. | Contact System Administrator |
| CC-00211 | "Authentication failed (Error CC-00211)" | Missing username attribute in authentication service configurations. | Contact System Administrator |
| CC-00212 | "Authentication failed (Error CC-00212)" | State received in authorization request is different from the one sent | Wait a few minutes and re-attempt login |
| CC-00213 | "Authentication failed (Error CC-00213)" | Nonce received in the jwt id token is different from the one sent | Wait a few minutes and re-attempt login |
| CC-00214 | "There is a problem with the SSO provider. Please contact your system admin (Error CC-00214)" | Non-supported SSO connection method has been configured within the Cato Management Application | Reconfigure the SSO provider settings within the 'Access' pages in the Cato Management Application. |
