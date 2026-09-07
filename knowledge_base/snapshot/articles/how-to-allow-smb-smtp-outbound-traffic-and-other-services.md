---
title: "How to Allow SMB/SMTP Outbound Traffic (and Other Services)"
slug: "how-to-allow-smb-smtp-outbound-traffic-and-other-services"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/how-to-allow-smb-smtp-outbound-traffic-and-other-services"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Allow SMB/SMTP Outbound Traffic (and Other Services)

As per cybersecurity best practices, the default [Internet Firewall](/v1/docs/what-is-the-cato-internet-firewall) policy blocks outgoing SMTP and SMB traffic. This is an example of an Internet Firewall policy where rule 6 blocks SMB and SMTP traffic:

![115011053309-mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303113790109.png)

In case you have a valid outbound service in your organization, you will have to create an exception to rule 6 to allow the SMTP access to maintain functionality.

As per Cato's best practices SMTP and SMB should only be opened for those specific entities that require it. In some occasions, you may want to limit the SMTP traffic to a specific server as well (e.g. Google, O365), so this can be considered also as a best practice.

At last, to be more specific you can also allow services such as Office365 (or Gmail), that will do the same work.

1. From the navigation menu, click **Security > Internet Firewall**.
2. Create a new exception for the desired protocol or service, from the more menu at the end of the rule, select **Add Exception**.

In the example above, rule 6.1 is an exception that allows SMTP **Service/Port** specific hosts for the HQ **Source**.
3. Create a rule above 6, that allows SMTP or SMB service for the specific servers and apps that require access.

In the example above, rule 5 allows the email apps used by the organization for the **Source** All SDP Users and All Sites.
