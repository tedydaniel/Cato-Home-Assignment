---
title: "User Not Mapped by WMI-based User Awareness"
slug: "user-not-mapped-by-wmi-based-user-awareness"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/user-not-mapped-by-wmi-based-user-awareness"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Not Mapped by WMI-based User Awareness

## Problem

After configuring User Awareness and making sure that the WMI Controller connection tests are successful under Access > User Awareness, some users are still not being identified.

## Solution

### **1. Check the Audit Policy on the Domain Controllers**

Make sure that **Audit account logon events** and **Audit logon events** are set to **Success** in the Local Security Policy on each Domain Controller.

The Audit Policy can be found under **Security Settings > Local Policies > Audit Policy** in the Local Security Policy settings.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360001888438.png)

Note: The Audit Policy can be controlled by GPO. If "Audit account logon events" are set to "No auditing" and the policy is controlled by GPO, you'll need to edit the settings in the GPO. You will not be able to change the setting in the Local Security Policy.

If logon events are set to success, you will be able to see events in the Event Viewer on the DC. Cato reads the following event IDs for User Awareness purposes:

- 4624
- 4768
- 4769
- 4770
- 5140
- 5145

### **2. Make sure all Domain Controllers are added to WMI Controllers for Real Time Sync in the Cato Management Application**

Audit events are not replicated across Domain Controllers, so it's necessary to add all the DCs that users may authenticate against to the **WMI Controllers for Real Time Sync** configuration in the Cato Management Application. If a user authenticates against a DC that is not added to the configuration, Cato will not be able to read the login event for that user, and the user will not be identified.

After all the DCs are added to the Cato Management Application, also make sure that the connection test is successful for all of them.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17380472171677.png)

### **3. Verify that the Domain controller is up and that it is not exhausted**

Confirm that no CPU or RAM spikes are occurring on the Domain Controller which may impact WMI querying for User Awareness. If the Domain Controller is presenting resource exhausting, follow the steps below:

- Increase the amount of RAM and CPUs on the server if possible.
- If adding more physical resources to the server is not possible, follow the steps below to increase WMI Provider Service memory, handle quotas, and decrease the size of the Security Event logs:

Follow the steps below to reduce the Security Log size limit to 1MB:
  - Increase the **WMI** **MemoryPerHost** value (see [Increase WMI Quota properties to maximum values](https://blogs.technet.microsoft.com/bulentozkir/2014/01/14/increase-wmi-quota-properties-to-maximum-values/))
  1. Open the **Event Viewer**
  2. Navigate to **Event Viewer > Windows Logs > Security**
  3. Right click **Security** and click **Properties**
  4. Set the **Maximum log size (KB)** to **1024**
  5. **When maximum event log size is reached** select **Overwrite events as needed (oldest events first)** or **Archive the log when full, do not overwrite events.**
  6. Click OK

### **4. Check that the user generated a logon event on a Domain Controller.**

You can determine what DC a user authenticated to by any one of the following commands from a command prompt on the user's computer:

- **set l**
- **echo %logonserver%**
- **nltest/dsgetdc:domain.com**

After determining the authenticating DC, open the Event Viewer on that DC and go to **Windows Logs > Security**. You can add a filter for the logon event ID from the list above, like 4624, and then search for the username.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360000609697.png)

If you find a successful logon event for the user, and that DC passed the WMI Controllers for Real-Time Sync connection test in the Cato Management Application, then UA should be working for the user. If UA still is not working, please contact Cato support for assistance.

If you do not find a successful logon event for the user, you can run a WMI query from a command prompt on a domain-connected computer to verify that the user is logged into the computer.

WMI query using IP address:

```plaintext
WMIC /NODE: <IP address> COMPUTERSYSTEM GET USERNAME
```

Example:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360001798857.png)

### **5. Check that the user is enabled in CMA**

Users imported to CMA can be disabled either by removing them from the user group on the IdP side or by disabling them manually in CMA. Users with **disabled** status will not be mapped by UA.

Make sure that the user is enabled in CMA.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17380472176925.png)
