---
title: "Understanding EPP Error Messages"
slug: "understanding-epp-error-messages"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/understanding-epp-error-messages"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding EPP Error Messages

This article provides information about the different EPP error messages and how to resolve them.

> [!NOTE]
> Note:
> 
> The error messages in this article are available starting from EPP Agent 1.3.1.

## Error Messages

- **Internal engine error**: This error means that the agent did not initiate correctly. To resolve this issue, on the **Access > Protected Endpoints** page, click the three dots alongside the host that has the error and select **Reset Service**. If this does not resolve the issue, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Mismatch driver in the behavioral module**: An internal driver does not match the expected version. Try updating the drivers, and if this does not resolve the issue, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Insufficient memory resource**: There was insufficient memory when trying to initiate the EPP agent. The agent will attempt to initiate again on its own, and if this fails, on the **Access > Protected Endpoints** page, click the three dots alongside the host that has the error and select **Reset Service**.
- **Error in module(s): atc/onaccess/selfprotect**: There is an issue with the EPP engine(s). To resolve this issue, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Detected conflicting anti-virus:** EPP cannot be activated because another anti-virus (AV) software has been detected on the machine. Remove the additional anti-virus software and restart the EPP agent.
- **C++ redistributable is missing or out-of-date (please install C++ redistributable 2019 or later)**: Verify that the C++ Redistributable version is installed and the version is later than 2019. After you install the package, reboot the computer for the changes to take effect.
- **Drivers are not installed correctly**: This error means that the solution has not been installed correctly and cannot run the EPP engine(s). To resolve this issue, on the **Access > Protected Endpoints** page, click the three dots alongside the endpoint that has the error and select **Reinstall Drivers**. If this does not resolve the issue, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- **Installation not complete**: Ensure the device has c++redist 2019 or later installed and reboot. If this issue persists, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

For more information about the different actions you can perform, see [Managing the Endpoint Protection Solution](/v1/docs/managing-the-endpoint-protection-solution).

## Uploading Logs to Cato Support

Sometimes Cato needs the agent logs to help understand and resolve issues. The logs from an agent can be sent directly to the Cato Technical Support team to investigate.

**To upload logs to Cato Support**

1. From the navigation menu, click **Access > Protected Endpoints**.
2. Click the three dots of the endpoint that you want to upload the logs of.
3. Click **Upload logs**.
4. On the **Actions History** tab, send the support team the Reference ID found in the **Details** column of the **Upload Logs** action.
