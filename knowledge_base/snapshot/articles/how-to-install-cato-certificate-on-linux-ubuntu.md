---
title: "How to install Cato Certificate on Linux (Ubuntu)"
slug: "how-to-install-cato-certificate-on-linux-ubuntu"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-install-cato-certificate-on-linux-ubuntu"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to install Cato Certificate on Linux (Ubuntu)

Here are the steps to download, convert and install the Cato Networks SSL certificate on Ubuntu.

1. sudo mkdir /usr/local/share/ca-certificates/Cato
2. sudo chmod 755 /usr/local/share/ca-certificates/Cato
3. cd /usr/local/share/ca-certificates/Cato;sudo wget --no-check-certificate '[https://clientdownload.catonetworks.com/public/certificates/CatoNetworksTrustedRootCA.pem](https://clientdownload.catonetworks.com/public/certificates/CatoNetworksTrustedRootCA.pem)' Note: #3 is a single line command with a single space between --no-check-certificate and the URL.
4. sudo openssl x509 -in CatoNetworksTrustedRootCA.pem -out CatoNetworksTrustedRootCA.crt
5. sudo rm -f CatoNetworksTrustedRootCA.pem
6. sudo update-ca-certificates
