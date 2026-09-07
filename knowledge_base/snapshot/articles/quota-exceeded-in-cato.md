---
title: "Quota Exceeded in Cato"
slug: "quota-exceeded-in-cato"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/quota-exceeded-in-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quota Exceeded in Cato

## ​Issue

In Cato, there are two types of quotas: one pertains to events, while the other relates to alerts. The default limit varies based on the DPA license the customer has.

- For customer with DPA 2021 license, the default threshold for event generation stands at 2.5 million events per hour, per sub-type.
- On DPA 23, the threshold is determined by the number of data units the customer acquires during the renewal or onboarding process. Specifically, 1 Data Unit is equivalent to 2.5 million events per hour. (aggregation of all sub-types).

**Note:** Cato API eventsFeed rate is not limited by the Events Quota, but rather it follows different API rate limits as explained in [Understanding Cato API Rate Limiting](/v1/docs/understanding-cato-api-rate-limiting)

For alerts, the default cap for alert generation is set at 50 alerts per hour, per sub-type.

To find out what DPA license you have, go to Administration > License

E.g. of DPA 2021

![dpa.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13825357141661.jpeg)

E.g. of DPA 2023

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/14870976875677.png)

For further information, refer to [Cato Cloud Thresholds and Limits](/v1/docs/cato-cloud-thresholds-and-limits).

This article aims to provide guidance on how to address situations where you have received an email notifying you of an exceeded events quota and/or alerts quota.

## Troubleshooting

1. [Cato Events Quota Exceeded](/v1/docs/quota-exceeded-in-cato#cato-events-quota-exceeded)
2. [Cato Alerts Quota Exceeded](/v1/docs/quota-exceeded-in-cato#cato-alerts-quota-exceeded)

## **Cato Events Quota Exceeded**

When the number of events exceeds the maximum quota for the account, Cato generates an email alert.

The following screenshot shows a sample alert of events quota exceeded message for Internet firewall events:

![blobid0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360012230417.png)

## Solution

Cato generates the **Events Quota Exceeded** alert when the number of events for a specific event type exceeds the maximum limits for events per hour. For more information about the event limits, see [Cato Cloud Thresholds and Limits](/v1/docs/cato-cloud-thresholds-and-limits).

#### WAN and Internet Events

You can identify the WAN or Internet rule that is generating the large number of events and then disable the **Track > Event** option.

To identify the firewall rule and disable the track events option:

1. Open the Cato Management Application and go to **Home > Events**.
2. Expand the **Rule** field under the **Fields** section.
3. Locate the firewall rule that generates the large number of events.

The following screenshot shows an example of a firewall rule (Allow all outbound) that generated 5.6 million events:

![blobid1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360012318178.png)
4. Go to **Security** > **WAN** or **Internet Firewall**, locate the rule (from the previous step) and edit the **Track** settings.
5. Disable the **Event** option for this rule.
6. Click **Apply** and then click **Save**.

#### IPS Events

If it is the IPS Engine blocking expected traffic, such as vulnerability scans, that is generating the large number of events, you can allowlist the source of the traffic as explained in [Allowlisting IPS Signatures](/v1/docs/allowlisting-ips-signatures)

To identify the source IP and allow list it:

1. Open the Cato Management Application and go to**Home > Events**.
2. Select the **IPS** preset
3. Expand the **Source IP** field under the **Fields** section and select the IP address with the highest amount of IPS events.
4. Click the **Signature ID** and configure the allowlist as convenient. Make sure that **Tracking** is disabled.
5. Click **Apply**

## **Cato Alerts Quota Exceeded**

An email will be sent to the customer's mailing list, under General Notification, when the number of alerts generated per hour exceed 50 for the account. Customer will received an email with the subject, "*Cato alerts* *Quota Exceeded*".

![Screenshot 2023-04-01 at 20.38.27.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13803238385949.png)

## Solution

1. Determine the alert quota exceeded email was generated for which Cato feature. For e.g, in the above Alert Quota Exceeded email, it was for IPS alerts.
2. Login to CMA to verify the authenticity of this alert
  - Go to Home > Events
  - Under Select Presets, select the IPS and customize the time period based on when the email was received. Since the threshold for generating the Alert Quota Exceeded email is 50 alerts **per hour**, customize the time period, starting from an hour before the email was received.![Screenshot 2023-04-01 at 21.28.17.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13803238387229.png)
3. Go through the events to determine the reason for the alert. For e.g., in the below screenshot, it can be observed that there were multiple events for a possible attack, and it was originating from the same source. ![Screenshot 2023-04-01 at 21.47.53.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13803238387613.png)
4. Investigate the events and take the necessary action.
5. If these alerts turns out to be false positive, contact Cato Support. To open a Support case, refer to [Submitting-a-Support-Ticket](/v1/docs/submitting-a-support-ticket).
6. If you do not wish to be notified of subsequent similar alerts, you can go to the respective rule or feature pertaining to this alert, and disable the email notification.
