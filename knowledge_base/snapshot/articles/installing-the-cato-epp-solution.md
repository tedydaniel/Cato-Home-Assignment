---
title: "Installing the Cato EPP Solution"
slug: "installing-the-cato-epp-solution"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/installing-the-cato-epp-solution"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing the Cato EPP Solution

This article explains how to install Cato's Endpoint Protection (EPP) solution on your endpoints

## Overview

Cato's EPP solution is installed on your endpoints to protect them from attack. The solution is associated with your account using a unique token and can be distributed to endpoints using a Managed Deployment Solution, or manually. The EPP solution is Cato's software that runs the EPP engines to identify malicious files or processes. It is independent of the Cato Client and does not connect to any Cato PoPs.

Cato automatically upgrades the EPP solution when a new version is available.

> [!NOTE]
> Note:
> 
> The minimum required version for the EPP Agent is 1.4.2.

### Prerequisites

Before the EPP solution is installed on an endpoint, ensure it meets the following requirements:

#### Endpoint Prerequisites

- The endpoint runs on Windows version 10 or higher and has x86-64 architecture (For more information about installing EPP on a Windows Server, see [Windows Server Prerequisites](/v1/docs/installing-the-cato-epp-solution#windows-server-prerequisites).)
- No other anti-virus solution is running on the endpoint, running the EPP solution with other security software may impact the level of protection
  - **Note:** From EPP agent v1.1 and higher, during installation and start-up, the agent checks for other anti-virus solutions installed on the endpoint.
    - If another solution is found during installation, the Cato Agent does not complete the installation
    - If another solution is found during start-up, an error is displayed in the Cato Management Application
- Devices located in China can't register the EPP agent with Cato because the Great Firewall of China blocks the traffic
- These installations are installed on the endpoint:
  - C++ Redistributable 2019 or newer
  - .NET 4.8 or newer

**Note:** These are automatically installed with the .exe installer but not with the .msi installer
- The endpoint can access these domains:
  - https://ep-registration.catonetworks.com
  - https://epp.catonetworks.com
  - https://epp.us1.catonetworks.com
  - https://epp.in1.catonetworks.com
  - https://epp.jp1.catonetworks.com
  - https://cc2.catonetworks.com
  - https://cc2.us1.catonetworks.com
  - https://cc2.in1.catonetworks.com
  - https://cc2.jp1.catonetworks.com
  - https://socketlogs.catonet.works
  - https://client-telemetry.main.prod.k8s.catonet.works
  - https://cato-15a028ee-1898-449e-8dbe-7056f3093fa6.2d7dd.cdn.bitdefender.net
- The following executables, located in C:\Program Files\Cato Networks\CatoEndPointProtection\bin\, are allowlisted:
  - cato-endpoint-protection.exe
  - CatoEppCli.exe
  - CatoEPPClient.exe
  - RegistrationTokenInsertion.exe

#### Windows Server Prerequisites

- Windows Server 2016, 2019, and 2022 are supported on agent version 1.2 and higher
- The server is a Windows Server Standard Edition or Windows Server Datacenter Edition
- The server has a Graphical User Interface
- For Windows Server 2016, .NET 4.8 or newer must be installed manually, even with the .exe installer

#### Account Prerequisites

- Your account has an endpoint protection license
- You know your account's **Agent Token**. Endpoints are only protected if the EPP solution is registered to an account with the **Account Token**. For more information, see [Associating EPP to your Account](/v1/docs/installing-the-cato-epp-solution#associating-epp-to-your-account).

## Distributing EPP to Endpoints

To distribute Cato's EPP solution to endpoints in your environment, Cato supports using a Mobile Device Management system. Cato's EPP Agent can also be manually installed.

### Associating EPP to your Account

The **Agent Token** is a unique token for your account that is used during the installation process. The Agent Token associates the EPP Agent to your account.

![Agent_Token.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28851104582941.png)

**To show the Agent Token:**

1. From the navigation menu, click **Security > Endpoint Protection**.
2. Click the **Setting** tab.

The **Agent Token** is displayed

> [!NOTE]
> Note:
> 
> You can refresh your Agent Token by clicking the refresh button. After the token is refreshed there is no impact on endpoints already associated with your account. To associate new endpoints to your account, use the updated Agent Token.

### Downloading EPP

You can download the EPP Agent to distribute or install it on the endpoints in your environment. An EXE and MSI version are available for download.

> [!NOTE]
> Note:
> 
> The EPP solution is only available with an additional license. For more information, contact your sales representative.

![Download_Agent.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28851115760669.png)

**To download EPP:**

1. From the navigation menu, click **Access > Client Rollout**.
2. In the **Windows EPP Client** widget, click **Download Client**.
3. Choose the file type to download.

The EPP solution is downloaded.

### Installing EPP with an MDM

To install EPP remotely, you can use a managed solution, for example, Microsoft Intune, to deploy the EPP solution to endpoints in your environment.

**To install EPP with an MDM:**

- Use the following command to install EPP:
  - For the MSI version:

`msiexec.exe /i "&lt;installer-path&gt;" /l*v &lt;logs-filename&gt; REGISTRATION_TOKEN=&lt;Agent-Token&gt;`

**Note**: Ensure the required installations are installed on the endpoint. For more information, see the Prerequisites.
  - For the EXE version:

`CatoEndPointProtection-&lt;version&gt;-win64.exe /q /l*v &lt;logs-filename&gt; REGISTRATION_TOKEN=&lt;Agent-Token&gt;`

### Installing EPP Manually

After you download the installation file, follow the steps in the Cato Endpoint Protection Setup Wizard. When prompted, insert the **Agent Token**.

## EPP Troubleshooting

Errors may occur when installing EPP. Error messages are displayed in the **Protected Endpoints** table, under the **Status** column. If there is an error, the endpoint is not protected. For information about the different error messages and to resolve them, see [Understanding EPP Error Messages](/v1/docs/understanding-epp-error-messages).

These are the error messages that could be displayed and how to resolve them:

## Understanding the Enduser Experience

The EPP solution is located in the Windows system tray and creates alerts for blocked activities according to the **Protection** level set in the **Profile**.

### The EndPoint Protection Agent

![image__3_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28851115786013.png)

Endusers can use the Agent to confirm that the endpoint is protected and to display basic **Statistics** and **Settings**. For example the Profile and the engines that are running,

Anti-Malware and Behavioral Protection scans use minimal resources and are invisible to the enduser.

### System Alerts

![2023-03-16_22-39-07.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28851115821085.png)

If malicious activity is identified on an endpoint a system alert is displayed to the enduser. The alert displays the path of the malicious file and the file status. This information is also visible in Windows notifications.

Access to the file is determined by the **Protection** level set in the **Profile**.

> [!NOTE]
> Note:
> 
> To receive system alerts, the EPP solution must be open and Windows notifications enabled on the endpoint.
