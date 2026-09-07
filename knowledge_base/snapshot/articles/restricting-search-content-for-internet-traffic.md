---
title: "Restricting Search Content for Internet Traffic"
slug: "restricting-search-content-for-internet-traffic"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/restricting-search-content-for-internet-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Restricting Search Content for Internet Traffic

This article explains how to use the IPS service to restrict and block users from searching for explicit Internet content.

## Overview

You can configure the **Content Policy** in the IPS service to define how the Cato Cloud manages Internet search engines and YouTube content. The DNS server in the Cato Cloud creates a CNAME (canonical name) record for these conditions to redirect the appropriate Internet traffic:

- Google search engine routes to forcesafesearch.google.com
- Bing search engine routes to strict.bing.com
- Strict YouTube policy routes to restrict.youtube.com
- Moderate YouTube policy routes to restrictmoderate.youtube.com

When the **Content Policy** is enabled, the appropriate SafeSearch settings for the Google, Bing, or YouTube search engines are applied to the Internet or YouTube search. For example, if a user searched for **nudity**, the search engine SafeSearch filter removes all the results that are explicit. The search engine only shows websites with no explicit content. However, if a user browsed directly to **www.explicit_sample.com**, the connection to the website doesn't use the search engine and isn't restricted.

![ContentPolicy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33357221582109.png)

If you believe that content is classified incorrectly, please contact the appropriate Internet search engine or YouTube.

> [!NOTE]
> **Note:**
> 
> You can use the Internet firewall to block specific websites or categories. For more information, see [What is the Cato Internet Firewall?](/v1/docs/what-is-the-cato-internet-firewall).

**To configure the Content Policy for your account:**

1. From the navigation pane, click **Security > IPS**.
2. On the **Content Policy** tab, select each **Search Engine** that is included in the Content Restriction policy.
3. If you are including YouTube in the policy, configure the settings for the **YouTube content restrictions**:
  1. To enforce the content policy for YouTube, select **YouTube content restrictions**.
  2. In **Restrictions Level**, select to enforce **Moderate** or **Strict** content restrictions.
4. Click **Save**.

### Best Practices for Content Restrictions

When you implement Content Restrictions, it's possible that cached data in servers and user devices may prevent the traffic redirection required for enforcing the restrictions. We therefore recommend the following best practices when you first configure the restrictions:

- If your environment has internal DNS servers, clear the DNS cache on the servers
- Clear all cached DNS data on user devices, and clear all browser caches and cookies

### Using the Explicit Content Restriction Policy with Secure DNS

Internet browsers include an option to use DNS over HTTPS (DoH) as an additional security measure. When DoH is enabled for a browser, then it bypasses the SafeSearch settings in the Content Restriction policy. This means that even if the **Content Restriction** feature is enabled for your account, it doesn't apply to browsers that are using DoH for secure DNS.

Each browser has different DoH settings:

- Is DoH enabled by default for the browser?
- Some browsers (such as Chrome and Firefox) automatically disable DoH when they detect that the computer is managed by an organization

For accounts that enable the **Content Policy** feature, we recommend that you review the browsers that are used in your organization and the specific DoH settings.
