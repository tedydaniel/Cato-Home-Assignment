---
title: "Mitigating Threats in XOps Stories"
slug: "mitigating-threats-in-xops-stories"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/mitigating-threats-in-xops-stories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mitigating Threats in XOps Stories

This article discusses how to mitigate a threat in an XOps story.

## Overview

XOps stories often involve suspicious activity originating from either a specific user or a Target (such as an IP address or FQDN). For example, a story might indicate that a user's remote session was compromised or that a device is communicating with a suspected phishing domain. The story Overview page in the Stories Workbench lets you mitigate both types of threats effectively by either:

- **Revoking the User Session**: You can revoke the user's session directly from the story. This logs the user out and prompts them to reauthenticate via the Client login screen, ensuring only legitimate users regain access. If the user isn't connected at the time of mitigation, their authentication token is revoked and they'll need to reauthenticate upon reconnection.
- **Add Target to Blocklist**: You can add suspicious Targets to a Container which you can include in your blocklist policies. This ensures that no users connected to Cato can access the Target.

[Containers](/v1/docs/integrating-custom-ioc-lists-with-containers) are user-defined categories that help you manage groups of items such as IP addresses or FQDNs. Once you create a Container it can be added to a Firewall rule with the Block action. Suspicious Targets are only blocked once the Container is included in a firewall rule. When you mitigate a threat from an XOps story, you can add a Target to an existing container or create a new one. Users can still access Targets that are added to a Container but not included in a firewall rule.

### Use Case - Unusual User Activity

Analysts at Example Corp. investigated an XOps story in the Overview page, and identified a user uploading a large amount of data to a file-sharing application. They are unsure if the upload activity is for legitimate reasons or not. The analysts further notice that the user agent in use for this upload activity is anomalous for this user, indicating a possible case of credential theft by an adversary. They therefore decide to revoke the user session to force reauthentication on the device. The analysts can then continue their investigation knowing that only a legitimate authenticated user is connected to the network.

### Use Case - Malware Attack

A security analyst investigates an XOps story in the Overview page and identifies an IP address associated with malware. After additional investigation, the analyst confirms that this is an attack originating from a known malicious actor.

The analyst adds the Target to the company's suspicious IP address Container that is included in an Internet firewall rule with a Block action.

The threat is contained as no other users are able to access the IP address.

## Mitigating Threats in an XOps Story

In the story Overview page, mitigate threats from the **Actions** menu.

![Placeholder.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356129141533.png)

**To mitigate threats:**

1. In the story Overview, click the **Actions** button.
2. Select the mitigation action you want to take:
  - To revoke a user, click **Revoke User Session**. The Revoke User Session panel opens. Select the user whose active session you want to revoke. The panel automatically shows the user identified in the story.
  - To add a Target to the block list, click **Add Target to Blocklist**. Select a Target to mitigate and either select an existing Container you want to add it to, or click **Create New** to create a new Container. Ensure the Container is included in a firewall rule.
3. (Optional) Add a note.
4. Confirm your action.

## Reviewing Mitigation Actions in the Action Center

The Action Center tab in the **Home > Detection & Response Policy** page lets you review the XOps mitigation actions taken in your account.

![XDR_Action_Center.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356138483613.png)

The Action Center shows the following information for each mitigation action:

- **Time** - Timestamp for when the mitigation action was sent
- **Action** - Description of the mitigation action
- **Subject** - The user the action was performed on
- **Status** - Status of the action. For the **Add Target to Blocklist** action, these are the **Status** values:
  - **Success** - The request to revoke the session was sent to the Cato user service
  - **Failure** - There was an issue with the request to revoke the session
- **Author** - Admin who performed the action
- **Trigger** - The **Story ID** for the story from which the action was sent. Click to open the Overview page for the story
- **Note** - Optional note entered by the admin

## Known Limitations

- The **Revoke User Session** action is available only for remote users connecting to the network with the Cato Client. It is not supported for users behind a site
- The **Revoke User Session** action is supported for stories that identified a user and that are generated by one of the following producers:
  - Threat Prevention
  - Threat Hunting
  - Events Anomaly
  - Usage Anomaly
  - Cato Endpoint Alerts
- It may take up to 10 minutes for the user session to be revoked
- There may be a short delay between adding a container to a block firewall rule and the target being blocked
