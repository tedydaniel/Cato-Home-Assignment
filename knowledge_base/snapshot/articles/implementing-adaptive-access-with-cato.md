---
title: "Implementing Adaptive Access with Cato"
slug: "implementing-adaptive-access-with-cato"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/implementing-adaptive-access-with-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Implementing Adaptive Access with Cato

## Executive Summary

Modern enterprises operate in environments where users, devices, and applications are highly distributed, and access decisions must continuously adapt to changing risk conditions. Static, point-in-time authentication is insufficient to protect against evolving threats such as credential compromise, device misconfiguration, and user-driven risk.

Adaptive access is an architectural approach that enables dynamic access decisions based on continuously evaluated contextual signals, including:

- User risk score
- Device posture
- Authentication confidence
- Network and location
- Application and resource context
- Session integrity
- Threat context

Within the Cato SASE platform, adaptive access capabilities are implemented across multiple control planes and enforced at the PoP. Adaptive access is applied across a range of access methods, ensuring that context-based controls are consistently enforced by the relevant Cato policies. This allows consistent, identity-aware, and context-aware enforcement for connectivity, application access, and network traffic without relying on static trust assumptions.

By combining continuous signal evaluation with policy enforcement, organizations can reduce exposure to compromised users and devices, enforce least-privilege access, and trigger step-up authentication when higher assurance is required. At the same time, administrators gain visibility into user risk, device compliance, and session state, enabling informed operational and security decisions.

## Business Context and Drivers

Organizations need adaptive access to replace static trust with continuous, context-aware decisions across users, devices, and sessions. Trust conditions can change after login, and access control must react to those changes.

Initial authentication and network location are insufficient against credential theft, unmanaged endpoints, and rapidly changing threat conditions.

Cato implements adaptive access through four pillars:

- **Build Trust with Strong Signals:** Adaptive access depends on signals that are current, reliable, and continuously updated. These signals create the foundation for policy decisions during session establishment and throughout the session lifecycle.
- **Unified Trust through Signal Aggregation:** Signals are correlated at the PoP to reflect the current session state. Identity attributes, posture results, and behavioral indicators are evaluated together for each request.
- **Enforce by Trust across Control Planes:** Policies are enforced inline at the PoP across connectivity, application access, and network traffic. The same context is applied consistently to Client Connectivity, ZTNA, and firewall decisions.
- **Trust Visibility for Analysis and Response:** The Cato Management Application (CMA) provides centralized visibility into policy decisions and the signals behind them. A single management console helps admins investigate sessions, validate outcomes, and apply consistent policy changes across control planes.

This approach enables continuous, risk-aware enforcement aligned with Zero Trust, without relying on static trust assumptions.

## Common Use Cases

Adaptive access capabilities in the Cato platform support scenarios where access decisions must change when user, device, or session conditions change.

- **Risk-based access to private applications:** Control access to internal applications based on the current state of the user session and device.
  - Example: A user is allowed to access an internal HR application when the device passes posture checks, and the user risk score remains within the acceptable range. The same user can be blocked from that application in the middle of the session if the risk score increases. For example, they download malware or connect to a known command-and-control domain.
- **Device-aware connectivity control:** Ensure that only compliant and secure devices can establish connectivity to the Cato Cloud.
  - Example: A managed corporate laptop with the required endpoint protection agent is allowed to connect to the Cato Cloud. The same device can be blocked if the endpoint protection is not running the newest version.
- **Step-up authentication for sensitive access:** Require re-authentication when users access sensitive resources or when session assurance is insufficient.
  - Example: A user is allowed to browse standard internal resources with the existing session. When the user attempts to open a sensitive finance application, the policy can require re-authentication before access is allowed.
- **Controlled remote access for users:** Define which users are allowed remote connectivity and restrict others to office-based access only.
  - Example: Employees in approved user groups are allowed remote access to private applications through the Cato Client. Users who are restricted to office-only access are blocked when they attempt to connect remotely.
- **Operational visibility for administrators:** Provide visibility into user sessions and access decisions to support troubleshooting and policy validation.
  - Example: Admins can review why a user was allowed, blocked, or challenged by examining user activity and events in the CMA. For example, the Users Directory page lets you filter users by risk level (such as **High** or **Critical**), and quickly identify users that require investigation.

## Contextual Signals

Adaptive access decisions are based on contextual signals that describe the current state of the user, device, and session. These signals are evaluated continuously and used by CMA policies to determine whether access should be allowed, restricted, or challenged.

- **User Risk Score:** Represents the [current security risk of the user session](/v1/docs/understanding-the-user-risk-level). The score is continuously updated based on behavioral activity and security detections, including:
  - Indicators of systems that have already been compromised
  - Indicators of blocked attempts that could lead to infection
  - Policy violations or risky activities that could potentially lead to compromise
- **Device Posture:** Represents the security state of the endpoint. In the CMA, posture is defined using [Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks). The Cato Client enforces these checks on the device before and during access, and the resulting posture state can be referenced across multiple policies that require device compliance.
  - Device Checks evaluate specific conditions on the endpoint (for example, endpoint protection status, OS version, certificates, or configuration).
  - Device Posture Profiles group one or more checks into reusable profiles that represent a required security baseline.
- **External MDM Compliance:** Extends device posture with signals from external systems such as [Microsoft Intune](/v1/docs/configuring-intune-mdm-compliance-checks-for-device-posture). These signals indicate whether the device complies with organizational policies, such as encryption or patch level.
- **Authentication Confidence:** Represents the freshness and validity of the [user’s authentication token](/v1/docs/adding-device-conditions-to-firewall-rules). It is derived from the Cato token and indicates whether the session still meets the required authentication assurance level.

These signals are evaluated at the PoP and provided to the policy engine, enabling continuous, risk-aware access decisions throughout the session lifecycle.

## Traffic and Control Flows

Adaptive access enforcement is performed at the Cato PoP, where identity, device, and session signals are evaluated during both session establishment and ongoing activity.

![adaptive_access_diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35418941991581.png)

1. **User authentication and session establishment:** A user connects to the nearest Cato PoP, which forwards the authentication request to the configured identity provider (IdP). After successful authentication, the PoP establishes the session and retrieves the user identity and group attributes.
2. **Initial policy evaluation:** When the session is established, the PoP evaluates the relevant contextual signals against the configured policies. This establishes the initial access decision for the user session and determines whether the user is allowed to connect.
3. **Accessing an application:** When the user attempts to access an application, the PoP evaluates the relevant policy conditions for that request.
4. **Step-up authentication:** If the policy requires stronger authentication, the PoP redirects the user to the configured IdP. After successful re-authentication, the session continues with the required assurance level.
5. **Continuous enforcement:** After access is granted, the PoP continues to evaluate session conditions. If risk increases, posture fails, or authentication assurance is no longer sufficient, the policy can block access or require the user to authenticate again.

## Cato Policies for Adaptive Access

Adaptive access in the Cato platform is implemented through multiple CMA policies that enforce access decisions across connectivity, application access, and network traffic. Each policy evaluates contextual signals and applies controls at different stages of the user session.

### Client Connectivity Policy

The Client Connectivity Policy controls whether a user device is allowed to establish a connection to the Cato Cloud. This policy enforces Zero Trust principles at the point of connection by validating the device and session before access is granted.

Administrators use this policy to prevent unmanaged or non-compliant devices from connecting, and to enforce authentication requirements before a session is established.

### Private Access Policy

Cato Private Access lets you provide secure, identity-based access to private applications without extending your network to users. Instead of granting direct network-level connectivity like a traditional VPN, you enforce least-privileged, application-specific access based on user identity and context.

The Private Access Policy controls access to the private applications and enforces least-privilege access to only users to connect to the specific private applications that they use.

### Always-On Policy

The Always-On Policy lets admins define which users and devices must remain continuously connected to the Cato Cloud so their traffic is always inspected and controlled by security policies. This is a granular policy that supports different connectivity requirements for different user populations. For example, employees or managed devices can be required to stay connected, while contractors or unmanaged devices can be allowed on-demand connectivity or direct Internet access.

Always-On enables organizations to align connectivity enforcement with risk and trust. High-trust or high-risk scenarios can require continuous inspection, while lower-risk scenarios can allow more flexible connectivity without compromising overall security posture.

### Security Policies

The following Security policies also support contextual signals to apply the same controls at different stages of the user session:

- Internet and WAN Firewall
- Application Control (CASB) and DLP

## Policy Support for Adaptive Access Signals

The following table summarizes which contextual signals are supported by each Cato policy discussed in the previous sections. Each row represents a policy, and each column represents a contextual signal. This table provides a quick reference for where adaptive access signals are applied across the Cato platform.

| Policy Name | User Risk Score | Device Posture | External Compliance | Authentication Confidence |
| --- | --- | --- | --- | --- |
| Client Connectivity Policy | No | Yes | Yes | Yes |
| Private Access (ZTNA) Policy | Yes | Yes | Yes | No |
| Always-On Policy | No | Yes | Yes | No |
| Internet Firewall Policy | Yes | Yes | Yes | Yes |
| WAN Firewall Policy | Yes | Yes | Yes | No |
| Application Control & DLP Policy | No | Yes | Yes | No |
