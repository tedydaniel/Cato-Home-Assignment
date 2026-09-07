---
title: "SDP User Doesn't Receive SMS MFA Code"
slug: "sdp-user-doesn-t-receive-sms-mfa-code"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/sdp-user-doesn-t-receive-sms-mfa-code"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SDP User Doesn't Receive SMS MFA Code

When multi-factor authentication (MFA) is enabled for users, they choose to receive MFA codes through SMS on their phones. In order for this to work, the country code must precede the user's phone number or else the user will not receive the MFA code.

You can verify that the phone number includes the country code by checking the SDP Users configuration in the Cato Management Application.

![VPN_General.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360017329077.png)

## SDP Users Created Through LDAP Sync

The failure to receive an MFA code over SMS is mostly seen when SDP users are imported from LDAP. As part of the LDAP sync, Cato imports the SDP user's phone number from one of two attributes:

- mobile
- telephoneNumber (if the mobile attribute does not exist)

It's important to populate these attributes with a phone number that includes the country code for MFA to work with SMS.

If the phone number is incorrect, fix the number in LDAP and then run another LDAP sync in the Cato Management Application. Once the LDAP sync is complete, the SDP user should start receiving MFA.

Go to Access **> Directory Services** > LDAP and click the Sync Now button to update an LDAP SDP user's phone number.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20552666024733.png)

## Manually Created SDP Users

If the SDP user is manually created, end users have control over the phone number to which the MFA code is sent through the Cato [User Portal](/v1/docs/managing-sdp-clients-with-the-cato-user-portal). If these users are not receiving MFA codes and their number is incorrect in the Cato Management Application, direct them to the Cato User Portal to change their phone number.

After logging in, users can find the "View/Change 2FA Settings" link at the bottom of the page.

![Change_2FA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360017329037.png)

Clicking that will take them to another page where they can click the "(Change Settings)" link next to 2 Factor Authentication. A pop-up window will then guide them through changing their phone number.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20552666031773.png)

The phone number that the user inputs is validated, and they are forced to choose a country, which automatically populates the country code.

## SDP User is Not in a Supported Location

SMS MFA codes are only sent to users in these locations:

| Australia | Isle of Man | Saudi Arabia |
| --- | --- | --- |
| Austria | Israel | Serbia |
| Belarus | Italy | Singapore |
| Belgium | Japan | Slovakia |
| Bosnia and Herzegovina | Kazakhstan | Slovenia |
| Brazil | Latvia | South Africa |
| Bulgaria | Lithuania | South Korea |
| Canada | Macedonia | Spain |
| Chile | Malaysia | Sweden |
| China | Mexico | Switzerland |
| Colombia | Morocco | Taiwan |
| Croatia | Netherlands | Thailand |
| Czech Republic | New Zealand | Turkey |
| Denmark | Norway | U.S. Virgin Islands |
| Egypt | Russia | Ukraine |
| France | Peru | United Arab Emirates |
| Germany | Philippines | United Kingdom |
| Greece | Poland | United States |
| Hong Kong | Portugal | Uruguay |
| Hungary | Puerto Rico | Uzbekistan |
| India | Qatar | Vietnam |
| Indonesia | Romania | Ireland |
