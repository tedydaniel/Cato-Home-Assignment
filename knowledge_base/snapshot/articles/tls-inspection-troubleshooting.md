---
title: "TLS Inspection Troubleshooting"
slug: "tls-inspection-troubleshooting"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/tls-inspection-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TLS Inspection Troubleshooting

## Introduction

This article covers advanced troubleshooting scenarios for TLS Inspection. Before proceeding, it is recommended to review the [TLS Inspection configuration](/v1/docs/using-the-tls-inspection-configuration-wizard) and behavior to understand how traffic is processed and enforced.

Under normal conditions, TLS Inspection is not visible to end users. To verify whether traffic is being inspected, check the **TLS Inspection** field in Account Events (`1 = inspected, 0 = bypassed`), review the certificate issuer in the browser (Cato Networks), or use TLS Inspection reports.

Cato includes a set of **default bypass rules** for well-known applications, devices, and domains. These system-managed rules are not editable and should always be reviewed before creating custom rules. For additional details, see [Default Bypass Rules](/v1/docs/configuring-tls-inspection-policy-for-the-account)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34997911042973.png)

## Symptoms

- [Website doesn’t load / times out](/v1/docs/tls-inspection-troubleshooting#troubleshooting-website-or-application-loading-issues)
- [Browser TLS / Certificate errors](/v1/docs/tls-inspection-troubleshooting#troubleshooting-browser-certificate-warning) Users may see errors such as:
  - “Your connection is not private”
  - “Secure connection failed”
  - `ERR_SSL_PROTOCOL_ERROR`
  - `ERR_SSL_VERSION_OR_CIPHER_MISMATCH`
  - `ERR_EMPTY_RESPONSE`
- [Application not working or loading](/v1/docs/tls-inspection-troubleshooting#troubleshooting-website-or-application-loading-issues)
- [Works outside network (e.g., hotspot) but not behind Cato](/v1/docs/tls-inspection-troubleshooting#troubleshooting-cato-certificate-validation-errors)
- [Valid certificate shown, but connection fails](/docs/tls-inspection-troubleshooting#h_01KN7DBKN3CVF5NMMWMS2YMP0G)
- [Inconsistent behavior across devices/platforms](/v1/docs/tls-inspection-troubleshooting#troubleshooting-osspecific-tls-issues-expected-limitations)
- [Block page displayed](/v1/docs/certificate-warnings-with-blocked-https-websites)

## Possible Causes

Most TLS Inspection issues are related to a few common conditions.

- Some applications are not compatible with TLS Inspection. Applications using **certificate pinning, strict TLS validation, or mutual TLS** will reject interception and fail to connect.
- Certificate trust issues on the client are another frequent cause. If the Cato root certificate is missing, not trusted, or inconsistently deployed, inspected traffic will fail even though the policy is correct.
- In other cases, the issue originates from the destination server. Problems such as **expired certificates, incomplete chains, hostname mismatches, or unknown certificate authorities** may not always be visible in the browser when TLS Inspection is enabled, but are still enforced by the PoP.
- Legacy systems may fail due to **TLS protocol or cipher mismatch**. Applications using outdated TLS versions or weak cipher suites may not meet the requirements defined in the TLS Inspection policy.
- Modern websites can also introduce issues due to **multiple dependent domains**. If only the main domain is allowed or bypassed while supporting domains are blocked or inspected differently, users may experience slow loading or missing content.
- Finally, platform-specific behavior plays a role. Mobile devices, BYOD endpoints, and Linux systems may behave differently due to **certificate trust limitations, application-specific validation, or default bypass rules**.

## Initial Troubleshooting

When investigating TLS-related issues, the primary goal is to determine whether the problem originates from the **client, the network (TLS Inspection), or the destination server**.

### 1. Isolate the Scope

Start by validating whether the issue is client-specific. Test the same URL:

- From a different browser
- From another device on the same network
- From the same device on a different network (e.g., hotspot)

If the issue is limited to a specific browser or device, this typically indicates a **local trust or configuration issue**. If it works outside the network, the issue is likely related to **TLS Inspection or policy enforcement**.

### 2. Verify TLS Inspection / Certificate Issuer

From the browser:

- Open DevTools → **Security tab** or click the **lock icon**
- Inspect the certificate chain

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35056545482269.png)

**Check the Issuer:**

- **Proxy/Enterprise CA (e.g., Cato)** → TLS Inspection is active
- **Public CA (e.g., DigiCert, Let’s Encrypt)** → direct TLS session

### 3. Validate Certificate Trust on Client

- Ensure the Cato root certificate is properly installed on the endpoint.
- Verify that the root certificate is in the OS trust store:
  - On Windows, open the *Computer Certificate Manager* by typing `certlm.msc` and search for the root certificate under *Trusted Root Certification Authorities*
  - On Mac, open *Keychain Access* and search for the root certificate under the *System Keychain*
- Check system time and date
- If the Cato root certificate is missing from the endpoint, download it and install it as explained in [Installing the Cato Certificate on Devices](/v1/docs/installing-the-cato-certificate-on-devices)
- Missing or incorrect trust configuration will cause immediate TLS failures.

### 4. Test TLS Handshake from Client

Use client-side tools to simulate a TLS connection and identify **exactly where and why the handshake fails**. These tools expose errors that are often hidden behind generic browser messages.

Run the following or similar from the affected endpoint:

```plaintext
curl.exe -v https://<domain>
```

If OpenSSL is available:

```plaintext
openssl s_client -connect <domain>:443 -servername <domain>
```

Expected Output (Success)

```plaintext
* SSL connection using TLS1.2 / TLS1.3
* Server certificate:
*  subject: CN=www.google.com
*  issuer: CN=GTS CA 1C3
> GET / HTTP/1.1
< HTTP/1.1 200 OK
```

It is important to first determine whether the issue is related to the **client, the destination server, or the TLS Inspection configuration itself**.

## Troubleshooting Common Issues

> [!NOTE]
> Note:
> 
> The issues listed below represent common scenarios observed in TLS Inspection deployments. Many of these errors are **generic** and may or may not directly apply to your specific environment. If the described symptoms or resolutions do not align with your case, it is recommended to collect diagnostic data (e.g., **SSS, HAR, and PCAP**) from the client machine and raise a support ticket for deeper analysis.

### Troubleshooting Failing Application

**Issue:** Certain applications fail to establish secure connections or stop functioning after TLS Inspection is enabled.

**Behavioral Expectation:** Applications with strict security controls (e.g., banking apps, endpoint security tools) may **immediately fail connections**, crash silently, or repeatedly retry connections. This occurs because TLS Inspection introduces a **man-in-the-middle (MITM) certificate**, which these applications are specifically designed to detect and reject.

**Resolution:** Validate by bypassing TLS Inspection for a **single user or source IP** using a rule at the top of the policy. If the application works when bypassed, create a **targeted exclusion** (domain/FQDN-based) and avoid broad rules. In addition, Cato's [TLS Inspection Configuration Wizard](/v1/docs/using-the-tls-inspection-configuration-wizard) can be used to bypass sensitive domains with minimal configuration.

If the application or server enforces certificate pinning or strict TLS requirements, **TLS Inspection cannot be applied**. In such cases, the correct approach is to **permanently bypass** that traffic.

**Example:** If a financial app fails to log in and works immediately after bypassing TLS Inspection for that user, this confirms incompatibility - add the app domain to the bypass list.

### Troubleshooting Browser Certificate Warning

**Issue:** Users see certificate warnings or applications fail after enabling TLS Inspection.

**Behavioral Expectation:** Users may encounter browser warnings (e.g., *“connection not secure”*) or complete connection failures. Behavior may vary across devices depending on whether the Cato certificate is properly installed.

**Resolution:** Ensure the **Cato TLS Inspection root certificate** is installed and trusted on all endpoints. Deploy using **GPO/MDM** and verify the full certificate chain on the client.

If private/internal certificates are used, ensure they are properly trusted or follow relevant TLS Inspection certificate handling procedures.

If behavior is inconsistent, validate by bypassing TLS Inspection for a **single user or device** to confirm certificate-related impact.

Refer to [Securing Traffic with TLS Inspection Using Private Certificates](/v1/docs/securing-traffic-with-tls-inspection-using-private-certificates) if using Private certificates in your organization.

### Troubleshooting Hostname Mismatch

**Issue:** Users encounter certificate errors or blocked connections due to hostname mismatch when accessing certain websites, especially when TLS Inspection is enabled.

**Behavioral Expectation:** When a server presents a certificate whose Common Name (CN) or SAN does not match the requested hostname, the connection is considered invalid.

Without TLS Inspection, the browser directly detects this mismatch and displays a certificate warning.

With TLS Inspection enabled, the browser establishes the TLS session with the Cato PoP instead of the origin server. The PoP re-signs the certificate using the Cato Root CA, making it appear valid to the client. As a result, no mismatch is shown in the browser, even though the issue still exists in the backend.

**Resolution:** Validate the behavior by bypassing TLS Inspection for a specific user or source IP. If the browser then shows a hostname mismatch error, this confirms the issue originates from the destination server.

Since the mismatch is caused by the server’s certificate configuration, it cannot be corrected by TLS Inspection. The appropriate action is to either:

- Allow access by bypassing TLS Inspection for the specific domain, or
- Block the traffic based on policy if the mismatch is considered a security risk

Avoid broad bypass rules and instead use targeted domain/FQDN exclusions where required.

**Example:** When accessing `https://www.testingmcafeesites.com/`, the server presents a certificate for `platformsplat1.mcafee.com`.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35056561685149.png)

Without TLS Inspection, the browser immediately flags a hostname mismatch.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35950711498013.png)

With TLS Inspection enabled, the browser sees a valid certificate issued by the Cato Root CA for `www.testingmcafeesites.com`, so no error is displayed. However, the Cato PoP detects the mismatch in the background and enforces the configured policy (block or warning).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35056545491357.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35950735582493.png)

### Troubleshooting Website or Application Loading Issues

**Issue:** Websites fail to load, partially render, or behave unexpectedly when TLS Inspection is enabled.

**Behavioral Expectation:**

- Pages may hang, load indefinitely, or render partially
- Login/authentication flows may fail or loop
- Some sites may appear slow due to TLS decryption/re-encryption overhead
- Behavior may be inconsistent (e.g., works on one network, fails via Cato)

This is typically observed with **modern web apps using strict security controls or complex TLS dependencies**.

**Resolution:** Validate by bypassing TLS Inspection for a **specific user or source IP**. If the site works when bypassed, create a **targeted domain/FQDN exclusion**.

Avoid broad bypass rules — scope exclusions to only required domains.

If the application relies on strict security mechanisms (e.g., pinned certs or advanced TLS handling), **inspection may not be supported**, and bypass is the correct approach.

**Scenario – Modern Web Applications (SaaS):** Some SaaS platforms (e.g., apps with multiple backend domains/CDNs) may partially load (UI works, APIs fail). In these cases, identify all required domains via **HAR/DevTools** and ensure complete coverage in the bypass rule.

### Troubleshooting Cato Certificate Validation Errors

**Issue:** Cato TLS-related errors appear during browsing or application use.

**Behavioral Expectation:**

Users may encounter generic errors such as:

- “Secure connection failed”
- “Certificate not trusted”
- Unexpected connection resets or drops

These errors are typically non-specific and do not clearly indicate whether the issue originates from the client, server, or TLS Inspection process.

**Resolution:** Validate the behavior by temporarily **bypassing TLS Inspection** for a single user or source IP.

- If the issue is resolved when bypassed, this confirms a **certificate validation failure during inspection**
- In cases where intermediate or issuing CAs are not recognized, this may be due to the certificate not yet being included in Cato’s trusted certificate bundle

As a temporary workaround, it is recommended to **bypass TLS Inspection for the affected domain/application** while opening a support case.

Cato continuously updates its **trusted certificate bundle** in line with industry standards and the most commonly used certificate authorities. If the certificate is valid and widely trusted, it is likely to be added in a future update.

Permanent remediation should focus on:

- Ensuring the server presents a **complete and valid certificate chain**
- Using certificates issued by **well-known, trusted CAs**

If the server presents an invalid or incomplete certificate chain, TLS Inspection will **correctly block the connection**. Remediation should be performed on the **server side**, or bypass TLS Inspection if required.

#### Newly Trusted / Recently Published Domains

Domains that are newly published, recently updated, or reclassified on the internet may not yet be consistently recognized across all reputation engines, certificate authorities, or trust stores.

This can lead to scenarios where traffic is blocked or flagged — not due to a TLS failure alone, but as a result of **security enforcement by Internet Firewall policies** or incomplete certificate trust.

**Behavioral Expectation:** Such domains may:

- Be misclassified or inconsistently categorized across security engines
- Present certificates that are not fully propagated or trusted globally
- Trigger TLS errors during inspection due to incomplete trust chains
- Be blocked based on policy rather than an actual connectivity issue

This behavior is common shortly after a domain becomes active or undergoes changes.

**Resolution:**

- Validate the certificate directly from the endpoint to confirm legitimacy
- If the domain is verified as safe:
  - Re-categorize it to an allowed category based on policy requirements, or
  - Create a **targeted allow/bypass rule** (avoid broad exclusions)
- Treat bypass rules as temporary where possible
- Reassess the domain after some time, once its reputation and certificate trust are fully established globally

**Key Note:** Even if a domain is legitimate, incomplete certificate propagation may still cause TLS-related errors. In these cases, the behavior is expected and should be handled through controlled policy adjustments rather than assuming a misconfiguration.

**Scenario – Incomplete Certificate Chain:** A site may work directly in a browser (due to cached intermediates) but fail under TLS Inspection. This indicates the server is not presenting the full certificate chain. The resolution is to **fix the server configuration** or **bypass the domain**.

### Unsupported Protocols and Legacy Systems

**Issue:** Connections fail for applications or systems using **outdated TLS versions or weak cipher suites** that are not supported under TLS Inspection.

**Behavioral Expectation:** Failures typically occur during the TLS handshake and are **visible directly in the browser or client**.

Common browser errors include:

- `ERR_SSL_PROTOCOL_ERROR`
- `ERR_EMPTY_RESPONSE`
- `ERR_SSL_VERSION_OR_CIPHER_MISMATCH`
- `ERR_CONNECTION_CLOSED`
- ```plaintext
400 Bad Request
No required SSL certificate was sent
```

In some cases:

- The page may fail to load entirely
- The connection may reset immediately
- Thick clients or legacy apps may fail silently or show generic connection errors

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35950695276573.png)

This happens because the client or server cannot negotiate a compatible TLS version or cipher suite with the **Cato PoP acting as the MITM**.

In the events, you will also notice TLS Error Description field populated with specific information

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35085080189981.png)

For more on the errors visit [Understanding TLS errors](/v1/docs/understanding-tls-errors)

**Resolution:**

- Temporarily bypass TLS Inspection for a specific user or source IP to validate behavior
- If the application works when bypassed → confirms a **TLS negotiation mismatch during inspection**

Next, validate TLS capabilities using external tools like [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)[](https://www.ssllabs.com/ssltest/)

Compare results with your TLS Inspection policy:

- Minimum allowed TLS version
- Cipher suite enforcement level

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35084290243741.png)

If confirmed:

- Update or upgrade the application or server to support **modern TLS versions and strong cipher suites**
- If upgrades are not feasible, configure a **targeted TLS Inspection bypass** for the affected application or domain

> [!NOTE]
> Note:
> 
> By default, Cato allows a broad range of TLS versions and cipher suites. However, administrators can enforce stricter controls in the TLS Inspection policy (e.g., minimum TLS version or cipher strength), which may cause legacy applications to fail. For more information read [here](/v1/docs/configuring-tls-inspection-policy-for-the-account)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34997911045405.png)

**Scenario – Legacy Internal Application:** An internal or third-party legacy application may fail only when routed via Cato with TLS Inspection enabled but work when bypassed. This typically indicates dependency on **deprecated TLS versions**, requiring either **application upgrade or permanent bypass**.

### Troubleshooting OS-Specific TLS Issues (Expected Limitations)

**Issue:** Connectivity issues, inconsistent behavior, or lack of TLS Inspection visibility on certain operating systems and device types (e.g., mobile, BYOD, Linux).

**Behavioral Expectation:**

Behavior varies significantly depending on the operating system and application design.

For **Android and Linux devices**, TLS Inspection is **bypassed by default** due to certificate trust limitations and application behavior. However, newer configurations (via Advanced Settings in CMA) allow administrators to **enforce TLS Inspection on these platforms**, provided certificate trust can be properly established.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35057108832285.png)

For **iOS devices**, TLS Inspection is supported, but several applications (e.g., social media platforms such as Instagram, Facebook, and similar apps) are **bypassed by default** due to certificate pinning and known incompatibilities. Other applications that enforce strict validation may fail and require **manual bypass configuration**.

In general:

- Browsers may work as expected once the Cato certificate is installed
- Native/mobile applications may fail immediately due to **certificate pinning or restricted trust stores**
- Behavior may differ per application, even on the same device

**Resolution:**

These behaviors are generally **expected and platform-driven**, not indicative of misconfiguration.

- Apply TLS Inspection primarily to **managed devices** where certificate deployment is controlled
- Use **MDM solutions** to install the Cato certificate at the system level (where supported)
- Be aware of **default bypass rules** for well-known applications and platforms
- For applications that fail due to certificate pinning or strict validation, configure a **targeted TLS Inspection bypass**
- When enforcing TLS Inspection on platforms like Android or Linux, validate compatibility carefully before broad rollout

**Scenario – Mobile Application Failure:** A mobile app (e.g., banking or security app) fails to connect over Cato while the browser works. The app enforces **certificate pinning** and does not trust the Cato certificate. This is expected — the correct action is to **bypass TLS Inspection** for that application or service.

## Raising cases to Cato Support

In case TLS inspection is mandatory for an application due to compliance or regulatory reasons or in case you believe the TLS block is unexpected, please submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Details of the experienced issue and overall impact on users. Timestamp/Timezone of the user experiencing the issue.
- Related events and Firewall/TLS Rule configuration.
- Reproduce the issue and run the [Support Self Service](/v1/docs/support-self-service-supportme-portal). Include the ticket number generated by the Tool.
