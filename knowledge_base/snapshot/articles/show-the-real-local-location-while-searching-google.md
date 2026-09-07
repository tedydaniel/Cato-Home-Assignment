---
title: "Show the real local location while searching Google"
slug: "show-the-real-local-location-while-searching-google"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/show-the-real-local-location-while-searching-google"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Show the real local location while searching Google

Google uses an algorithm that includes the IP address, location history, and recent location searches to identify where a user is located (see [https://support.google.com/websearch/answer/179386](https://support.google.com/websearch/answer/179386)).

The reliance on using the IP address means that Google will detect users coming from the location of Cato PoP that the tunnel is connected to.

If you perform a Google search and scroll to the very bottom, there should be a message stating how Google found your location. The screenshot below for instance, while Cato Client is connected to Chicago PoP. Google detected the location from the PoP's IP address even though physical location is different.

Google does provide the "Update location" or "Use precise location" link.

A possible way to workaround this would be to add a destination bypass for all of Google's IP ranges in the Cato Management Application (Configuration > Sites > [Site Name] > Bypass). If you're in control of your DNS server, you might also be able to configure an intercept and return a single IP address for all [google.com](http://google.com/) DNS requests so you wouldn't need to bypass multiple ranges.

Adding the bypass for Google's ranges would mean all that traffic would be sent using the tunnel own IP address and bypass the Cato Cloud. The downside of doing this is that the traffic would not be subject to any security policies, including threat prevention.

For reference, a Google's public IP ranges at [https://kx.cloudingenium.com/cloud/google-cloud/google-ip-address-ranges/](https://kx.cloudingenium.com/cloud/google-cloud/google-ip-address-ranges/) which is subject to be changed, thus, can't guarantee the accuracy of that list, but the author does provide a method to get more current results. You would need to add each network on a separate line, and you can use CIDR notation.
