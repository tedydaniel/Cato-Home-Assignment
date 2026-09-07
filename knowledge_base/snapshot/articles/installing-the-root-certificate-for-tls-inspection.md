---
title: "Installing the Root Certificate for TLS Inspection"
slug: "installing-the-root-certificate-for-tls-inspection"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/installing-the-root-certificate-for-tls-inspection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing the Root Certificate for TLS Inspection

To enable TLS Inspection in the Cato Cloud, the Cato root certificate must be installed as a trusted certificate on every client device, allowing the Cato Cloud to inspect encrypted traffic and display HTTPS block pages without browser warnings.

## Installing the Cato Root Certificate on End-user Devices

The Cato root certificate must be installed as a trusted certificate on every Client device that connects to the Cato Cloud. Installing the Cato certificate is mandatory for TLS Inspection and lets the Cato Cloud inspect traffic to and from the device.

We recommend that this is one of the first steps in any Cato deployment. It serves the following purposes:

- **TLS Inspection:** When TLS Inspection is enabled, the Cato root certificate is presented to the client as the issuer of every HTTPS website certificate. Web browsers do not trust Cato’s certificate by default, and the browser will display a certificate warning when a user visits an HTTPS website without Cato’s certificate installed. TLS Inspection is transparent to the end user if the Cato certificate is installed.
- **Displaying HTTPS block pages:** If TLS traffic is blocked by URL Filtering or Internet firewall rules, the Cato certificate allows access to Cato’s block page. You don't need to enable TLS Inspection to block access to HTTPS websites. However, users will see a certificate warning instead of the block page if the Cato certificate isn't installed on their computer.

### Installing the Cato Root Certificate for an End User

The process for installing the certificate is different for each operating system:

- For Windows Clients, the Cato certificate is automatically added to the Windows certificate store and supports the Chrome and Edge browsers

You can manually install the Cato certificate for other browsers (such as Firefox), use an Active Directory Group Policy Object (GPO), or use an MDM to install it with the browser, see [Installing the Cato Certificate on Windows Devices](/v1/docs/installing-the-cato-certificate-on-windows-devices)
- For macOS Clients, for organizations that use an MDM, the Cato certificate is automatically installed as part of the CA keychain

Otherwise, the SDP user manually installs the Cato certificate. For more information, see [Installing the Cato Certificate on macOS Devices](/v1/docs/installing-the-cato-certificate-on-macos-devices).
- For iOS and Android Clients, the SDP user manually installs the Client or use an MDM to install the certificate with the Client. For more information, see [Installing the Cato Certificate on iOS Devices](/v1/docs/installing-the-cato-certificate-on-ios-devices) or [Installing the Cato Certificate on Android Devices](/v1/docs/installing-the-cato-certificate-on-android-devices).
- The Cato certificate and Client installation files can be downloaded from:
  - The [Client download portal](https://clientdownload.catonetworks.com/) in CER format
  - The **Security > Certificate Management** page in PEM and DER format

### Installing the Root Certificate for the Windows Domain

Microsoft recommends [blocking internet access for Domain Controllers](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/securing-domain-controllers-against-attack#blocking-internet-access-for-domain-controllers). Perform steps 1-3 below on a computer other than a Domain Controller.

**To install the Cato root certificate on Windows computers with GPO:**

1. From the navigation menu, click **Security > Certificate Management**.
2. From the **Actions** menu at the end of the certificate row, select **Download DER** and save the file with the Cato certificate.
3. Transfer the certificate file to a Domain Controller.
4. On the Domain Controller, go to **Administrative Tools** and then open **Group Policy Management**.
5. Right-click the top level domain and then select **Create a GPO in this domain, and Link it here…**.

**Note:** If you want to use an existing GPO, skip to step 8.

![360002921098-image-2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700838916637.png)
6. Enter a name for the GPO and click **OK**.
7. Right-click the GPO created in the previous step or the existing GPO and select **Edit…**.

![360002921398-image-4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700838984477.png)
8. Open **Computer Configuration > Policies > Windows Settings > Security Setting > Public Key Settings**, right-click the Trusted Root Certification Authorities folder, and then select **Import…**.
9. Click **Next** on the **Welcome to the Certificate Import Wizard** window.
10. On the **File to Import** window, click **Browse…**, select the Cato certificate that you downloaded in step 3, and then click **Open**.
11. Click **Next** and make sure that **Place all certificates in the following store** is selected and the Certificate store shown is **Trusted Root Certification Authorities**.

![360002921618-image-8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700848811037.png)
12. Click **Next**. Verify that all the information is correct and click **Finish**.

The window states, **The import was successful**.
13. Click **OK**.

## Understanding Certificate Management

Cato aligns with industry-standard PKI practices by relying on the Common CA Database (CCADB) for managing public root certificates. CCADB is jointly maintained by leading vendors (Mozilla, Microsoft and Google), and represents the authoritative CA trust store for TLS root certificates.

This replaces the previous method, where Cato combined Mozilla’s CA store with an internal certificate repository and fetched missing certificates on an ad-hoc basis — a reactive approach with potential inefficiencies. The CCADB-based store reduces the likelihood of missing certificates and ensures conformance with modern TLS best practices.

Our R&D team validated CCADB thoroughly, confirming that previously missing certificates reported by customers were present in the CCADB database before the migration.

In rare cases — for example, when a root CA issues a new certificate that has not yet propagated into CCADB or into our periodic sync cycle — the certificate may still be missing in the Cato store. If that happens, please share the following details with Cato Support for expedited resolution:

- Certificate serial number, validity dates, issuer, and Common Name or Subject Alternative Name (SAN)
- SHA-256 fingerprint of the certificate
- The certificate file in .CER format

You can obtain certificate details via your browser (using the padlock icon) or via your OS certificate manager (for example, on Windows: Start → type certmgr.msc → locate the certificate).

Once validated by our security team, the CA will be added first to our development environment and then rolled out globally to all PoPs.

If you become aware of a new or uncommon CA certificate that is used by your organization, proactively share it with your Cato representative. This helps avoid TLS-related connectivity issues or the need to add temporary TLS bypass rules.
