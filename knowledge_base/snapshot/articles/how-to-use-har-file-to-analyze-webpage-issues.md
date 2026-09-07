---
title: "How to Use HAR File to Analyze Webpage Issues"
slug: "how-to-use-har-file-to-analyze-webpage-issues"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-use-har-file-to-analyze-webpage-issues"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Use HAR File to Analyze Webpage Issues

## Overview

A webpage rendering issue occurs when a webpage fails to display or function correctly on a user's device. This issue can manifest in various ways, such as incomplete or distorted images, broken layout, slow loading times, or unresponsive features. The cause of these issues may stem from various factors.

HTTP Archive (HAR) is a tool that can help diagnose and resolve webpage rendering issues. HAR allows network administrators to capture and analyze network traffic data, including requests, responses, and timings, generated when a user accesses a webpage. This data can provide insights into how a webpage is loading and performing, identify any bottlenecks or errors, and help pinpoint the root cause of rendering issues.

This article will discuss on how we can use HAR data to troubleshoot webpage rendering issue.

## Environment

HAR data is required.

## Instructions

Collect the HAR data while replicating the issue. For instructions on how to collect HAR data, refer to [this article](/v1/docs/how-to-collect-har-data). We will look at how to make use of the collected HAR data to reveal issues by looking at the HTTP status codes as well as the response time of the HTTP requests.

## HTTP Status Codes

HTTP status codes provide information about the status of a client's request to a server, helping to diagnose and troubleshoot any issues that may arise during the communication process. Below are the common HTTP status codes and what they mean. Refer to [HTTP/1.1 Status Code Definition](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes) page for the details.

- 200 - Success
- 404 - Page not found / Bad Request
- 401 - Unauthorized
- 403 - Forbidden
- 304 - Not Modified (Content is cached)
- 500 - Internal Server Error

### Steps

1. Load the collected HAR data into [Google HAR analyzer](https://toolbox.googleapps.com/apps/har_analyzer/)
2. Filter the requests by HTTP status codes. **Example** Below shows a HAR file which was loaded to the Google HAR analyzer. This connection is an attempt to browse Facebook in which the content didn't load correctly. Filtering by non-successful (non-2xx) HTTP status codes, we can see that there are many 403 (forbidden) responses for the domain name x.x.fbcdn.net (marked in yellow). The next step would then to investigate further why these request are forbidden. ![har-status-code.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10066686248477.jpeg)
3. For country where access to Google is restricted (for e.g. China), accessing [Google HAR analyzer](https://toolbox.googleapps.com/apps/har_analyzer/) is not possible. In this case, you can load the HAR data in the same developer tool in which the data was collected, and you can then sort by the HTTP status code in descending order. ![har-sort.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10067829910429.jpeg)

## Long Webpage Load Time

One of the most prevalent issues encountered with web applications is their slow webpage loading or, in some cases, failure to load the webpage altogether. By utilizing the collected HAR data, we can delve into the details of each request and identify which ones are experiencing significant delays in loading. It's possible that certain requests may be stuck in a perpetual loading state, contributing to the overall slowness of the application. Analyzing the HAR data allows us to pinpoint these problematic requests and take appropriate measures to address them.

### Steps

1. Load the collected HAR data into [Google HAR analyzer](https://toolbox.googleapps.com/apps/har_analyzer/)
2. Click on the delay responding request (typically the longest bar viewing the total time)
3. Check what is the main contributor towards the delay (Blocking, Waiting or Receiving) Important Timing fields **Blocked time** - Time the request spent waiting before it could be sent by the browser. **Wait time** - Amount of time waiting for the Server to respond. If this value is high, it could mean that the server is busy or suffering a performance issue. Below we can see that there is around 5 seconds wait time from the server: ![har-longpageload.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10165460865821.jpeg)**Receive time** - This one is the amount of time used for the server to transfer the required information to the client. Typically this is the where we detect is a network issue. **NOTE**: The timing field is also available when using the developer's tool in Chrome, providing a similar breakdown of timing phases. For a detailed explanation of the timing breakdown phases, please refer to the [timing-preview](https://developer.chrome.com/docs/devtools/network/reference/?utm_source=devtools#timing-preview).
4. For country where access to Google is restricted (for e.g. China), access [Google HAR analyzer](https://toolbox.googleapps.com/apps/har_analyzer/) will not be possible. In this case, you can load the HAR data in the same developer tool in which the data was collected.
5. The analysis would be similar to step 2 where we focus on identifying connections with the longest response times. To illustrate, in the screenshot provided below, under the Overview Section, we can observe several connections that are experiencing significant delays in loading. By highlighting these connections within the Overview Section, we can identify some requests take more than 30 seconds to load. Selecting one of these connections reveals that it is a request to app.launchdarkly.com. ![har-longpageload.-1jpg.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10167339289885.jpeg)
6. Once the requests that experience long loading times have been identified, further investigation can be carried out to find out the underlying cause of the delay. One potential factor to explore is the presence of on-premise firewalls that might be blocking these requests.
7. In certain regions, such as **China**, it is a *known issue* that some long-pending requests within applications may be attributed to embedded trackers. For more details, refer to [China | Webpage Having Rendering Issues](https://support.catonetworks.com/knowledge/editor/01H165QP7MGBDRA8W4BDS28YQE/en-us?brand_id=1168669).
