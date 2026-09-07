---
title: "Extend the IP Ranges Available for Remote Users"
slug: "extend-the-ip-ranges-available-for-remote-users"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/extend-the-ip-ranges-available-for-remote-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Extend the IP Ranges Available for Remote Users

We have identified a misconfiguration in your account. The IP range that is used to allocate IP addresses to remote users is too small.

There are fewer IP addresses available for remote users than the number of SDP licenses used in your account. For example, the configured IP range has 500 IP addresses, however you are using 600 SDP licenses.

This could result in IP conflicts that cause Client connectivity issues.

To resolve this issue, in the [IP Allocation Policy](/v1/docs/ip-allocation-policy-for-remote-users), ensure the IP range has more IP addresses than the number of SDP licenses used in your account. You can view the number of SDP licenses used in your account from the Access > License Assignment page.

## What Is the Impact to My Account?

If you do not extend the IP range available to remote users, remote users may experience connectivity issues.

## What Action do I Need to Take?

In your [IP Allocation Policy,](/v1/docs/ip-allocation-policy-for-remote-users) extend the Dynamic IP range so that you have more IP addresses available than the number of remote users in your account. You can view the number of SDP licenses used in your account from the Access > License Assignment page. For more information on SDP Licenses, see [Assigning SDP Licenses to Users.](/v1/docs/assigning-ztna-licenses-to-users)

To avoid remote users being disconnected, this action should be done as soon as possible.

## Who Do I Talk to If I Have Questions?

Please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
