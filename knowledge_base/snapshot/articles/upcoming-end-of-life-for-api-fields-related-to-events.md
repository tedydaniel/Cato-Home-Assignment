---
title: "Upcoming End of Life for API Fields Related to Events"
slug: "upcoming-end-of-life-for-api-fields-related-to-events"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/upcoming-end-of-life-for-api-fields-related-to-events"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upcoming End of Life for API Fields Related to Events

> [!NOTE]
> Note:
> 
> This schema change has been delayed. For more information, see [Update to End of Life Announcement for API Fields Related to Events](/v1/docs/update-to-end-of-life-announcement-for-api-fields-related-to-events).

Cato is announcing the End of Life (EoL) of some fields related to events that are used in the `appStats` API query and others. For more information on where these fields are used, see the [Cato Networks GraphQL API Reference.](https://api.catonetworks.com/documentation/#definition-EventFieldName)

The table below shows the impacted fields and an alternative supported field.

Most of these fields will be declared EoL from December 1st, 2024. The `vpn_user_id` field will be declared EoL from September 1st, 2024.

After these dates, the fields will no longer be available in the Cato API

## Fields Declared End of Life

These are the fields that are declared EoL:

| **Field Name** | **Alternative Supported Field** |
| --- | --- |
| application | application_name application_id |
| custom_categories | custom_category_id |
| custom_category | custom_category_namecustom_category_id |
| dest_site | dest_site_name dest_site_id |
| device_posture_profiles | device_posture_profile |
| parent_pid | src_process_parent_pid |
| pid | src_pid |
| process_path | src_process_path |
| rule | rule_name rule_id |
| src_site | src_site_name src_site_id |
| vpn_user_id Note: EoL Sept. 1 2024 | user_id |

## What is the Impact to my Account?

After the EoL date, the API fields will no longer be available in the relevant API queries. This can have the following impacts:

- Running an API query with EoL fields will likely return an error. For example, in the `events` query, if you use the `rule` field in a filter, the query will fail and an error will be returned.
- If you have analytics or workflows that rely on these EoL fields, there could be changes in behavior. For example, a SIEM widget doesn't display accurate data.

You can use the alternative fields in the table above to accurately retrieve the relevant data.

## What Changes Do We Need to Make?

If you are using these fields in your automation flows, migrate to the suggested alternative fields before the EoL date.

If you are not using any fields that will be declared EoL, no changes are required and there is no impact on your Cato API queries.

## Who Do I Talk to If I Have Questions?

Please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
