---
title: "Setting Up Redundant VPN Tunnels to Google Cloud Platform (GCP)"
slug: "setting-up-redundant-vpn-tunnels-to-google-cloud-platform-gcp"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/setting-up-redundant-vpn-tunnels-to-google-cloud-platform-gcp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Up Redundant VPN Tunnels to Google Cloud Platform (GCP)

GCP recently released a new HA option for VPN gateway. If redundant VPN gateway is chosen, it provides two IP addresses for maximum resiliency. BGP activation is required to monitor which tunnel is active.

This is Cato's recommendation for the most resilient connection to GCP.

**Step 1**

In the Cato Management Application, navigate to **Network > IP Allocation**. Select new PoP locations for the GCP site. The IP that is allocated will appear on the right side. Take note of the IP address - you'll need to enter it in the GCP configuration.

**Step 2**

In GCP, navigate to the **Hybrid Connectivity → VPN → Cloud VPN Gateway.** Create a new VPN gateway:

![mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248131597469.png)

Now fill in the details:

- **Name -** Identifiable name for the Gateway
- **VPC Network -** This is your VPC
- **Region -** The Geographical Region you want to create the gateway in

Pay attention that it will create two IP addresses as stated:

![mceclip3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248109124765.png)

**Step 3**

Navigate to **Peer VPN Gateways** and create a new VPN gateway. Make sure to select two interfaces under Interfaces section.

![mceclip4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248109204893.png)

- **Interface 0 IP address**: type in the IP of the *primary* PoP IP (step 1)
- **Interface 1 IP address**: type in the IP of the *backup* PoP IP (step 1)

**Step 4**

Now you must create a Cloud Router that will manage BGP peering. BGP is required for prioritizing which tunnel is active and which is backup.

Go to **Hybrid Connectivity → Cloud Routers** and create a new Router.

For Google ASN use private ASN value (RFC 1918): 64512 to 65535.

**Step 5**

Go back to VPN section and choose Cloud VPN Gateway. Click the recently created VPN gateway and choose Add VPN tunnel. Under peer VPN gateway choose VPN peer (Cato PoPs) and make sure Create a pair of VPN tunnels is selected under High Availability. In Cloud Router choose the recently created Cloud Router.

Now, at the bottom, it forces you to edit two VPN tunnels. Click on each one of them and enter the details:

![mceclip5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248155728669.png)

Fill the name for each tunnel (master/ backup) and choose a pre-shared key.

Once complete, the wizard will prompt for BGP configuration. For each tunnel configure the relevant BGP settings:

- Name - just a name for the BGP peering
- Peer ASN - BGP ASN you would like to assign to Cato side
- MED - **100** for primary tunnel and **110** for backup
- Cloud Router BGP IP - Router IP on GCP side
  - Must belong to the same /30 CIDR within 169.254.0.0/16
  - Can't use the broadcast or network IP addresses on those /30 networks
- BGP Peer IP - Router IP on Cato side

**Step 6**

Go back to the Cato Management Application and create an IPsec IKEv2 site type (Networks > Site and click **New**). Use the following site configuration:

IPsec IKEv2 Section

- **Service Type:** choose Generic.
- **Primary/ Secondary Source (Egress) IP**: select the IP address allocated in step 1.
- **Primary/ Secondary Destination IP**: enter the Cloud VPN Gateway IP addresses from the GCP.
- **Set/Change Primary/ Secondary Password**: Enter the Pre-Shared Key that you specified for each tunnel.

BGP

- Create two BGP peers for Master and Backup.
- Neighbor ASN and IPs as configured in GCP.
- Metrics: for master, BGP specify **100** and for the backup **110**.
- Hold Time and Keepalive intervals can be changed to 30 and 10 respectively for faster convergence.
- Routing - do not Accept any routes from GCP. Subnets behind GCP should be configured in Networks section just like with regular Cato sites. For advertising, you can choose between Default Route (one 0.0.0.0/0 route - WAN + Internet over Cato) and All Routes (all networks in your Cato account will be advertised to GCP - WAN traffic only).

**Step 7**

Shortly after saving the configuration in the Cato Management Application, you should see Established status for BGP and VPN of the two tunnels under Cloud VPN Tunnels in GCP:

![mceclip7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248131864349.png)
