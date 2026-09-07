---
title: "Directory Services and User Awareness Errors Troubleshooting"
slug: "directory-services-and-user-awareness-errors-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/directory-services-and-user-awareness-errors-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Directory Services and User Awareness Errors Troubleshooting

This article describes common directory services and user awareness issues and suggested solutions. For more information, see [Configuring the Windows Server for Directory Services](/v1/docs/configuring-the-windows-server-for-directory-services).

## Error: Unable to Connect to the Domain Controller

### Challenge

This error message indicates a connectivity failure with the domain controller (DC) mostly because of invalid credentials. This error message is usually followed by “Invalid Credentials” error message.

### Solution

Verify that you entered the LDAP Authentication Connection Settings (Login DN, Base DN and password) correctly in the Cato Management Application (Access > Directory Services).

## Error: NT_STATUS_ACCESS_DENIED

### Challenge

This error message indicates on permissions issue. The Cato Management Application notifies when it’s unable to access the DC. This error message is usually followed by the event: “DC_Connectivity_Failure” in the analytics section. The Cato Management Application generates this event (once an hour) when the connection with the DC fails.

### Solution

Follow these steps to troubleshoot this issue:

1. Check the username and password. Verify that you entered the correct Login DN and password. Verify that the Cato Socket sends the correct username in the connection attempt by capturing the packets (PCAP) on the LAN interface of the Socket or the DC itself.
2. Check the user permissions to read the event log from domain controller settings. Follow the online help guide - windows configuration.
3. If you enabled the Daily sync Directory Service Groups and Users (User Awareness), verify that you configure the Domain Controllers for Real Time Sync. Click “Test Connection” and see if you get “Connection Successful” result.
4. Check for events in the Events in the Monitoring section. You can filter the events based on event type: system and event sub type: Directory Services and look for DC connectivity or sync errors.
5. Follow the online help guide and verify domain controller configuration settings.
6. Check that traffic isn’t blocked by the internet or WAN firewall. Firewall rule that blocks unidentified users can block the Cato sync user and blocks the directory services.
7. Walk through all the configuration steps in the Online Help Guide once again to verify that every step was performed correctly. If permissions are not set correctly on the service account used for the connection, you will get an access denied error.

## Error: NT_STATUS_UNSUCCESSFUL

### Challenge

The Cato Management Application generates this error when the PoP is unable to access the DC for real time sync. This error appears when clicking on the "Show Status" button in the Domain Controllers for Real Time Sync section or by email to the Account Admins.

### Solution

This error usually indicates a misconfiguration of the User Awareness feature settings. It can also occur due to firewall or routing configuration. Follow these steps to troubleshoot the issue:

1. Check the Events and verify if there are events of unidentified users.
2. Check that traffic isn’t blocked by Internet/WAN Firewall because of unidentified users.
3. If this is the first time you've enabled the User Awareness feature and you're getting DC sync errors, verify that every step is configured correctly.
4. Make sure that the DC is up and running.
5. Run a traffic capture from the Socket UI, capturing the packets (PCAP) on the LAN interface of the Socket. Click on the Show Status button. Stop the capture and look for the WMI query from the Cato PoP and the server response in the capture file (using any network packet analyzer tool such as Wireshark). If the DC is behind an IPsec site, run the capture on the DC itself.

## Error: NT_RPC_NT_CALL_FAILED

### Challenge

The error NT_RPC_NT_CALL_FAILED indicates that the RPC service on the DC doesn’t respond. This error appears when clicking on the "Show Status" button in the Domain Controllers for Real Time Sync.

### Solution

1. Verify that the Domain controller is up and running, and check the CPU and memory. Sometimes high CPU or memory causes the server overload.
2. Verify that the DC Windows services are started and set for automatic startup:
  - Server
  - Remote Registry
  - WMI

## Error: NT Code 0x80010111

**Challenge**

This error means the PoP cannot communicate with the DC because of an RPC header mismatch between the PoP and the DC.

**Solution**

This error is common specifically on Windows Server 2022 where the DC's RPC version is validated.This is a known issue that customers may run into. If you receive this error please open a ticket with Cato Support to address it.

## UA Sync Error NT code 0xc002001b

## Issue

The error 0xc002001b NT code 0xc002001b will appear when the RPC service on the domain controller has failed to respond.

This error can appear when clicking "Test Connection" under Access > User Awareness > LDAP or when emailing the Account Admins.

The issue can cause:

- Users are not identified in Events and Analytics.
- Traffic is blocked by the Internet/WAN Firewall due to users not being identified.
- Customer new setup of User Awareness and getting DC sync errors.

## Possible Cause

This issue might happen due to exhausted resources on the Domain controller.

## Troubleshooting

The following steps are troubleshooting steps that can be followed:

- Verify that the Domain controller is up and that it is not exhausted (no CPU or RAM spikes).
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
- Verify that the required domain controller services are running (open services.msc and check that Server, Remote Registry, and Windows Management Instrumentation are started and set for automatic startup.
- In case the domain controller is showing stress signs, it might be required to restart the server.

## Error: Cannot connect to Domain Controller 0xc0000001 NT_STATUS_UNSUCCESSFUL

If you see the unsuccessful status error message in the Cato Management Application as follows:

“Cannot connect to Domain Controller 0xc0000001 NT_STATUS_UNSUCCESSFUL . Verify that you have correctly integrated the Domain Controller with Cato Network. If issue persists, contact Cato Support for assistance. Click here for details.”

This is a general error that can be the result of misconfigurations of the Domain Controller. We recommend to follow the configuration guide.

## Error - Cannot connect to Domain Controller (code 6)

If you see a code 6 connection error in the Cato Management Application, as follows:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20981096060957.png)

There are some steps you can take to troubleshoot the problem.

### Reconnecting the Cato Socket

Sometimes this problem is solved when you use the Socket WebUI to disconnect and reconnect the Socket to the Cato Cloud.

**WARNING!** A Socket reconnect action disconnects all current sessions for the site. The Socket connects back to the Cato Cloud within a few seconds, and then connectivity is restored immediately. However, some connection-sensitive traffic (like phone calls) are dropped.

**To perform a reconnect action on the Socket:**

1. Connect to the Socket WebUI, in your web browser, enter **https://<Cato Socket IP address>** For example: **https://10.0.0.26**
2. Enter the username and password.
3. Select the **Cato Connection Settings** tab. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20981101423645.png)
4. Click **Reconnect**.
5. Log out of the Socket WebUI.

### Troubleshooting Connectivity to the DC

After you perform the Socket reconnect action, the DC error still persists, here are some additional suggestions to troubleshoot connectivity to the DC:

1. Verify the DC connection to the Cato Cloud.
2. Verify that there is two-way communication between the DC and the Cato Cloud.

**To verify that the DC is connected to the Cato Cloud:**

1. Make sure that your DC is powered on.
2. In the Cato Management Application, go to **Home > Topology** and make sure that the site with the DC is connected to the Cato Cloud.
3. Verify that you ping the DC from a host at a different site, or while you are connected to the Cato VPN.
4. If you can't ping the DC, here are some ways to troubleshoot the problem:
  - In the Cato Management Application, check **Home > Events** for a block event. Do you need to change the **WAN Firewall** policy to allow ICMP traffic to the DC?
  - Check the routing table on the DC and make sure that the traffic is being routed to the Cato Socket or IPsec tunnel.
  - Check the Windows Firewall policy on the DC to make sure that ICMP traffic is not blocked.

**To verify the communication between the DC and the Cato Cloud:**

1. Run a packet capture either on the Socket's LAN interface.
  - If the DC is behind an IPsec site, run the capture on the DC itself.
2. If there is two-way communication, you can see a connection on TCP/135 to your DC initiated from the Cato VPN range (10.41.0.0/16 by default). **Note:** Cato can use any IP address from the VPN range to initiate the connection. **Note:** Starting in Windows Server 2008, you must also allow TCP 49152-65535 for the WMI process through any firewall. It is also possible to add a Windows firewall rule for the WMI service specifically. See : [https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista)
3. If you can't find a connection that shows two-way communication, here are some to troubleshoot the problem:
  - If you don't see any traffic coming from the VPN range to the DC, contact Cato support.
  - If you only see SYN packets on TCP/135 from the Cato VPN range to your DC, check the connectivity of the DC:
    1. Inspect the routing table on the DC and make sure that the traffic is routed to the Cato Socket or IPsec tunnel.
    2. Check the Windows Firewall policy on the DC and make sure that the traffic is not blocked.

## User Isn’t Mapped by User Awareness

### Challenge

In some cases, users are shown as "unmapped user" in the Event Discovery window. The reason for an unmapped user is that the PoP was able to discover the username in real time (using WMI queries) but this user wasn’t imported during the LDAP sync and is unidentified. Therefore, the event AD Name field shows unmapped user.

### Solution

1. Verify that the user belongs to the group. If you configured Cato’s Directory Services to import users and groups from the DC, and a user doesn’t belong to the configured group, it then appears as an unmapped user.
2. Check the audit policy configuration for the DC. For more information see [Configuring the Audit Policy for the Domain Controller](/v1/docs/directory-services-and-user-awareness-errors-troubleshooting#configuring-the-audit-policy-for-the-domain-controller).

## Logon Events Don’t Appear in the Event Discovery

### Challenge

If you enabled User Awareness for your account but you can’t see any users log on events in the Event Discovery follow the steps that described in the following solution.

### Solution

Check the audit policy configuration on the DC. For more information see [Configuring the Audit Policy for the Domain Controller](/v1/docs/directory-services-and-user-awareness-errors-troubleshooting#configuring-the-audit-policy-for-the-domain-controller).

## The Directory Services Sync Doesn’t Import Users

### Challenge

With User Awareness, shows in real time what are the usernames of hosts behind sites. It allows you to see the usernames of hosts and not just the IP addresses in the Analytics sections. Users are populated from the Directory Services Sync. The Sync uses LDAP to query the Active Directory (AD) server. Sometimes the LDAP sync fails because of different reasons. For example, Microsoft LDAP has a known limitation that only allows objects with less than 1500 attributes to be returned in any single query. Large organizations can easily have more than 1500 members assigned to a group. Thus, when the PoP runs the LDAP query, any groups with more than 1500 members will return an empty members list to the Cato Management Application, resulting in deactivated/deleted users in CMA.

### Solution

As mentioned in [Syncing Users with LDAP](/v1/docs/syncing-users-with-ldap), to prevent the unwanted deactivation/deletion of users due to this limitation, you can customize the maximum number of users that can change user group membership in a single sync by configuring the "Prevent updating group membership" option in CMA.

To resolve the empty query response from the Domain Controller, you can follow these steps:

1. Verify that the following windows services in the DC are running and set to automatic:

- Server
- WMI
- Remote Registry

1. You can adjust the DC Microsoft LDAP policy attribute for MaxValRange. This attribute controls how many values will be returned. Use the following two articles to raise the MaxValRange or remove the restriction entirely. If you don’t want to modify the AD attribute, then Cato can collect groups with less than 1500 users.

MS article on how to adjust MaxValRange using tool ntdsutil: [https://support.microsoft.com/en-gb/help/315071/how-to-view-and-set-ldap-policy-in-active-directory-by-using-ntdsutil](https://support.microsoft.com/en-gb/help/315071/how-to-view-and-set-ldap-policy-in-active-directory-by-using-ntdsutil)

MS article/blog on how to remove restriction completely: [https://docs.microsoft.com/en-us/archive/blogs/qzaidi/override-the-hardcoded-ldap-query-limits-introduced-in-windows-server-2008-and-windows-server-2008-r2](https://docs.microsoft.com/en-us/archive/blogs/qzaidi/override-the-hardcoded-ldap-query-limits-introduced-in-windows-server-2008-and-windows-server-2008-r2)

## Missing Audit Events when using GPO

### Challenge

If you are using a GPO with advanced security audit policy settings and not all Event IDs are being logged, follow the steps that are described in the solution.

### Solution

Check the audit policy configuration for the DC. For more information see [Configuring the Audit Policy for the Domain Controller](/v1/docs/directory-services-and-user-awareness-errors-troubleshooting#configuring-the-audit-policy-for-the-domain-controller).

## Configuring the Audit Policy for the Domain Controller

The audit policy can either be defined locally on the DC or applied via GPO. GPO overrides the local security policy. Advanced audit policy settings override the basic audit policy settings.

Verify that the audit policy is configured with the Event IDs that User Awareness uses in the Windows security log in order to map users to IP addresses.

The following list contains the Event IDs the Cato uses in the audit policy:

- 4768 - A Kerberos authentication ticket (TGT) was requested
- 4769 - A Kerberos service ticket was requested
- 4770 - A Kerberos service ticket was renewed
- 4776 - The domain controller attempted to validate the credentials for an account\
- 4624 - An account was successfully logged on
- 4648 - A logon was attempted using explicit credentials
- 5140 - A network share object was accessed
- 5145 - A network share object was checked to see whether client can be granted desired access

To Configure the Audit Policy Locally on the DC

1. Open Local Security Policy.
2. Go to Security Settings > Local Policies > Audit Policy to configure the basic audit policy, or go to Security Settings > Advanced Audit Policy Configuration > Audit Policy to configure the advanced audit policy that provides more granular control over logging.

To Configure the Audit Policy using Group Policy:

1. Open Group Policy Management Editor.
2. Right click on the GPO that applies to all Domain Controllers and select "Edit"
3. Expand Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Audit Policy for basic audit policy or Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policy for advanced audit policy.

The following list contains the Event IDs that are used by Cato’s User Awareness:

Basic Audit Policy

- Audit logon events - 4624, 4648
- Audit account logon events - 4768, 4769, 4770, 4776
- Audit object access - 5140, 5145

Advanced Audit Policy

- Account Logon
  - Audit Kerberos Authentication Service – 4768
  - Audit Kerberos Service Ticket Operations - 4769, 4770
  - Audit Credential Validation – 4776
- Logon/Logoff
  - Audit Logon - 4624, 4648
- Object Access
  - Audit File Share – 5140
  - Audit Detailed File Share - 5145

You can verify what the effective audit policy on a DC is by running the following command from a command prompt: **auditpol /get /category:***
