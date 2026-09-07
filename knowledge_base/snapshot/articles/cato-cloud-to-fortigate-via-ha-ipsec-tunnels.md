---
title: "Cato Cloud to FortiGate via HA IPSec Tunnels"
slug: "cato-cloud-to-fortigate-via-ha-ipsec-tunnels"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/cato-cloud-to-fortigate-via-ha-ipsec-tunnels"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Cloud to FortiGate via HA IPSec Tunnels

This article discusses how to connect an IPsec site with FortiGate devices in a High Availability (HA) configuration to the Cato Cloud.

## Overview of Cato to FortiGate VPN with IPsec Sites

This article assumes that you are working in an environment with a FortiGate connected to the Internet with two WAN links that we are going to build the IPsec connections to two Cato PoPs.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247862096285.png)

The Cato PoP IP can be obtained by allocating a new IP address (or using an old one) from the Cato Management Application in Network > IP Allocations. We recommend that you choose the primary IP for the PoP location that is closest to the site and the secondary IP from a different PoP location.

**Note:** This configuration in this article was tested with firmware version 7.0.8.

## IKEv2 with Cato-initiated Site - Configuring the FortiGate Appliance (CLI)

This section explains how to configure the FortiGate appliance for a Cato IPsec IKEv2 site with Cato-initiated routing.

Please connect with SSH to your FortiGate appliance with an administrator account.

**To configure the FortiGate appliance to connect to an IKEv2 Cato-initiated site:**

1. Enter the settings to define IPsec phase 1:

```plaintext
config vpn ipsec phase1-interface
    edit “CATO_IPSECV2-1” #[Primary VPN Name]
        set interface "wan1"  #[Local FGT site network WAN interface]
        set ike-version 2
        set keylife 19800
        set peertype any
        set net-device disable
        set proposal aes256gcm-prfsha512
        set comments “Primary VPN To CATO Cloud XCATD01”
        set dhgrp 16
        set remote-gw #[Cato POP 1 IP]
        set psksecret  #[Primary Cato configured PSK]
    next
end

config vpn ipsec phase1-interface
    edit “CATO_IPSECV2-2” #[Secondary VPN Name]
        set interface "wan2" #[Secondary FGT site network WAN interface – if not available use the same WAN interface]
        set ike-version 2
        set keylife 19800
        set peertype any
        set net-device disable
        set proposal aes256gcm-prfsha512
        set comments “Secondary VPN To CATO Cloud XCATD01”
        set dhgrp 16
        set remote-gw #[Cato POP 2 IP]
        set psksecret #[Primary Cato configured PSK]
     next
end
```
2. Enter the settings to define IPsec phase 2:

```plaintext
config vpn ipsec phase2-interface
    edit "CATO_IPSECV2-1" #[VPN phase 2 Name]
        set phase1name "CATO_IPSECV2-1" #[VPN phase 1 Name]
        set proposal aes256gcm
        set dhgrp 16
        set keylifeseconds 3600
    next
    edit "CATO_IPSECV2-2” #[VPN phase 2 Name]
        set phase1name "CATO_IPSECV2-2” #[VPN phase 1 Name]
        set proposal aes256gcm
        set dhgrp 16
        set keylifeseconds 3600
    next
end
```
3. Route the traffic though the VPN tunnel to the Cato Cloud.

You can do this with static routing or dynamically using BGP. In this example we are using static routing.

```plaintext
config router static
   edit #[Local FGT unique route ID]
        set dst 172.101.0.0 255.255.255.0 #[Remote CATO Networks subnet]
        set distance 1
        set device "CATO_IPSECV2-1"
    next
   edit #[Local FGT unique route ID]
        set dst 172.101.0.0 255.255.255.0 #[Remote CATO Networks subnet]
        set priority 10
        set distance 1
        set device "CATO_IPSECV2-2”
    next
    edit #[Local FGT unique route ID]
        set dst 172.101.0.0 255.255.255.0 #[otherwise send to black hole - Remote CATO Networks subnet]
        set blackhole enable
        set distance 254
    next
end
```
4. **(Optional)** Create a zone, which makes it easier when creating a new rule or if you need to change the VPN names.

```plaintext
config system zone
    edit "Cato-Cloud-S2S" #[Zone name]
        set intrazone allow
        set interface "CATO_IPSECV2-1" "CATO_IPSECV2-2" #[the 2 IPSEC VPN’s]
    next
```

**WARNING!** This zone configuration might cause issues on some versions of FortiOS operating system.
5. Configure the firewall policy with rules that allow traffic inside the tunnel.

```plaintext
config firewall policy
    edit #[Local FGT rule ID]
        set name “CATO Firewall”
        set srcintf "Virtual Lan" #[Local FGT site network interface]
        set dstintf "Cato-Cloud-S2S"#[Remote CATO Networks VPN zone or VPN interfaces]
        set action accept
        set srcaddr "all" #[Best practice – filter by local address / group]
        set dstaddr "all" #[Best practice – filter by CATO address / group]
        set schedule "always"
        set service "ALL"
    next
end
```

## IKEv1 Aggressive (Firewall Initiated) Site - Configuring the FortiGate Appliance (CLI)

This section explains how to configure the FortiGate appliance for a Cato IPsec IKEv1 site where the routing is started by the FortiGate appliance to support dynamic public IP address for WAN traffic.

**Note:** This configuration in this article was tested with firmware version 7.0.8.

**To configure the FortiGate appliance to connect to an IKEv1 Firewall-initiated site:**

1. Enter the settings to define IPsec phase 1:

```plaintext
config vpn ipsec phase1-interface
edit "CATO_Cloud_M1" #[Primary VPN Name]
        set interface "wan1" #[Local FGT site network WAN interface]
        set keylife 19800
        set mode aggressive
        set peertype any
        set net-device disable
        set proposal aes256-sha512
        set localid "<site_name>.<acc_name>" #[Set the local ID - You can get that from Site Configuration -> IPsec menu]
        set dhgrp 16
        set remote-gw  #[Cato pop primary IP]
        set psksecret #[Primary Cato configured PSK]
next
edit "CATO_Cloud_M2" #[Secondary VPN Name]
        set interface "wan2" #[Secondary FGT site network WAN interface – if not available use the same WAN interface]
        set keylife 19800
        set mode aggressive
        set peertype any
        set net-device disable
        set proposal aes256-sha512
        set localid "<site_name>.<acc_name>" #[Set the local ID - You can get that from Site Configuration -> IPsec menu]
        set dhgrp 16
        set remote-gw  #[Cato pop secondary IP]
        set psksecret #[Secondary Cato configured PSK]
next
```
2. Enter the settings to define IPsec phase 2:

```plaintext
config vpn ipsec phase2-interface
    edit "CATO_Cloud_M1" #[VPN phase 2 Name]
        set phase1name "CATO_Cloud_M1" #[VPN phase 1 Name]
        set proposal aes256-sha256
        set dhgrp 16
        set auto-negotiate enable
        set comments "Phase2"
        set keylifeseconds 3600
    next
    edit "CATO_Cloud_M2" #[VPN phase 2 Name]
        set phase1name "CATO_Cloud_M2" #[VPN phase 1 Name]
        set proposal aes256-sha256
        set dhgrp 16
        set auto-negotiate enable
        set comments "Phase2"
        set keylifeseconds 3600
    next
```
3. Route the traffic though the VPN tunnel to the Cato Cloud.

You can do this with static routing or dynamically using BGP. In this example we are using static routing.

```plaintext
edit #[Local FGT unique route ID]
        set dst 10.254.254.0 255.255.255.0  #[Remote CATO Networks subnet]
        set distance 1
        set device "CATO_Cloud_M1"

next
edit #[Local FGT unique route ID]
        set dst 10.254.254.0 255.255.255.0  #[Remote CATO Networks subnet]
        set distance 1
        set priority 20 #[this will be the backup connection so a higher priority is needed]
        set device "CATO_Cloud_M2"
next
edit #[Local FGT unique route ID]
        set dst 10.254.254.0 255.255.255.0 #[otherwise send to black hole - Remote CATO Networks]
        set blackhole enable
        set distance 254    
next
```
4. **(Optional)** Create a zone, which makes it easier when creating a new rule or if you need to change the VPN names.

```plaintext
config system zone
    edit "Cato-Cloud-Dial-up" #[Zone name]
        set intrazone allow
        set interface " CATO_Cloud_M1" " CATO_Cloud_M2" #[the 2 IPSEC VPN’s]
    next
```

**WARNING!** This zone configuration might cause issues on some versions of FortiOS operating system.
5. Configure the firewall policy with rules that allow traffic inside the tunnel.

```plaintext
config firewall policy
    edit #[Local FGT rule ID]
        set name “CATO Firewall”
        set srcintf "Virtual Lan" #[Local FGT site network interface or interfaces]
        set dstintf "Cato-Cloud-Dial-up"#[Remote CATO Networks VPN zone or VPN interfaces]
        set action accept
        set srcaddr "all" #[Best practice – filter by local address / group]
        set dstaddr "all" #[Best practice – filter by CATO address / group]
        set schedule "always"
        set service "ALL"
    next
end
```

## IKEv1 Site - Configuring FortiOS VS 3 (CLI)

This section explains how to configure FortiOS VS3 for a Cato IPsec IKEv1 site to support dynamic public IP address for WAN traffic.

**To configure a FortiOS VS 3 to connect to an IPsec IKEv1 site:**

1. Enter the settings to define IPsec phase 1:

```plaintext
config vpn ipsec phase1
    edit "Cato"
        set interface "wan1"
        set localid "<site_name>.<acc_name>" #[Set the local ID - You can get that from Site Configuration -> IPsec menu] 
        set nattraversal enable
        set proposal aes256-sha1
        set keylife 86400
        set mode aggressive
        set add-gw-route enable
        set remote-gw <ip> #[Cato PoP secondary IP]
        set psksecret #[Primary Cato configured PSK]
     next
end
```
2. Enter the settings to define IPsec phase 2:

```plaintext
config vpn ipsec phase2
    edit "Cato"
        set keepalive enable
        set pfs enable
        set phase1name "Cato"
        set proposal aes256-sha1
        set replay enable
        set keylifeseconds 3600
        set src-subnet 10.230.230.0 255.255.255.0
    next
```
3. Configure the firewall rule:

```plaintext
    edit <name> #[the firewall rule name]
        set srcintf "internal"
        set dstintf "wan1"
            set srcaddr "all"
            set dstaddr "all"
        set action ipsec
        set schedule "always"
            set service "ANY"
        set logtraffic enable
        set inbound enable
        set outbound enable
        set vpntunnel "Cato"
   next
```
4. Configure the routing for the site:

```plaintext
config router static
     edit X
        set device "Cato” #[the ipsec name]
        set dst 10.230.230.0 255.255.255.0 #[Remote CATO Networks subnet]
        next
end
config router static
    edit Y
        set blackhole enable
        set dst 10.230.230.0 255.255.255.0 #[Remote CATO Networks subnet] 
        set distance 254
    next 
end
```

## IKEv2 Site – Configuring Cato IPsec IKEv2 Responder-Only with FortiGate

This section explains how to configure FortiOS for a Cato IPsec IKEv2 responder-only site to support dynamic public IP address for WAN traffic. This part of the article explains a route based VPN configuration.

This configuration was tested on FortiOS 6.0.X and on FortiOS 7.0.X.

First thing to do is to create the IKEv2 site in the CMA and in the IPsec settings choose the connection mode as a **Responder only**. In this way Cato will not initiate the connection.

A new sub-menu will appear that will give you the option to select an authentication identifier. Select here the option KEY_ID. The system will proceed and generate a Local.ID in this form: [XXXXXXXX].[SiteID]. Configure the PSK and the DH group to 16.

**To configure the IPsec settings for the FortiOS:**

1. Enter the settings to define IPsec phase 1:

```plaintext
config vpn ipsec phase1-interface
    edit "CATO_Cloud_MK21" #[Primary VPN Name] 
        set interface "wan1" #[Local FGT site network WAN interface]
        set ike-version 2
        set keylife 19800
        set peertype any
        set mode-cfg disabled
        set proposal aes256gcm-prfsha512
        set localid "[XXXXXXXX].[SiteID]" #[Set the local ID - You can get that from Site Configuration -> IPsec menu]
        set comments "Primary IPSEC 2 Cato FW Initiated"
        set dhgrp 16
        set nattraversal forced
        set remote-gw                  #[Cato PoP primary IP]
        set psksecret         #[Primary Cato configured PSK]
    next
    edit "CATO_Cloud_MK22" #[Secondary VPN Name] 
        set interface "wan2" #[Secondary FGT site network WAN interface – if not available use the same WAN interface
        set ike-version 2
        set keylife 19800
        set peertype any
        set mode-cfg disabled
        set proposal aes256gcm-prfsha512
        set localid "[XXXXXXXX].[SiteID]" #[Set the local ID - You can get that from Site Configuration -> IPsec menu]
        set comments "Secondary IPSEC 2 Cato FW Initiated backup"
        set dhgrp 16
        set remote-gw    #[Cato PoP secondary IP]
        set psksecret    #[Secondary Cato configured PSK]
    next
```
2. Enter the settings to define IPsec phase 2:

```plaintext
config vpn ipsec phase2-interface
    edit "CATO_Cloud_MK22" #[VPN phase 2 Name]
        set phase1name "CATO_Cloud_MK22" #[VPN phase 1 Name] 
        set proposal aes256-sha512
        set dhgrp 16
        set auto-negotiate enable
        set keylifeseconds 3600
    next
    edit "CATO_Cloud_MK21" #[VPN phase 2 Name]
        set phase1name "CATO_Cloud_MK21" #[VPN phase 1 Name] 
        set proposal aes256-sha512
        set dhgrp 16
        set auto-negotiate enable
        set keylifeseconds 3600
    next
```
3. Route the traffic though the VPN tunnel to the Cato Cloud:

```plaintext
config router static
    edit X #[Local FGT unique route ID]
        set dst 10.254.254.0 255.255.255.0 #[Remote Cato Networks subnet – replace as you see fit]
        set device "CATO_Cloud_MK21"
    next
    edit Y #[Local FGT unique route ID]
        set dst 10.254.254.0 255.255.255.0 #[Remote Cato Networks subnet – replace as you see fit]
        set priority 10 #[this will be the backup connection so a higher priority is needed]
        set device "CATO_Cloud_MK22"
    next
    edit Z #[Local FGT unique route ID]
        set dst 10.254.254.0 255.255.255.0 #[otherwise send to black hole - Remote Cato Networks]
        set distance 254
        set blackhole enable
    next
```
4. Configure the firewall policy with rules that allow traffic inside the tunnel.

```plaintext
config firewall policy
    edit #[Local FGT rule ID]
        set name "From_Cato_Primary_IPsec"
        set srcintf "CATO_Cloud_MK21" #[Remote Cato Networks VPN zone or VPN interfaces]
        set dstintf "internal_LAN" #[Local FGT site network interface or interfaces]
        set srcaddr "all" #[Best practice – filter by Cato address / group]
        set dstaddr "all" #[Best practice – filter by local address / group]
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
        set fsso disable #[Not needed in newer FortiOS versions]
        set comments "Traffic From the_Cato primary IPSec"
    next
    edit #[Local FGT rule ID]
        set name "To_Cato_Primary_IPsec"
        set srcintf "internal_LAN" #[Local FGT site network interface or interfaces]
        set dstintf "CATO_Cloud_MK21" #[Remote Cato Networks VPN zone or VPN interfaces]
        set srcaddr "all" #[Best practice – filter by local address / group]
        set dstaddr "all" #[Best practice – filter by Cato address / group]
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
        set fsso disable #[Not needed in newer FortiOS versions]
        set comments "Traffic From the local network to the_Cato primary IPSec"
    next
    edit #[Local FGT rule ID]
        set name "From_Cato_Secondary_IPsec"
        set srcintf "CATO_Cloud_MK22" #[Remote Cato Networks VPN zone or VPN interfaces]
        set dstintf "internal_LAN" #[Local FGT site network interface or interfaces]
        set srcaddr "all" #[Best practice – filter by Cato address / group]
        set dstaddr "all" #[Best practice – filter by local address / group]
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
        set fsso disable #[Not needed in newer FortiOS versions]
        set comments "Traffic From the_Cato secondary IPSec"
    next
    edit #[Local FGT rule ID]
        set name "To_Cato_Secondary_IPsec"
        set srcintf "internal_LAN" #[Local FGT site network interface or interfaces]
        set dstintf "CATO_Cloud_MK22" #[Remote Cato Networks VPN zone or VPN interfaces] 
        set srcaddr "all" #[Best practice – filter by local address / group]
        set dstaddr "all" #[Best practice – filter by Cato address / group]
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
        set fsso disable #[Not needed in newer FortiOS versions]
        set comments "Traffic From the local network to the_Cato secondary IPSec"
    next
end
```

### Configuring the FortiOS Applicane with the GUI

**To configure a FortiOS to connect to an IPsec IKEv2 FW-initiated site via GUI:**

1. Configuring the FortiOS IPsec settings:
  1. Go to **VPN > IPsec Wizard**, and enter the name of the VPN and select the template name – **Custom**. Click **Next**.

![image001.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247862186909.png)
  2. In the next screen configure as below:

![image002.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247868661917.png)![image003.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247868729501.png)![image004.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247877832861.png)![image005.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247862609693.png)
2. Configure the Firewall Policy settings:

Create a Firewall Policy to allow traffic from and to the Cato IPsec site. Go to Policy > Objects > Firewall policy and click **Create New**. We suggest to allow all the traffic from all the FW Networks but you can select the source / destination / services as you prefer.

![image006.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247893126685.png)

**Note:** Usually you don’t need to NAT your traffic.
3. Configure the Static Routes:

Finally, add the route from the Network > Static routes > Create New. Compile it with the Cato IP range that you want to access through the IPsec connection.

![image007.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247869145373.png)
  1. To create the backup tunnel repeat the process (1. IPsec connection creation with a different Cato PoP IP / 2. FW Policy creation for the new IPsec) and when arriving to the routing phase set the priority / administrative distance to a higher number.
  2. Configure the dynamic routing settings for the site in the Cato Management Application. Define the Private IPs for the Primary and Secondary tunnels of the site.

If you want to have a dynamic routing configured on your environment, you will have to skip step 4.

![image008.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247893376541.png)
  3. Configure the Primary and Secondary BGP settings for the site.

![image009.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247885715741.png)
4. Configure the dynamic routing settings in the FortiGate GUI.
  1. Configure each of the interfaces with Cato and the FortiGate private IP’s and enable Ping administrative access:

![image011.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247885807901.png)![image012.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247893703965.png)
  2. Go to Network > BGP and create a two new neighbors mirroring the Cato configuration:

![image013.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247886037405.png)
  3. Configure the Local AS with same settings as the Cato Management Application:

![image014.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247886148381.png)
  4. Click **Save** .

You will see both tunnels up and in the Cato Management Application in Site Configuration > BGP, the status is **Established via incoming connection** on both IPsec connections:

![image015.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247869830685.png)
