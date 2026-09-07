---
title: "Upcoming Changes to PoPs in the Cato Cloud - June 1, 2024"
slug: "upcoming-changes-to-pops-in-the-cato-cloud-june-1-2024"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/upcoming-changes-to-pops-in-the-cato-cloud-june-1-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upcoming Changes to PoPs in the Cato Cloud - June 1, 2024

In the past, some accounts worked with teams at Cato Networks to connect to special AWS PoP locations. As of June 1, 2024, these special PoP locations will be decommissioned and no longer available. To avoid a service disruption you need to change the relevant Network Rules, RPF rules, and site settings to use a different PoP location.

These configurations are impacted by the upcoming decommissioning for one or more of the PoP locations (listed below) because they use an IP that belongs to the PoP location:

- Network Rules set to egress traffic with **Route via** or **NAT** option
- Remote Port Forwarding (RPF) rules set to forward to external connections
- IPsec sites - the **Public IP** for the Primary and/or Secondary tunnel
- Socket sites - the **Primary** or **Secondary** Preferred PoP Location

**Best Practice:** Use physical Cato PoP locations for settings in your account.

## What PoP Locations are Cato Decommissioning?

These are the PoP locations that will be decommissioned as of June 1, 2024:

- California_AWS
- Frankfurt_AWS
- Ireland_AWS
- London_AWS
- Montreal_AWS
- Ohio_AWS
- Oregon_AWS
- Paris_AWS
- Sao_Paulo_AWS
- Singapore_AWS
- Sydney_AWS
- Virginia_AWS

> [!NOTE]
> Note:
> 
> Cato is maintaining the following AWS PoP locations: Mumbai_AWS, Seoul_AWS, and Tokyo_AWS.

## What Changes Do I Need to Make to the Network Rules?

Edit rules in the [Network Rules policy](/v1/docs/configuring-network-rules) (Network > Network Rules) that egress traffic using an IP address that belongs to one of the impacted PoP locations, so that the rule uses a different PoP location. The IP address is defined for the **Route via** or **NAT** method.

**Note:** The best practice is to configure at least two PoP locations to egress from.

![AWS_Decome_NetworkRule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16737089455901.png)

## What Changes Do I Need to Make to the RPF Rules?

Edit the [RPF rules](/v1/docs/configuring-remote-port-forwarding-for-the-account) (Network > Remote Port Forwarding) that forward traffic using an IP address that belongs to one of the impacted PoP locations, so that the rule uses a different PoP location.

![AWS_Decom_RPF.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16737104087197.png)

## What Changes Do I Need to Make to IPsec Sites?

Edit the **Public IP** for the **Primary** and **Secondary** tunnel for the [IPsec site](/v1/docs/ipsec-sites) (Network > Sites > {site name} > Site Configuration > IPsec) and assign IPs from a different PoP location.

![AWS_Decom_IPsec.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16737104128413.png)

## What Changes Do I Need to Make to Socket Sites with Preferred PoP Location?

Edit the **Primary** and **Secondary location** for the [Preferred PoP Location](/v1/docs/defining-a-preferred-pop-for-a-site) in the Socket sites, and choose a different PoP location.

![AWS_Decom_PreferredPoP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16737075587613.png)

## What Happens If I Don’t Make these Changes?

After June 1, 2024, if one of the settings above are configured to use a special PoP location, then there can be connectivity issues and service issues for items that match the Network Rules, RPF rules, IPsec sites, or Socket sites.

## Who Do I Talk to If I Have Questions?

Please contact your authorized Cato representative.

## Who Do I Talk to If I Have Technical Issues?

Please reach out to Cato [Support](https://support.catonetworks.com/hc/en-us/requests/new) team.
