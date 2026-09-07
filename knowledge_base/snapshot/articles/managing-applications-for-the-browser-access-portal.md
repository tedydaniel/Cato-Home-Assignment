---
title: "Managing Applications for the Browser Access Portal"
slug: "managing-applications-for-the-browser-access-portal"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/managing-applications-for-the-browser-access-portal"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Applications for the Browser Access Portal

## Overview of Browser Access Applications

When users log in to the Browser Access Portal, they see all the Browser Access applications according to their access permissions. You can customize the name and icon for each application in the portal. When a user clicks an application, the application opens in a new window and the authentication token is used to log in users with SSO. If the authentication token is valid, then users can also directly enter the application URL to open the application without the portal.

This is an example of a Browser Access Portal:

![SDP_Portal.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218293210141.png)

> [!NOTE]
> Note:
> 
> Browser Access applications don’t support NTLM authentication.

## Adding Internal Applications

When you add a new application that's hosted on an internal server, define the URL for users to directly access the application without using the portal. After you define the external URL prefix for the application, you can configure the following settings:

- Base path of URLs that can access the application, this is a security feature that prevents access outside of this path
- Internal IP address or host name, and internal port number for the application
- Custom HTTP or HTTPS (TLS SNI) header for the application

You also have the option to configure the **Landing Page** for the application.

Later you can edit the application and configure the look and feel in the Browser Access Portal.

### **Defining the Internal Address for the Application**

You can customize the HTTP header, or TLS SNI for HTTPS, to support different deployments for internal servers. The following list summarizes the options to define the Internal address for Browser Access applications:

- Option 1 - Don't customize the header, and configure the **Host Address** with the IP address that is used to connect to the internal server. You don't define the **Host Name** field.
- Option 2 - Define the **Host Name** for the application which is added to the header. The **Host Address** (IP address or host name) is used to resolve the address or connect to the application.
- Option 3 - Configure the **Host Address** with the host name that is used to connect to the internal server. This host name is added to the header, and you don't define the **Host Name** field. Cato sends DNS queries for the host name to the DNS servers configured for the account with source IP 10.254.254.1 (or the corresponding IP address). If configured, DNS Forwarding rules are applied for the DNS queries.

#### Sample Configurations for Custom Internal Address

This section shows sample configurations for each of the **Internal host** options.

**Defining Host Address with an IP Address (Option 1)**

![Internal_Host_-_Option_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218324305693.png)

In the screenshot above, the **Host Address** is **10.20.20.20** and it is also used to connect to the application. There is no change to the HTTP header, or SNI.

**Defining Host Address with a Hostname and Adding a Host Name (Option 2)**

In the screenshot below, the **Host Address** is **gandalf.local** and the **Host Name** for the application is **samplehost.local**. **gandalf.local** is used to resolve the address, and **samplehost.local** is added to the HTTP header, or SNI.

![Internal_Host_-_Option_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218324360221.png)

**Defining Host Address with an IP Address and Adding a Host Name (Option 3)**

In the screenshot below, the **Host Address** is 10.20.20.20 and the **Host Name** for the application is **samplehost.local**. **10.20.20.20** is used to connect to the application, and **samplehost.local** is added to the HTTP header, or SNI.

![Internal_Host_-_Option_3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218298406045.png)

### Configuring the New Internal Application

Add a new application to the **Applications** window and define the settings for it. You can configure the look-and-feel, choose the Icon that is shown in the Browser Access Portal and the **Description** for the hover text.

You can enable the **Use source NAT IP range** option to define the translated source IP addresses for this application. For example, applications that use an Access Control List (ACL) to only allow connections from a specific IP range and admins that only use specific IP addresses in the network.

> [!NOTE]
> Note:
> 
> If the **Use source NAT IP range** option is grayed out, then you need to configure the **NAT IP Range** setting in the **Browser Access > Settings** tab or section.

**To add a new application to the Browser Access Portal:**

1. From the navigation menu, click **Access > Browser Access Control**.
2. From the **Applications** tab or section, click **New**.

The **Edit Application** panel opens.
3. Enter the application **Name** for the Browser Access Portal.
4. Enter a **Description** to configure the hover text for the application in the Browser Access Portal.
5. Configure the settings for the application URL:
  - **(Optional)** Application **Landing Page** for the users
  - **(Optional)Base Path** for the application, resources outside of this path are blocked and users can't access them
  - **URL prefix** that is added to the beginning of the URL
6. In **Icon**, upload the file with the icon for the application.
7. To enable the Browser Access Portal to translate the source IP address for an application, select **Use source NAT IP range**.
8. Configure the **Internal Host** settings for the application:
  1. In **Host Address**, enter the IP address or host name for the internal server that hosts the application.

When you define a host name as the **Host Address**, then it is added to the header. Otherwise, the IP address is used to connect to the internal server
  2. Enter the internal **Port** for the application.
  3. Select the **Protocol**, **HTTP** or **HTTPS**.
  4. **(Optional)** Enter the **Host Name** for the application server.

The **Host Name** is added to the header.
9. Click **Apply**.
