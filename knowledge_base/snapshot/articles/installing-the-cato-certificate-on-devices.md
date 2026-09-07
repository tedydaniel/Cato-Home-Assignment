---
title: "How to Install the Cato Certificate"
slug: "how-to-install-the-cato-certificate"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/how-to-install-the-cato-certificate"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Install the Cato Certificate

To install the Cato Certificate, download it from the Cato Client download portal and add it to your device's operating system certificate store.

## Installing the Cato Certificate

You can download the Cato certificate from the [Client download portal](https://clientdownload.catonetworks.com/) and install it on the required devices.

- Select **Cato Client**, and then choose the operating system.

![download_cert.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35137805514269.png)

Installing the certificate will add it to the relevant operating system store (ie. Keychain for macOS, Certificate Management for Windows)

In case you're running third party tools which requires and manages its own certificate system, you'll need to import it there as well.

Few examples with references:

- **Java** SE - You will be required to push the certificate to the Java cert store as well:

![115002657409-mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700835551261.png)

Or using the keytool - https://docs.oracle.com/javase/tutorial/security/toolsign/rstep2.html
- **InteliJ** - https://intellij-support.jetbrains.com/hc/en-us/community/posts/206153629-How-to-add-a-SSL-root-certificate-to-IDEA-on-OS-X-?sort_by=votes
- **Git** - http://stackoverflow.com/questions/9008309/how-do-i-set-git-ssl-no-verify-for-specific-repos-only
- **Firefox** - https://wiki.mozilla.org/CA:AddRootToFirefox

### Known Issues

- Unable to install the certificate. Error: "Couldn't install because certificate file couldn't be read"
  - Workaround: Install a certificate from Settings/Additional Settings/Privacy/Install certificate from SD/Choose the relevant certificate

## Installing Root CA Certificate to Firefox_ARCHIVED

Starting with version 120, Firefox can automatically trust third-party root certificates installed in the OS certificate store. For more information, see the [Mozilla documentation](https://support.mozilla.org/en-US/kb/automatically-trust-third-party-certificates).

**To manually install the Cato certificate to Firefox:**

1. From the browser options menu, click **Settings**.
2. Search for **Certificates** and click **View Certificates**.
3. In the **Authorities** tab, click **Import**.
4. Browse to where you stored the Cato root certificate and select it and click **Open**.

This should resolve any certificate issues with TLS inspection in Firefox.
