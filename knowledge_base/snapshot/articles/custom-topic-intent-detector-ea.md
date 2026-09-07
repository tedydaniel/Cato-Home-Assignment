---
title: "Custom Topic & Intent Detector (EA)"
slug: "custom-topic-intent-detector-ea"
updated: 2026-07-12T08:08:15Z
published: 2026-07-12T08:08:15Z
canonical: "knowledge.catonetworks.com/custom-topic-intent-detector-ea"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Topic & Intent Detector (EA)

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information about enabling the feature, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

This feature is part of the licensed AI Security for End Users and AI Security for Applications service.

## Overview

The **Custom Topic & Intent Detector** analyzes user prompts in real time to identify **risky topics and underlying intent** before they are processed by AI applications.

This enables organizations to enforce **acceptable use policies**, prevent misuse, and ensure that AI interactions align with corporate, legal, and regulatory requirements, tailored to their organizational specific needs.

It evaluates each AI interaction with the following:

- Topic – What the user is asking about
- Intent – Why or how the user is asking

### Use Cases

Organizations can define custom topics and intents to match their specific business risks and compliance needs. Use cases include:

- Attempts to access or expose confidential company information, not covered by predefined detectors
- Organization-specific IP assets
- Unique acceptable use standards not covered by standard detectors

### Limits for Custom Topics & Intent Detectors

To ensure optimal performance and detection accuracy, the Custom Topic & Intent Detector enforces the following limits:

- **Detector limit** – Up to 5 Custom Topic & Intent Detectors can be enabled per account
- **Input length requirements** – Custom Topic & Intent Detectors must contain a minimum of 3 words and a maximum of 50 words

These constraints are designed to maintain high-quality signal detection, prevent overly broad or ineffective definitions, and ensure consistent policy enforcement across AI applications.

## Best Practices

Custom Topic & Intent detection accuracy and effectiveness depend on how well custom topics and intents are defined. Vague, overly broad, or poorly structured inputs may lead to reduced detection quality or unintended results. Following recommended guidelines is essential for achieving optimal outcomes.

### Be Specific and Avoid Vague Definitions

Clearly defined topics and intents produce more accurate results.

- Overly broad definitions may match too many prompts (high false positives)
- Overly narrow definitions may miss relevant activity (high false negatives)

Examples:

- DON'T use a broad category: Information about our competitors​
- DO include the company name: Information about Sample Company​

### Use Descriptive Phrases Instead of Keywords

Single-word definitions provide weak signals. Descriptive phrases give the model better context, improving precision and reducing false positives.

Examples:

- DON'T use a keyword: Internal system credentials
- DO use phrases: Extracting credentials from internal systems

### Use Action-Oriented Phrasing

The AI Engine evaluates **what the user is trying to do**, not just what they mention. This means that prompts can be detected even without exact keyword matches.

Intent-aware phrasing improves detection accuracy, especially for ambiguous prompts. Use 3–6 word verb phrases that clearly describe user intent.

Examples:

- DON'T use a description: Proprietary network information
- DO describe the action: Requests to access proprietary network security architecture designs

### Avoid Overlapping Definitions

Defining multiple topics or intents with similar meaning reduces effectiveness. These are likely to trigger on the same prompts, adding noise without improving coverage. Consolidate similar concepts into a single, well-defined topic or intent.

### Test and Iterate

Custom Topic & Intent Detectors should be continuously refined based on real usage. It is highly recommended to test and iterate your detectors and profiles in the Playground.

- If detection is too broad, then make definitions more specific
- If detection is too narrow, then expand the definition or rephrase

Start with a balanced configuration and refine based on observed activity.
