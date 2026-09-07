---
title: "ADUC Loads Slowly While Connected to Cato SDP Client"
slug: "aduc-loads-slowly-while-connected-to-cato-sdp-client"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/aduc-loads-slowly-while-connected-to-cato-sdp-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ADUC Loads Slowly While Connected to Cato SDP Client

## Issue

Active Directory Users and Computers (ADUC) may experience latency or slowness while connected to the Cato SDP Client.

## Environment

- Cato SDP Client v4.2 and above

## Troubleshooting

While it is running, ADUC makes DNS queries for non-standard, non-existent SRV records. These queries are not necessary and it's not known why ADUC makes them. For more information, see [DNS client resolver behavior](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn593685(v=ws.11)#dns-client-resolver-behavior)

Cato SDP Client blocks DNS requests on every network interface except for the Cato VPN interface in order to direct DNS through the VPN tunnel. This works well for almost all applications but ADUC because of the SRV queries mentioned above.

If ADUC does not receive a positive response to the queries from the DNS servers configured on the Cato VPN adapter, it sends the queries to the DNS servers configured on the physical (WiFi, Ethernet) adapter. These queries are blocked by the Cato VPN client so ADUC never receives a response. Although this has not been acknowledged or confirmed by Microsoft, we believe that ADUC waits for the DNS queries to time out on the physical adapters before proceeding, and that explains the slow load times. As far as we know, ADUC is the only application exhibiting this behavior, and it could very well be a Microsoft bug.

To verify that the above issue is encountered, a PCAP capture can be taken on the tunnel. Filter for DNS (port 53) while the user opens ADUC. Apply the following filter in Wireshark to view SRV queries:

```plaintext
dns.qry.type == 33
```

ADUC makes queries for non-existent SRV records in two distinct formats:

1. _ldap._tcp.*DCName*.*Domain.com*
2. _ldap._tcp.*SiteName.*_sites.*DCName*.*Domain.com*

Where *DCName* is the NetBIOS name (hostname) of a Domain Controller (DC), *SiteName* is the name of the site in which the DC resides, and *Domain.com* is the domain.

ADUC can potentially query SRV records for every DC in a domain. The problem stated in this article exists if you see any of the SRV queries and a "No such name" response in the PCAP.

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079598986653.png)

## Solutions

- Use Remote Desktop or another remote access tool to log into the DC and manage Active Directory.
- Use Active Directory Administration Center (ADAC) to manage Active Directory remotely. ADAC is a newer and more powerful tool than ADUC when it comes to AD management, but there is a learning curve. For more information about ADAC visit [Active Directory Administrative Center](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-administrative-center)
- Create the SRV records that ADUC queries for in Windows DNS. See the instructions below.
  - [Manually Create SRV Records](/v1/docs/aduc-loads-slowly-while-connected-to-cato-sdp-client#manually-create-srv-records)
  - [Automatically Create SRV Records Using PowerShell](/v1/docs/aduc-loads-slowly-while-connected-to-cato-sdp-client#automatically-create-srv-records-using-powershell)
- Contact [Cato Support](/v1/docs/submitting-a-support-ticket) for additional troubleshooting and backend alternative solutions.

### Manually Create SRV Records

1. Open DNS Manager on the DNS server.
2. Expand Forward Lookup Zones.

![mceclip2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079591305757.png)
3. Right-click your domain and click “New Domain…”.

![mceclip3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079569874333.png)
4. Enter the hostname of the DC as the domain name.

![mceclip4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079598987805.png)
5. Right-click the subdomain created in the previous step and select “Other New Records…”.

![mceclip5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079583160861.png)
6. Select Service Location (SRV) and click “Create Record…”.

![mceclip6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079604847773.png)
7. Enter the following parameters in the pop-up window:

![mceclip7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079598990621.png)
  - **Service:** _ldap
  - **Protocol:** _tcp
  - **Host offering this service:** the FQDN of the DC with a period at the end.
8. Click "OK". An SRV record will be created.

![mceclip8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079591308317.png)
9. Right-click the subdomain named after the DC you created in step 4 and select “New Domain…”

![mceclip9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079569880221.png)
10. Name the domain “_sites” and click "OK".

![mceclip10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079598994205.png)
11. Right-click the _sites domain and select “New Domain...”.

![mceclip11.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079583185437.png)
12. Name the subdomain created in the previous step after the site that the DC resides in and click "OK".

![mceclip12.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079604849949.png)
13. Right-click the subdomain created in the previous step and select "Other New Records...".

![mceclip13.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079598995101.png)
14. Select Service Location (SRV) and click "Create Record...".

![mceclip14.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079583189917.png)
15. Enter the following parameters in the pop-up window:

![mceclip15.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079569884701.png)
  - **Service:** _ldap
  - **Protocol:** _tcp
  - **Host offering this service:** the FQDN of the DC with a period at the end.
16. Click "OK". A new SRV record will be created.

![mceclip16.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079598997917.png)
17. Repeat steps 3-16 for each DC in your domain.

### Automatically Create SRV Records Using PowerShell

The PowerShell script below can be run on a DC to create all the necessary SRV records for a domain as long as the DNS servers are also Domain Controllers. Please note that this script may have to be modified to work in the customer's environment and Cato Support is not responsible for making any modifications to this script. Customers should use this script at their own risk.

**Recommended Usage:**

1. Save the script in a file with extension .ps1 and copy it to a DC.
2. On the DC, open PowerShell with administrator privileges and run the script:

```plaintext
path_to_script.ps1
```
3. Observe that the correct domain and a DNS server were detected by the script and that the list of all DCs in the domain is correct.
4. By default, the script prompts before creating SRV records for each DC. we recommend using this method at least for the first DC and then verify that the SRV records were created successfully before continuing.
5. If the SRV records for the first DC were created successfully, you can execute the script again but choose the "Bulk create" option [B] to create all SRV records at once without prompts.

Sample Output:

![mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12079583193373.png)

Script:

```plaintext
$allDCs = (Get-ADForest).Domains | %{ Get-ADDomainController -Filter * -Server $_ } | Select-Object -Property Name, HostName, Domain, Site
$Domain = (Get-ADForest).Name
Write-Host ""
Write-Host "Domain:"
Write-Host " $Domain"
$DNSstring = nslookup -type=ns $Domain | Select-String -Pattern 'nameserver'
$DNSstring -match '(?<=nameserver = )(.*)' > $null
$DNSserver = $Matches[1]

Write-Host ""
Write-Host "Found DNS server:"
Write-Host " $DNSserver"
Write-Host ""
Write-Host "Found Domain Controllers:"
Foreach ($DC in $allDCs) {
 Write-Host " $($DC.HostName)"
}

$title = 'Create SRV Records'
$question = 'How do you want to create SRV records?'

$bulk = New-Object System.Management.Automation.Host.ChoiceDescription "&Bulk create", "Creates all SRV records at once."
$prompt = New-Object System.Management.Automation.Host.ChoiceDescription "&Prompt for each", "Prompts before creating each SRV record."
$choices = [System.Management.Automation.Host.ChoiceDescription[]]($bulk, $prompt)

$decision = $Host.UI.PromptForChoice($title, $question, $choices, 1)
if ($decision -eq 0) {
 Foreach ($DC in $allDCs) {
 Add-DnsServerResourceRecord -Srv -Name "_ldap._tcp.$($DC.Name)" -ZoneName $DC.Domain -DomainName "$($DC.HostName)" -Weight 0 -Priority 0 -Port 389 -ComputerName $DNSserver
 Add-DnsServerResourceRecord -Srv -Name "_ldap._tcp.$($DC.Site)._sites.$($DC.Name)" -ZoneName $DC.Domain -DomainName "$($DC.HostName)" -Weight 0 -Priority 0 -Port 389 -ComputerName $DNSserver
 }
 Write-Host ""
 Write-Host "Created SRV records for all DCs."
} elseif ($decision -eq 1) {
 Foreach ($DC in $allDCs) {
 Write-Host ""
 Write-Host "Create SRV records for $($DC.HostName)?" -ForegroundColor Yellow 
 $Readhost = Read-Host " ( y / n ) "
 if ($Readhost -eq 'y') { 
 Add-DnsServerResourceRecord -Srv -Name "_ldap._tcp.$($DC.Name)" -ZoneName $DC.Domain -DomainName "$($DC.HostName)" -Weight 0 -Priority 0 -Port 389 -ComputerName $DNSserver
 Add-DnsServerResourceRecord -Srv -Name "_ldap._tcp.$($DC.Site)._sites.$($DC.Name)" -ZoneName $DC.Domain -DomainName "$($DC.HostName)" -Weight 0 -Priority 0 -Port 389 -ComputerName $DNSserver
 }
 }
 Write-Host ""
 Write-Host "Done creating SRV records."
} else {
 Write-Host 'Cancelled'
}
```
