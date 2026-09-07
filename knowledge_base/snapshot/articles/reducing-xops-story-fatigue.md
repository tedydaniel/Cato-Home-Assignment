---
title: "Reducing XOps Story Fatigue"
slug: "reducing-xops-story-fatigue"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/reducing-xops-story-fatigue"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reducing XOps Story Fatigue

This article provides recommendations for identifying XOps stories that can be muted to reduce story fatigue.

## Overview

XOps provides advanced visibility and control over security events through the Stories Workbench. However, excessive or repetitive alerts can overwhelm security teams and obscure genuine threats, a challenge known as alert fatigue. When analysts face large volumes of stories, including low-value or redundant notifications, they risk overlooking critical incidents that require immediate attention.

The recommendations in this article help identify stories that do not need story generation and create [Mute Stories](/v1/docs/muting-xops-stories) rules that help streamline alert management. By doing so, organizations can maintain focus on high-priority stories while reducing unnecessary noise.

You can then note the impact of these changes by comparing alert volumes, reviewing analyst workload, and confirming that no critical detections were inadvertently muted, ensuring that alert reduction improves efficiency without sacrificing security visibility.

## Identifying Stories to Mute

These are some examples of stories that could be muted to reduce story fatigue. These best practices are recommended based on Cato's experience. However, they are not mandatory, and you can mute any stories that are not relevant or helpful for your organization’s triage process.

### Stories Originating from Guest Networks

Guest networks are typically isolated environments designed for visitors or temporary access. Activity on these networks often includes routine browsing, updates, or legitimate external communications that may resemble low-level threat behaviors. By filtering or muting stories generated from guest networks, you can reduce the number of stories without compromising visibility into the managed corporate environment.

To mute Stories originating from your guest network, create a Mute Stories rule and set the **Source** to the IP range of your guest network.

### Stories Originating from Unmanaged Mobile Devices

Unmanaged devices, such as employee-owned smartphones or tablets, are not centrally controlled or monitored by corporate security tools. These endpoints can generate Stories that appear anomalous simply because they operate outside the organization’s security baseline. Identifying and suppressing stories from such devices ensures that analysts spend time on Stories tied to managed, higher-value assets.

To mute Stories originating from an Unmanaged mobile device, create a Mute Stories rule and set the **Device** to iOS and Android.

### Stories Triggered by Penetration Testing or Security Assessment Tools

Security testing platforms, or internal red team tools, often simulate attacks to validate system resilience. These actions can produce predictable, repetitive stories that clutter the analysis view. By recognizing and muting stories associated with scheduled tests, teams can prevent false positives while maintaining oversight of real-world threat activity.

To mute stories that are triggered by penetration testing or a security assessment tool create a Mute Stories rule and set the **Source** as the user running the tests or the IP of the security scanner in your network.

## Measuring the Impact

After one month, review the effectiveness of your mute rules and overall alert-tuning process to ensure that story volume has decreased without losing visibility into meaningful threats. To support this validation, you can set an expiration date on mute-story rules. The rule applies only within the defined timeframe, helping you confirm that it isn’t too broad or unintentionally suppressing important alerts. Once you’re confident in its accuracy, you can extend the rule’s expiration or make it permanent as part of your ongoing tuning workflow.

### Compare the Number of Total vs. Muted Stories

Track the total number of stories generated before and after implementing mute rules. A significant reduction in low-risk or repetitive stories indicates that the filters are working as intended. This data can also highlight areas where additional fine-tuning may be needed to maintain a balance between alert reduction and visibility.

### Review Analyst Workload and Story Triage Time

Evaluate how much time administrators or analysts spend investigating new stories. A noticeable decrease in triage time suggests that fewer false positives are being surfaced, allowing teams to focus on genuine incidents. These improvements can directly translate to faster response times and higher overall operational efficiency.

### Refine or Extend Mute Rules Criteria

Based on the results, determine whether certain mute rules can be expanded or need to be narrowed. Adjusting thresholds or entity scopes ensures ongoing optimization of alert coverage. Over time, this iterative approach builds a sustainable framework for reducing noise while preserving strong security posture.
