---
title: "Device Certificate Troubleshooting"
slug: "device-certificate-troubleshooting"
status: "update"
updated: 2026-09-03T15:02:13Z
published: 2026-09-03T15:02:13Z
canonical: "knowledge.catonetworks.com/device-certificate-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Device Certificate Troubleshooting

## Overview

When configuring device authentication for Cato Clients, certificate-related issues may occur. This article covers basic device certificate troubleshooting. For more information about the feature, see [Controlling Certified Corporate Devices](/v1/docs/legacy-device-authentication).

## Troubleshooting

The following are possible troubleshooting steps that can be taken while investigating Device Certificate issues.

1. As mentioned in [Use the Client Connectivity Policy to Manage your Device Authentication Requirements](/v1/docs/use-client-connectivity-policy-manage-device-authentication), the device certificate per OS configuration should be done using the Client Connectivity Policy.

Under Device Posture, you can create Device Checks for certificates (supported on [these Client versions](/v1/docs/creating-device-posture-profiles-and-device-checks#supported-device-checks)) that are installed on the end-user device. The check validates that there is a certificate installed on the device that matches one of the signing certificates defined for the account. For more information, see [Creating a Device Certificate Device Check](/v1/docs/creating-device-posture-profiles-and-device-checks)
2. All the CA certificates uploaded to CMA are listed under **Access** -> **Client Access** -> **Device Authentication**. These are Certificate Authority certificates that signed the device certificate. Clicking on the "Show details" icon lists the certificate details in readable form. [![devauth2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12593388253597.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12593388253597.png)
3. It's important to confirm that the CA certificate isn't expired. If it is, the PoP allows the connection only if the certificate authority signed the device certificate before it expired. For device certificates, Cato doesn’t allow a Client to connect with an expired certificate. For more information, see [Handling Expired Certificates](/v1/docs/legacy-device-authentication)
4. One way to ensure that the necessary CA certificates are uploaded to CMA is to look at the client certificate chain (certification path). In this example, the client certificate was signed by the intermediate certificate with "CN= Issuing CA Client", which in turn was signed by the root certificate with "CN= Root CA". These have to match the certificates installed in CMA.

[![cert-chain__1_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12593388254237.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12593388254237.png)
5. As per [RFC3280](https://www.ietf.org/rfc/rfc3280.txt), the Authority Key Identifier of the client certificate must match the issuer's Subject Key Identifier (in this case, the Intermediate Certificate). This is another way to confirm that the correct intermediate and root CA certificates are uploaded to CMA.[![key_identifier__1_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12593418369309.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12593418369309.png)
6. After we make sure that the configuration looks good and that the certificate is valid, we will verify that the certificate is present on the client's OS.

**Note:** For more information about certificate distribution, see [Distributing and Installing Device Certificates](/v1/docs/distributing-and-installing-device-certificates)

## Windows:

In Windows, device certificates must be installed on the **Local Computer** and not under the Current User. There are two ways to verify the existence of the device certificate:

- Open the command prompt and type **certutil -store My** to list all the available user certificates on the device. In the example below, the first certificate issuer matches the subject of the CA certificate installed in step #2. If this isn't the case, the client doesn't have the necessary certificate on the device. **Certutil** is a very powerful tool that can be used to list, revoke or renew certificates. You may find more information about the tool [here](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certutil).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12593416088349.png)
- **certutil** can also be used to install the PFX (p12) certificate file on the device by running the command below. This is the recommended way to install the certificate on Windows devices as explained in [Distributing Device Certificates to Windows Devices](/v1/docs/distributing-device-certificates-to-windows-devices-with-certutil).

`/certutil&nbsp;-csp "Microsoft Software Key Storage Provider" -importpfx&nbsp;My &lt;path-to-p12-file&gt;&nbsp;NoExport`
- Alternatively, you can verify installed certificates on the device by typing **certlm.msc** from the Windows Start Menu. This will show all certificates installed on the **Local Computer**. The device certificate must be installed under the Local Computer's Personal/Certificates Folder and include a private key that the PFX file should have installed.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12592963085213.png)

### MacOS and iOS:

#### Any iOS version:

Verify that the iOS device contains the configuration profile previously distributed via MDM or Apple Configurator. The profile can be found under General > VPN & Device Management > configuration profile for iOS18. To locate the profile in older iOS versions, see [iOS user guide](https://support.apple.com/en-ca/guide/iphone/iph6c493b19/18.0/ios/18.0).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23120092257181.png)

Make sure that the VPN profile is correctly configured. The VPN payload must be configured as per the device type (macOS or iOS):

- **Connection Type:** Custom SSL
- **Identifier:**
  - For macOS: com.catonetworks.mac.CatoClient
  - For iOS: CatoNetworks.CatoVPN
- **Server:** vpn.catonetworks.net
- **Account:** add your account name. For example: CatoNetworksAccount.
  - **For iOS Client v5.6 and above:** set the account as "CatoClientVPN."
- **ProviderBundle Identifier:**
  - For macOS: com.catonetworks.mac.CatoClient.CatoClientSysExtension
  - For iOS: CatoNetworks.CatoVPN.CatoVPNNEExtenstion
- **Provider Designated Requirement:** empty
- **User Authentications:** Certificate
- **Provider Type:** Packet Tunnel
- **Credentials:** Choose the certificate from the ‘Certificates’ payload
- **Proxy Setup:** None

For detailed information on VPN profile configuration, see [Distributing Device Certificates to macOS and iOS Devices](/v1/docs/distributing-device-certificates-to-macos-and-ios-devices-with-jamf).

#### macOS v5.5 and above:

Starting with macOS Client v5.5, the certificate can be installed directly on the device without MDM distribution. The certificate and private key can be found in Keychain Access.

Device certificates may be distributed to macOS devices as explained in [Distributing Device Certificates](/v1/docs/distributing-and-installing-device-certificates) and via Microsoft Active Directory using a Windows Enterprise CA. See: [How to Create and Deploy a Client Certificate for Mac Computers Independently from Configuration Manager](https://techcommunity.microsoft.com/t5/configuration-manager-archive/how-to-create-and-deploy-a-client-certificate-for-mac-computers/ba-p/273224)

The user certificate can be found under the login section in Keychain Access:

- Make sure that the certificate is set to 'Always Trust'.
- Make sure that the private key's access control setting allows Cato Client or 'Allow all applications to access this item'.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20401457256477.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20401457259037.png)![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20401457260061.png)

## OID Verification

OID verification is configured in the account's **Advanced Configuration**. The configuration specifies the certificate extension (OID) to validate and one or more accepted values.

By default, OID verification is disabled. You can configure OID verification using the format described in the article [Working with Advanced Configuration for the Account](/v1/docs/working-with-advanced-configuration-for-the-account). The following example verifies that the certificate contains the **Certificate Template Information** extension (1.3.6.1.4.1.311.21.7) with either of the two accepted values:

cert_ext_obj(cert, "1.3.6.1.4.1.311.21.7") == "1.3.6.1.4.1.67291.458.7;1.3.6.1.4.1.58472.73142.918.5"

On the client side, verify that the required OID is present in the client certificate:

- On Windows, the Windows Certificate Manager will display the certificate details to confirm that the required OID extension is present and contains one of the expected values. The “certutil -v -store My” command will also provide detailed information about the certificate, including its OID values.
- On macOS, use Keychain Access or the appropriate certificate inspection tool to view the certificate extensions.

The following certutil output shows the certificate extension OID and its associated template information:

```plaintext
1.3.6.1.4.1.311.21.7: Flags = 0, Length = 30

    Certificate Template Information

        Template=1.3.6.1.4.1.58472.73142.918.5

        Major Version Number=100

        Minor Version Number=36
```
