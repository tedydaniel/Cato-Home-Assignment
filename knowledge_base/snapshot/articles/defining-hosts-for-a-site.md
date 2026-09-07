---
title: "Defining Hosts for a Site"
slug: "defining-hosts-for-a-site"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/defining-hosts-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Defining Hosts for a Site

You can define static hosts, which you can then use in security rules and policies.

This definition can also be used to account for **DHCP Reservation**, where a static IP is assigned as part of the DHCP flow based on the client's MAC address.

You can’t create static hosts learned via BGP. Instead, you can:

- Define a network range for the site that includes the static host
- Create a [global IP Range](/v1/docs/using-ip-ranges-in-policies) for the host

**Translated IP** shows the IP address that the PoP translates for the internal host IP address. When **Static Range Translation** (**Administration > System Settings**) is enabled for the account, you can define the translated IP range in the **Networks** screen.

**To add a host to a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Static Host Reservations**.
3. Click **New**. The **Add Host** panel opens.
4. Enter these settings for the host:
  - Name
  - IP Address
  - **(Optional)** MAC address
5. Click **Apply**. The **New Host** panel closes, and the host is added to the screen.
6. Click **Save**. The host is added to the site.

## Editing a Host

Use the **Edit Host** panel to edit the settings for a host.

**To edit a host:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Static Host Reservations**.
3. In the **Name** column, click the host.

The **Edit Host** panel opens.
4. Edit the settings for the host.
5. Click **Apply**. The **Edit Host** panel closes.
6. Click **Save**. The changes to the host are saved.

## Deleting a Host

Before you can delete a host, make sure that it isn't used somewhere else in the Cato Management Application, such as groups or firewall rules.
