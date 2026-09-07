---
title: "Install New EPP Agent version 1.4.2"
slug: "install-new-epp-agent-version-1-4-2"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/install-new-epp-agent-version-1-4-2"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Install New EPP Agent version 1.4.2

Cato Networks has detected a bug with the EPP agent failing to load on some devices. Cato Networks has created version 1.4.2 of the EPP agent that resolved the bug and we have begun the automatic gradual deployment.

Any device with a version below 1.4.2 **after 23rd of June** must be manually updated to avoid service interruption of EPP.

Actions Needed:

- Check the EPP agent version on all managed devices via the protected endpoints [dashboard](/v1/docs/managing-the-endpoint-protection-solution) and export the list to filter.

- If the version is earlier than 1.4.2:
  - Deploy the EXE installer using your MDM solution, or
  - Manually run the provided EXE installer on the device.

For detailed instructions to install the EPP agent refer to the Knowledge Base article provided by Cato Networks.

[Installing the Endpoint Protection Solution](/v1/docs/installing-the-cato-epp-solution)

**Note:** This update does not impact the Cato SDP Client or other Cato services.
