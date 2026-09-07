---
title: "Best Practices to Measure Last-Mile Performance"
slug: "best-practices-to-measure-last-mile-performance"
tags: ["Best Practices"]
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/best-practices-to-measure-last-mile-performance"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices to Measure Last-Mile Performance

This article discusses the best practices to measure the last-mile performance of the Cato Cloud compared to the public Internet, as well as considerations when analyzing the results. There can be many reasons for different performance test results, as discussed below.

## Preparing for Performance Test

- Network congestion is an integral aspect of any performance test. Review your bandwidth management profiles to minimize th impact of link congestion on the performance test. For more information, see [What are the Cato Bandwidth Management Profiles](/v1/docs/what-are-the-cato-bandwidth-management-profiles)
- Make sure the bandwidth setting is configured according to the terms of your Cato site license. If the Cato site license has a higher bandwidth value than the ISP link bandwidth, set each link’s bandwidth according to the ISP bandwidth. For more about Cato site licenses, see [Working with Cato License Types](/v1/docs/working-with-cato-license-types).

Reformat the following items:

- Speed tests are influenced by the hardware on which you run the test, and the method by which the speed test is run. Speed tests, especially when run from a browser instead of a dedicated app, can utilize a high percentage of the CPU. Oftentimes, poor results are due to underpowered hardware, not any underlying network condition.
- Speed tests rely on third-party servers and networks which measure throughput in different ways. Results are dependent on the testing method. Cato recommends that you use the speed test provided in the Socket WebUI as directed [here](/v1/docs/troubleshooting-socket-site-packet-loss#14-testing-the-link-with-iperf).
- There are a variety of reasons why speed test results using Cato might be lower than a test bypassing Cato. For example, the DTLS tunnel adds overhead and reduces throughput. In addition, bandwidth management also needs to be considered. The Cato license alone should not be considered the only possible limiting factor.

## Running the Performance Test

- We recommend that you run your tests from WebUI and not through external 3rd-party entities. As mentioned above, hardware configuration can influence speed tests, which could lead to bad results. In addition, when using 3rd-party entities, you might have inconsistent results.
- Traffic that bypasses the Cato Cloud will have different results from traffic that traverses the Cato Cloud.
