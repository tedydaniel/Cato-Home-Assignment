---
title: "Securing Traffic with TLS Inspection Using Private Certificates"
slug: "securing-traffic-with-tls-inspection-using-private-certificates"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/securing-traffic-with-tls-inspection-using-private-certificates"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Securing Traffic with TLS Inspection Using Private Certificates

## Why Use Your Own CA Certificates for TLS Inspection?

Excellent question! The primary use case for using your own CA certificates is for internal compliance, security and governance over your traffic inspection. This means that you can utilize your certificate infrastructure to decrypt and inspect the traffic traversing your environment. As a reminder, TLS inspection is a prerequisite feature for other Cato features, such as RBI, CASB, and DLP.

## How does TLS Inspection with Private CA Certificates Work?

There are two main approaches to using TLS inspection with your own CA certificates:

- Upload your own CA certificate with the CA private key
- Certificate Signing Request from Cato (Customer signed certificate)

The option to use the Cato provided certificate for TLS inspection is always available as well. You can read more about that option [here](/v1/docs/installing-the-root-certificate-for-tls-inspection).

It is important to note that you can create multiple certificates, but only one certificate can be active at any given time.

In addition to enhancing the overall security posture of the customer environment, once configured, the custom certificate will be used for TLS inspection on the following rules:

- Firewall
- Anti-malware
- IPS
- CASB/DLP
- RBI

With TLS inspection enabled with one of these methods, all TLS traffic will be decrypted for inspection except for traffic that is bypassed using rules.

### Uploading an Existing CA Certificate for TLS Inspection

![certificate_management.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303186756253.png)

For the option of using an existing enterprise CA certificate for TLS inspection, first, you will want to upload that signed certificate along with the unencrypted private key.

When the CA certificate is uploaded, you will be presented with a detailed view of the certificate, including the signed CA's name, certificate chain, and expiration date.

If you need to upload a new certificate to update the validity period of the certificate, you can remove the current uploaded files, and start the process again with a new certificate and key pair. The Cato Management Application will start alerting administrators 60 days before certificate expiration both on the Cato Management Application and with an email notification (and repeat at 30 days, 7 days, and the day of expiry) to avoid any inconvenience and lapse of security with an expired certificate.

Certificates that are less than 60 days of validity will have an orange triangle icon beside the Activate button. When you hover your cursor over it, it will display "Certificate is about to expire in XX days". Once the certificate has expired, there will be a red circle icon beside the Activate button, and it will display "Certificate expired" when hover your cursor over the icon, and the Activate button will be greyed out.

> [!NOTE]
> Note:
> 
> Cato is currently unable to revoke certificates.

**To upload an existing custom certificate:**

1. From the navigation menu, click **Security > Certificate Management**.
2. Click **New**, and then select **Custom Certificate**
3. In the **Custom Certificate** panel, browse and upload both the custom certificate and the private key for the certificate. After both of those files have been uploaded successfully, click **Submit**.

![Custom_certificate_panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303215250077.png)

After you click **Submit**, the certificate and key are validated to ensure all of the required information is correct and ready to be used. The uploaded certificate and key will be validated for:

If any of these validations fail, an error will be displayed.
  - The certificate must be an intermediate or CA publisher certificate (the certificate must be able to sign other certificates)
  - The certificate chain exists and includes the root CA
  - Certificate file must be in PEM format
  - Key file is not password protected and minimum encryption key length is 2048 bits in RSA format
  - Private key must match the uploaded CA certificate

Using that certificate key pair, Cato will generate a new key pair, then the custom intermediate certificate. The newly created key pair will be signed using the imported private key and be encrypted and stored in the Cato key store. After the new intermediate certificate is generated, the uploaded unencrypted key will be deleted from the system and only the newly generated intermediate certificate will be used.

### Generating a Certificate Signing Request

This option will allow you to generate a Certificate Signing Request (CSR) from your Cato tenant, and then signed by any intermediate certificate that is signed by the organization’s CA. This option, while also increasing the security posture of an environment makes it easier for administrators to create the necessary certificates since the CSR will be generated by the platform that will be using them.

> [!NOTE]
> Note:
> 
> While many CSRs can be generated, only one certificate can be activated at a time per account.

**To generate a custom CSR for your account:**

1. From the navigation menu, click **Security > Certificate Management**.
2. Click **New** , and then select **CSR - Certificate Signing Request**.

The Create CSR panel appears.
3. Fill in the following required fields:

Note: While other fields of the CSR are optional, it is best practice to fill in all information.
  - **Certificate Name**
  - **Organization Name**
  - **Common Name**
4. Click **Create CSR** to generate the CSR to be signed by your certificate authority.

![Create_CSR.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303158660509.png)

After you generate the CSR, you will have an option presented to upload the signed certificate.

![Create_CSR_Upload.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303215395101.png)
5. The completed CSR will automatically be downloaded to the administrator's local machine, where you can submit the CSR file to your certificate authority for signing.
6. The signed certificate from the CA will need to be uploaded to the Cato Management Application. Return to the Certificate Management menu and click **Upload Certificate**.
7. Select the signed certificate from your local machine to upload to the Cato environment, which will enable the certificate to be used for TLS inspection rules.

NOTE: The signed certificate must include the following:

- Signed by either of the following RSA algorithms:
  - sha256WithRSAEncryption
  - sha512WithRSAEncryption
- Signed with minimum key size of 2048
- Needs to include the following attributes:

Attributes can be confirmed using the following command:

```plaintext
openssl x509 -in signed_cert.crt -text -noout
```

NOTE: Certificate revocation is not supported at this time.
  - authorityKeyIdentifier=keyid,issuer
  - basicConstraints=CA:TRUE
  - keyUsage = keyCertSign,cRLSign

## Monitoring and Auditing

No events are generated for expired certificates, however, audit log entries are created when certificates are generated, uploaded, or removed. Search using "tls account" under Account > Audit Trail > Search field, and it will show the audit trail of the Created and Deleted certificates:

| ![image-20230423-104436.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303200040477.png) |
| --- |

## How It Looks When It's Working

When a custom certificate is working, the browser shows the returned certificate is the same as the custom certificate which was uploaded by the customer to 'Certificate Management' in the Cato Management Application. You can then compare the common name and the certificate fingerprint of the returned certificate with the active certificate in the Cato Management Application.

| ![image-20230423-104907.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303156204445.png) |
| --- |

## Resources

Here are some useful OpenSSL commands that may help when working with certificates:

- Checking the private key length using OpenSSL:
  - `openssl rsa -in myCA.key -text -noout`
- Validating the CA and private keys:

Where:

Compare the output from both commands. If they are identical then the private key matches the certificate.
  - `openssl x509 -noout -modulus -in cert.crt | openssl md5`
  - `openssl rsa -noout -modulus -in privkey.txt | openssl md5`
  - **cert.crt** is your certificate
  - **privkey.txt** is your private key
- Signing the certificate using OpenSSL:

Where:
  - `openssl x509 -req -sha256 -CA myCA.pem -CAkey myCA.key -in test\ request.csr -out signed_cert.crt -days 365 -CAcreateserial -extfile signed_cert_attributes.conf`
  - **sha256** is the signature algorithm. In mac default is **sha-1** . You can use **sha512** as well.
  - **myCA.pem** is your CA
  - **myCA.key** is your private key
  - **request.csr** is the csr file you got from cc2
  - **signed_cert.crt** is your new signed certificate
  - The **signed_cert_attributes.conf** file has the following example content:
    - `basicConstraints=CA:TRUE`
    - `authorityKeyIdentifier=keyid,issuer`
    - `keyUsage = keyCertSign,cRLSign`
