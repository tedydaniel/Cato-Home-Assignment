---
title: "Troubleshooting Cato Windows Client Installation Issues During Upgrades"
slug: "troubleshooting-cato-windows-client-installation-issues-during-upgrades"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/troubleshooting-cato-windows-client-installation-issues-during-upgrades"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Cato Windows Client Installation Issues During Upgrades

This article describes upgrade issues for the Cato Windows VPN Client and suggested solutions for the following common installation errors:

- The Client installation fails with error code 1603
- The Client installation fails with the error message: "Installation Failed – Another version of this product is already installed"
- The Client installation fails with the error message: "The older version of Cato Client cannot be removed. Contact your technical support group"

## Solving the Cato Client Upgrade Failures

If you are trying to upgrade the Cato Windows VPN Client and the upgrade fails, these are recommended solutions to help you upgrade the Client to the new version. Start with the first solution, and if the problem continues, go on to the next solution.

1. From the Windows command line, reinstall the new VPN client: ***msiexec /i setup.msi REINSTALL=ALL REINSTALLMODE=vomus***
2. Uninstall the current VPN client version and then install the new version.
  - To make sure that the Client is completely removed from the computer, perform the following steps:
    - Check the registry and remove the Cato Client entry. For more about removing the registry key for the Cato Client, see [How to uninstall Windows VPN Cato Client via MsiExec exe.](/v1/docs/how-to-uninstall-the-windows-client-using-msiexec-exe)
    - Check the Windows settings "Apps & Features", if the Cato Client application exists in the list of the installed applications, uninstall it.
    - Open Windows **Task Manager > Services** tab, and check if the **CatoNetworksVPNService** is listed. If it does, stop and then uninstall the service from the command line. We also recommend to check and make sure there are no running processes for the Cato VPN Client (also in the Windows **Task Manager > Processes** tab).
3. Uninstall the current SDP client version and reinstall the same version again, and then install the new version.
  - If the below error is encountered during uninstallation of the current VPN client, perform the following steps: ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16282147944477.png)
    - Check the version of the SDP Client currently in use.
    - If you happen to still have the MSI of the current installed version, run this command (as an admin) to uninstall the current package. If you do not have the MSI of the current installed version, contact [Cato Support](/v1/docs/submitting-a-support-ticket) to request for one.

```plaintext
msiexec /x c:\<path to the msi installer of current version>
```
    - Reboot the device
    - Run this command (as an admin) to install the new version

```plaintext
msiexec /i c:\<path to the msi installer of new version>
```
4. If step 3 didn't work, then as a last resort, follow this [Microsoft article](https://support.microsoft.com/en-us/topic/fix-problems-that-block-programs-from-being-installed-or-removed-cca7d1b6-65a9-3d98-426b-e9f927e1eb4d) on how to fix problems that blocks programs from being installed or removed.
