---
title: "For Microsoft Azure Sites - Changing Cato vSocket VMs to the Standard D8ls v5 VM Size"
slug: "for-microsoft-azure-sites-changing-cato-vsocket-vms-to-standard-d8ls-v5-vm-size"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/for-microsoft-azure-sites-changing-cato-vsocket-vms-to-standard-d8ls-v5-vm-size"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# For Microsoft Azure Sites - Changing Cato vSocket VMs to the Standard D8ls v5 VM Size

We are informing you that at least one of the Microsoft Azure sites in your account uses a vSocket virtual machine (VM) with the **Standard_D2s_v4** VM size. It is urgent that you plan to resize all the **Standard_D2s_v4** VMs to the **Standard_D8ls_v5** VM size inside your Azure tenant to prevent a future outage for those sites.

There are different procedures to change the VM size based on the site configuration (HA or single vSocket), and the Socket version (above v19 or not). Make sure to follow the correct procedure for each vSocket VM.

## Why Do We Need to Make these Changes Urgently?

Microsoft Azure no longer allows the **Standard_D2s_v4** VM size with more than 2 NICs. Cato’s Azure vSocket requires 3 NICs and Microsoft implemented a validation that prevents these D2s VMs from starting after they are powered off. The **Standard_D8ls_v5** VM size fully supports the Azure vSocket.

## What Changes Do I Need to Make to Single vSocket Sites?

For each site in your account with a single Azure vSocket in your account, change the VM from **Standard_D2s_v4** to the **Standard_D8ls_v5** size. For more information, see the Cato Knowledge Base article: [Changing Azure vSockets to a Different VM Size](/v1/docs/changing-azure-vsockets-to-a-different-vm-size). These are the procedures based on the Socket version:

1. For vSockets running v19.x or higher, resize the VMs from **Standard_D2s_v4** to **Standard_D8ls_v5**.
2. For vSockets that are running versions lower than v19:
  1. (Recommended) Unregister the current vSocket and deploy a new one from the Azure Marketplace. The vSocket deploys to the **Standard_D8ls_v5** VM size to v19.x.
  2. If it necessary to keep the same version, contact the [Cato Support](https://support.catonetworks.com/hc/en-us/requests/new) team to manually recreate the site with the **Standard_D8ls_v5** VM size.

**Note:** The **Standard_D8ls_v5** instance uses 8 vCPU cores and the Standard_D2s_v4 only uses 2 vCPU cores. Ensure that the Microsoft Azure quota for the site region has enough resources for additional vCPU cores. For more information see the Microsoft documentation: [Check Azure resource usage against limits](https://learn.microsoft.com/en-us/azure/networking/check-usage-against-limits).

If you encounter issues during the process to change a VM to a different size, please contact the [Cato Support](https://support.catonetworks.com/hc/en-us/requests/new) team.

## What Changes Do I Need to Make to HA vSocket Sites?

For each HA Azure vSocket site in your account, change the VM instance type from **Standard_D2s_v4** to **Standard_D8ls_v5**. For more information, see the Cato Knowledge Base article: [Changing Azure vSockets to a Different VM Size](/v1/docs/changing-azure-vsockets-to-a-different-vm-size). These are the procedures based on the Socket version:

1. For HA vSockets running v19.x or higher, see the article [Changing Azure vSockets to a Different VM Size](/v1/docs/changing-azure-vsockets-to-a-different-vm-size) for the most up-to-date procedures.
2. For vSockets that are running versions lower than v19:
  1. (Recommended) Unregister the current vSockets and deploy new ones from the Azure Marketplace. The vSocket deploys to the **Standard_D8ls_v5** VM size with v19.x.
  2. If it necessary to keep the same version, contact the [Cato Support](https://support.catonetworks.com/hc/en-us/requests/new) team to manually recreate the site with the **Standard_D8ls_v5** VM size.

**Note:** The **Standard_D8ls_v5** instance uses 8 vCPU cores and the Standard_D2s_v4 only uses 2 vCPU cores. Ensure that the Microsoft Azure quota for the site region has enough resources for additional vCPU cores. For more information see the Microsoft documentation: [Check Azure resource usage against limits](https://learn.microsoft.com/en-us/azure/networking/check-usage-against-limits).

If you encounter issues during the process to change a VM to a different size, please contact the [Cato Support](https://support.catonetworks.com/hc/en-us/requests/new) team.

## What Happens if I Don’t Make these Changes?

For Azure vSockets that are installed on the **Standard_D2s_v4** VM, if the VM instance powers off, the Microsoft validation will prevent the vSocket from starting because the number of NICs exceeds the maximum allowed interfaces. This means that the site would lose all connectivity until the VM is resized to the **Standard_D8ls_v5** VM size.

## Who Do I Talk to If I Have Questions?

Please reach out to the [Cato Support](https://support.catonetworks.com/hc/en-us/requests/new) team.
