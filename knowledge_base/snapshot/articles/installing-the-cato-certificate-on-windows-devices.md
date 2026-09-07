---
title: "Installing the Cato Certificate on Windows Devices"
slug: "installing-the-cato-certificate-on-windows-devices"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/installing-the-cato-certificate-on-windows-devices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing the Cato Certificate on Windows Devices

> [!NOTE]
> Note:
> 
> For accounts that are using the 2014 Cato certificate as the default certificate for the account, this certificate will expire on Oct 29. 2025. You need to activate the new 2024 Cato certificate, for more information, see [FAQ for the New Default Cato Certificate for TLS Inspection](https://support.catonetworks.com/hc/en-us/articles/22781778613149#UUID-d5edae38-3ed8-8549-c28e-9ace74f38d1e).

When using the Cato SDP Client, we recommend that you install the Cato CA certificate on the device to provide the best security and user experience. In addition, depending on the settings for your organization, the Cato certificate is required to connect to the network.

The Cato certificate is automatically installed on the Windows device when you install the Cato Client. In some situations, it's necessary to manually install the Cato certificate.

The screenshots and instructions below are based on Windows 11, there may be small differences for other versions of Windows.

**To install the Cato certificate as a trusted certificate on the Windows device:**

1. Download the Cato certificate from the [Client download portal](https://clientdownload.catonetworks.com/).
2. Right-click the Cato certificate file and select **Install Certificate**.
3. If the **Security Warning** pop-up window opens, click **Open**.

The Windows **Certificate Import Wizard** opens.
4. In **Store Location**, select **Current User** or **Local Machine**, and then click **Next**.

The **Local Machine** options requires admin permissions for the device.

![01_local_machine.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700863164829.png)
5. In **Certificate Store**, select **Place all certificates in the following store**, and click **Browse**.

![02_cert_store.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700856915869.png)
6. In the **Select Certificate Store** pop up, choose **Trusted Root Certification Authorities**, click **OK** and then **Next**.

![Select_Store.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700848096669.png)
7. In the **Completing the Certificate Import Wizard**, click **Finish**.

![03_finish.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700857161245.png)
8. In the pop-up window, click **OK**. The Cato certificate is installed on the device.
