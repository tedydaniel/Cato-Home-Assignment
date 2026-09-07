---
title: "Browser Access Configuration Update"
slug: "browser-access-configuration-update"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/browser-access-configuration-update"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser Access Configuration Update

Starting May 1st, 2024, we are updating the [Browser Access Portal](/v1/docs/browser-application-portal-overview-securing-remote-access-to-applications) configuration so that only users with an SDP license can access the Browser Access Portal.

## What Are the Updates?

In your [Browser Access Policy](/v1/docs/defining-the-browser-access-policy), the **All authenticated users** User Group will no longer be supported. Only users with a SDP license can access the Browser Access Portal and the configured applications.

## What Are the Impacts to My Account?

- By May 1st, 2024, you must assign an SDP license to any user that needs to access the Browser Access Portal. Users without a license will not be able to access the Brower Access Portal.
- After May 1st, 2024, any Browser Access Policy rules that include the All authenticated users User Group will automatically change to the All SDP Users User Group

## How Do I Check How Many SDP Licenses Are Available in My Account?

To view how many SDP Licenses are available in your account from the Cato Management Application, navigate to **Access > License Assignment.**

For more information, see [Assigning SDP Licenses to Users.](/v1/docs/assigning-ztna-licenses-to-users)
