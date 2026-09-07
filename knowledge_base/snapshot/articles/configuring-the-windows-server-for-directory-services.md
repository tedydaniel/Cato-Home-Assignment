---
title: "Configuring the Windows Server for Directory Services"
slug: "configuring-the-windows-server-for-directory-services"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/configuring-the-windows-server-for-directory-services"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Windows Server for Directory Services

This article explains how to configure the settings and permissions in a Windows server to allow the PoPs in the Cato Cloud to integrate with the Active Directory Domain Controller.

> [!NOTE]
> Notes:
> 
> - The screenshots and procedures in this article are based on Windows Server 2016. The details may be different for other versions.
> - If you need more information about Cato's IP address for the LDAP service, see [Resolving Issues with LDAP Sync](/v1/docs/resolving-issues-with-ldap-sync) (you must be logged in to the Cato Knowledge Base to view this article).

## Creating a New Domain User for Directory Services

Create a dedicated domain user for the integration between your Cato account and the AD domain.

These are the AD password requirements for this user:

- The password never expires
- Disable the setting that forces the user to change the password for the initial login

**To create a user for Directory Services:**

1. Create a new domain user (this user is only used for Cato Directory Services).
2. In the **Member Of** tab, make sure that the user is a member of the **Domain Users** group.
3. Add the user to the following groups:
  - Distributed COM Users
  - Event Log Readers

![Prerequisites_For_Enabling_User_Awareness_01.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218215308829.png)
4. Click **OK** to create the user.

## Configuring the DCOM Settings

Configure these Distributed COM (DCOM) settings on the Windows server to allow the PoPs in the Cato Cloud to remotely communicate with the domain. These are the DCOM settings that you need to configure:

- Windows services
- DCOM properties and protocols
- COM security permissions

### Configuring the Windows Services

Start the Server, Remote Registry, and WMI Performance Adapter Windows services and configure them to automatically startup with the Windows server.

> [!NOTE]
> Note:
> 
> The **WMI Performance Adapter** service is called **WMI** on other versions of Windows server.

**To enable the Windows services:**

1. From the **Run** menu, enter **services.msc** and click **OK**.
2. In the **Services** window, verify that each of the services **Server**, **Remote Registry**, **WMI Performance Adapter** are started and set for automatic startup.
  1. To change a service property, right-click on the service name, and then click **Properties**.
  2. For **Startup type**, select **Automatic**.
  3. If the service status has not started, click **Start**.
3. Click **OK** and close the **Services** window.

### Configuring the DCOM Communication Properties and Protocols

The DCOM properties define the Authentication and the Impersonation Level for the server. Configure the server Authentication Level to **Connect**, which means that the session key is only used for the authentication handshake.

Set the Impersonation Level to **Identify**, to allow the PoPs to only access the user data that is relevant to Cato Directory Services.

The DCOM Protocol Sequence for the server defines how the server communicates over the network. Directory Services uses the connection-oriented TCP/IP protocol.

**To configure DCOM for Directory Services:**

1. From the **Run** menu enter **dcomcnfg** and click **OK**. The **Components Services** window opens.
2. From **Component Services > Computers > My Computer**, right-click **My Computer** and select **Properties**. The **My Computer Properties** window opens.

![Windows_DCOM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218240289821.png)
3. Configure the DCOM communication properties for the Windows server:
  1. In the **My Computer Properties** window, select the **Default Properties** tab.
  2. Select **Enable Distributed COM on this computer**.
  3. From **Default Authentication Level**, select **Connect**.
  4. From **Default Impersonation Level**, select **Identify**.
4. Make sure that the DCOM protocols includes **Connection-oriented TCP/IP**.

![Windows_DCOM_Protocols.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218226289565.png)
  1. Click the **Default Protocols** tab. If the **DCOM Protocols** includes **Connection-oriented TCP/IP**, continue with step 6 below.
  2. Click **Add**. The **Select DCOM protocol** window opens.
  3. From **Protocol Sequence**, select **Connection-oriented TCP/IP**.
  4. Click **OK** to close the **Select DCOM protocol** window.
5. Click **OK**.
6. A message notifies you about to change the DCOM Machine wide settings. Click **Yes** to continue.

### Configuring the COM Security Permissions

In the **Components Services** window (**dcomcnfg**), configure the COM security Access Permissions and Launch and Activity Permissions to give the PoPs default access to:

- Distributed COM Users
- Event Log Readers

**To configure the COM Security permissions for Directory Services:**

1. If necessary open the My Computer Properties window, from **Component Services > Computers > My Computer**, right-click **My Computer** and select **Properties**.
2. Click the **COM Security** tab.

![Windows_COM_Security.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218215605789.png)
3. Configure the default access permissions for the distributed COM users and the event log readers:
  1. In **Access Permissions**, click **Edit Default**.
  2. Under **Group or user names**, add and configure **Distributed COM Users** with the following permissions:
    - **Local Access** - **Allow**
    - **Remote Access** - **Allow**
  3. Repeat the previous two steps for the **Event Log Readers** group.
  4. Click **OK**.
4. Configure the launch permissions for the distributed COM users and the event log readers:
  1. In **Launch and Activation Permissions**, click **Edit Default**.
  2. Under **Group or user names**, add and configure **Distributed COM Users** with the following permissions:
    - **Remote Launch** - **Allow**
    - **Remote Activation** - **Allow**
  3. Repeat the previous two steps for the **Event Log Readers** group.
  4. Click **OK**.
5. Click **OK** and close the **My Computer Properties** and the **Component Services** window. The COM security permissions are configured.

## Configuring Windows Server WMI

This section discusses how to configure the WMI permissions to allow Cato User Awareness to send WMI queries from the PoPs to the Windows server.

### Configuring WMI to Connect to the Cato Management Application

To connect to a remote computer using WMI, make sure that the correct DCOM settings and WMI namespace security settings are enabled for the connection.

For more about how to configure the WMI settings to allow connections from the Cato Management Application, see the Microsoft documentation.

### Configuring WMI User Access

The user or group that you configured for DCOM access must also have WMI permission to access the Windows event logs that give Cato access to the login events for the AD users. Configure WMI to allow remote access for Distributed COM Users and Event Log Readers.

**To configure WMI user access settings:**

1. From the **Run** menu, enter **wmimgmt.msc** and click **OK**. The **Windows Management Instrumentation** window opens.
2. Right-click on **WMI Control (Local)** and select **Properties**. The **WMI Control (Local) Properties** window opens.
3. Select the **Security** tab. The Namespace menu tree appears.
4. Expand the **Root** branch and click **CIMV2**.

![Windows_WMI_Security.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218230632477.png)
5. Click **Security** below the menu tree. The **Security for ROOT\CIMV2** window opens.
6. Configure the launch permissions for the distributed COM users and the event log readers
  1. Under **Group or user names**, add and configure **Distributed COM Users** with the following permissions:
    - **Enable Account** - **Allow**
    - **Remote Enable** - **Allow**
  2. Repeat the previous step for **Event Log Readers**.
7. Configure the advanced settings for the distributed COM users:
  1. Select **Distributed COM Users** and click **Advanced**. The **Advanced Security Settings for CIMV2** window opens.
  2. In the **Principal** column, select **Distributed COM Users** and click **Edit**. The **Permission Entry for CIMV2** window opens.
  3. In the **Applies to** drop-down menu, select **This namespace and subnamespaces**.

![Windows_COMusers_Advanced.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218240664221.png)
8. Click **OK**. Close the **Advanced Security Settings for CIMV2** window.
9. Configure the advanced settings for the event log readers:
  1. Select **Event Log Readers** and click **Advanced**.

![Windows_EventLog_Advanced.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218230780573.png)

The **Advanced Security Settings for CIMV2** window opens.
  2. In the **Principal** column, select **Event Log Readers** and click **Edit**. The **Permission Entry for CIMV2** window opens.
  3. In the **Applies to** drop-down menu, select **This namespace and subnamespaces**.
10. Click **OK** to close the **Advanced Security Settings for CIMV2** window.
11. **Click** OK to close the **Security for ROOT\CIMV2**, and the **WMI Control (Local) Properties** window.

The WMI user access settings are configured.

### Configuring the WMI Controller Registry

Edit the Windows registry to give read permissions for distributed COM users and event log readers.

**To configure the registry permissions for the WMI controller:**

1. Run **Regedit**.
2. Navigate to

`HKEY_LOCAL_MACHINE\SYSTEM\`

`CurrentControlSet\`

`Services\Eventlog\Security`
3. Right-click the **Security** folder and select **Permissions**.
4. Add and configure these groups with **Read** permissions:
  - **Distributed COM Users**
  - **Event Log Readers**
5. Click **OK**.

### Configuring a WMI Controller with an IPsec Tunnel

Since the connection to the DC uses a source IP in Cato’s system range, if you are using an IPsec tunnel to connect to Cato Socket, you must configure Phase 2 for the Cato system range: **10.254.254.12**.

For accounts that use a custom system range instead of the default one, use the custom range to calculate the fixed IP address for User Awareness sync based. The fixed IP address is the 9th in the custom range. For example, if the custom reserved range is 10.10.10.0/16, then the fixed IP address is 10.10.10.9.

For accounts that use a smaller IP range, they still use the 9th in the custom range. For example, if the custom reserved range is 10.200.200.64/28, then the fixed IP address is 10.200.200.73 (10.200.200.64 + x.x.x.9).

### Configuring the Windows Firewall to Allow DCOM

Configure the Windows or third-party firewall to allow access for the fixed IP address for the system range (or for a custom range). For more about system and custom ranges, see above Configuring a WMI Controller with an IPsec Tunnel.

- If you are using a Windows firewall, you must add an exception that allows DCOM communications
- If you are using a third-party firewall between the Windows Server and the Cato Network, add the same exception to it

**To configure the Windows firewall to permit DCOM communications:**

1. Open the **Run** menu.
2. Type **wf.msc** and click **OK**.
3. Select **Inbound Rules**.
4. In the **Action** menu, select **New Rule**. The **New Inbound Rule Wizard** opens.

![Windows_FW_NewRule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218240848029.png)
5. Select **Custom** and click **Next**. The **Program** window opens.
6. Select **All programs**, and click **Next**. The **Protocol and Ports** window opens.
7. For **Protocol type**, select **TCP** and click **Next**. The **Scope** window opens.
8. For **Which remote IP addresses does this rule apply to**, select the **These IP addresses** option.
9. Click **Add**. In **This IP address or subnet**, enter the fixed IP address for the system range: **10.254.254.12**.
  - If you are using a custom range, see enter the fixed IP address for your range.
10. Click **OK** and then click **Next**. The **Action** window opens.
11. Select **Allow the connection** and click **Next**. The **Profile** window opens.
12. Select one or more network profiles to which the rule applies and click **Next**. The **Name** window opens.
13. Enter the **Name** for the firewall rule, and then click **Finish**.
