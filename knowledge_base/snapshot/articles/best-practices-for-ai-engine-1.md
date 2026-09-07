---
title: "Best Practices for AI Engine"
slug: "best-practices-for-ai-engine-1"
tags: ["AI Sec - Apps", "AI Sec - Users", "AI Security", "Best Practices"]
updated: 2026-07-31T16:01:42Z
published: 2026-07-31T16:01:42Z
canonical: "knowledge.catonetworks.com/best-practices-for-ai-engine-1"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices for AI Engine

## Overview

AI Security controls are most effective when they are deployed in a way that produces accurate, understandable, and operationally useful detections. The Cato AI Security engine helps admins do this by analyzing user prompts, LLM responses, and agentic tool calls in real time to identify sensitive content, risky activity, and unsafe AI usage.

This article explains how to deploy and tune the engine using practical AI Security guidance. It helps admins deploy the engine in a way that improves detection quality, minimizes false positives, and makes policy behavior easier to understand and validate. It also explains how to build coverage gradually, so teams can strengthen AI Security controls without creating avoidable user disruption or operational overhead.

For more information, see [Configuring AI Security Engine Profiles](/v1/docs/configuring-ai-security-engine-profiles-1).

## Start with Clear Protection Goals

Define a clear AI security goal, because it determines what the engine needs to detect and protect against. Engine Profiles group related detectors around a specific protection outcome, making policy logic easier to tune, validate, and maintain. Detectors identify the specific data types, content categories, and risky behaviors that the engine should inspect, giving admins more precise control over what the profile is designed to catch.

Use the detector families that support the protection and operational goals. Some detectors are designed to identify sensitive data such as personal information or confidential business content, while others focus on code, secrets, or unsafe AI activity such as jailbreak attempts and prompt injection. When these goals are mixed together without a clear purpose, profile behavior becomes harder to interpret and tune.

A better approach is to map each profile to a specific protection use case. For example, one profile might focus on personal and regulated data, another on technical secrets and source code, and another on risky AI misuse. This structure makes validation easier and helps admins understand why a specific interaction was flagged.

## Build Focused Profiles

Focused Engine Profiles make detections easier to interpret and tune because they isolate related logic around a narrow protection use case. This gives admins clearer visibility into why an interaction was flagged and makes it easier to validate profile behavior across different detector types, including entities and content.

Profiles can combine detectors with AND, OR, and EXCLUDE logic, which lets admins build more precise detection behavior. This logic is most effective when each profile is narrowly scoped to a specific protection outcome. For example, a profile that focuses on technical secrets should be tuned independently from a profile that focuses on sensitive business information or unsafe prompts.

It is also important to tune entity detection and content detection differently. Entity detection typically identifies specific items in the interaction, such as credentials, account identifiers, or other structured data. Content detection evaluates the broader meaning or context of the interaction, which often requires more careful review and tuning. Treating these detection types as interchangeable can make profile results harder to interpret. For example, it can mislead admins about how to review detections in the Session Explorer and how to interpret why a profile was matched.

To reduce false positives while maintaining strong detection coverage, add exclusions to the profile. When a known safe pattern is repeatedly matched, exclude the pattern to preserve the overall effectiveness of the detection logic. Other approaches often make the overall profile less effective at detecting real risks.

## Tune for Accuracy

Accurate tuning helps admins improve detection quality by reducing false positives without making the profile less effective at detecting real risks. When confidence settings and profile logic are tuned carefully, the engine produces more actionable results and makes it easier to review detections, refine policies, and maintain useful coverage over time.

Set the confidence level according to how much certainty admins want before the engine flags an interaction, and balance that choice against the amount of review overhead they are willing to accept.

- High Confidence requires stronger evidence, which improves precision and reduces false positives
- Low Confidence casts a wider net, which can increase coverage but may also increase review overhead

Detection quality should be evaluated using realistic traffic volume and the percentage of interactions that are flagged, not just the total number of detections. A small number of false positives may be acceptable in a large traffic set, while the same number could be significant in a small sample. Admins should review how often profiles trigger relative to total AI usage and assess whether the resulting signal is operationally useful.

A controlled troubleshooting and tuning process makes it easier to understand which adjustment improved or degraded results. Before changing multiple settings at once, verify the profile logic, confirm that the intended detectors are enabled, and review the selected confidence settings.

## Test with Realistic AI Interactions

Realistic testing helps admins understand how profiles behave in production-like AI interactions before those profiles are relied on for enforcement or review. Use representative prompts, documents, code, and realistic secret formats for both third-party AI apps and internal AI tools.

Simplistic examples can produce misleading conclusions because they do not reflect how users actually interact with AI tools. If a test prompt is too artificial, the result may not accurately represent how the engine will behave in real traffic. The AI Security engine is trained on real-world data, so it produces the best results for actual user prompts. Validate the profiles with test cases that reflect real workflows, realistic content patterns, and the typical AI interactions for your organization.

AI interactions across multiple interactions should also be included in validation because the engine uses conversation context when evaluating risk. Some AI security concerns only become clear across multiple messages, such as gradual disclosure of sensitive information, follow-up prompts that change the meaning of earlier content, or staged prompt injection attempts. Testing only isolated prompts does not fully show how the engine will perform in real conversational sessions.

## Use the Playground for Iterative Validation

[The Playground](/v1/docs/testing-engine-profiles-in-the-playground-1) is the baseline for understanding how the engine detects prompts within a session. It gives admins a controlled way to validate profile behavior, compare expected results, and build confidence that a detection is working as intended before reviewing the same behavior in live AI traffic.

Use the Playground to test one profile at a time with representative prompts and session context. When a prompt is detected in the Playground, the same profile should detect that same prompt under the same conditions. If the prompt is detected in the Playground but not in an AI chat, the issue may not be with the detection logic itself. It may indicate a rule configuration issue in the User Interaction or Guards Interaction policy.

1. Start by confirming that the profile detects the intended content in the Playground.
2. Review expected false positives and validate detected real risks.
3. After changing a profile or detector, repeat steps 1 and 2.

This process makes it easier to separate profile behavior from rule configuration problems and to understand which adjustment changed the result.

## Write Custom Detectors Carefully

Well-defined custom detectors help admins extend AI Security coverage to business-specific content that built-in detectors may not fully address. When a custom detector is narrowly scoped to one clear need, it is easier to validate, easier to tune, and less likely to generate unnecessary noise.

Regex and Custom Topic and Intent detectors serve different purposes.

- Regex is best for content that follows a defined pattern
- Custom Topic and Intent is better for describing a specific content type, business context, or risk scenario that cannot be captured reliably with pattern matching alone

**Note:** Custom Topic and Intent for custom detectors will be available soon.

Define each custom detector for one clear protection use case. Avoid broad definitions that try to cover too many content types or business scenarios at once. Narrow detector logic gives admins better control over what the profile is designed to catch and makes detections easier to interpret and validate.

## Build a Practical Baseline and Expand Gradually

A practical baseline helps admins launch AI Security coverage faster without trying to solve every use case at once. Starting with a focused set of high-value protections makes the initial rollout easier to validate, easier to tune, and easier to expand as AI usage grows. In most environments, the baseline should cover the most common AI security and governance risks. This usually includes:

- Personal data, secrets, and credentials
- Source code and technical identifiers
- Sensitive business information
- For AI Security for Apps - Unsafe AI activity, such as jailbreak attempts, prompt injection, and other harmful content patterns

**Note:** These risks sometimes also apply to AI Security for Users

Expand coverage in phases after the baseline is validated.

1. Start with the most important protection goals.
2. Confirm that profiles behave as expected.
3. Add new use cases as AI usage matures across the organization.

This phased approach is usually more effective than enabling broad coverage all at once and helps reduce operational noise and unnecessary user disruption during early deployment. It gives admins time to refine profile logic based on real usage patterns, and keeps the profile set easier to understand as coverage expands over time.
