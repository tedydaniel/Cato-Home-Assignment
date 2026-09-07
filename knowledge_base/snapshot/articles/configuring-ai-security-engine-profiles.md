---
title: "Configuring AI Security Engine Profiles"
slug: "configuring-ai-security-engine-profiles"
updated: 2026-07-12T08:08:15Z
published: 2026-07-12T08:08:15Z
canonical: "knowledge.catonetworks.com/configuring-ai-security-engine-profiles"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring AI Security Engine Profiles

AI Security Engine Profiles let you define how Cato evaluates AI interactions and enforces your AI usage policy. A profile is a logical container for one or more detectors that identify specific types of data, behavior, or content in AI prompts and responses. You attach a profile to an AI Interaction Policy rule, and the rule action determines how Cato handles matching traffic.

Detectors are the building blocks of a profile. Each detector identifies a specific category of content, such as personal identifiers, sensitive business information, secrets, or regulated AI usage scenarios. You can use the predefined detectors provided by Cato, or create custom detectors based on Custom Topic & Intent or regular expressions (regex) to match your organization’s unique requirements.

By separating detection logic (profiles and detectors) from enforcement logic (policy rules and actions), you gain flexibility and reusability. You can apply the same profile across multiple rules and update the profile centrally to immediately affect all associated rules.

After you create a profile, you select it in the Engine Profile field of an [AI Interaction Policy](/v1/docs/working-with-the-ai-interaction-policy-for-user-protection) rule and define the appropriate action, such as Block or another enforcement option.

## Use Case

As a security admin for Company ABC, you are responsible for preventing employees from sharing sensitive data with public AI tools.

You decide to create an Engine Profile called Personal Identifier Protection to detect when users attempt to submit personal or regulated information to AI applications.

First, you create the profile and add predefined detectors from the Personal Identifiers category, including:

- Name
- ID Number/SSN
- Email
- Phone Number

You also create a custom detector using a regex pattern to identify your organization’s internal customer account numbers, which are not covered by the predefined detectors.

Next, you create an AI Interaction Policy rule and select the **Personal Identifier Protection** profile in the Engine Profile field. In the Action section, you choose **Block**.

Now, when a user attempts to enter customer personal information or internal account numbers into an AI application, the interaction is blocked according to the policy.

This targeted approach lets you protect sensitive data without restricting all AI usage across the organization.

## Create an Engine Profile

Create an Engine Profile to group detectors that represent the types of data or content you want to control.

**To create an Engine Profile:**

1. From the navigation menu, select **Security > AI Security > Engine Profiles**.
2. Click **New Profile**.
3. Enter a **Profile Name** and an optional **Description**. Cato recommends that you provide a description that will make it easy to identify the profile when applying it in a rule.
4. Click **Add Detectors**.
5. Select the detectors to include in the profile:
  - Choose from predefined detector categories
  - Or select custom detectors that you previously created
6. Configure the matching logic.

Select whether the profile satisfies **Any (OR)** or **All (AND)** of the selected detectors
7. Click **Apply** and then **Save**.

The profile is now available to select in the Engine Profile field when you create or edit an AI Interaction Policy rule.

## Configuring Detectors

You can create detectors based on predefined categories provided by Cato or define custom detectors to match organization-specific patterns. For each detector, you can configure the confidence level and strings to ignore for the given detector.

The Confidence Level setting determines how strict the detection criteria are.

- A higher confidence level generates fewer alerts and focuses on issues with a higher probability of being true positives.
- A lower confidence level increases sensitivity and can detect more potential issues, but may generate additional borderline or false positive alerts.

Excluding a string lets you define strings that would normally be relevant for the detector, e.g. a proper noun, but you want to ignore for some reason, for example, if it's the name of your company.

### Using Predefined Detectors

Cato provides out-of-the-box detectors organized by category, such as:

- Personal Identifiers
- Code & Technical Identifiers
- AI Usage Regulation
- Sensitive Business Information

These detectors (and more) are ready to use and do not require additional configuration.

**To add predefined detectors to a profile:**

1. During profile creation, click **Add Detectors**.
2. Click **Select from Detectors**.
3. Determine the logic to be applied between the different detectors.
4. Browse or search for detectors in the **Select Detectors** panel.
5. Expand a category, for example, **Personal Identifiers** or **Code & Technical Identifiers** and select the relevant detectors.
6. Click **Apply**.
7. (Optional) In the Profile pane, you can click the 3 dots to the side of a detector to determine:
  - Strings to exclude
  - Confidence thresholds
8. Click **Save**.

### Creating a Custom Detector

Create a custom detector when predefined detectors do not meet your requirements.

You can define a custom detector using:

- Regular expressions (regex) for structured patterns

**To create a custom detector:**

1. During profile creation, click **Add Detectors**.
2. Click **Create Custom Detector**.
3. Enter a **Name** and under **Custom Detector Type**, select either:
  - Regex
4. Define the matching criteria.
  - For regex, enter the regular expression pattern
5. Click **Apply**.
