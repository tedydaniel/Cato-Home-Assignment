---
title: "Windows SDP Client Hangs Due To High CPU Utilization"
slug: "windows-sdp-client-hangs-due-to-high-cpu-utilization"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/windows-sdp-client-hangs-due-to-high-cpu-utilization"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows SDP Client Hangs Due To High CPU Utilization

## Issue

Users running the Windows SDP Client alongside multiple high-resource applications may occasionally experience **high CPU utilization**. This can lead to the **client hanging**, **degraded download/upload speeds**, and a generally **disrupted user experience**.

## Environment

- Windows SDP Client

## Troubleshooting

As a first step, assess possible [SDP Client Performance Issues](/v1/docs/cato-sdp-client-performance-troubleshooting). Once the issue is isolated, proceed with checking the client's utilization within the user's environment.

1. Access **Task Manager** > **Performance** to inspect the current CPU Utilization.

In the following example, the CPU is maxed out at 100% with 280Mbps going through the VPN adapter.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12339829523869.png)
2. Within **Task Manager** > **Details**, locate the process **winvpnclient.cli.exe.** Ensure the **Base Priority** column is visible (right-click on column headers to add it if it is missing). Verify whether the client is being prioritized compared to other running processes.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29383853088925.png)

## Solution

1. Upgrade Windows Client to v5.4 or higher, which includes an updated VPN adapter driver that offloads much of the work from the CPU.
2. Changing the process priority is a workaround to temporarily boost the VPN process's performance over other running processes.

Windows automatically assigns a priority to applications and offers values ranging from '**Low**' all the way to '**High**' or '**Realtime**' priorities. If the Base Priority is the same for multiple processes, the CPU load will be shared equally between them.

Our SDP Client is not prioritized by default and competes for CPU power with all other processes.

To change the process priority, right-click on the **winvpnclient.cli.exe** process and select '**High**' or '**Realtime**' as the priority.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29383853089693.png)

**NOTE:** Setting the Client as 'Realtime' can prioritize the process over Windows system processes and should be used with caution. Also, if the process is killed or restarted, the priority will default back to its normal priority.
3. Alternatively, you can permanently increase the SDP client CPU priority via registry:
  - Navigate to `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN`.
  - Add the DWORD (32-bit) value: `LoopThreadPriority` with a value of `2` (decimal).
  - Restart the **CatoNetworksVPNService**: From Windows Tools > Services, select `CatoNetworksVPNService` and click "Restart the service."
  - If a rollback is needed, remove the registry key and restart the service.
