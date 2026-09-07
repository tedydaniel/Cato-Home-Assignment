---
title: "Configure Custom Allowlists for SSO"
slug: "configure-custom-allowlists-for-sso"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configure-custom-allowlists-for-sso"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Custom Allowlists for SSO

This article provides information about creating custom allowlists as required by your IdP.

## Overview

Custom Allowlists enable you to define additional FQDNs or IP addresses required by your Identity Provider (IdP) during the authentication process. This is useful when your IdP uses external resources, such as scripts, stylesheets, or redirect URLs, that are not already included in Cato’s default allow list. You can configure entries using IP/mask or FQDN formats, and include single-level wildcards (e.g., *.example.com).

### Use Case

ABC company uses a third-party IdP that references additional external assets hosted on a content delivery network (CDN) like cdn.idp-example.com. While Cato automatically allows common IdP-related URLs, this custom domain isn’t included in the static allow list. To ensure a smooth login experience, you can add cdn.idp-example.com or *.idp-example.com to the Custom Allowlist, allowing users to authenticate without connection issues.

## Configuring Custom Allowlists

**To configure a Custom Allowlist**

1. Navigate to Access > Single Sign-On and click the **Custom Allowlist** tab.
2. Under **Allowlist Details**, select **IP/Mask** or **FQDN**.
3. Enter the value, for example 10.10.0.0/32 or *.idp-example.com.
4. Click **Add** and then click **Save**.
