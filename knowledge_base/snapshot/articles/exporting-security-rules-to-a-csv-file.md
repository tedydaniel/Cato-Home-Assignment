---
title: "Exporting Security Rules to a CSV File"
slug: "exporting-security-rules-to-a-csv-file"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/exporting-security-rules-to-a-csv-file"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting Security Rules to a CSV File

You can generate a CSV file that contains the data of all the rules for a Security policy rulebase in your account.

## Exporting Security Rule Data

You can export the Security rule data to a CSV file for the following policies:

- Internet firewall
- WAN firewall
- TLS Inspection
- Application Control

> [!NOTE]
> Note:
> 
> Firewall sections are not included in the export data.

Only Cato Management Application admins with **Editor** role have permissions to export to a CSV file. For more about configuring admin roles, see [Managing Administrators](/v1/docs/managing-admins).

**To export the rule data:**

1. From the navigation menu, select the relevant page.
2. Click **Export**, and in the pop-up window click **OK**.

The **Save** window for the browser opens.
3. Select the location for the CSV file and save the file.

The Cato Management Application exports the data for the Security rules to a CSV file.

## Understanding the Contents of the Exported File

The top row in the exported CSV file lists the field names and options for rules in the relevant rulebase. Then the rules themselves are listed according to priority, starting with the lowest number value (Cato predefined rules have a priority of -1). Exceptions immediately follow their parent rules.

Fields containing multiple values include the relevant logical operator between the values (OR or AND).

Some fields specify a data type and a value. For example, a **Source** configured with the IP address 10.10.10.0 appears in the CSV file as **IP is 10.10.10.0**.

This is an example of a CSV file for an Internet firewall rulebase:

![CSV_Example_Internet_FW.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24198327893917.png)
