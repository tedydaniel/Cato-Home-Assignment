---
title: "Scanning Files in the Sandbox"
slug: "scanning-files-in-the-sandbox"
updated: 2026-08-26T10:33:57Z
published: 2026-08-26T10:33:57Z
canonical: "knowledge.catonetworks.com/scanning-files-in-the-sandbox"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scanning Files in the Sandbox

The Sandbox is an environment where files can be safely executed and analyzed to provide advanced threat protection. This article provides an explanation of the Sandbox and details how to enable it.

## Overview

The Sandbox is an isolated, secure, and virtual, environment where potentially malicious files are executed and analyzed without risk to your network. This provides in-depth forensic analysis for comprehensive malware investigation.

Once a file is executed and analyzed in the Sandbox, a comprehensive report is generated and made available for download in the CMA. This report includes both static and dynamic analysis offering a complete view of the file’s potential risk. For more information, see [Understanding the Sandbox Analysis Report](/v1/docs/understanding-the-sandbox-analysis-report),

The Sandbox is only available with an Advanced Threat Protection License. For more information, contact your sales representative.

### Scanning Files with the Sandbox

Any file the Anti-Malware policy identifies as malicious or suspicious is automatically scanned in the Sandbox. Once you enable the Sandbox, the Action for the [default ANY - ANY rules](/v1/docs/what-is-the-cato-anti-malware-policy) for blocking suspicious and malicious files changes to **Block & Scan**.

You can also upload specific files to scan in the Sandbox.

Files are scanned in a virtual Windows 10 OS environment.

### Understanding Static and Dynamic Analysis

In the Sandbox, files are scanned with static and dynamic analysis. This ensures broader detection of both known and unknown threats.

#### Static Analysis

Static analysis leverages machine learning (ML) models to detect threats by analyzing file properties without execution. The Sandbox static analysis:

- Scans file metadata and embedded attributes
- Quickly detects known threats based on signatures, file operations, PE headers, and behavioral traits

#### Dynamic Analysis

Dynamic analysis executes the files in the isolated environment to observe their behavior and detect malicious activity. The Sandbox dynamic analysis:

- Observes the file’s behavior in real time to identify evasive or unknown threats
- Detects advanced malware, including polymorphic threats that avoid detection in static analysis

### Use Cases

#### In-depth Forensic Analysis

Company ABC's relies on detection-only anti-malware solutions. This does not provide visibility into how a threat operates and prevents them from fully understanding attack tactics, payload behavior, or potential system impacts.

To address this, they enable the Sandbox to enhance their threat analysis capabilities. When a suspicious file is detected, it is automatically sent to the sandbox environment for Static and Dynamic analysis. The Sandbox monitors activities such as unexpected network connections, attempts to modify critical files, or privilege escalation efforts.

From the scan report the company can:

- Investigate root causes with in-depth insights
- Understand the attack's full impact on their systems
- Map the behavior to frameworks like MITRE ATT&CK for a structured response.

Using the Sandbox feature, reduces Mean Time to Detect and Mean Time to Respond, and strengthens their overall security posture.

#### Testing Suspicious Files in a Controlled Environment

An employee at company ABC received an email with a suspicious file that is blocked by their Anti-Malware policy. The employee contacts the IT security team claiming the file is safe and they require access to it.

Before providing the employee access to the file, they upload it to the Sandbox so it can be executed in a controlled environment.

The Dynamic analysis in the Sandbox identified the file attempted privilege escalation techniques and has a malicious verdict. The IT team do not provide access to the file and avoid a potential attack.

## Enabling the Sandbox

This Sandbox is enabled from the Anti-Malware Policy.

![Sandbox.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24708635258013(1).png)

**To enable the Sandbox:**

1. From the navigation menu, click **Security > Anti-Malware**.
2. Enable the **Sandbox** toggle.

## Scanning Specific Files in the Sandbox

You can investigate and analyze a specific file you believe is suspicious by manually uploading it to the sandbox. After you upload the file a report is generated.

![Sandbox_manual.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24708682098973(1).png)

**To scan specific files:**

1. From the navigation menu, click **Security > Sandbox Reports**.
2. Click **Upload File & Generate Report**.

The **Upload File** panel opens.
3. Upload the file you want to scan.
4. Click **Upload File & Generate Report**.

## Scanning Password-Protected Files

Attackers frequently deliver malware inside password-protected archives and Office documents to evade security scanning. When the Sandbox receives an encrypted file of a supported type, it attempts to open the file using a pre-defined list of passwords commonly observed in malware campaigns. If one of the passwords succeeds, the file content is extracted and analyzed with the standard static and dynamic analysis.

To see the list of pre-defined passwords, see [Scanning Password-Protected Files in the Sandbox](/v1/docs/scanning-password-protected-files) (you must be signed in to view this article)

## Testing the Sandbox

To test the Sandbox, and receive an example report, manually upload the zip file at the bottom of this article to the Sandbox. This file is a Malware test file.

## Sandbox File Requirements

The Sandbox supports the following file types:

- PE / 32-bit & 64-bit, EXE & DLL
- Office documents / OLE & Open XML formats
- RTF documents
- PDF documents
- Scripts / Javascript (JS/JSE/WSF), Visual Basic Script (VBS/VBE), PowerShell
- Java / JAR files
- Windows shortcuts / LNK & URL files
- Windows batch / BAT files
- Archive or compression types:
- 7-zip archive
- ace archive
- arj archive
- bzip2 compressed
- gzip compressed
- lha 1.x & 2.x archive
- microsoft cabinet archive
- tar archive
- posix tar archive
- rar archive
- xz compressed
- zip archive
- iso 9660 cd-rom
- .app (macOS supported for static analysis only)
- .dmg (macOS supported for static analysis only)

## Known Limitations

- Files exceeding 100MB are not supported

## Attachments

- [Cato_Sandbox_Test_File_manual(1).zip](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Cato_Sandbox_Test_File_manual(1).zip)
