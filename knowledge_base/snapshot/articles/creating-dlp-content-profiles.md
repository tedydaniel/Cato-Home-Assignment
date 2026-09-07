---
title: "Creating DLP Content Profiles"
slug: "creating-dlp-content-profiles"
updated: 2026-06-22T19:32:34Z
published: 2026-06-22T19:32:34Z
canonical: "knowledge.catonetworks.com/creating-dlp-content-profiles"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating DLP Content Profiles

This article explains how to create a Content Profile for Cato's DLP service. This profile includes one or more of the DLP Data Types which you can use in an Application Control policy or SaaS Security API Data Protection policy.

## Overview

Cato’s Data Loss Prevention (DLP) service helps you monitor and control sensitive information across your network. You can add DLP content profiles to a Data Control rule to detect or block sensitive data and prevent potential exfiltration. DLP can scan text-based content, include data embedded in images by using OCR-based inspection, and documents embedded in files.

Content Profiles can include predefined data types or custom data types, including User-Defined Data Types and Sensitivity Labels. For more about data types, see the following articles:

- [Working with Predefined Data Types for DLP](/v1/docs/working-with-predefined-data-types-for-dlp)
- [Working with Custom Data Types for DLP](/v1/docs/working-with-custom-data-types-for-dlp)
- [Using MIP Sensitivity Labels in your Cato DLP Policy](/v1/docs/using-mip-sensitivity-labels-in-your-cato-dlp-policy)
- [Working with Google labels in your Cato DLP Policy](/v1/docs/using-google-labels-with-the-data-protection-api)
- [Working with Exact Data Matching (EDM) for DLP](/v1/docs/working-with-exact-data-matching-edm-for-dlp)

The DLP **Content Profile** is a global object for the Cato Management Application which includes one or more Data Types.

### OCR Image Scanning for Content Profiles

You can configure a Content Profile so the DLP engine includes image files and images embedded in files in content matching for the profile. The engine uses OCR to extract text that appears in image files and sends the extracted text for content matching. The OCR scanning option appears when configuring a Content Profile. OCR image scanning includes:

- Low-resolution and blurred mobile images
- Warped, rotated, or crumpled images
- Images that contain text in two languages

#### Language Support

Predefined ML Classifiers identify sensitive data, for example, a resume, in over a hundred languages. For more information, see [Working with Predefined Data Types for DLP](/v1/docs/working-with-predefined-data-types-for-dlp).

## Creating a Content Profile

Use the DLP Configuration page to create and edit Content Profiles. When you are adding Data Types to a profile you can filter the types according to a specific country or **Universal** (for all countries). In addition, you can sort the Data Types in ascending or descending alphabetical order according the the category or name, or according to the country.

When you add multiple Data Types to a profile, select the relationship between them:

- **Any (OR)** - Match only one of the Data Types in the profile
- **All (AND)** - Match all the Data Types in the profile (otherwise, the rule with this profile is ignored)

A Data Control rule can contain up to 20 Data Types across all Content Profiles.

When you configure a Content Profile, optionally enable [OCR scanning](/v1/docs/creating-dlp-content-profiles#ocr-image-scanning-for-content-profiles) for the profile.

![DLP_Configuration.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32002107369885.png)

**To create a DLP Content Profile:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and in the **DLP Profiles** tab select **Content Profile**.
2. Click **New**.

The **Add Content Profile** panel opens.
3. Create the profile and add the Data Types.
4. Optionally, select **OCR Scan Enabled** for the profile.
5. Click **Apply** and then click **Save**.

### Viewing the Data Types

The **Data Types** page shows all the Data Types that you can add to a profile. This lets you research and understand more about specific Data Types that you are using in your organization. The catalog also shows the **Threshold** for each data type, indicating the minimum number of occurrences to activate the data type. For more about data type thresholds, see [Working with Custom Data Types for DLP](/v1/docs/working-with-custom-data-types-for-dlp).

![Data_Types6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643826162333.png)

**To show the Data Types:**

- From the navigation menu, select **Security > Data Types & Profiles,**, and click the **Data Types** tab.

## DLP File Requirements

Files up to 50 MB are supported. The supported file types are listed below (Audio, video, and binary files are not supported).

### Document Files

- CSV files: `.csv`
- Excel Template: `.xlt, .xltx`
- Excel Workspace: `.xlw`
- Microsoft Access Database: `.mdb`
- Microsoft Excel: `.xls, .xlsx, .xlsm, .xlam, .xlsb, .slk, .xltm`
- Microsoft PowerPoint: `.ppt, .pps, .pot, .pptx, .ppsx, .pptm, .ppsm, .potx, .potm`
- Microsoft Word: `.doc, .docx, .docm, .dotx`
- MS Access Project: `.ade`
- ODF Documents: `.odt, .ods, .odp`
- ODF Presentation Template: `.otp`
- ODF Spreadsheet Template: `.ots`
- ODF Text Template: `.ott`
- Outlook Form Template: `.oft`
- Portable Document Format: `.pdf`
- Rich Text Format: `.rtf`
- SQL files: `.sql`
- Text files: `.txt`
- XPS files: `.xps`
- XML files: `.xml`

### Embedded Documents

Documents embedded in these file types are scanned. Up to 5 embedded files per file, if a file contains more than 5 embedded files, only the 5 largest files are scanned.

- Microsoft Excel: `.xls, .xlsx`
- Microsoft PowerPoint: `.ppt, .pptx`
- Microsoft Word: `.doc, .docx`

### Archive Files

- 7-Zip: `.7z`
- ARJ: `.arj`
- Bzip2: `.bz, .bz2`
- Cab Archive: `.cab`
- GZIP: `.gzip, .gz`
- LHA: `.lha, .lzh`
- RAR: `.rar`
- RPM: `.rpm`
- Tar: `.tgz, .gtar, .tar`
- Unix Archive: `.cpio, .shar`
- UUE: `.uue`
- WAR: `.war`
- XAR: `.xar`
- ZIP: `.zip`

### Image Files

For PNG and JPEG files, scanning is only supported for the Upload action

- Bitmap: `.bmp`
- BMP Uncompressed: `.bmp-uncompressed`
- JFIF files: `.jfif`
- JPEG files: `.jpeg, .jpg`
- PBM files: `.pbm`
- PGM files: `.pgm`
- PNG files: `.png`
- PNM files: `.pnm`
- PPM files: `.ppm`
- Progressive JPEG: `.pjpeg, .pjp`
- TIFF files: `.tiff, .tif`
- WebP files: `.webp`

### Embedded Images

Images embedded in these files types are scanned. Up to 5 images are scanned per file, if a file contains more than 5 images, only the 5 largest images are scanned.

- Microsoft Excel: `.xls, .xlsx`
- Microsoft PowerPoint: `.ppt, .pptx`
- Microsoft Word: `.doc, .docx`
- Portable Document Format: `.pdf`

### Email and Message Files

- Base64 encoded: `.base64`
- Microsoft Outlook Data File: `.pst`
- Microsoft Outlook Message: `.msg, .eml`
- MIME: `.mime`
- Outlook Express: `.dbx`
- TNEF / winmail.dat: `.dat`
- Unix mbox: `.mbox`
- UTF-16: `.utf-16`

### Source Code and Script Files

- Bash scripts: `.sh`
- Basic source code: `.bas`
- Batch files: `.cmd, .bat`
- C, C++, and C# source files: `.c, .h, .cc, .hh, .cs, .cpp, .hpp`
- Go files: `.go`
- HTML files: `.html`
- Include files: `.inc`
- Java files: `.java, .jav, .j`
- JavaScript files: `.js`
- Make files: `.mak, .mk, .pmk`
- Matlab files: `.mat`
- Perl files: `.pl, .pm, .plf`
- Python files: `.py, .pyi, .pyc, .pyd, .pyo, .pyw, .pyz`
- Ruby files: `.rb`
- Scripts / config files: `.ini, .json`

### Other Supported Files

- HTTP form data: `.http`
- Internet signup files: `.isp, .ins`
- PCAP files: `.pcap`
- TrueType font files: `.ttf`
