---
title: "Managing XOps Story Investigations"
slug: "managing-xops-story-investigations"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/managing-xops-story-investigations"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing XOps Story Investigations

This article discusses how to use the tools in the Stories Workbench to manage story investigations.

For more about the Stories Workbench, see [Reviewing Detection & Response XOps Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench).

## Overview

The Stories Workbench drill-down page provides tools that help your analyst team track and manage the story investigation throughout the story lifecycle. You can perform a number of different actions to manage and record results of the story investigation, such as defining a verdict for the story, or setting the status to closed. You can also post comments on a story to detail the progress of the investigation and aid in collaboration with other team members. The page also lets you create a [Mute Stories](/v1/docs/muting-xops-stories) rule for when you determine that a story is benign and want the XOps engines to stop generating stories for similar incidents.

> [!NOTE]
> Note:
> 
> For MDR customers, please contact `&lt;mdr@catonetworks.com&gt;` to define Mute Stories rules for your account.

### Prerequisites

- Story actions and comments are available for XOps customers. MDR customers can't perform actions or post comments.
- Users with edit permissions can perform story actions and post comments. Users with viewing permissions can view comments.

## Performing Story Actions

The **Story Actions** panel lets you perform various actions to manage the story. These are the actions you can perform:

- Set the **Analyst Verdict** - Define the story as **Suspicious**, **Malicious**, **Informational**, or **Benign**
  - When you set a verdict to **Suspicious**, **Informational**, or **Benign**, you can then also define:
    - **Type** - Select the specific threat type from the dropdown list

When you select a **Type**, details about the type and recommended actions are shown
    - **Classification** - Select a more detailed description of the threat from the dropdown list. The **Classification** section appears only after selecting a **Type**
  - When you set the verdict to **Malicious** you can then also define:
    - The story **Severity**. Possible values are **High**, **Medium**, and **Low**.
    - **Type** - The **Type** section appears only after selecting a **Severity**.
    - **Classification** - The **Classification** section appears only after selecting a **Type**.
- Enter **Additional Info** - Add information relevant to the story
- Set the story **Status** - Possible values are **Closed**, **Open**, **Pending Analysis** (for example, for when the story is awaiting attention from an analyst), and **Pending More Info** (for example, for when a story is awaiting a reply from a customer)
- Add the story to a new Muted Stories rule. For more about mute stories, see [Muting XOps Stories](/v1/docs/muting-xops-stories).

![XDR_Actions_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356143604893.png)

**To perform story actions:**

1. In the story drill-down page, click the **Actions** button.

![XDR_Comment_buttons.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356151247773.png)
2. Click **Manage Story**. The **Story Actions** panel opens.
3. Define the relevant settings in the action sections.
4. Click **Save**. The story is updated with the action settings.

## Commenting on a Story

Use the **Story Comments** panel to post comments that help track the story investigation. When you post a comment, it is visible to all users with permissions to view the story. Additionally, some comments are created automatically by the system to help track significant developments in the story lifecycle, such as when the story is created or when new targets related to the story are identified.

You can delete a comment that you posted, but can't delete other comments. Comments can't be edited. Only text can be entered in a comment.

The number of comments posted for a story appears on the **Comments** button in the story drill-down page.

- Comments are limited to 500 characters
- A single story can't have more than 200 comments

![XDR_Comments.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356128804893.png)

**To comment on a story:**

1. In the story drill-down page, click the **Comments** button. The **Story Comments** panel opens.

![XDR_Comments_comment_button.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356151431453.png)
2. Enter the text for the comment and click ![post_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356138172061.png). The comment is posted.
