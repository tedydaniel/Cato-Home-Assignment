---
title: "Upcoming EoL for Some SubTypes of Cato Event Data"
slug: "upcoming-eol-for-some-subtypes-of-cato-event-data"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/upcoming-eol-for-some-subtypes-of-cato-event-data"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upcoming EoL for Some SubTypes of Cato Event Data

From January 2, 2025, Cato is announcing the End of Life (EoL) for some SubType values used in the event consumption APIs related to the Cato Clients. After January 2, 2025, the values below will no longer be reported and will be unavailable for queries and scripts.

This table shows the impacted values and a value you can use as a replacement.

> [!NOTE]
> Note:
> 
> The rollout of some of these changes is on pause. See the table for more information.

| SubType Value | Replacement Value(s) | Notes | Update February 11, 2025 |
| --- | --- | --- | --- |
| VPN Never-Off-Bypass | Always-On Bypass | The **VPN Never-Off-Bypass** SubType value is being replaced with the value **Always-On Bypass** | This change has been deployed |
| Reconnected | Connected or Disconnected | To increase granularity, the **Reconnected** SubType value is being split into 2 new values, **Connected** and **Disconnected** | The rollout of this change is paused for accounts that use the Ireland CMA location ([cc.catonetworks.com](http://cc.catonetworks.com/)). For more information, see [Working with the CMA](/v1/docs/cma-technical-guidelines) |
| Changed PoP | Connected or Disconnected (The PoP name is returned in the lastPopName field.) | To increase granularity, the **Changed PoP** SubType value is being split into 2 new values, **Connected** and **Disconnected** | The rollout of this change is paused for accounts that use the Ireland CMA location ([cc.catonetworks.com](http://cc.catonetworks.com/)). For more information, see [Working with the CMA](/v1/docs/cma-technical-guidelines) |

## What Changes Do We Need to Make?

If you are using these values in your automation flows, for example in an integration to push events to cloud storage or to query events to a SIEM solution, you must update the flows to use the replacement values in the table above.

For example, if you use the **Reconnected** value in a filter, you need to change this filter to the **Connected** or **Disconnected** value.

If you are not using any values that will be declared EoL, no changes are required and there is no impact on your account.

## What is the Impact on My Account?

After the EoL date, **VPN Never-Off-Bypass,Reconnected**, and **Changed PoP** SubType values will no longer be available for data related to the Cato Clients. You can use the alternative values listed above to accurately retrieve the relevant data.

## What Happens if I Do Not Make Any Changes?

If you do not make any changes before the EoL date, you could experience the following impact with the Cato API:

- Running an API query with EoL values will likely return an error. For example, in the EventFieldName query, if you use the **VPN Never-Off-Bypass** value in a filter, the query will fail and will return an error.
- If you have analytics or workflows that rely on these EoL values, there could be changes in behavior. For example, a SIEM widget doesn’t display accurate data.

## Who Do I Talk to If I Have Questions?

Please contact your account representative or [Support](https://support.catonetworks.com/agent/).
