---
title: "How to Remove macOS SDP Client User Profiles"
slug: "how-to-remove-macos-sdp-client-user-profiles"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-remove-macos-sdp-client-user-profiles"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Remove macOS SDP Client User Profiles

## Issue

In macOS, it isn't enough to send the SDP Client to trash for User Profiles to be removed from the Client. They will continue to show up after re-installing the Client.

## Environment

- macOS SDP Client (any version)

## Solution

User Profiles can be manually removed one-by-one from the client UI. Hover over each user profile and click the delete button:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20555561631261.png)

If there are issues removing profiles manually or if Always-On is enabled, user profiles can also be deleted from a macOS directory. The following steps describe the process to remove User Profiles this way:

- Remove the SDP Client from the Computer. You can do so from the Applications folder.
- Remove all CatoClient system extensions from /Library/SystemExtensions/../com.catonetworks.mac.CatoClient.CatoClientSysExtension.systemextension
- Go to Terminal and run:

```plaintext
cd /Users/username/Library/Group Containers
ls
```
- You should see a directory called: CKGSB8CH43.group.
- Run:

```plaintext
rm -rf CKGSB8CH43.group/*
rm -rf CKGSB8CH43.group
```
- Deleting that directory will clear all but the primary profile (used in the last connection). That one will need to be removed manually from the SDP Client in any case.
- After re-installing the SDP Client, you will see that the directory CKGSB8CH43.group is recreated.
