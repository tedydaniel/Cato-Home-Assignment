---
title: "VoIP Troubleshooting"
slug: "voip-troubleshooting"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/voip-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VoIP Troubleshooting

## Overview

This playbook provides a troubleshooting guide for common VoIP issues. It covers symptoms like phone registration problems and poor call quality, offering insights into potential causes such as network connectivity issues and misconfigurations. The troubleshooting steps outlined here aim to help users isolate and resolve these issues.

## Symptoms

- Phone Registration issue
- Cannot make outgoing calls
- Poor call quality (Dropped calls, One-way audio, Jittery, Call distortion)

## Possible Causes

- Network connectivity problem
- Misconfiguration
- Packet loss
- Hardware malfunctions
- Phone account not configured on SIP server
- Wrong username/password entered on the phone (401 Unauthorized)

## Troubleshooting the Issue

This section will delve into the step-by-step troubleshooting instructions to address previously mentioned symptoms.

### Phones Cannot Register Successfully with the VoIP Server

Before delving into the steps for troubleshooting the VoIP registration issue, the below illustrates the flows between the IP phone and the SIP server during successful registration (4-step process). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17711791172765.png)

1. The phone sends a register request to the SIP server.
2. The server responds with a 401 Unauthorized message prompting the phone for authentication.
3. The phone sends another registration request that includes login credentials.
4. If registration is successful, the server responds with a 200 OK message.

This is how it looks like in a packet capture for VoIP registration.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17712094847517.png)

Now that we understand how phone registration works, let's explore the troubleshooting steps below to isolate registration issues further.

#### Name resolution of VoIP server

Verify the connectivity and resolution of the VoIP server configured on the phone.

- First, validate that the DNS server configured on the IP phone is correct.
- Next, note down the FQDN or IP address of the VoIP server configured on the phone
- From a device that is sitting on the same LAN as the VoIP Phone and configured with the same DNS server:
  - Use **nslookup** to check if the server's FQDN is resolvable.
  - **Ping** the server's FQDN/IP address
- Refer to the [Resolving DNS Issue](/v1/docs/voip-troubleshooting#resolving-dns-issue) section for detailed steps to resolve this.

#### DHCP Options

- In certain deployments, the IP phone must download configuration files from its TFTP Server before registration. This is done through the DHCP options. Validate whether the VoIP phone uses specific DHCP options to ensure it has the necessary network information for registration and operation on the network. This could involve **options 66 and 150** (TFTP server information) or **option 43** (TFTP, call server, Layer 2, and DSCP priority). If needed, contact the VoIP vendor for additional information.
- See [Resolving DHCP Option Issue](/v1/docs/voip-troubleshooting#resolving-dhcp-option-issue) for instructions on configuring the DHCP option if required.

#### Blocked SIP Traffic

- Ensure the SIP ports (UDP/5060 and UDP/5080) are not blocked. In the CMA, under Home > Events, set the filter to Destination Port in 5060,5080 and the Action is Block. Ideally, you should not see any block events. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17626432932253.png)
- Validate if Cato blocks the VoIP traffic for any reason. In the CMA, under Home > Events, set the filter to "Category is Voip Video" and "Action is Block." ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17629154293661.png)
- Perform [packet capture](/v1/docs/how-to-capture-traffic-on-a-socket) on the LAN side of the socket. The below PCAP shows the unidirectional flow from the IP phone to the SIP server. No response was seen from the SIP server back to the IP phone, suggesting that it is either a routing issue, SIP service is not enabled on the destination server, or a Firewall blocks the connection (WAN/Internet). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17712750160541.png)
- To resolve this issue, review the WAN/Internet Firewall rules that may be blocking the SIP traffic and make any necessary adjustments.
- If there are no block events observed on the CMA, then check the network to identify any devices that might be blocking this connection

#### Wrong username/password entered on the phone (401 Unauthorized)

- If a phone fails to register and repeatedly receives 401 Unauthorized messages from the server without ever receiving a 200 OK response, it suggests that the phone account may not be correctly configured on the SIP server or that the username and password entered on the phone are incorrect (see above registration flow).
- The PCAP below shows the 401 unauthorized access from the SIP server. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17712094862237.png)
- See [Resolving 401 Unauthorized](/v1/docs/voip-troubleshooting#resolving-401-unauthorized) on how to prevent this from happening.

#### Encrypted SIP

- If TCP/5061 is used, it is likely that the SIP is encrypted through TLS. In such cases, ensure that the TLS inspection is bypassed for the SIP server.
- Go to [Resolving Encrypted SIP](/v1/docs/voip-troubleshooting#resolving-encrypted-sip) to learn how to resolve this.

### Cannot Make Outgoing Calls

#### IP Fragmentation

- Validate that phones are registered on the SIP Server and that SIP invite logs are present on both the phones and the SIP server.
- Attempt a phone call and perform a packet capture (PCAP) to analyze the traffic on the phone, server, and network devices. Specifically, look for **SIP_INVITE** messages.
- Identify whether SIP UDP packets are being fragmented by the network and ensure that the fragments are being received by both the phones and the SIP server. Note that by default, Cato allows fragmentation at the PoP level, which is the desired behavior.

#### Egress IP

- Having a different egress IP for the SIP traffic can cause unexpected issues, such as being unable to make outgoing calls or having calls dropped. Network rules for SIP should be configured to egress to a single egress IP.
- Verify the Routing Method for the VoIP traffic on the network rule and ensure that **1, and only1 egress IP** is used. The below shows 2 egress IP addresses. Although it provides redundancy, it will cause issues if the SIP flow is NATTED using a different IP address. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17711482397085.png)
- To confirm if this is causing the issue, perform PCAP capture to analyze the traffic on the phone, SIP server, and network device (look for SIP_REGISTER messages).
- As long as the server responds, you can verify the Cato egress IP in the Via section of the Message Header in packets sent by the server. The Received IP is the Cato egress IP, and RPort is the NAT source port of outbound packets from the PoP. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17713025053597.png)
- For best practice, configure only **1 egress IP** on the network rule for VoIP traffic when the SIP server is reachable via the Internet. This can be achieved by using the NAT option. Refer to [Allocating-IP-Addresses-for-the-Account](/v1/docs/allocating-ip-addresses-for-the-account) on how to allocate a public IP for your account.
- Additional configuration must be configured in Advance Configurations to ensure that only 1 egress IP is used for VoIP traffic. For more details, refer to [Resolving Not Able To Make Outgoing Calls/Call Drop/One-way Voice](/v1/docs/voip-troubleshooting#resolving-not-able-to-make-outgoing-callscall-droponeway-voice).

### Poor Call Quality

Poor call quality is commonly caused by packet loss or discards, high latency, or jitter over the Cato tunnel. This section will discuss how to isolate further whether the issue is related to Cato or potentially a misconfiguration.

#### Packet Loss

- Check in the Network Analytics for packet loss in upstream and downstream traffic. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17629168777757.png)
- If packet loss coincides with last-mile packet loss, it suggests an ISP issue or possibly a faulty WAN cable. This would affect all traffic. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17629154332957.png)For detailed troubleshooting for packet loss - How-to-Troubleshoot-Packet-Loss

#### Discarded Packets

- If we see a high percentage of Discard packets in Network Analytics, this would be due to a QoS-related issue and possible network congestion. Go to Network > Priority Analyzer to validate which class is discarding packets. Expand the Class (click on the + icon to expand) and check the Top Apps for VoIP traffic to verify if the VoIP traffic is in the same class.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17639810640029.png)
- Refer to the [Resolving Packet Discards (QoS)](/v1/docs/voip-troubleshooting#resolving-packet-discards-qos) section for instructions on assigning VoIP to the highest priority class.

#### High Latency/Jitter

- For Jitterring and Delay, check [Network Analytics](/v1/docs/analyzing-data-for-a-site-in-real-time) to identify any high latency or jitter over the Cato tunnel. Perform a PCAP as required. [ITU-T G.114](https://www.itu.int/rec/T-REC-G.114) recommends less than 150ms of one-way latency for VoIP.
- If high latency is observed, ensure the Socket is connected to an [optimal PoP](/v1/docs/voip-troubleshooting#resolving-suboptimal-pop).
- If high jitter is observed, [QoS and BW Management](/v1/docs/configuring-bandwidth-management-profiles) may also be considered/reviewed to resolve this issue by assigning VoIP traffic to the highest priority class.

### One-Way Voice

- For one-way sound encountered, perform a PCAP of the Call and identify the IP/ports used. SIP ALG may need to be enabled or disabled, depending on the VoIP vendor's requirements.
- SIP ALG translates the phone/PBX private IP address to the Cato public IP address (and vice versa) in the plaintext SIP message after Cato performs NAT. SIP ALG is disabled by default at Cato. If you need more details, contact the VoIP vendor.
- Refer to [Resolving Not Able To Make Outgoing Calls/Call Drop/One-way Voice](/v1/docs/voip-troubleshooting#resolving-not-able-to-make-outgoing-callscall-droponeway-voice) for instructions on enabling ALG in Advance Configuration.

## Resolving Discovered Issues

#### Resolving DNS Issue

- If the VoIP server's FQDN failed to resolve successfully, validate that the server's FQDN is correct.
- If the VoIP server's FQDN is correct, verify that the DNS settings are correct. For Instructions on setting up DNS in Cato, refer to [Configuring-DNS-Settings](/v1/docs/configuring-dns-settings).
- Ping directly to the server using its IP address
- If pinging the VoIP server IP fails, validate connectivity by checking cables and WiFi settings.
- Verify that the server allows ICMP ping through the Firewall
- Ensure that the server is up and running
- Perform a traceroute and see where it fails.

#### Resolving DHCP Option Issue

- If a specific DHCP option is required for the VoIP phone to connect to download configurations, the DHCP option can be configured in *Network > DHCP > DHCP Options*. To configure DHCP options for Groups, refer to [Configuring DHCP Group Options](/v1/docs/configuring-dhcp-settings). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17645424870429.png)

#### Resolving Packet Discards (QoS)

- Always ensure that VoIP has the highest priority for bandwidth management (QoS) because low-priority traffic will be dropped when congestion happens.
- Navigate to *Network > Bandwidth Management.* By default, VoIP is classified as a P10 priority. If you have defined other higher-priority classes (less than P10), consider moving the VoIP to the highest-priority class to avoid drops during network congestions.
- [Configuring-Bandwidth-Management-Profiles](/v1/docs/configuring-bandwidth-management-profiles) provides details on how to set up Bandwidth Management in Cato.

#### Resolving Packet Loss

- If last-mile packet loss is present, replace the cable connected to the socket's WAN port. If that doesn't solve the issue, contact your Internet provider to isolate the problem further.
- High socket utilization can result in packet loss. If a constant high CPU is observed while packet loss occurs in the network, please [Contact Support](/v1/docs/submitting-a-support-ticket).
- If high packet loss is observed in VoIP traffic, consider enabling packet loss mitigation. For details, refer to [Optimizing Traffic](/v1/docs/accelerating-and-optimizing-traffic). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17645400451229.png)

#### Resolving Encrypted SIP

- Apply a [TLSi bypass rule](/v1/docs/configuring-tls-inspection-policy-for-the-account) to prevent TLSi from inspecting VoIP traffic if TCP/5061 is used.

#### Resolving 401 Unauthorized

- Successful registration of IP phones depends on accurate configurations for both the server and the client, which are the SIP server and the IP phone, respectively. Hence, the correct entry of both the SIP URI and the password is essential for successful service registration. Validate that these are configured correctly on the VoIP phones.

#### Resolving Not Able To Make Outgoing Calls/Call Drop/One-way Voice

- If an Egress IP is selected, make sure that the Preferred IP for SIP Traffic setting under Resources > Advance Configuration is enabled. When enabled, SIP traffic always egresses from the same IP address to avoid temporary NATTed to different egress IPs, preventing potential issues. If the egress IP is unavailable (e.g., during PoP maintenance), packets are dropped. Make sure that IP Phones are reset after making this change. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17711568197021.png)
- If the VoIP protocol is not SIP, please [Contact Support](/v1/docs/submitting-a-support-ticket) to apply backend changes to force traffic to stay on the egress IP.
- If SIP ALG is required, enable it under *Resources >* [*Advanced Configuration*](/v1/docs/working-with-advanced-configuration-for-the-account)*.* ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17714892723997.png)

#### Resolving Sub-Optimal PoP

- Ensure you are connected to the closest PoP. Navigate to Network > Site > Snapshot. Under the Device Overview, you will see the Link's ISP and the connection PoP.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17640279809181.png)
- If the device is not connected to an optimal PoP, verify if the "Preferred POP locations" setting is configured. To do this, navigate to *Network > Site > Site Configurations > General > Preferred POP locations*. If the setting was set incorrectly, select the optimal location.

## Raising cases to Cato Support

If the above steps did not help isolate and resolve the issue, please open a case with [Cato Support](/v1/docs/submitting-a-support-ticket). When opening a case, consider the following questions and provide the corresponding answers:

- Do you have a cloud-based VoIP provider or is your phone system on-premises?
  - If cloud-based:
    - Where are the affected phones located (which Cato site)?
    - Who is the VoIP provider?
    - What is the IP address or URL of the phone registration server?
  - If on-premises:
    - Where are the affected phones located (which Cato site)?
    - What is the IP address of the phone registration server?
- What is the issue? Are the phones registering successfully? Are there any audio issues?
- If this is an audio problem:
  - Do both sides hear a ringtone?
  - Do both sides hear audio?
  - Are there call quality issues (choppy audio)?
- Are calls disconnected prematurely?
  - Do calls disconnect after a specific amount of time on the call?
  - Did calls get disconnected at a specific time?
