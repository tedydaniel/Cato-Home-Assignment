---
title: "Websites with Prompt Page Don't Load Properly"
slug: "websites-with-prompt-page-don-t-load-properly"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/websites-with-prompt-page-don-t-load-properly"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Websites with Prompt Page Don't Load Properly

You can configure the Internet Firewall to use the **Prompt** action for the specific websites or applications. Users that try to go to these websites (or use the applications), they see a prompt page in their browser. They can click **Proceed** to continue to the website.

## Question

Sometimes users click **Proceed** in the prompt page, but the web content doesn't load.

For example:

**Facebook**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/FB_DoesntLoad.png)

**YouTube**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/YouTube_DoesntLoad.png)

## Answer

This behavior is caused by the Cato Cloud sends the prompt page to the client (the browser) which is HTML content. However, the browser is expecting a different type of content, for example images or a video.

This is a known limitation of the prompt rule. The following section explains the workarounds to this limitation.

## Workaround

You can create an exception to the Internet firewall rule with the Prompt action, and add the domain name to the exception.

Another solution, is to use the domain name in the Internet firewall rule instead of the application object. For example, instead of adding the Spotify application, configure the rule to Prompt for the domain **spotify.com**.
