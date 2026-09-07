---
title: "Supported IdPs for SSO Authentication"
slug: "supported-idps-for-sso-authentication"
updated: 2026-08-02T12:37:24Z
published: 2026-08-02T12:37:24Z
canonical: "knowledge.catonetworks.com/supported-idps-for-sso-authentication"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Supported IdPs for SSO Authentication

This article summarizes the officially supported Identity Providers (IdPs) for Cato’s Single Sign-On (SSO) features.

## Overview

Cato supports a wide range of OIDC-compatible IdPs to securely authenticate users and admins. These are the features that support SSO:

- **Remote Users** – User authentication to the Cato Client
- **CMA Admins** – Admin login to the Cato Management Application
- **Browser Access** – Authentication flows through the Application Portal
- **Browser Extension** – Authentication via browser extension (where applicable)
- **Enterprise Browser** - Authentication via enterprise browser
- **Headless Authentication** – Automated authentication flows without user interaction (for Linux OS)

For more about using SSO with your Cato account, see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account).

## IdP Support Matrix

The table below shows which SSO authentication capabilities are supported for each Identity Provider (IdP).

| Identity Provider | Remote Users | CMA Admins | Browser Access | Browser Extension | Enterprise Browser | Headless Auth |
| --- | --- | --- | --- | --- | --- | --- |
| [Azure](/v1/docs/configuring-azure-sso-for-your-account) | Yes | Yes | Yes | Yes | Yes | Yes |
| [CyberArk](/v1/docs/configuring-cyberark-sso-for-your-account) | Yes | No | Yes | Yes | Yes | No |
| [DTS](/v1/docs/configuring-dts-identity-sso-for-your-account) | Yes | Yes | Yes | Yes | Yes | No |
| [DUO](/v1/docs/configuring-duo-sso) | Yes | Yes | Yes | Yes | Yes | No |
| [Forgerock](/v1/docs/configuring-forgerock-sso) | Yes | No | Yes | Yes | Yes | No |
| [Google](/v1/docs/configuring-google-sso-for-your-account) | Yes | Yes | Yes | Yes | Yes | No |
| [Hennge](/v1/docs/configuring-hennge-one-sso) | Yes | No | Yes | Yes | Yes | No |
| [JumpCloud](/v1/docs/configuring-jumpcloud-sso-for-your-account) | Yes | No | Yes | No | No | No |
| [Keycloak](/v1/docs/configuring-keycloak-sso) | Yes | Yes | Yes | Yes | Yes | No |
| [Okta](/v1/docs/configuring-okta-sso-for-your-account) | Yes | Yes | Yes | Yes | Yes | Yes |
| [OneLogin](/v1/docs/configuring-ldap-sync-and-sso-with-onelogin) | Yes | Yes | Yes | No | No | No |
| [OneWelcome](/v1/docs/configuring-onewelcome-sso-for-your-account) | Yes | Yes | No | No | No | No |
| [PingFederate](/v1/docs/configuring-pingfederate-sso-for-your-account) | Yes | Yes | No | No | No | No |
| [PingOne](/v1/docs/configuring-pingone-identity-sso) | Yes | Yes | Yes | Yes | Yes | No |
| [RSA](/v1/docs/configuring-rsa-sso-ea) | Yes | Yes | Yes | Yes | Yes | No |
| [SafeNet (Classic)](/v1/docs/configuring-safenet-trusted-access-sso-for-your-account) | Yes | No | Yes | No | No | No |
| [SafeNet (EU)](/v1/docs/configuring-safenet-trusted-access-sso-for-your-account) | Yes | No | Yes | No | No | No |
