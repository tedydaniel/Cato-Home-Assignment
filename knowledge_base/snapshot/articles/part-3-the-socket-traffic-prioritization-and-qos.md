---
title: "Part 3: The Socket Traffic Prioritization and QoS"
slug: "part-3-the-socket-traffic-prioritization-and-qos"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/part-3-the-socket-traffic-prioritization-and-qos"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Part 3: The Socket Traffic Prioritization and QoS

This article explains how the Cato QoS engine works and significantly helps you improve network bandwidth utilization and optimize the network performance.

## Managing Bandwidth with Cato QoS

In the Cato Management Application, use BW management profiles to configure the QoS priorities for the different traffic types. Each profile contains both the QoS priority and the traffic bandwidth limits. You can then assign the BW management profile to a network rule and prioritize the specific type of traffic.

You can set priority values between 2 to 255 where 0 and 1 are reserved for Cato administrative traffic and 255 is reserved as the lowest priority. If you configure the bandwidth profile with priority P10, the matching traffic has a higher priority over traffic with priority P20. You can provide a different priority to different applications and achieve the required performance for this type of traffic. We recommend that you assign a lower priority value to a more significant type of traffic. For example, if VoIP traffic is more important for your account than RDP, assign VoIP network rules a higher priority than RDP rules.

**Note:** If you configure a Remote Port Forwarding (RPF) for your account, the RPF traffic is assigned automatically with the lowest priority of 255. For more details on RPF, see [Configuring Remote Port Forwarding for the Account](/docs/part-3-the-socket-traffic-prioritization-and-qos#UUID-ee5b4f6d-76ad-fa7f-cf00-bf5a433c32ef).

## How Cato Sends Traffic Based on the BW Management Policy

Cato Networks uses a standard traffic shaping technique to optimize the network performance by controlling the **Upload** and **Download** average rate.

The following diagram shows how the QoS engine assigns priority to different traffic types.

| ![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248031156765.png) |
| --- |

### Implementing the BW Management Algorithm

Cato uses the Leaky Bucket algorithm to measure the limits of the bandwidth and burstiness. Implementing Leaky Bucket as a traffic shaper means that when the incoming packets rate is higher than the outgoing rate, like with network congestion, packets enter into the queue and are discarded once the queue is full. When packets are transmitted, they are removed from the queue, first-in first-out (FIFO) and new packets can then enter the queue.

#### Under the Hood - How the Traffic Is Sent According to the Priorities

The Leaky Bucket algorithm measures the traffic rate and identifies when the bucket is full. It uses these metrics to send the prioritized traffic using the example of water filling a bucket:

- **Average rate** - the actual BW limit. The rate of water that leaks from the bucket in every clock tick.
- **Burst capacity** - the bucket size. The total amount of water that the bucket can carry before it starts to discard packets.
- **Burst rate** – during a traffic burst, the rate that water is allowed into the bucket. The burst rate is not limited, and any burst can get into the bucket.

If the bucket is not full, all the packets are sent. However, when the priority for a bucket is full, new packets for that priority are queued and possibly discarded. Each priority has a different queue, and packets are sent by order (FIFO) according to the priorities. When all the queues are full, then all packets are discarded regardless of the priority. ​ However, Cato implements the Weighted Random Early Detection (WRED) to avoid discarding a massive number of packets. For TCP traffic, Cato discards the data packets and not the ACK packets in order to trigger the sender congestion algorithm. And in response, the sender reduces the rate at which it sends packets.

#### How the Traffic Is Sent from the Priority Queues

The Socket sends the packets from the priority queues in two iterations: hard limit iteration and the best effort iteration. The traffic shaper first sends the packets according to the configured BW limits and then make the best effort to send the remaining packets. During every 1ms tick, it performs both iterations:

1. Hard Limits Iteration – in this iteration the sequence is to evaluate each queue starting from the higher priority to the lower priority. For each priority queue, the Socket sends the packets according to their configured QoS limits. During this iteration, if the total BW limit of the link is exceeded, the Socket stops sending packets.
2. Best Effort Iteration – if the transmitted packets in the Hard Limits Iteration do not exceed the total bandwidth limit, then in this iteration the Socket evaluates each queue again. Starting from the higher priority to the lower priority, it sends the remaining packets. The motivation is to utilize the entire bandwidth of the link without exceeding the total BW limit.

#### Example of The Traffic Shaper Iterations

This section shows an example of how the Cato QoS engine prioritizes packets in the traffic queues.

**Five Priority Queues with Packets**

![qos_queues.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248008092189.png)

The diagram above shows the packets in 5 priority queues before the Socket starts the iterations.

**QoS – Hard Limits Iteration**

![QoS_hard_limits.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248008169117.png)

This diagram shows the first iteration, which is the Hard Limits Iteration. Starting from P10, P20, P30, P40 and at last P255. The available bandwidth for each queue is: two packets from P10 queue, one packet from P20, one packet from P30, two packets from P40 and one packet from P255 queue.

**QoS – Best Effort Iteration**

![qos_best_effort.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248055819549.png)

This diagram shows the second iteration, which is the Best Effort Iteration. In this iteration, three packets were sent from P10 , and one each from P20, P30, P40 and at last P255. In this case all the available bandwidth is used and one packet in the P255 queue remains for the next tick. Then, new packets arrive to the queues and the algorithm runs the two iterations again and sends the remaining packet.
