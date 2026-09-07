---
title: "Browser Access Portal Troubleshooting"
slug: "browser-access-portal-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/browser-access-portal-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser Access Portal Troubleshooting

## Overview

The Application Portal (AKA Browser access) portals allow users to access their internal corporate resources by establishing a secure tunnel via the Internet. This service doesn't require an SDP connection, but it does require users to be licensed SDP users. This playbook discusses common Browser Access issues and provides troubleshooting steps to address them.

## Symptoms

- User accessing the Application Portal gets an Access Denied Page
- The application doesn't show up in the Browser Access Portal
- The application fails to load.
- Missing contents in web application
- Wrong format of contents in web applications. For example, the elements are arranged randomly on the page, text is in the wrong font size, images are not correctly aligned, etc.
- Apps time out for Clientless Browser Access; SDP client users operate normally.

## Possible Causes

- Misconfigurations
- Use of HTTP protocol and web application contains absolute HTTP links to other contents

## Troubleshooting the Issue

This section will investigate the steps for troubleshooting common Application Portal issues.

### Users Cannot Access The Application Portal

When the user accesses the Application Portal using the Portal URL specified in *Access > Application Portal > Setting*s, they are greeted with the Access Denied message.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16437466159133.png)

1. Validate that the subdomain does not contain special characters. Characters such as hyphens are not supported. Refer to Changing the subdomain to exclude special characters for instructions on how to validate that special characters are used in the Subdomain.
2. Verify the user is an SDP (licensed) user. Only users that have been assigned a license can access the Browser Access Portal. Refer to [Assigning license to users](/v1/docs/browser-access-portal-troubleshooting#assigning-licenses-to-users) for instructions on how to validate this.
3. If SSO authentication is enabled and "Allow login with Single Sign-On" is checked (*Access > Single Sign-On*), verify that the user domain is included in the Allowed Domains. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16436758448925.png)
4. Check in the Events for any obvious errors. Go to *Home > Events* and add a Filter as shown below. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19149440007581.png)All events related to the browser access portal will be shown. Below is an example of an Access denied event. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19149440009373.png)

### Applications Didn't Show Up In Application Home Page

When the user logs into the Browser Access Portal, specific applications do not appear.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16437466160797.png)

1. Validate that the application is added in *Access > Applications Portal > Applications*. If it is not added there, it won't reflect on the Application Portal homepage.
2. Ensure that the user has access to the application. If not, he won't be able to see it on the application's home page. This can be done in the *Access > Applications Portal > Access Policy*.
3. For instructions on resolving these issues, refer to [Adding application to browser access portal](/v1/docs/browser-access-portal-troubleshooting#adding-an-application-to-the-browser-access-portal) and [Configure access policy for allowed users](/v1/docs/browser-access-portal-troubleshooting#configure-access-policy-for-allowed-users).

### The Application Fails to Load

When clicking the Application icon, the browser may show no content, and the Application stays loading until it times out.

If the above occurs, collect the following data:

1. Collect a PCAP capture from the Socket from the site where the Application server is hosted, as explained in [How to Capture Traffic on a Socket](/v1/docs/how-to-capture-traffic-on-a-socket). Filter the web server's IP address and port 80 or 443, depending on the port configured for the application in CMA.
2. Confirm whether there is TCP traffic flow from the web server. If not, check local connectivity to the server. Without NAT, traffic reaching your internal server will be sourced from a public IP address.
3. Verify whether or not using the [NAT IP range](/v1/docs/configuring-the-browser-access-portal) is needed for proper routing to/from the internal network. Without NAT IP range, traffic reaching the internal server will be sourced from a public IP address.
4. If TCP traffic is seen in step #2, collect a HAR file through the Browser Access Portal while accessing the application by following these steps:
  1. From the browser access portal, right-click anywhere on the page and select "Inspect" from the context menu.
  2. Click on the settings button located in the top right corner. This option is available in Chrome. If you're using a different browser, proceed to step #4. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21505484090269.png)
  3. Under Preferences > Global, select 'Auto-open DevTools for popups'.
  4. Click on the application from the browser access portal. A second tab will open. This is where the recording must take place. Unless your browser records from this second tab automatically (step #3), you will need to perform this action manually in the next step.
  5. Follow the instructions from [How-to-Collect-HAR-Data](/v1/docs/how-to-collect-har-data) to reproduce the issue and collect the HAR file.
  6. Submit this information to Cato Support for further investigation. See [Raising cases to Cato Support](/v1/docs/browser-access-portal-troubleshooting#raising-cases-to-cato-support)
5. If the HAR file shows a redirection to an internal domain, the external browser won't be able to resolve it since it does not perform DNS resolution with the internal network. This is currently a limitation of the Browser Access solution, and the user should connect to Cato via SDP Client.

Submit this information to Cato Support for further investigation. See [Raising cases to Cato Support](/v1/docs/browser-access-portal-troubleshooting#raising-cases-to-cato-support).

### The Web Application Exhibits Formatting Issues

The formatting of the web application is problematic, with elements placed in a disorderly manner on the page, text displaying inconsistent font sizes, and images appearing misaligned. This problem may arise when a customer accesses a web application through the Browser Access Portal using the HTTP protocol, and the HTML code of the web application includes absolute HTTP links to other contents. Because the Browser Access Portal connection operates on HTTPS, contemporary web browsers will restrict access to HTTP content, commonly referred to as "mixed content.

Follow these steps to verify if you are encountering this issue.

1. You can collect the HAR file through the Browser Access Portal while accessing the application. For detailed instructions, refer to [How-to-Collect-HAR-Data](/v1/docs/how-to-collect-har-data).
2. If this is the problem, web developer tools will display mixed content blocks, accompanied by a warning indicating that the connection to the website is not secure. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16879638350493.png)
3. Right-click anywhere on the page and select "View Page Source." This will open up the website's source code.
4. Examine for any links beginning with "http://" as illustrated below: <link href="http://nms-ubuntuserver.via.catonetworks.com/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
5. The presence of the HTTP links in the source code is why the browser is blocking the content.
6. Follow the suggestions outlined in [Formatting Issues](/v1/docs/browser-access-portal-troubleshooting#formatting-issues) to resolve this problem.

### Apps time out for Clientless Browser Access; SDP client users or site users can access normally.

The portal loads, but the apps behind it won’t open. Users on the client-based SDP app or users behind cato sockets can reach everything normally. Users coming through Clientless Browser Access hit timeouts when they try to open any application.

> [!NOTE]
> Note:
> 
> Browser-based remote access doesn't support overlapping IPs between an SNAT IP range and IP range for the site.

For example Browser Access is using a NAT range like **10.60.10.0/24**. At the same time, your network is advertising a broader route, such as **10.0.0.0/8**, into Cato. Because **10.60.10.0/24** sits inside that **10.0.0.0/8** block, the platform sees the returned traffic as overlapping with the site’s own subnet. When traffic tries to come back to a Browser Access user, the platform drops it to avoid creating a routing loop, since the broader **/8** route would pull the packet back toward the site instead of to the user. This overlap prevents the platform from installing a clean return route for Browser Access traffic.

To resolve the issue, validate SNAT and Account Routes

1. Identify the SNAT IP range configured for Browser Access. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32373400742301.png)
2. Navigate to Routing Table under your account > network. Check all account routes and confirm none overlap with the SNAT range. No data means no overlap exists in the routing table.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32373400743581.png)
3. If an overlap exists:
  - Adjust the routing configuration to remove the conflict.
  - Ensure BGP-advertised routes do not cover the SNAT range.

## Resolving Discovered Issues

### Misconfiguration

Many of the issues mentioned above are related to configuration. Once you've identified the misconfigured areas, resolving them should address the problem.

#### Changing the Subdomain to Exclude Special Characters

Navigate to Access > Single Sign-On and ensure no special characters are in the Subdomain field. This requirement is also mentioned in [Configuring-the-Browser-Access-Portal](/v1/docs/configuring-the-browser-access-portal). For more information on the impact of changing the subdomain, refer to [Changing-your-Account-Name-and-Subdomain](/v1/docs/changing-your-account-name-and-subdomain).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16928423415709.png)

#### Assigning Licenses to Users

Navigate to Access > Users > Users Directory and validate that the user accessing the browser access portal is a licensed SDP user

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16928366563229.png) To assign a license to a user, refer to [Assigning-SDP-Licenses-to-Users](/v1/docs/assigning-ztna-licenses-to-users)

#### Adding an Application to the Browser Access Portal

Navigate to Applications Portal > Application and validate that the application is added. Refer to [Managing-Applications-for-the-Browser-Access-Portal](/v1/docs/managing-applications-for-the-browser-access-portal) for configuration details. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24071477626269.png)

#### Configure Access Policy for Allowed Users

Navigate to Access > Applications Portal > Access Policy and validate that the user can access the applications. For configuration details, refer to [Defining-the-Browser-Access-Policy](/v1/docs/defining-the-browser-access-policy). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24071477629725.png)

### Formatting Issues

The solution involves modifying the application's source code as the browser is responsible for blocking mixed content, not Cato. The customer is advised to transform absolute links (those starting with http://) in the HTML code into relative links. Relative links can be either protocol-relative or root-relative. For instance, if you have a link resembling:

```plaintext
href="http://www.mywebsite.com/css/stylesheet.css"
```

A protocol-relative link would be like this:

```plaintext
href="//www.mywebsite.com/css/stylesheet.css"
```

A root-relative link would look something like this:

```plaintext
href="/css/stylesheet.css"
```

For more information on absolute and relative links, you can refer to [absolute-vs-relative-urls](https://stackoverflow.com/questions/2005079/absolute-vs-relative-urls).

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the troubleshooting steps outlined above. For issues related to accessing browser portal applications, please also include answers to the following questions:

1. What is the affected application server? (IIS, Nginx, etc.)
2. Does the application require additional authentication?
3. Does the user have access to application logs or configuration files? If so, do these logs capture the issue?
4. What are the locations from which users are connecting to the SDP portal?
5. Can users connect to the application when using the Cato Client or when they are behind a Socket site?
6. Is there a load balancer/API server/firewall between them?
