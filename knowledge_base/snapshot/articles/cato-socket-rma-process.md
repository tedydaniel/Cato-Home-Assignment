---
title: "Cato Socket RMA Process"
slug: "cato-socket-rma-process"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/cato-socket-rma-process"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Socket RMA Process

When a Socket goes offline, the primary concern is restoring service as quickly as possible. Cato’s Sockets are software-based, and the majority of issues with the Sockets are software issues. Correcting the software issue is the quickest route to restoring service. As such, Cato’s first step to resolving the problem and restoring service is to reinstall the software and reset the Socket. The articles in this section explain how to reset the Sockets: [Reimaging Cato Sockets](/v1/docs/reimaging-cato-sockets).

**Note:** You can connect to a brand new Socket by plugging a PC to the Socket’s LAN2 interface on an X1500 Socket or on the MGMT interface of an X1700. Then open an Internet browser and go to https://169.254.100.1/.

If flashing the Socket doesn't restore service, it may be necessary to replace the Socket via the Cato Return Merchandise Authorization (RMA) process. For information about the RMA process, please see the [Cato Master Service Agreement](https://www.catonetworks.com/MSA/).

Please go to [https://support.catonetworks.com/hc/en-us/requests/new](https://support.catonetworks.com/hc/en-us/requests/new) to file a new Support request.

## Support Request

When filing the request, please select the Cato Socket request type.

In general, please complete the Cato Socket form as completely as possible. The more details provided in the initial request, the quicker and more accurately Cato can respond to the issue.

To make it easier to complete the form with the correct information, see these guildelines concerning some of the Cato Socket form fields:

- For the ​**Category**​​, select ​​**Installation, Deployment, and Hardware**​​.
- For **Topic**, select Socket Hardware
- For **Socket Platform**, select the applicable hardware platform (e.g. X1500)
- For **Socket S/N**, please provide the Serial number or MAC address of the socket:

The MAC address can be found in the Cato Management Application, by accessing to Network > Sites > {site name} > Site Configuration > Socket:

![X1500_Socket_CMA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248004811549.png)

![image-20210301-162023.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248004931357.png)The serial number is attached to the bottom of the Socket :

![x1500 sticket](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248021201949.png)

- For the **Description**, please answer the following questions:

```plaintext
* Detailed description of the issue: 

* Power Cable Type (ie. US, EU, JP)

* Site Address details and Contact Information: 

* Please describe the service impact: 

* Can you indicate a possible trigger? ( e.g. power outage): 

* Did the issue persist after physically disconnecting the socket from power for 15 seconds and reconnecting:

* When reflashing the socket, did the socket shutdown by itself at the end of the flashing process: 

* Did the issue persist after reflashing the socket: 14 15* After reflashing, was the socket web UI accessible by directly connecting a computer to the sockets LAN2 port?
```
- For attachments, please provide:
  1. A photograph of the lights displayed on the front of the socket after reflashing it
  2. A screenshot of the Socket WebUI, if available (see example below)

![image-20210301-163610.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248036277021.png)
