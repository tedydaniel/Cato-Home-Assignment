---
title: "How to Verify if Cato or Custom Root Certificate is Installed"
slug: "how-to-verify-if-cato-or-custom-root-certificate-is-installed"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/how-to-verify-if-cato-or-custom-root-certificate-is-installed"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Verify if Cato or Custom Root Certificate is Installed

## **Overview**

TLS inspection is a prerequisite for many Cato security products like IPS, RBI, Anti Malware etc. Every Client device that connects to the Cato Cloud must have the Cato or Custom root certificate installed as a trusted certificate for TLS inspection to take place. Failure to install the root certificate will prevent TLS Inspection and prevent the Cato Cloud from inspecting traffic from the device. This article shows how to verify if Cato or Custom Root Certificate is installed on your Windows or Mac device. It also shows how to locate the Root Certificate on the browser/device.

**NOTE**: For simplicity, the examples shown in this article are geared towards verifying of Cato Root Certificate. For Custom Root Certificate, the steps are exactly the same, except that instead of identifying for Cato CA, you should be looking out for your custom Root CA.

For instruction on how to install Cato Root Certificate, refer to [How to install the Cato Certificate](/v1/docs/how-to-install-the-cato-certificate)

For instruction on how to install Custom Root Certificate, refer to [Securing-Traffic-with-TLS-Inspection-Using-Private-Certificates](/v1/docs/securing-traffic-with-tls-inspection-using-private-certificates)

## **Instructions**

## Verifying Installation of Root Certificate

A simple way to verify that the Cato Root Certification is installed and working is to browse to [https://example.com](https://example.com) while the device is connected behind a socket site, or while you are connected to your SDP client. In this section, we will show you how to verify if the Cato Root Certificate is installed on some of the commonly used browsers in Windows and Mac.

[Google Chrome](/v1/docs/how-to-verify-if-cato-or-custom-root-certificate-is-installed#chrome)

[Mozilla Firefox](/v1/docs/how-to-verify-if-cato-or-custom-root-certificate-is-installed#firefox)

[Microsoft Edge or Internet explorer](/v1/docs/how-to-verify-if-cato-or-custom-root-certificate-is-installed#edge-or-internet-explorer)

[Apple Safari](/v1/docs/how-to-verify-if-cato-or-custom-root-certificate-is-installed#safari)

### Chrome

If Cato Root CA is installed, clicking on the "lock" icon in the address bar and it will show "Connection is secure".

![exampledotcom-trusted.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10104771032861.jpeg)

If the Cato Root CA is not installed, you will get a prompt stating that "Your Connection is not private".

![exampledotcom-untrusted.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10104775065373.jpeg)

### Firefox

If Cato Root CA is installed, clicking on the "lock" icon in the address bar and it will show "Connection secure".

![ff-secure.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10164974075421.jpeg)

If the Cato Root CA is not installed, you will see the page "Software is Preventing Firefox From Safely Connecting to this Site.

![ff-nocert.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10165011325853.jpeg)

### Edge or Internet Explorer

If Cato Root CA is installed, clicking on the "lock" icon in the address bar and it will show "Connection is secure".

![edge-cert.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10165082162845.jpeg)

If the Cato Root CA is not installed, you will see the Not secure on the Address bar, and clicking on it will show that "Your connection to this site isn't secure".

![edge.nocert.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10157139922973.jpeg)

### Safari

If Cato Root CA is installed, the "lock" icon can be seen in the address bar. Clicking on it will show "Safari is using an encrypted connection to example.com".

![Screenshot 2023-04-01 at 14.50.03.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10164623107869.png)

If the Cato Root CA is not installed, you will see "This Connection Is Not Private".

![Screenshot 2023-04-01 at 15.22.19.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10164851308573.png)

## Location of the Cato Root Certificate

The following section shows where to locate the Cato Root Certificate for the above browsers. For Mac devices, if a root certificate is installed on the system Keychain, it will be inherited by all applications that use the system's certificate store, including web browsers like Safari, Chrome, Edge, etc. In this section, we will also show you how to verify if the Cato Root Certificate is installed on the system keychain on your Mac.

### Chrome:

- Go to chrome://settings.
- On the left, click Privacy and security.
- Click Security.
- Scroll to Advanced.
- Click Manage certificates and make sure you can see the Cato Network CA under the Trusted Root Certification Authorities

![hrome.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10103682742173.jpeg)

### Firefox

- Launch Firefox
- Click on the hamburger icon on the top right and go to Settings
- Click on Privacy & Security
- Scroll to View Certificates and make sure you can see the Cato Networks

![FF.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10103657485597.jpeg)

### Edge

- Go to edge://settings/privacy
- Scroll down to the Security section and click on Manage Certificates
- The Certificates prompt box will open. Click on Trusted Root Certificate Authorities and you should see Cato Networks CA under it.

![edge.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10103776782749.jpeg)

### Mac

- Click on the "Finder" icon in the Dock (the icon with a smiling face).
- Go to the "Applications" folder.
- Open the "Utilities" folder.
- Double-click on "Keychain Access".
- Keychain Access will open
- Make sure you can find Cato Networks CA

![mac.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10103657741853.jpeg)
