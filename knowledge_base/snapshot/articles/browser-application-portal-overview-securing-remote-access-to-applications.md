---
title: "Browser Application Portal Overview - Securing Remote Access to Applications"
slug: "browser-application-portal-overview-securing-remote-access-to-applications"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/browser-application-portal-overview-securing-remote-access-to-applications"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser Application Portal Overview - Securing Remote Access to Applications

This article explains how browser access works in the Cato Cloud, to provide secure access to applications and protocols without using the Cato Client.

## What is Browser Access

Browser Access is the ability to access applications and remote hosts via the web browser (HTTP/S) while preventing direct communication between the users and the resources they are accessing.

You can provide access to hosted services like your time management system, or expense reporting, as well as configuring RDP or SSH access to virtual or physical hosts.

Define the specific applications and protocols that will appear in the corporate portal. Your users use a standard web browser to access the portal, and the traffic is securely routed through the Cato Cloud to that resource.

> [!NOTE]
> Note:
> 
> Browser access is supported on common browsers, including Chrome, Edge, and Safari on Windows and macOS devices, as well as iOS and Android devices.

By preventing direct access over the Internet to the resource, you are adding an additional layer of security while still enabling users to access the resources that they need.

### Use Case - RDP

![VDI.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24709785700765.jpg)

ABC Company has several hosts located in a data center in Atlanta, Georgia. Their admins need to periodically access these hosts for maintenance work. They set up RDP access to each of these hosts and define exactly which operations the admins can perform remotely.

The admins connect to the Application Portal via HTTP/S, and click on the icon for the remote host. The request is forwarded to the Translation Engine, which sits on the PoP, and their connection request is then sent using RDP to the remote host.

### Use Case - Expense Reporting

![Application.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24709838251165.jpg)

XYZ Company requires all of their contractors to fill out an expense report via an internal reporting system. Instead of giving the contractors direct access to the system, they expose it through the access portal so that the contractors can access it externally.

The contractors connect to the Application Portal via HTTP/s, and click on the icon for the relevant application (i.e. Concur). The request is forwarded to the application server located at an internal IP address to which the contractors have no direct access.

### Use Case - SSH for IoT Devices

![IoT-OT.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24709813684509.jpg)

ABC Company works with different IoT devices to manufacture its products. When one of those devices requires maintenance, ABC is able to provide the technician SSH access to the device so they can fix or update what needs to be maintained.

The technicians connect to the Application Portal via HTTP/S, and click on the icon for the remote IoT host. The request is forwarded to the Translation Engine, which sits on the PoP, and their connection request is then sent using SSH to the remote host.

## High-Level Overview of Configuring the Browser Access Portal and Applications

This section is a high-level overview of the process to configure the Browser Access Portal and apps for your account. These are the options for users to authenticate to the portal:

- SSO authentication tokens from the IdP defined for the account
- Cato user credentials defined in the CMA

> [!NOTE]
> Note:
> 
> Browser-based remote access doesn't support overlapping IPs between an SNAT IP range and IP range for the site.

1. **(Optional)** Configure (or verify) the Single sign-on (SSO) settings for the account (see [Configuring SSO and the Subdomain for the Account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account)).
2. Configure the settings for the Browser Access Portal (see [Configuring the Browser Access Portal](/v1/docs/configuring-the-browser-access-portal)):
  1. Configure the basic settings for the portal, the URL and logo.
  2. Define the domains that are allowed to connect to the portal.

The email domains of the clientless users are validated against the allowed domains for the Browser Access Portal.
  3. Configure the SSO provider for your Cato account and define the authentication cookies.
  4. If necessary, define the NAT IP range for the Browser Access applications.
3. Create the Browser Access applications (see [Managing Applications for the Browser Access Portal](/v1/docs/managing-applications-for-the-browser-access-portal) or [Defining Browser Access to Remote Hosts](/v1/docs/defining-browser-access-to-remote-hosts) ):
  1. Configure the application name and URL prefix.
  2. Define the host server IP address, port number, and web protocol.
  3. Determine which actions the user can perform
4. Define the rules for the Browser Access access policy to control which users are allowed to access the applications (see [Defining the Browser Access Policy](/v1/docs/defining-the-browser-access-policy)):
  1. Define the users and groups that are allowed to access the applications for the rule.
  2. Add the applications for the rule.

## Known Limitations

- ​IPv6 IP addresses are not supported
- Browser Access is not supported in China
- RDP connections to Remote Desktop Services (RDS) environments that use a connection broker or load balancer (RDP farms) are not supported. Only direct RDP connections to a specific host are supported.
