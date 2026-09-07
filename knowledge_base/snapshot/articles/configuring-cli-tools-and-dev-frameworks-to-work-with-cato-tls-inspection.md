---
title: "Configuring CLI Tools and Dev Frameworks to Work with Cato TLS Inspection"
slug: "configuring-cli-tools-and-dev-frameworks-to-work-with-cato-tls-inspection"
updated: 2026-07-21T07:42:27Z
published: 2026-07-21T07:42:27Z
canonical: "knowledge.catonetworks.com/configuring-cli-tools-and-dev-frameworks-to-work-with-cato-tls-inspection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring CLI Tools and Dev Frameworks to Work with Cato TLS Inspection

## Overview

This article shows how to make command-line tools and developer frameworks trust the Cato Networks TLS Inspection certificate, so HTTPS works without errors while traffic is inspected. It covers how to install the Cato certificate system-wide and how to point specific tools to the certificate when they don’t use the OS trust store.

In all examples below, replace `/path/to/CatoNetworksTrustedRootCA.pem` with the actual path for your environment.

## Install the Certificate System-Wide (Recommended)

Installing the Cato Root CA in the host OS lets most apps trust inspected traffic automatically. You can install the Cato Root CA as described in [How to Install the Cato Certificate](/v1/docs/how-to-install-the-cato-certificate).

If something doesn’t work as expected, you can manually add the Cato Root CA to the OS trust store. For more information about installing the Cato certificate, see the relevant article:

- [Installing the Cato Certificate on Windows Devices](/v1/docs/installing-the-cato-certificate-on-windows-devices)
- [Installing the Cato Certificate on macOS Devices](/v1/docs/installing-the-cato-certificate-on-macos-devices)
- [Installing Device Certificates on Linux Devices](/v1/docs/installing-device-certificates-on-linux-devices)

## Combined Certificate Bundle (For Tools That Override the Trust Bundle)

Some tools override the CA trust bundle instead of extending it, meaning they actually delete all the certificates that were there before. To ensure these tools trust both public websites and Cato-inspected traffic, create a combined bundle that includes the OS trusted root certificates plus the Cato Root CA.

**Recommendation:** Install the Cato Root CA in the system store. Use a combined bundle only for tools that require a single CA file.

**Maintenance tip:** Rebuild the combined bundle periodically (for example, monthly or after OS trust updates).

### Windows (PowerShell)

```powershell
# Run in elevated PowerShell
$dest="$env:ProgramData\CatoNetworks\TLS\cato_combined_ca.pem"; $destDir=Split-Path $dest; New-Item -ItemType Directory -Force -Path $destDir | Out-Null; Get-ChildItem Cert:\CurrentUser\Root, Cert:\LocalMachine\Root, Cert:\CurrentUser\CA, Cert:\LocalMachine\CA | Sort-Object Thumbprint -Unique | ForEach-Object { "-----BEGIN CERTIFICATE-----"; [System.Convert]::ToBase64String($_.RawData,'InsertLineBreaks'); "-----END CERTIFICATE-----"; "" } | Out-File -Encoding ascii $dest; Write-Host "Combined bundle written to: $dest"
```

Output path: `C:\ProgramData\CatoNetworks\TLS\cato_combined_ca.pem`

### macOS

```bash
sudo mkdir -p "/Library/Application Support/CatoNetworks/TLS"

security find-certificate -a -p \
  /System/Library/Keychains/SystemRootCertificates.keychain \
  /Library/Keychains/System.keychain \
  > /tmp/cato_combined_ca.pem && \
  sudo install -m 0644 /tmp/cato_combined_ca.pem \
  "/Library/Application Support/CatoNetworks/TLS/cato_combined_ca.pem"
```

Output path: `/Library/Application Support/CatoNetworks/TLS/cato_combined_ca.pem`

### Linux

Concatenate the OS bundle with the Cato CA to produce a single file.

**Debian/Ubuntu:**

```bash
sudo bash -c 'cat /etc/ssl/certs/ca-certificates.crt > /etc/ssl/certs/cato_combined_ca.pem'
```

Output path: `/etc/ssl/certs/cato_combined_ca.pem`

**RHEL/CentOS/Alma/Rocky:**

```bash
sudo bash -c 'cat /etc/pki/tls/certs/ca-bundle.crt > /etc/pki/tls/certs/cato_combined_ca.pem'
```

Output path: `/etc/pki/tls/certs/cato_combined_ca.pem`

## Tool-Specific Configurations

Some tools ignore the OS trust store or run in environments where it’s not available. In these cases, explicitly configure them to use the Cato CA or the combined bundle.

### General Variable Setting Syntax

**Linux/macOS:**

```bash
export VARIABLE_NAME=/path/to/file
```

or for a permanent solution:

```bash
echo 'export VARIABLE_NAME=/path/to/file' >> ~/.zshrc or ~/.bashrc 
source ~/.zshrc  or  ~/.bashrc
```

**Windows CMD**

```plaintext
set VARIABLE_NAME=C:\path\to\file
```

or for a permanent solution:

Run `setx VARIABLE_NAME "C:\path\to\file"` and then reopen the CMD window.

**Windows PowerShell**

```powershell
$env:VARIABLE_NAME="C:\path\to\file"
```

- For a permanent solution for the current user:

Run `setx VARIABLE_NAME "C:\path\to\file"` and then reopen the CMD window.
- For a permanent solution for all users on the device:

Run `[System.Environment]::SetEnvironmentVariable("VARIABLE_NAME", "C:\path\to\file", "Machine")`

### Python (Requests, AWS CLI, Azure CLI, Gcloud CLI)

Python tools often use **certifi**, which ships its own CA bundle (separate from the OS trust store).

#### Recommended General Python Fix

- macOS or Linux – set the REQUESTS_CA_BUNDLE variable to the combined bundle (instructions above [Combined Certificate Bundle (For Tools That Override the Trust Bundle)](/v1/docs/configuring-cli-tools-and-dev-frameworks-to-work-with-cato-tls-inspection#combined-certificate-bundle-for-tools-that-override-the-trust-bundle)).
- Windows – run `pip install pip-system-certs` to make Python use the Windows trust store directly.

#### Tool-Specific Python Fix

Only for macOS/Linux, you can either append the Cato Root CA to the tool’s certifi bundle, or point its CA variable to the combined bundle.

**Azure CLI (macOS/Linux)**

Append the Cato Root CA to the certifi bundle shipped with the CLI. To find Cerifi’s bundle location, run the following command:

```bash
$(az --version 2>&1 | awk -F"'" '/Python location/ {print $2}') -m certifi
```

**AWS CLI / Boto (MacOS/Linux)**

Set the variable:

```bash
AWS_CA_BUNDLE=/path/to/cato_combined_ca.pem
```

Or add this line to the config file (`~/.aws/config`)

```ini
ca_bundle = /path/to/cato_combined_ca.pem
```

**Gcloud CLI**

Append the Cato Root CA to the certifi bundle shipped with the SDK:

```bash
~/google-cloud-sdk/platform/bundledpython*/lib/python*/site-packages/certifi/cacert.pem
```

**Note:** Paths may vary depending on how you installed the tool. If you don’t see `certifi/cacert.pem` in these locations, search inside the tool’s directory.

### OpenSSL (Curl, Composer, Ruby/Fastlane)

Many tools (such as Curl, Composer, and Ruby/Fastlane) rely on OpenSSL for TLS. By default, OpenSSL reads the system CA bundle on Linux, but on macOS (Homebrew OpenSSL) and Windows, it uses its own CA files instead of the OS trust store.

#### Recommeded General OpenSSL Fix

Set the `SSL_CERT_FILE` variable to the [combined bundle](/v1/docs/configuring-cli-tools-and-dev-frameworks-to-work-with-cato-tls-inspection#combined-certificate-bundle-for-tools-that-override-the-trust-bundle).

#### Tool Specific OpenSSL Fix

If needed, configure each OpenSSL-based tool to point to the combined bundle, or append the Cato Root CA into the OpenSSL certs directory and run `c_rehash`.

**Curl**

For built-in curl on macOS (SecureTransport), Windows (Schannel), and most Linux builds (OpenSSL/LibreSSL), no additional configuration is required. These builds already use the OS trust store.

To confirm which TLS library curl is using, run: `curl --version`

For OpenSSL/LibreSSL builds that don’t use the OS store, explicitly set the variable `CURL_CA_BUNDLE` to point to the combined bundle file (using the syntax explained above).

**Composer (PHP)**

Configure Composer to use the combined bundle: `composer config -g cafile /path/to/cato_combined_ca.pem`

**Ruby, Bundler, and Fastlane**

Configure Ruby/Fastlane to trust the combined bundle: `bundle config --global ssl_ca_cert /path/to/cato_combined_ca.pem`

### Node.js and npm

Node.js and npm handle certificate stores differently depending on the OS.

- **Windows** - Node.js often uses the system store, so installing the Cato Root CA system-wide is usually enough.
- **Linux/macOS** - Node.js typically uses its own CA bundle, which does not include the Cato Root CA.

#### Node.js

If you encounter TLS errors, configure Node.js to trust the Cato Root CA:

- Set the **NODE_EXTRA_CA_CERTS** variable to point to the Cato Root CA file (not the combined bundle):

`export NODE_EXTRA_CA_CERTS=/path/to/CatoNetworksTrustedRootCA.pem`

This variable tells Node.js to trust the additional CA on top of the built-in ones.

#### npm

npm requires the combined bundle instead of a single CA file. Configure npm as follows:

`npm config set cafile "/path/to/cato_combined_ca.pem"`

This ensures npm trusts both the Cato Root CA and public root CAs.

### Java (Maven, Gradle, JDBC, etc...)

Java uses its own trust store file called `cacerts`. To enable TLS inspection, import the Cato Root CA into this store.

The default password for `cacerts` is `changeit`.

**Linux/macOS**

```bash
sudo keytool -importcert -noprompt \
  -alias cato-root-ca \
  -file /path/to/CatoNetworksTrustedRootCA.pem \
  -keystore $JAVA_HOME/lib/security/cacerts \
  -storepass changeit
```

**Windows (PowerShell)**

```powershell
keytool -importcert -noprompt `
  -alias cato-root-ca `
  -file "C:\path\to\CatoNetworksTrustedRootCA.pem" `
  -keystore "C:\Program Files\Java\jdk-17\lib\security\cacerts" `
  -storepass changeit
```

All Java-based tools (such as Maven, Gradle, JDBC drivers, Salesforce Apex Data Loader) will trust the Cato CA once it’s added to the `cacerts` store.

### Docker

Docker consists of two parts: the engine/daemon on the host and any images/containers.

- The Docker **engine** uses the host OS trust store, so installing the Cato Root CA system-wide is sufficient.
- For **images**, you must import the Cato Root CA into the container.

**Debian/Ubuntu-Based Images:**

```dockerfile
COPY CatoNetworksTrustedRootCA.pem /usr/local/share/ca-certificates/cato-root-ca.crt
RUN update-ca-certificates
```

**RHEL/CentOS-Based Images:**

```dockerfile
COPY CatoNetworksTrustedRootCA.pem /etc/pki/ca-trust/source/anchors/
RUN update-ca-trust
```

This ensures applications inside the container can trust Cato-inspected TLS traffic.

### Go

Go has its own TLS implementation, but by default, it relies on the OS trust store. Installing the Cato Root CA system-wide is usually sufficient.

In some cases (for example, in CI/CD pipelines or containers), you may need to override the trust configuration explicitly by setting the variable `SSL_CERT_FILE` to point to the combined bundle file.

### Android Studio

Android Studio uses its own cacerts trust store inside the bundled JDK. To enable TLS inspection, import the Cato Root CA into that store. The default password is `changeit`.

**Linux/macOS**

```bash
sudo keytool -importcert -noprompt \
  -alias cato-root-ca \
  -file /path/to/CatoNetworksTrustedRootCA.pem \
  -keystore $ANDROID_STUDIO_JDK/lib/security/cacerts \
  -storepass changeit
```

**Windows (PowerShell)**

```powershell
keytool -importcert -noprompt `
  -alias cato-root-ca `
  -file "C:\path\to\CatoNetworksTrustedRootCA.pem" `
  -keystore "C:\Program Files\Android\Android Studio\jre\lib\security\cacerts" `
  -storepass changeit
```

### Git

Git normally uses the OS trust store. If the Cato Root CA is installed system-wide, no additional configuration is needed.

If Git fails to trust the Cato Root CA, configure it explicitly to use the combined bundle:

```bash
git config --global http.sslCAInfo /path/to/cato_combined_ca.pem
```
