---
title: "Traffic Fails to Reach the Socket When Micro-Segmentation Is Enabled on Linux Hosts with Multiple Interfaces"
slug: "traffic-fails-to-reach-socket-when-micro-segmentation-enabled-linux-hosts"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/traffic-fails-to-reach-socket-when-micro-segmentation-enabled-linux-hosts"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Traffic Fails to Reach the Socket When Micro-Segmentation Is Enabled on Linux Hosts with Multiple Interfaces

## Issue

For Linux-based systems, enabling micro-segmentation does not create a route entry for the default gateway when there are already two default routes connected to two routers (one for local traffic and one for internet traffic).

## Troubleshooting

### Check the routing table

Check the routing table by running the command **route -n**

```plaintext
Destination    Gateway      Genmask         Flags Metric Ref Use Iface
0.0.0.0        10.40.0.254  0.0.0.0         UG    202    0   0   eth0
0.0.0.0        192.168.2.1  0.0.0.0         UG    1024   0   0   eth1
10.10.0.0      10.40.0.254  255.255.0.0     UG    0      0   0   eth0
10.30.0.0      10.40.0.254  255.255.0.0     UG    0      0   0   eth0
10.40.0.0      0.0.0.0      255.255.0.0     U     202    0   0   eth0
10.52.0.0      10.40.0.254  255.255.0.0     UG    0      0   0   eth0
10.53.0.0      10.40.0.254  255.255.0.0     UG    0      0   0   eth0
52.214.167.240 10.40.0.254  255.255.255.255 UGH   0      0   0   eth0
172.17.10.41   10.40.0.254  255.255.255.255 UGH   0      0   0   eth0
192.168.2.1    0.0.0.0      255.255.255.255 UH    1024   0   0   eth1
```

In the example above, we can see that the gateway to 192.168.2.1 is 0.0.0.0, indicating that there is a default route via eth1 specifically for that IP. However, since the gateway is not in the same subnet, the first default route will be chosen instead of the correct one, causing traffic to be sent via eth0 due to a lower metric.

## Solution

Add a manual route with the missing subnet by running the following command

```plaintext
ip route add <IP/CIDR> dev <interface>
```

For example: **ip route add 192.168.2.0/24 dev eth1**

Once done, check the routing table to confirm the route was added.

```plaintext
Destination    Gateway     Genmask         Flags Metric Ref Use Iface
0.0.0.0        10.40.0.254 0.0.0.0         UG    202    0    0  eth0
0.0.0.0        192.168.2.1 0.0.0.0         UG    1024   0    0  eth1
10.10.0.0      10.40.0.254 255.255.0.0     UG    0      0    0  eth0
10.30.0.0      10.40.0.254 255.255.0.0     UG    0      0    0  eth0
10.40.0.0      0.0.0.0 255.255.0.0         U     202    0    0  eth0
10.52.0.0      10.40.0.254 255.255.0.0     UG    0      0    0  eth0
10.53.0.0      10.40.0.254 255.255.0.0     UG    0      0    0  eth0
52.214.167.240 10.40.0.254 255.255.255.255 UGH   0      0    0  eth0
172.17.10.41   10.40.0.254 255.255.255.255 UGH   0      0    0  eth0
192.168.2.0    0.0.0.0     255.255.255.0   U     0      0    0  eth1
192.168.2.1    0.0.0.0     255.255.255.255 UH    1024   0    0  eth1
```
