---
title: "Testing TLS Inspection in the Cato Cloud"
slug: "testing-tls-inspection-in-the-cato-cloud"
updated: 2026-06-22T09:27:06Z
published: 2026-06-22T09:27:06Z
canonical: "knowledge.catonetworks.com/testing-tls-inspection-in-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing TLS Inspection in the Cato Cloud

## Overview of Enabling and Deploying TLS Inspection

[According to Google](https://transparencyreport.google.com/https/overview), over 70% of all web pages in 2019 are served over HTTPS, the HyperText Transfer Protocol Secure. HTTP is the protocol web browsers and web servers use to exchange data, and the “S” at the end of HTTPS means that the data is encrypted by TLS, Transport Layer Security. TLS is great at providing privacy and confidentiality of data, the reason that it’s being so widely adopted across the Internet.

Unfortunately, that guarantee of privacy and confidentiality doesn’t apply just to legitimate traffic. Malware and threats can hide just as well on HTTPS sites as they do on HTTP sites. As the popularity of HTTPS grows, it’s no surprise that security researchers are finding more and more malware threats on HTTPS websites. To make matters worse, HTTPS renders antivirus and IPS engines less effective because they can’t scan for threats in TLS encrypted traffic.

When TLS Inspection is enabled, the Cato PoP acts as a man-in-the-middle between the web browser and the web server:

1. The PoP decrypts TLS traffic it receives from the client or server.
2. The PoP scans the decrypted traffic with the Anti-Malware and IPS engines.
3. The PoP encrypts the traffic again.
4. The PoP sends the encrypted packets to the destination.

TLS Inspection in combination with Anti-malware and IPS protects your network from both encrypted and unencrypted malicious threats. If you’re using threat protection without TLS Inspection, your network is vulnerable to attack from encrypted sources. Therefore, we strongly recommend that you enable TLS Inspection if you are using Anti-Malware or IPS.

This guide walks you through a gradual deployment of TLS Inspection. Start by enabling TLS Inspection for a few users and see how it works for them. Then you can enable the feature for the entire account.

For more about the Cato certificate, see [Installing the Root Certificate for TLS Inspection](/v1/docs/installing-the-root-certificate-for-tls-inspection).

## Testing TLS Inspection

Enabling TLS Inspection for a small group of users allows you to perform testing and catch any issues with certificate installation or website compatibility prior to rolling out the feature to all your end users. Your test base can be as large as a site or as small as an individual computer. You can choose to enable TLS Inspection on the following:

- Sites
- Networks within a site
- VPN users
- Individual computers (Hosts)
- Any combination of the options above

## Enabling TLS Inspection for Test Users

Testing should be performed on every device and operating system that your organization uses. Test users should perform normal business activities and report all anomalies to the network or system admin for further investigation.

When you enable TLS Inspection, the out of the box policy is to inspect all HTTPS traffic by default. To perform testing on only specific users, first you need to configure a **Bypass** rule with **Source** defined as **Any**. Then create an **Inspect** rule with higher priority and add the test users to the **Source** field. This is an example TLS Inspection policy for testing specific users:

![TLS_Inspection_Test_User_Rules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303185651869.png)

For more about enabling the TLS Inspection policy for test users, see [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account).

## How Do I Know if Cato TLS Inspection is Active for a Website?

Modern browsers show a padlock icon in the URL bar if a site is encrypted with TLS. Clicking the padlock icon reveals an option that lets you see the certificate details, including the root CA. TLS Inspection is active when you see Cato Networks followed by the POP name as the certificate issuer or verifier.

![HTTPS_padlock.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303154701981.png)

For more about installing a root CA, see [Testing TLS Inspection in the Cato Cloud](/v1/docs/testing-tls-inspection-in-the-cato-cloud).

### Testing TLS Inspection on Chrome

1. Click the padlock icon and then click **Certificate**.

![360002921818-image-14.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303170479517.png)
2. Check the “Issued by” field.

![360002841817-image-15.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303154833181.png)

### Testing TLS Inspection on Firefox

1. Click the padlock icon and then click the **>** button next to Connection.

![360002921998-image-16.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303154906525.png)
2. Check the “Verified by” field.

![360002921978-image-17.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303147293341.png)

## Bypassing Traffic from TLS Inspection

During testing, you may find that some websites or applications don’t work with TLS Inspection enabled. You can exempt destination domains, IP addresses, and even full URL categories from TLS Inspection by creating a new rule with the Bypass action in the TLS Inspection policy. You may need to add a website to Trusted Destinations for one of the following reasons:

- Certificate pinning: the server instructs the client to check the public key it receives from the server with a provided hash of the true public key. This mitigates the man-in-the-middle method used by TLS Inspection since the public key sent to the client from the PoP does not match the hash.
- Client authentication: the web server requires the client to authenticate itself with a client certificate. TLS Inspection fails because the PoP does not have the client certificate.

### Enabling TLS Inspection Globally

After all issues found by the test users have been resolved, enable TLS Inspection for all users.
