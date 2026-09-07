---
title: "How to Uninstall the Windows Client Using MsiExec.exe"
slug: "how-to-uninstall-the-windows-client-using-msiexec-exe"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/how-to-uninstall-the-windows-client-using-msiexec-exe"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Uninstall the Windows Client Using MsiExec.exe

Sometimes you can run into issues with uninstalling a Windows application and MsiExec.exe can help. Make sure that you have the correct globally unique identifier (GUID) for the installed application.

**To uninstall the Windows Client using MsiExec.exe:**

1. From the command line, run **regedit.exe** to open the registry.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\` and right click the **Uninstall** folder and select **Find**.
3. In the **Find** window, search for **Cato Client**.
4. In the Cato Client key, double click the **UninstallString**.

![image-1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218268933789.png)
5. Copy and save the **Value data**.

You will use the data in Step 8.
6. Verify that there are no other uninstall keys in the **..\CurrentVersion\Uninstall\** location:
  1. Press CTRL-F to open the **Find** window and search for **Cato Client** again.

If you find more than one string, save the other strings because they could be causing the problem.
  2. Repeat the previous step until you no longer find all the Cato Client keys within this location.

Ignore any Cato Client keys that are in other locations.
  3. Close the registry.
7. Open a CMD window with administrator privileges.
8. Paste the MsiExec.exe /X string from the registry (for example, **MsiExec.exe /X{DED483C6-2FD4-4B71-8AAD-4AD6761362CB}** ) and run it.
