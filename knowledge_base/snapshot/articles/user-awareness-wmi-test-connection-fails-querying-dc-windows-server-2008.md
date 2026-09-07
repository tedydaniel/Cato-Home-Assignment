---
title: "User Awareness | WMI \"Test connection\" fails when querying a DC on Windows server 2008"
slug: "user-awareness-wmi-test-connection-fails-querying-dc-windows-server-2008"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/user-awareness-wmi-test-connection-fails-querying-dc-windows-server-2008"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Awareness | WMI "Test connection" fails when querying a DC on Windows server 2008

The following article would help if the WMI "Test connection" fails and the DC installed on Windows server 2008.

For Windows server 2008 we got few additional steps which are **must:**

1. Use **regedit**
2. Navigate to **HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog\Security**
3. Grant **Read** permissions to the **Distributed COM Users** and **Event Log Readers** groups, as shown in the attached screenshot: ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360000598465.png)
4. Open **wmimgmt.msc**
5. **Right-click the WMI Control** and choose **Properties**
6. Choose the **Security** tab
7. Choose the **CIMV2** item
8. Click the **Advanced** button
9. Choose the **Distributed DCOM Users** group and press **edit**
10. In the “Apply to” popup choose **“This namespace and subnamespaces”**
11. Repeat the last step for the Event Log Readers group**![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360000598485.png)**

For more information, see [Configuring the Windows Server for Directory Services](/v1/docs/configuring-the-windows-server-for-directory-services).
