---
title: "Data Control Rule Doesn't Work on JAR File When Match By Source Code"
slug: "data-control-rule-doesn-t-work-on-jar-file-when-match-by-source-code"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/data-control-rule-doesn-t-work-on-jar-file-when-match-by-source-code"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Control Rule Doesn't Work on JAR File When Match By Source Code

## Issue

Data Control rule doesn't work on .JAR Files when it is configured to match by File Attribute where Content Type is "Source Code".

## Troubleshooting

The following Data Control rule was set up to Block the downloading of files with a Content Type identified as "source_code."

![dlp.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13207613566621.jpeg)

Next, we proceed to download two .jar files:

1. `java-1.0.jar`
2. `sample.jar`

**Observation**:

The download of `java-1.0.jar` was completed successful.

![successfuldl.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13207588787229.jpeg)

However, the download of `sample.jar` was blocked.

![blocksourcecode.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13207613572381.jpeg)

Why is the same rule treating these two .jar files differently?

## Solution

The reason is because a .jar file can either be a Zip archive or a specialized Java archive (JAR) file. When identified as a Zip archive, the aforementioned rule, configured to match by File Attribute where Content Type is "Source Code", would therefore result in no match. This explains on why the first file, `java-1.0.jar`, was not blocked during the download process.

We can use the `File`command in Linux to find out the content type of the .jar file.

**$ file java-1.0.jar**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13207433498141.png)

**$ file sample.jar**

**![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13207426744733.png)**

If the intent is to block all JAR file, regardless of the content type, then the solution would be to include the "Archives" Content-Type to the rule too. Note that this would also match all archives files like cab, tar, zip, gzip, etc. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13207575615261.png)
