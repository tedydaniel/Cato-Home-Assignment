---
title: "Distributing Device Certificates to Android Devices with Microsoft Intune"
slug: "distributing-device-certificates-to-android-devices-with-microsoft-intune"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/distributing-device-certificates-to-android-devices-with-microsoft-intune"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Distributing Device Certificates to Android Devices with Microsoft Intune

## Overview

You can distribute your corporate self-signed certificates to Android devices in your network using Microsoft Intune as your MDM. This streamlines the distribution of device certificates across devices. By managing certificate distribution through an MDM, you can centrally control certificate deployment, ensuring robust security measures are consistently enforced.

This article explains how to configure two policies in Intune for Android devices:

- A trusted certificate profile for the Root CA certificate
- A PKCS certificate profile for the client certificate deployment

![Intune_Android_policies.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35312032406813.png)

### Prerequisiste

An Enterprise Certificate Authority (e.g., Microsoft Certificate Services) is required for certificate signing, as Intune relies on a CA infrastructure to securely issue PKCS certificates to devices.

## Configure the Root CA as a Trusted Certificate

1. In Microsoft Intune, go to **Devices > Android > Configuration**.
2. Under **Policies**, click **Create** and select **New Policy**.
3. In the **Create a profile** panel, configure these settings:

![01_create_profile.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35312047056285.png)
  - Platform: Android Enterprise
  - Profile type: Templates
  - Template name: Trusted certificate
4. Click **Create**. The **Trusted certificate** page opens.
5. In the **Basics** tab, enter a name and description for the profile, and then click **Next**.
6. In **Configuration settings**, upload the Root CA certificate file to the **Certificate file** field, and then click **Next**.

![02_config_settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35312006980509.png)
7. In **Assignments**, add the required user groups or device groups in **Included groups**, and then click **Next**.

![03_assignments.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35312007044509.png)
8. In **Review + create**, review the summary and click **Create**.

## Configure the PKCS Certificate Profile

The PKCS profile is the policy that defines the client certificate that Intune requests and deploys to the Android devices. Intune does not let you upload a private key directly in this workflow. Instead, Intune uses the certificate authority infrastructure to request the certificate securely and deliver it to the assigned managed devices. This profile depends on the trusted CA certificate profile from the previous section.

1. In Microsoft Intune, go to **Devices > Android > Configuration**.
2. Under **Policies**, click **Create** and select **New Policy**.
3. In the **Create a profile** panel, configure these settings:
  - Platform: Android Enterprise
  - Profile type: Templates
  - Template name: PKCS certificate
4. Click **Create**.
5. In the **Basics** tab, enter a name and description for the profile, and then click **Next**.
6. In **Configuration settings**, enter the certificate settings for your Active Directory certificate authority environment.
7. Configure these PKCS settings:

![04_PKCS_cert.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35312032506141.png)
  - **Certification authority**: Enter the FQDN of the certificate authority that Intune communicates with.
  - **Certification authority name**: Enter a friendly name for the certificate authority.
  - **Certificate template name**: Enter the name of the certificate template defined in Entra ID for this certificate deployment.
  - **Certification authority type**: Select **Microsoft**.
  - **Certificate type**: Select **User**.
  - **Subject name format**: for example, CN={{UserName}},E={{EmailAddress}}

**Note:** This format must match the certificate template configuration.
  - **Extended key usage**: Configure **Client authentication** with the default values.

Enter custom values for the Client authentication if required.
  - **Root certificate**: Select the trusted certificate profile that you created in the previous section.
8. Configure any other certificate values required by your certificate authority, and then click **Next**.
9. In **Apps**, select **Require user approval for all apps**, and then click **Next**.
10. In **Assignments**, add the required user groups or device groups in **Included groups**, and then click **Next**.
11. In **Review + create**, review the summary and click **Create**.

**Note:** When the [certificate Device Check](/v1/docs/creating-device-posture-profiles-and-device-checks) is enabled for the account, after installing the certificate, the user will be prompted to select the certificate the first time they connect using the Cato Client.
