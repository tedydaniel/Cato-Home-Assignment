---
title: "Managing Certificates for TLS Inspection"
slug: "managing-certificates-for-tls-inspection"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/managing-certificates-for-tls-inspection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Certificates for TLS Inspection

This article discusses how to manage the certificates required for performing TLS inspection.

## Overview

TLS Inspection decrypts and inspects HTTPS traffic to identify and mitigate potential threats hidden within encrypted sessions. The Certificate Management page lets you manage the certificates used for performing TLS Inspection. You can view information about the certificates, configure private certificates, and activate a certificate to be used for TLS Inspection.

![certificate_management.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27394192927261.png)

## Understanding the Certificate Details

The Certificate Management table shows useful information for each certificate configured for your account. The table also lets you download a certificate in different formats, and activate a certificate. For more about activating certificates, see below [Activating a Certificate](/v1/docs/managing-certificates-for-tls-inspection#activating-a-certificate).

![certificate_management_details_table.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27394193010333.png)

This is the information shown for each certificate in the Certificate Management table:

- **Type** - Shows whether the certificate is a Cato certificate or private certificate (including custom certificate or Certificate Signing Request (CSR)). For more about private certificates, see [Securing Traffic with TLS Inspection Using Private Certificates](/v1/docs/securing-traffic-with-tls-inspection-using-private-certificates)
- **Creation Date** - The start date of the validity period for the certificate
- **Expiration Date** - The end date of the validity period for the certificate
- **Common Name** - The name of the server protected by the certificate
- **Status** - Shows if the certificate is the active certificate or is not activated
- The **Actions** menu lets you download the certificate as PEM or DER, or activate the certificate

When you expand a row of a certificate, the following details are shown:

- **Certificate Hierarchy** - Shows the chain of trust for the certificate
- **Certificate Fields** - Details for the certificate, including:
  - **General** information including the certificate version, serial number, certificate signature algorithm, and issuer
  - **Validity** - The start and end dates of the validity period for the certificate
  - **Fingerprints** - The hashes of the certificate's public key

## Activating a Certificate

When you activate a certificate, that certificate is the one used by the TLS Inspection policy. Only one certificate can be activated at any given time, therefore when you activate a new certificate, all other certificates become inactive.

**To activate a certificate:**

1. From the navigation menu, click **Security > Certificate Management**.
2. Click ![horizontal-more-menu.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27394193075869.png) in the row of the certificate and select **Activate**. The certificate becomes the active certificate used for TLS inspection, and the previous active certificate become inactive.

## Configuring a Private Certificate

For information about configuring private certificates for use with Cato TLS Inspection, see [Securing Traffic with TLS Inspection Using Private Certificates](/v1/docs/securing-traffic-with-tls-inspection-using-private-certificates).
