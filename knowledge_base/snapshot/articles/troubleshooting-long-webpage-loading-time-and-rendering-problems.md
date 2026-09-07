---
title: "Troubleshooting Long Webpage Loading Time and Rendering Problems"
slug: "troubleshooting-long-webpage-loading-time-and-rendering-problems"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/troubleshooting-long-webpage-loading-time-and-rendering-problems"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Long Webpage Loading Time and Rendering Problems

## Issue

Web applications are among the most widely used applications today due to their accessibility, flexibility, and convenience. They can be accessed from any device with an internet connection, including desktop computers, laptops, tablets, and smartphones, making them ideal for users who are on the go or who work remotely.

A webpage rendering issue can lead to various problems, including slow webpage loading, incomplete webpage loading, or the webpage not loading at all. It's essential to troubleshoot and resolve rendering issues quickly to ensure that users can access web applications seamlessly. This article will discuss on some of the common causes of webpage rendering issue and how we can perform troubleshooting steps to further isolate the issue.

## Possible Causes

There are numerous reasons that the webpage failed to render or very slow in rendering. A few common ones are:

- Sub-Optimal Routing Path to Server
- Corrupted/Outdated Browser Cache and Cookies
- Server problems
- Broken links or missing resources
- Content blocking by ad blockers or firewalls

## Troubleshooting

## Sub-Optimal Routing Path to Server

Slow loading of the webpage can sometimes be due to sub-optimal routes to the web server. To ensure an optimal route between the site and the server, we can employ the following simple methods to verify latency. By conducting a ping test or traceroute, we can compare the results obtained when the connection passes through Cato, with the results obtained when bypassing Cato altogether.

**1. Ping** You can use the ping command to check if the web server is responding. If the server is reachable, you will receive a response from the server with the round trip time (RTT). If the RTT values are higher when the connection is going through Cato, then refer to [Higher Latency Going Through Cato](/v1/docs/troubleshooting-long-webpage-loading-time-and-rendering-problems#higher-latency-going-through-cato) for further troubleshooting.

![pingresponse.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10395960691101.jpeg)

**2. Traceroute** You can use the traceroute command to check the path the connection takes to the destination. The number of hops displayed in a traceroute is not the definitive factor for determining the speed of a connection. Instead, the Round-Trip Time (RTT) holds greater significance when evaluating connection speed.

The following example highlights this scenario: Although the number of hops in the network path decreases significantly when the connection goes through Cato, the Round-Trip Time (RTT) is unexpectedly higher compared to the result obtained when the connection is bypassed.

The below connection bypassed Cato:

![traceroute.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10979210932765.jpeg)

The below shows the same connection, but goes through Cato:

![traceroute1.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10979246241693.jpeg)

**NOTE**: When traversing through the Cato cloud, it is common to observe a reduction in the number of hops. This is because the internal hops within the Cato cloud infrastructure are not reflected in the traceroute results.

### Higher Latency Going Through Cato:

To address higher latency when the connection goes through Cato, it is essential to examine the following configurations:

#### Ensure Socket connects to Closest PoP

- In the CMA, go to Monitoring tab and then select the affected site
- On the right pane, under Recent Connections, click on View Log. It will open another pane with information on the connected PoP. ![connectedPoP.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11004929060125.jpeg)
- If it is not connected to a PoP closest to the site location, check if socket was manually configured to connect to a preferred PoP by navigating to Network > Sites > Sites Configuration > General > Preferred PoP Locations
- If it was incorrectly configured to the wrong PoP, then follow this [Defining-a-Preferred-PoP-for-a-Site](/v1/docs/defining-a-preferred-pop-for-a-site) to set it to the closet PoP, or set the Primary Location to Automatic (default) and the Socket will select and connect to the best PoP automatically.

#### Check For Any Egress or Backhaul Rules

- In the CMA, go to Network Rules and scan through the list to verify if there are any rules that pertains to the web server in question, and has Routing method configured.
- If there are any, review the configured egress PoP/Site and assess its proximity to the web server.
- If the PoP/Site is located far away from the web server, you have two options to optimize the configuration: -- Modify the existing network rule by removing the web server IP address from the rule. This change will (by default) allow the traffic to egress from the PoP that the socket is connected to. However, it's important to note that this may not always be ideal, as the directly connected PoP may not be in close proximity to the web server. -- Alternatively, create a new network rule specifically for the web server. In this new rule, configure the egress to a PoP/Site that is closer to the actual location of the web server. Refer to [How-to-Configure-an-Egress-Rule](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic) and [Configuring-Internet-Traffic-Backhauling](/v1/docs/configuring-internet-traffic-backhauling) for instructions in configuring an egress rule and Internet traffic backhauling respectively.

## Corrupted/Outdated Browser Cache and Cookie

Browser cache and cookie can sometimes lead to rendering issues on a web page if the cached resources are outdated or corrupted. This can happen when a web page's CSS or JavaScript file is updated, but the browser still uses the cached version, resulting in incorrect rendering or errors on the page. To confirm if this resolves the issue, user can try to access the page in incognito mode. If it works in incognito mode, users can clear their browser's cache and reload the page. Following are some of the ways to clear the browser cache and cookie for some of the commonly used browsers.

**Google Chrome:**

- Open Google Chrome and click on the three dots icon at the top right corner of the window.
- Click on "More tools" and then "Clear browsing data".
- Select the time range you want to clear, and check the boxes for "Cookies and other site data" and
- "Cached images and files".
- Click "Clear data".

**Mozilla Firefox:**

- Open Firefox and click on the three lines icon at the top right corner of the window.
- Click on "Settings" and then "Privacy & Security".
- Scroll down to the "Cookies and Site Data" section and click on "Clear Data".

**Apple Safari:**

- Open Safari and click on "Safari" in the menu bar at the top of the screen.
- Click on "Preferences" or "Settings" and then "Privacy".
- Click on "Manage Website Data".
- Click "Remove All" and then "Done".

**Microsoft Edge:**

- Open Microsoft Edge and click on the three dots icon at the top right corner of the window.
- Click on "Settings" and then "Privacy, search, and services".
- Click on "Choose what to clear" under the "Clear browsing data" section.
- Check the boxes for "Cookies and other site data" and "Cached images and files".
- Click "Clear now".

## Isolate Further by Following the Issue

In this section, we will explore troubleshooting techniques that involve isolating the problem to pinpoint its root cause. To help with this process, consider asking the following questions:

- **Is this happening only in China?**
- If the answer is 'Yes', refer to [China | Webpage Having Rendering Issues](/v1/docs/china-webpage-having-rendering-issues) to determine if this issue is caused by trackers or adware which are blocked by the GFW of China.
- **Is this issue only affecting a particular (group of) users?** If the answer is 'Yes', then we need to identify what is the difference between the device which this (group of) user(s) is using compared with the rest.
- **Is the issue occurring only on certain hours of the day?** If so, then we need to check on the bandwidth utilization and potentially packet loss during that period. If we do see packet loss during this period, refer to [How-to-Troubleshoot-Packet-Loss](/v1/docs/troubleshooting-socket-site-packet-loss) for more troubleshooting instructions.
- **Does the issue affect only a particular site?** If this is only affecting one site, then check for any firewall/network rules, which are sourcing from the affecting site. Examine those rules to verify if they could be contributing to the issue.
- **Does the issue only happen when connection is originating from a particular country?** If this also affects a particular country, then this is likely related to Geo blocking. Refer to [Website Inaccessible due to Cato IP Blacklisting or Geo-Blocking](/v1/docs/website-inaccessible-due-to-cato-ip-blacklisting-or-geo-blocking) for more details.
- **Does the issue only happen when connection is going through Cato?** If the answer is 'Yes', then this could be possibly be due to IP blacklisting. Refer to [Websites-Blacklisting-Cato-IP](/v1/docs/website-inaccessible-due-to-cato-ip-blacklisting-or-geo-blocking) for more details.
- **Does the issue happen only for a particular browser?** If so, this is likely due to corrupted cache and/or cookie. It can also be due to outdated browser. Try browsing in incognito mode and also update the browser if required.
- **Does the user need to click on "Proceed" before advancing to the website?** If a Cato prompt page appears and the webpage loads partially upon user clicking "Proceed", then this is a known limitation. Refer to [Websites-with-Prompt-Page-Don-t-Load-Properly](/v1/docs/websites-with-prompt-page-dont-load-properly) for more details on this limitation.

If you have reached this section of the article, it is likely that the rendering issue you are experiencing is complex and requires data collection for further analysis. HAR, or HTTP Archive, is a file format used to capture and record the interaction between a web browser and a website. The next step involves collecting HAR data while replicating the issue. This data will provide valuable insights for further analysis, helping to identify the potential causes of the rendering issue. Refer to [How-to-Collect-HAR-Data](/v1/docs/how-to-collect-har-data) for the instructions.

Once you have collected the HAR data, you can refer to [How to Use HAR File to Analyze Webpage Issues](/v1/docs/how-to-use-har-file-to-analyze-webpage-issues) for detailed steps on how to effectively analyze the collected HAR file. This guide will provide you with the necessary instructions to isolate and identify the specific issue causing the rendering problem.

## Cato Support

If the aforementioned steps did not help in identifying and resolving the webpage rendering issue, we kindly request your assistance in collecting the necessary data for further review by our Support team:

- Collect SSS. Please refer to [Support-Self-Service-SupportMe-Portal](/v1/docs/support-self-service-supportme-portal) for detailed instructions on how to collect and provide the necessary data for Support.
- Collect the HAR data while the issue is being replicated and upload to the Support Case. Refer to [How-to-Collect-HAR-Data](/v1/docs/how-to-collect-har-data) for detailed instructions.
