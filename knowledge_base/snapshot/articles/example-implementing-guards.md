---
title: "Example Implementing Guards for a Chat Bot"
slug: "example-implementing-guards"
updated: 2026-07-06T13:38:06Z
published: 2026-07-06T13:38:06Z
canonical: "knowledge.catonetworks.com/example-implementing-guards"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Example Implementing Guards for a Chat Bot

Securing AI Applications with Cato Guards (Sample Configuration)
---
 
## Overview
 
This guide walks you through the end-to-end process of securing a custom AI application using Cato AI Security Guards. It is structured as a three-stage flow, each building on the previous one, so you can see exactly what changes at each step and why.
 
The application used throughout this guide is **TravelBot** — a simple AI-powered travel assistant chatbot. While the example is specific, the concepts and steps apply to any custom AI application you build and want to protect.
 
The guide covers three stages:
 
- **Stage 1** establishes the baseline: a working AI application communicating directly with an LLM, with no security controls in place. This stage helps you understand the starting point and the risks it introduces.
- **Stage 2** introduces the guard: a Cato Proxy Guard is created and inserted between the application and the LLM. Traffic is rerouted through the guard, which begins logging all interactions. No policy rules are configured yet — the goal at this stage is simply to verify that the flow still works with the guard in place.
- **Stage 3** activates enforcement: interaction policy rules are configured and published, instructing the guard to block jailbreak attempts and monitor health-related content. The application is now fully protected.
By the end of this guide, you will have a clear picture of how a custom AI application can be secured with Cato Guards — from a completely open connection to an actively enforced, monitored, and governed AI workflow.
 
---

## Stage 1 — The Baseline: Your AI App Without a Guard

---

### What This Stage Covers

Before we introduce any security controls, it's important to understand how the application works on its own. This stage walks you through the baseline setup — a working AI-powered chat application that communicates directly with a large language model (LLM). Think of this as the "before" picture: the app is functional, but there is nothing yet standing between the user and the model.

---

### How the App Works

The application is a simple travel assistant chatbot called **TravelBot**. It consists of three components that work together:

**1. The Frontend**
This is what the user sees and interacts with — a chat interface in the browser where they can type questions and receive responses.

**2. The Backend**
This is the engine running behind the scenes. It receives the user's message, keeps track of the conversation history, and passes the message along to the LLM. It also handles errors and returns the model's response back to the user. The backend is built with Flask, a lightweight web framework.

**3. The LLM Connection**
This is where the intelligence lives. The backend sends the user's message (along with the conversation history) to a large language model, which generates a response. At this stage, the backend communicates with the LLM directly — there is nothing in between.

The flow looks like this:

```
User (browser) → Backend (Flask) → LLM → Response back to User
```

---

### A Note on Language and Framework

The sample application in this guide is built with **Python**, using a lightweight web framework called Flask. Python is a popular choice for AI application development, but it is by no means the only one. The same concepts and flow apply whether your application is built in Node.js, Java, Go, or any other language. The configuration values, the request structure, and the guard integration all follow the same logic — only the syntax changes.

---

### The Configuration File

The connection between the backend and the LLM is controlled by a file called `config.py`. This file holds three critical values:

```python
OPENAI_API_KEY = "sk-proj-xK92mLqP3nVwTz8YdR5eN1uJbF7cQm4HsAo6WpGi0XvCl"
BASE_URL       = "https://bedrock-mantle.eu-north-1.api.aws/v1"
MODEL_ID       = "amazon.nova-pro-v1:0"
```

- **`OPENAI_API_KEY`** — This is the credential that proves to the LLM provider that your application is authorized to make requests. 
- **`BASE_URL`** — This is the address the backend sends requests to. Right now, it points directly at the LLM provider.
- **`MODEL_ID`** — This tells the LLM provider which specific model to use when generating responses.

To get the app running at this stage, you (or your developer) would fill in these three values with the credentials provided by your LLM provider.

---

### What the App Does With Your Message

When a user sends a message, here is what happens step by step:

1. The user types a message in the chat interface and hits send.
2. The browser sends the message to the Flask backend, along with a session ID that identifies the conversation.
3. The backend adds the message to the conversation history and forwards everything to the LLM, prepending a system instruction that tells the model to behave as TravelBot.
4. The LLM processes the full conversation and generates a reply.
5. The reply is sent back to the backend, added to the conversation history, and returned to the user's browser.
6. The user sees the response in the chat interface.

---

### What Is Not Happening Yet

At this stage, the application is fully functional but completely unprotected. This means:

- There is **no inspection** of what the user sends to the model.
- There is **no inspection** of the tool calls and responses.
- There is **no policy enforcement** — any message, including malicious ones, reaches the LLM.
- There is **no visibility** into how the application is being used.

A user could, for example, attempt to manipulate the model into ignoring its instructions, extract sensitive information, or use the application in ways that violate your organization's policies — and none of it would be detected or stopped.

This is exactly the gap that the next stage addresses.

---

### Summary

| Component | Role | Details |
|-----------|------|---------|
| Frontend | User interface | Chat UI served by Flask |
| Backend | Request handling | Flask app, manages conversation history |
| LLM Connection | Response generation | Direct connection via `BASE_URL` and `OPENAI_API_KEY` |

---

## Stage 2 — Introducing the Guard

---

### What This Stage Covers

In Stage 1, we established a working AI application that communicates directly with an LLM. The app works, but there is nothing standing between the user and the model. In this stage, we introduce a **Cato AI Security Guard** — the enforcement layer that sits between your application and the LLM, inspecting traffic in real time before it reaches the model and before responses are returned to the user.

By the end of this stage, all LLM traffic, user messages, tool definitions, tool use, etc., go through Cato. The user experience remains identical — but now every interaction is inspected and can be controlled.

The updated flow looks like this:

    
![Application-Proxy Mode.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Application-Proxy%20Mode(1).png){height="" width=""}

---

### What Is a Guard?

A guard is the enforcement point for AI Security. In this example, in which we're using Proxy Mode, it acts as an intermediary — sitting between your application and the LLM — and evaluates every prompt and response against the policies you define. Based on those policies, the guard can allow, block, or log an interaction.

There are three types of guards. For this guide, we are using a **Proxy Guard**. In proxy mode, the guard sits fully inline in the traffic path. Your application sends requests to the guard's endpoint instead of directly to the LLM, and the guard forwards them on after inspection. No changes to your application's logic are required — only the destination address changes.

---

### Step 1 — Create the Guard in the Cato Management Application

The first step is to create the guard as a logical entity in the Cato Management Application. This is done in the UI — no code required at this point.

1. From the navigation menu, select **AI Security > Guards**, then click **New**.
2. Enter a descriptive **Guard Name**. In our example, we use `E2E Sample Use Case`.
3. Under **Select Guard Type**, choose **Proxy**.
4. Under **Select AI Service**, choose **Custom Endpoint** from the dropdown. This option works with any OpenAI-compatible endpoint, which is what our application uses.
5. In the **Endpoint URL** field, enter the URL of your LLM provider. In our example, this is `https://bedrock-mantle.eu-north-1.api.aws/v1`. This is the same URL that was previously set as `BASE_URL` in `config.py` — you are now handing this address to the guard rather than using it directly in your application.
**Note:** The URL must include the path up to, and including, the /v1.
7. Under **Configure Guard Settings**, leave **Guard's Host** set to **Cato's Cloud**. This means the guard is managed and hosted by Cato — you do not need to deploy or maintain any additional infrastructure.
8. Click **Save**.

> **What just happened?** You have created a guard that knows where your LLM lives. Cato will now act as the intermediary for all traffic between your application and that LLM. The guard does not yet have any policy rules — we will add those in Stage 3. For now, we are simply establishing the connection and verifying the flow still works.

---

### Step 2 — Retrieve the Guard's Connection Details

Once the guard is saved, open it from the Guards page and navigate to the guard's **Docs** page, which provides everything your application needs to connect to the guard instead of connecting directly to the LLM.

You will find two key pieces of information here:

* The Guard Endpoint (your new `BASE_URL`) - This is the address your application will now send requests to: `https://api.aisec.catonetworks.com/fw/v1/proxy/openai`

    * This replaces the LLM's endpoint URL in your configuration. From this point on, your application talks to Cato, and Cato talks to the LLM on your behalf.

* The Guard API Key (your new `OPENAI_API_KEY`)
    * The Docs page also provides a **Guard API Key** — the credential your application uses to authenticate with the guard. This replaces the LLM API key that was previously in your configuration. It looks like this: `cato-1234-abcde`


> **Note:** Cato provides two Guard API Keys. You only need one to make requests. The second key exists so you can rotate credentials safely — you can update your application to use the new key while the old one is still active, avoiding any downtime.
> 
#### The LLM API Key

Previously, the LLM API key lived in your application's configuration. With the guard in place, that key moves into the request headers that your application sends to the guard — specifically in a header called `x-cato-provider-api-key`. The guard uses this to authenticate with the LLM on your application's behalf.

This is actually a security improvement: the LLM API key is no longer hardcoded in a configuration file, and the guard acts as the controlled pass-through for that credential.

---

### Step 3 — Update the Application Configuration

Now that the guard is created and you have its connection details, it is time to update the application. To keep Stage 1 and Stage 2 clearly separated, we create a new set of configuration files rather than overwriting the originals. This way, both stages remain intact for reference.

The new configuration file, `config_stage2.py`, reflects the updated connection details:

```python
# Stage 2 configuration — routing through the Cato Proxy Guard

GUARD_API_KEY        = "cato-xxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
BASE_URL             = "https://api.aisec.catonetworks.com/fw/v1/proxy/openai"
MODEL_ID             = "amazon.nova-pro-v1:0"
LLM_PROVIDER_API_KEY = "[SECRET_1]"   # Your LLM provider API key — passed to the guard, not the LLM directly

SYSTEM_PROMPT = (
    "You are TravelBot, a friendly and knowledgeable travel assistant. "
    "Help users discover destinations, plan itineraries, recommend hotels, "
    "and share practical travel tips. Keep responses concise and enthusiastic. "
    "If a question is unrelated to travel, politely redirect the conversation."
)

MAX_TOKENS = 1024
```

The key differences from Stage 1:

| Parameter | Stage 1 | Stage 2 |
|-----------|---------|---------|
| `OPENAI_API_KEY` | LLM provider API key | Replaced by `GUARD_API_KEY` — authenticates with the guard |
| `BASE_URL` | LLM provider endpoint | Cato guard proxy endpoint |
| `LLM_PROVIDER_API_KEY` | Did not exist — was `OPENAI_API_KEY` | LLM API key, now passed as a request header to the guard |

---

### Step 4 — Update the Client Code

The client code also gets a corresponding Stage 2 version — `bedrock_client_stage2.py`. The logic is largely the same as Stage 1, with two additions:

1. The Guard API Key is used to authenticate with the guard (in the `Authorization` header).
2. The LLM API key is passed as an additional header (`x-cato-provider-api-key`) so the guard can forward it to the LLM.
3. The session ID is passed as a header (`x-cato-session-id`) so the guard can group requests from the same conversation together — this maps directly to the `session_id` that already exists in the application logic.

```python
# bedrock_client_stage2.py

from openai import OpenAI
from config_stage2 import GUARD_API_KEY, BASE_URL, MODEL_ID, LLM_PROVIDER_API_KEY, SYSTEM_PROMPT, MAX_TOKENS


class BedrockClient:
    def __init__(self):
        self._client = None

    def _get_client(self) -> OpenAI:
        if self._client is None:
            self._client = OpenAI(
                api_key=GUARD_API_KEY,
                base_url=BASE_URL,
                default_headers={
                    "x-cato-provider-api-key": LLM_PROVIDER_API_KEY,
                }
            )
        return self._client

    def invoke(self, messages: list[dict], session_id: str = "") -> str:
        all_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

        response = self._get_client().chat.completions.create(
            model=MODEL_ID,
            messages=all_messages,
            max_tokens=MAX_TOKENS,
            extra_headers={
                "x-cato-session-id": session_id,
            }
        )

        return response.choices[0].message.content
```


---

### Verifying the Flow

Once the updated configuration and client files are in place, the application should behave exactly as it did in Stage 1 from the user's perspective. TravelBot responds to travel questions the same way — but now every interaction is passing through the guard.

At this point the guard has no policy rules configured, so it is not blocking or modifying any traffic. It is, however, logging every interaction. You can verify this by opening the guard in the Cato Management Application and reviewing the **Guard Logging** page, where you should see sessions appearing as the application is used.

This confirms that the integration is working correctly and the guard is receiving traffic.

---

### Summary of Changes from Stage 1 to Stage 2

| What Changed | Stage 1 | Stage 2 |
|---|---|---|
| Where traffic goes | Directly to the LLM | Through the Cato guard proxy |
| Authentication | LLM API key in config | Guard API key in config; LLM key passed as a header |
| Visibility | None | Full session logging in Cato |
| Policy enforcement | None | None yet — coming in Stage 3 |
| User experience | Unchanged | Unchanged |

---

## Stage 3 — Configuring Policy Rules

---

### What This Stage Covers

In Stage 2, we introduced the guard and verified that traffic is flowing through it correctly. The guard is active, but it is not yet enforcing any rules — it is observing traffic without acting on it. In this stage, we configure the **Guards Interaction Policy**: the set of rules that tells the guard what to do when it detects specific types of content.

By the end of this stage, the guard will be actively enforcing two rules against live traffic:

- **Block and anonymize** any interaction that includes information like PII or passwords
- **Monitor** any interaction that involves medical advice or health-related data

**Note:** We recommend you first test your rules by setting them to Monitor and moving them to Block after you validate that the detections are working as you expected.

---

### What Is the Guards Interaction Policy?

The Guards Interaction Policy is the rule base for your AI Security guards. Think of it as a firewall for AI traffic — instead of inspecting network packets, it inspects the content of AI interactions and applies the action you define when a match is found.

Each rule in the policy specifies:

- **Which guard** the rule applies to
- **What to look for** — defined by an Engine Profile, which is the detection category (for example, jailbreak attempts, PII, or medical data)
- **What to do** when a match is found — Block, Monitor, Anonymize & Block, or Anonymize & Monitor
- **Which direction** of traffic to inspect — incoming messages from the user, responses from the assistant, tool inputs, or tool outputs

One important behavior to be aware of: rules in the Guards Interaction Policy are evaluated regardless of their position in the rule base. If more than one rule applies to an interaction, the stricter action wins. For example, if one rule says Monitor and another says Block, the Block action is applied.

---

### Step 1 — Create Rule 1: Block Jailbreak Attempts

The first rule we create targets jailbreak attempts — deliberate efforts by users to manipulate the model into ignoring its instructions or bypassing its safeguards. For a customer-facing application like TravelBot, this is a meaningful risk: a user could attempt to force the model to behave outside its defined role or expose information it should not.

To get started, navigate to the Guards Policy page. You can do this either from the main navigation menu by selecting **AI Security > Guards Interaction Policy**, or directly from the guard's **Overview** page by clicking **Manage Policy** under the Active Rules section.

From the Guards Policy page, click **New** to open the rule editor, then configure the following:

**General**
- **Name**: `Block Some Traffic`
- **Description**: `This blocks jailbreak traffic from our travel bot`
- Leave the **Enabled** toggle on

**Guards**
- Select `E2E Sample Use Case` — this scopes the rule to our specific guard and does not affect any other guards in the account

**Engine Profile**
- Select `Sensitive Identifiers` — this is the detection category that identifies prompt injection attempts, jailbreak patterns, and attempts to extract secrets or credentials from the model

**Action**
- Select `Anonymize & Block` — when the guard detects a match, it will anonymize any sensitive data present in the interaction and block the prompt from reaching the LLM entirely

**Direction**
- Check `User` and `Tool Input` — the rule applies to content coming from the user and from any tool inputs. Responses from the assistant and tool outputs are not in scope for this rule.

Click **Save**. The rule is saved to an unpublished revision and will not yet affect live traffic.

---

### Step 2 — Create Rule 2: Monitor Medical Content

The second rule takes a different approach. Rather than blocking traffic, it allows interactions to proceed while flagging them for review. This is appropriate for content that is not necessarily malicious but may warrant visibility — in this case, interactions involving medical advice or health-related data.

For TravelBot, a user asking for medical travel advice (such as vaccination requirements or health precautions for a destination) is not inherently harmful, but it is the kind of content your organization may want to track for compliance or quality purposes.

From the Guards Policy page, click **New** again and configure the following:

* General
    * **Name**: Monitor Potentially Harmful Data
    * **Description**: This allows the communication to go through, but monitors the interactions
    Leave the **Enabled** toggle on

**Guards**
- Select `E2E Sample Use Case`

**Engine Profile**
- Select `Health Data Exposure` — this detects interactions that involve medical guidance, health data, or clinical information

**Action**
- Select `Anonymize & Monitor` — the interaction is allowed through to the LLM and the response is returned to the user as normal. Any personalized information is anonymized to protect personal details. The interaction is logged in Cato for review.

**Direction**
- Check all four directions: `User`, `Assistant`, `Tool Input`, and `Tool Output` — this rule monitors traffic in every direction, giving you full visibility into both sides of the conversation

Click **Save**.

---

### Step 3 — Publish the Policy

After saving both rules, the Guards Policy page will show an **Unpublished Revision** status and a **Publish (2)** button in the top right corner, indicating that two rules are ready to go live.

> **Important:** Until you publish, the active policy is unchanged. Your rules exist in a draft state and are not enforced against live traffic. This gives you the opportunity to review your changes before they take effect.

When you are ready, click **Publish (2)**. Both rules become active immediately and the guard begins enforcing them on all incoming traffic.

![sample-guard-policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/sample-guard-policy.png){height="" width=""}

---

### What the Guard Is Now Doing

With both rules published, every interaction that passes through the `E2E Sample Use Case` guard is now evaluated against the policy. Here is what that looks like in practice:

A user sends a message to TravelBot. Before the message reaches the LLM, the guard inspects it against both rules:

- If the message contains a jailbreak pattern or an attempt to extract secrets, the guard anonymizes and blocks it. The LLM never sees the message, and the user receives a blocked response.
- If the message contains medical advice or health-related content, the guard allows it through but logs the interaction for review.
- If the message matches neither rule, it passes through to the LLM unaffected.

The same evaluation applies to responses from the assistant, tool inputs, and tool outputs, depending on the directions configured for each rule.

---

### Verifying the Rules Are Active

To confirm that the rules are active and applied to your guard, navigate to the guard's **Overview** page. Under **Active Rules**, you should now see both rules listed. The Interactions Over Time chart and Violations Breakdown panel will begin populating as traffic flows through the guard and detections occur.

You can also navigate to **Guard Logging** to review individual sessions, see which rules fired, and inspect the details of flagged interactions — provided you have the necessary permissions to view sensitive content.

---

### Summary

| Rule | Engine Profile | Action | Direction |
|------|---------------|--------|-----------|
| Block Some Traffic | Secrets & Jailbreak | Anonymize & Block | User, Tool Input |
| Monitor Potentially Harmful Data | Medical Advice or Data | Monitor | All directions |

With these two rules in place, the application now has active security enforcement. Malicious prompt attempts are blocked before they reach the model, and sensitive health-related interactions are visible to your security team — all without any changes to the application code or any impact on the end user experience for legitimate interactions.

---

*This completes the end-to-end guide for securing a custom AI application with Cato AI Security Guards.*
