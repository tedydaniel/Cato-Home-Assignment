---
title: "China | Webpage Having Rendering Issues"
slug: "china-webpage-having-rendering-issues"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/china-webpage-having-rendering-issues"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# China | Webpage Having Rendering Issues

## Issue

This article highlights an issue primarily observed in China, stemming from the blocking measures enforced by the Great Firewall (GFW) of China. These measures could impact the complete rendering of certain webpages within the country. When a user in China tries to access a website, they might encounter one of two common issues. First, the webpage may keep loading indefinitely without fully displaying its content, leaving the user unable to access the complete page. Alternatively, the webpage may fail to load altogether, preventing the user from accessing any content on that particular website.

## Troubleshooting

While this article primarily discusses the ChromeRiver app, the insights and strategies discussed can be relevant and helpful for any websites experiencing similar symptoms.

The screenshot below illustrates an issue where the webpage exhibits symptom of continuous loading.

![chromeriver.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11138976558621.jpeg)

## Steps To Perform In Identifying The Problem:

The first step is to capture the HAR data using the developer tools available in commonly used browsers. For detailed instructions on how to capture HAR data in various browsers, please refer to [How to Collect HAR Data](/v1/docs/how-to-collect-har-data).

### Analyze The Captured HAR Data

1. Under the waterfall section (far most right column), we can identify which connection took the longest time to load. This can be easily identified as it will have the longest time bar as shown in the screenshot below. ![waterfall.bmp](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11161530234269.bmp)
2. By clicking on one of the connections, you can view the Request URL associated with it. In this case, Chromeriver directed the host to google-analytics.com, which serves as a tracker. However, due to China's blocking of Google, this connection remains in a constant state of loading.![referer.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11164256502941.jpeg)
3. Another instance of a prolonged loading connection can be observed with app.launchdarkly.com. A closer examination through nslookup reveals that this particular host is hosted on Fastly, a content delivery network that is also restricted by the Great Firewall (GFW) in China. Consequently, attempting to establish a connection with this host experiences persistent loading issues.![launchdark.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11164441352477.jpeg)

## Solution

Websites often contain hidden trackers and adware that can establish connections to URLs blocked by the Great Firewall (GFW). This can severely affect the normal rendering of webpages. To address this issue, we could employ the use of ad-blocker plugins or extension on the browser. Below are the suggested steps:

- Enable ad-blocker plugins or extension on your browser
- Add those identified domains into the block list.
- Examples of ad-blocker are UBlock Origin, AdBlock Plus, Ghostery, etc.

For general troubleshooting of webpage rendering problem, refer to [How to Troubleshoot Long Webpage Loading Time and Rendering Problems](/v1/docs/troubleshooting-long-webpage-loading-time-and-rendering-problems).

[waterfall.bmp](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/waterfall.bmp)
