---
title: "Handling Stolen or Compromised Sockets"
slug: "handling-stolen-or-compromised-sockets"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/handling-stolen-or-compromised-sockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Handling Stolen or Compromised Sockets

If a physical Socket has been compromised or stolen, immediate action is essential to prevent unauthorized access to the Cato Cloud and the private network for your account.

The steps in this article are crucial for mitigating the risks associated with a compromised Socket and safeguarding the integrity of the Cato Cloud network.

Follow these steps:

**1. Unassign the Socket from the Cato Management Application:** Log in to the Cato Management Application and unassign the compromised Socket as explained in [Managing Sockets](/v1/docs/managing-sockets). After the Socket is successfully unassigned, the [Socket Inventory](/v1/docs/using-the-socket-assignment-page) status changes to **Delivered**.

**2. Response to Connection Attempt:** If a malicious user attempts to connect the compromised Socket to the Internet:

- The Socket will get a response from the Cato Cloud refusing the connection and requesting to initiate a local Socket registration reset
- This prevents unauthorized access to the private network

**3. Initiate Site Registration Flow:** The compromised Socket will attempt to go through the standard [site registration process](/v1/docs/configuring-sites-with-cato-sockets). In the Cato Management Application, an **Activate New Socket** notification will appear. **IMPORTANT!** Do NOT assign the Socket to any site during this stage to prevent security breaches.

**4. Contact Support for Additional Measures:** Reach out to Cato's Support if the DTLS tunnel remains connected post-compromise. Support can force a tunnel tear-down to ensure the Socket's disconnection. Additionally, Support can perform back-end actions to delete the Socket's serial number and prevent someone from assigning it to a site by accident.

Immediate action, in conjunction with Cato Support, ensures a prompt and effective response to such security threats.
