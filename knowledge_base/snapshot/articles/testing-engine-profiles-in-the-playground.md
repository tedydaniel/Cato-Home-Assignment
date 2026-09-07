---
title: "Testing Engine Profiles in the Playground"
slug: "testing-engine-profiles-in-the-playground"
updated: 2026-07-12T08:08:15Z
published: 2026-07-12T08:08:15Z
canonical: "knowledge.catonetworks.com/testing-engine-profiles-in-the-playground"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing Engine Profiles in the Playground

The Engine Playground lets you validate how your AI Security Engine Profiles behave before applying them to production AI Interaction Policy rules. It provides a controlled simulation environment where you can test prompts against selected profiles and review detection results in real time.

In the Playground, you choose which profiles to activate, select a predefined testing scenario or create a custom one, and run the simulator. The system evaluates the prompt against the active profiles and shows whether any profile violations were triggered.

![playground-overview.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/playground-overview.png)

This feature helps you:

- Validate detection logic before enforcement
- Identify gaps in profile coverage
- Reduce false positives
- Fine-tune custom detectors and profile combinations

Because profiles are often reused across multiple policy rules, testing them in advance ensures that once they are enforced, they behave exactly as intended.

## Use Case

As a security admin for Company ABC, you recently created a profile called Personal Identifier Protection to prevent employees from sharing sensitive personal data with AI tools.

Before applying the profile to a blocking rule in your AI Interaction Policy, you want to verify that it correctly detects:

- SSNs
- Email addresses
- Customer account numbers (custom regex detector)

You navigate to the Engine Playground and enable only the Personal Identifier Protection profile.

Next, you select the predefined Personal Information scenario and run the simulator. The system evaluates the prompts in the scenario against your profile and shows whether violations were triggered.

You notice that SSNs and email addresses are correctly detected, but your internal account number pattern is not triggering.

You update the custom regex detector, return to the Playground, and run the simulation again. This time, the violation is correctly identified.

Now you are confident that when you apply the profile to a blocking rule, it will behave as expected in production.

## Test Profiles in the Playground

Use the Engine Playground to simulate prompts against selected profiles and review the detection results.

![playground_example.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/playground_example.png)

**To test profiles in the Engine Playground:**

1. From the navigation menu, select **Security > AI Security > Playground**.
2. In the Select Engine Profiles to Activate panel on the left, enable the profiles you want to test.
3. In the Session area, select the scenario you want to use:
  - Choose a predefined scenario, such as:
    - Personal Information
    - Jailbreak & Prompt Inection
    - API Keys & Secrets in Code
  - Or select Custom Session to create your own test prompts

If using a custom session, enter your prompt in the **User Prompt** field
4. Click **Run Simulator**.
5. Review the simulation results.

The system shows how many profiles the prompt was evaluated against. You see whether any Profile Violations were triggered. If violations occur, you can review which profiles were matched
6. Adjust profiles or prompts as needed and run the simulator again to validate your changes:
  - Modify detectors or profile logic
  - Enable or disable additional profiles
  - Update your test prompts
