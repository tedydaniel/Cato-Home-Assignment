---
title: "Activate & Distribute the New 2024 Cato Root Certificate Before Oct 29, 2025"
slug: "activate-distribute-the-new-2024-cato-root-certificate-before-oct-29-2025"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/activate-distribute-the-new-2024-cato-root-certificate-before-oct-29-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Activate & Distribute the New 2024 Cato Root Certificate Before Oct 29, 2025

As previously [announced](/v1/docs/product-update-november-11-2024), the default 2015 Cato root certificate used for TLS Inspection and Threat Prevention will expire on October 29, 2025.

If you have already activated the 2024 Cato certificate on your account, please ignore this email.

To prevent disruption to your Cato service, you need to distribute and activate the new Cato root certificate. These are the details:

- Name: 2024 Default Cato Certificate

- Common Name (CN): Cato Networks Root CA

- Expiration Date: March 3, 2034

Activating the new certificate on all devices ensures TLS Inspection continues to function, allowing Cato’s Threat Prevention engines to inspect encrypted traffic. It also prevents potential issues for users who are accessing HTTPS websites and SaaS applications with the expired certificate.

For more information, see this [video](https://catonetworks.wistia.com/medias/tbq3v1nlu1) and [FAQ article](https://support.catonetworks.com/hc/en-us/articles/22781778613149-FAQ-for-the-New-Default-Cato-Certificate-for-TLS-Inspection).

## What Action Do I Need to Take?

You must distribute and activate the new certificate to all devices in your network that rely on TLS Inspection before Oct. 29, 2025.

## How Do I Distribute the New Certificate?

The distribution method depends on the device OS and the Client version. Visit the **Access > Access Overview** page in the Cato Management Application (CMA) to see the devices and Client versions used across your organization.

- Devices running **Windows Client version 5.11** or higher or **macOS Client version 5.7** or higher already include the new certificate. No further action is required.

- For other devices or OSs, the old certificate is installed automatically. To install the new certificate, you must distribute the certificate using MDM or install it manually. You can download the new certificate from the **Security > Certificate Management** page in the CMA.

## How Do I Activate the New Certificate?

You can activate the new certificate from the [Certificate Management page](/v1/docs/managing-certificates-for-tls-inspection) in the CMA:

1. From the navigation menu, click **Security > Certificate Management**.
2. In the **Actions** column for the new certificate, click the three dots button.
3. If you are using the Cato certificate, select **2024 Default Cato Certificate**.
4. Click **Activate**.
5. In the Activate Certificate pop-up message, click **OK**.

## What is the Impact to My Account?

Failure to distribute the new certificate before October 29, 2025, will result in reduced visibility and protection for TLS traffic. Your users may also experience unexpected connectivity issues.

## How Can I Get More Information?

Please use the [Cato Knowledge AI assistant](/v1/docs/what-is-cato-s-ask-ai-agent) in the CMA to answer questions about activating the new Cato certificate and TLS inspection.

## Who Do I Talk to If I Have Technical Issues?

Reach out to Cato [Support](https://support.catonetworks.com/hc/en-us/requests/new).
