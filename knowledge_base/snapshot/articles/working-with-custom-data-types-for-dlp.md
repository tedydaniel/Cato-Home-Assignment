---
title: "Working with Custom Data Types for DLP"
slug: "working-with-custom-data-types-for-dlp"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/working-with-custom-data-types-for-dlp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Custom Data Types for DLP

This article explains how to create custom data types to identify sensitive data in your organization for the DLP policy.

## Overview of Cato Custom DLP Data Types

Cato provides hundreds of pre-defined out-of-the box data types and categories for typical scenarios of DLP policies. However, sometimes organizations require the ability to create custom defined data types to match specific data inspection which is not covered by the pre-defined type.

You can define the following custom data types to customize content inspection for your DLP policies:

- Use Microsoft Sensitivity Labels from the Microsoft Information Protection (MIP) framework in your Cato DLP policy
- User defined data types including:
  - Use keywords to define items that contain one word or phrase that the DLP engine searches for
  - Dictionaries are containers that contain up to 50 words or phrases, and the DLP engine searches to match any single item in the dictionary
  - Regex data types let you enter regular expressions that define the content that DLP engine searches for
- Custom machine learning classifiers
- Exact Data Matching (EDM) profiles let you define specific data for content matching instead of general data patterns. For more about EDM profiles, see [Working with Exact Data Matching (EDM) for DLP](/v1/docs/working-with-exact-data-matching-edm-for-dlp).

After creating the **User Defined Data Type** or **Sensitivity Label**, you can add them to existing [DLP Content Profiles](/v1/docs/creating-dlp-content-profiles) or create new ones.

## Manually Creating Sensitivity Labels in Cato DLP

You can define sensitive data with MIP labels, and then use the MIP labels as the data types in your Cato DLP policy.

### Read More

After you create the **Sensitivity Labels** in the Cato Management Application, you can add them to **Content Profiles**. You can then create DLP rules to manage access to content for different users and groups according to MIP labels.

For example, if you have files with the MIP label Classified, create the label in your Cato DLP policy and add it to the **Content Profile** Restricted Documents. Then define a DLP rule that blocks access for groups of users without sufficient security clearance.

The DLP engine scans for the defined labels in the file metadata and not in the actual content, which helps reduce false positive results. The engine enforces the **Sensitivity Label** according to the **Label ID** you configure, not according to the **Name**. Make sure that the **Label ID** of the **Sensitivity Label** exactly matches the MIP label ID. For more information about finding the MIP label IDs for your organization's account, see the [Microsoft documentation](https://learn.microsoft.com/en-us/powershell/module/exchange/get-label?view=exchange-ps).

![DLP_Sensitivity_Labels.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643778943901.png)

> [!NOTE]
> Note:
> 
> Files must be MIP labeled to be managed by this data type. To check if a file is labeled correctly, use the [DLP validator tool.](/v1/docs/dlp-troubleshooting)

**To create a Sensitivity Label:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and select the **Data Types** tab.
2. In **Sensitivity Labels**, click **New**. The **Add Sensitivity Label** panel opens.
3. Enter the **Name** and **Description** for the label.
4. Enter the same **Label ID** as the MIP label ID.
5. Click **Apply**.

## Creating User Defined Data Types

User defined data types can be either a Keyword, Dictionary, regex expression.

### Read More

#### Creating New Keyword and Dictionary Data Types

Create a custom keyword or dictionary for the custom sensitive content that the DLP engine is searching for. For dictionaries, you can maintain the entries in a CSV file, and then paste them as the values for that dictionary.

- The DLP engine searches for an exact match of each keyword or dictionary entry
- A keyword must contain at least 8 characters (either single byte or multibyte)
- No upper limit for the number of words or characters in a keyword
- Keywords and dictionaries are NOT case sensitive
- Entries in a dictionary have an OR relationship between them
- Phrases must be an exact match on each word, for example the phrase **health care** doesn't match **healthcare**

So for a dictionary, you would create the following three values to match the words above: health, care, healthcare
- Words and phrases are identified according to standard word boundaries, for example a space after a word. There must be boundaries before and after the word for it to be detected. For a complete list of supported word boundaries, see below [Word Boundaries for Keyword and Dictionary Data Types](/docs/working-with-custom-data-types-for-dlp#UUID-9c3a6b58-bd74-e71c-382c-df0f4619b093_section-idm4626877837753633248817579897)
  - To detect multibyte words, we recommend using a [Regex data type](/docs/working-with-custom-data-types-for-dlp#UUID-9c3a6b58-bd74-e71c-382c-df0f4619b093_section-idm4644560872051233237191932786), because typically there's no boundary before and after

**Working with Thresholds**

You can define the **Threshold** for each User Defined data type, the number of times that the keyword or dictionary matches in a file. When it matches or exceeds the **Threshold**, then the file matches the Data Control rule (in the Security > Application Control page).

- Keywords - The **Threshold** for keywords looks for repeat occurrences that are an exact match of that word or phrase.
  - For example, for the keyword **apple** with a **Threshold** of 3. If a file contains 3 instances of the word **apple**, then that file is blocked.
- Dictionary - The **Threshold** for dictionaries looks for repeat occurrences of ANY value in that dictionary.
  - For example, if the dictionary contains the entries **apple** and **orange** with a with a **Threshold** of 3. If a file contains 2 instances of the word **apple** and 1 instance of the word **orange**, the file is blocked.

Also, if a file contains 3 instances of the word **apple** and 0 instance of the word **orange**, the file is blocked.

**To create a User Defined data type:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and select the **Data Types** tab.
2. In **User Defined**, click **New** and then select **New Keyword** or **New Dictionary**.
3. To create a New Keyword:
  1. Enter the **Name** and **Description** for the keyword.
  2. Select the **Threshold**, the minimum number of times that the keyword appears in the file.
  3. Enter the **Keyword/Phrase**.
  4. Click **Apply**.
4. To create a New Dictionary:
  1. Enter the **Name** and **Description** for the dictionary.
  2. Select the **Threshold**, the minimum number of times that one of the dictionary entries appears in the file.
  3. Add (or paste) one or more values for the dictionary. Multiple values must be separated by commas.
  4. Click **Apply**.

![New_DLP_Dictionary.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643826214173.png)

#### Word Boundaries for Keyword and Dictionary Data Types

To match a keyword or phrase, the DLP engine uses standard word boundaries to identify the end of each word. These are the characters that the engine recognizes as word boundaries:

- `([\s,.:;“‘]|^)`

#### Creating New Regex Data Types

Use regular expressions to define the type of content that matches the Data Type. For example, regex formulas let you easily match a customized corporate ID with a specific number of digits. Each Regex Data Type supports a single regular expression, so if you need to use multiple regular expressions, create a separate data type for each expression.

Use word boundaries in the expression to correctly define the content that matches the Data Type.

The regex engine is based on UTF-8 and supports characters for non-English content.

**Regex Thresholds**

You can define the **Threshold** for the expression, the number of times that the content appears in a file. When it matches or exceeds the **Threshold**, then the file matches the Data Control rule.

For example, if you created an expression for an ID with a **Threshold** of **5**, then only files which contain the ID five or more times would be blocked.

**Validating Regular Expressions**

You can use the **Validate Expression** field to test the expression and make sure that it matches the content correctly. When you click **Test**, the DLP service checks if the content matches the regular expression. This is the same service that runs in the Cato Cloud, so the test results are the same behavior you will see in your account.

Validating the expression also includes the **Threshold** for the Data Type. So when the **Threshold** is greater than **1**, the value must appear at least that many times for the test to succeed.

![Regex_User_Data_Type.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643778987933.png)

**To create a User Defined Regex Data Type:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and select the **Data Types** tab.
2. Click **New** and then select **New Regex**.
3. Enter the **Name** and **Description** for the keyword.
4. Select the **Threshold**, the minimum number of times that the text that matches the **Expression** appears in the file.
5. In **Expression**, enter the regular expression for this Data Type.
6. **(Optional)** Expand **Validate Expression**, enter the text and click **Test**.
7. Click **Apply**.

#### Supported Operators and Quantifiers

These are the regular expression operators and quantifiers that are supported for the User Defined Regex Data Types:

| Operators | Matched Pattern |
| --- | --- |
| \ | Quote the next meta-character |
| ^ | Match the beginning of a line |
| $ | Match the end of a line |
| . | Matches any single character |
| \| | Alternation |
| () | Capture groups are not supported. Parentheses can be used for bounding sub-expressions. |
| [xy] | Matches a single character from those given between the brackets |
| [x-z] | The range of characters between **x** and **z** |
| [^z] | Any character except **z** |

| Quantifiers | Matched Pattern |
| --- | --- |
| * | Match 0 or more times (see note below) |
| + | Match 1 or more times (see note below) |
| ? | Match 0 or 1 time |
| {n} | Match exactly **n** times |
| {n,} | Match at least **n** times |
| {n,m} | Match at least **n** times, but not more than **m** |

> [!NOTE]
> Note:
> 
> The use of unrestricted greedy quantifiers of arbitrary characters such as, **.*** or **.+** are not allowed. If you are attempting to include the characters in a class or set, reverse them. For example, ***.**
> 
> Instead of using these greedy quantifiers, you can use .{1,50} that supports up to 50 characters for each keyword or pattern for the regex data type

## Creating User Defined ML Classifiers

To increase the protection of specialized documents relevant to your industry or company, you can create your own user defined Machine Learning (ML) Classifier.

### Read More

User defined ML Classifiers significantly reduce false positives and improve the overall efficacy and precision of the DLP engine. Using an advanced data science similarity model, the ML Classifiers offer better adaptability and accuracy in detecting sensitive data, as they can dynamically learn and evolve with changing data patterns.

#### Training User Defined ML Classifiers

By uploading text files as samples of the documents you want to protect, you can train a machine learning model that can identify similar documents in real-time, preventing unauthorized data exfiltration. The machine learning model is based on the text within a file, images or videos are ignored.

#### File Requirements for ML Classifiers

- Only content in English is used to train the ML model
- Supported file types: DOC, XLS, CSV, TXT, and PDF
- A maximum of 10 files can be uploaded
- The file contains a minimum of 100 words

#### Uploading Files to Create a User Defined ML Classifier

Upload the sample files to the CMA to train the ML model for your user defined Data Type. We recommend uploading at least 5 files to accurately train the machine learning model to protect your documents.

**To upload documents for the ML Classifier:**

1. From the navigation menu, select **Security > Data Types & Profiles**.
2. On the **Data Types** tab, click **User Defined ML Classifiers**.
3. Click **New**.
4. Enter a **Name** and **Description** for the classifier and click **Save and Continue**.
5. Add the files you want to train the model with.
6. **(Optional)** Validate the model by uploading an example file and click **Validate**.
7. Click **Save**.

## Validating Data Types and Best Practices

For each DLP Data Type, you can validate that the DLP engine recognizes and matches the sensitive data in a test file. The validation feature is embedded into the predefined, user-defined, and sensitivity label profiles located in the Data Types & Profiles page. With either a new or existing keyword, dictionary, or REGEX string, you can upload a document that will test your settings prior to deploying the new data type. You can also validate [predefined data types](/v1/docs/creating-dlp-content-profiles) and [Sensitivity Labels](/v1/docs/using-mip-sensitivity-labels-in-your-cato-dlp-policy).

One of the key uses of the DLP validation tool is to verify your DLP settings to ensure that keywords and strings of information (via regex) are being properly detected using the entered data for that particular data set. Another key use case is that you can upload sample documents to the rule to see if the file type and formatting are going to be scanned correctly to detect the prescribed data for the data types.

For troubleshooting and supportability for cases where the file doesn’t match the data type, you can download a parsed text file of the content as extracted by the DLP engine.

The following is an example procedure for validating a Dictionary data type:

**To validate a Dictionary data type with a test file:**

1. From the navigation menu, select **Security > Data Types & Profiles**, and select the **Data Types** tab.
2. Hover the mouse in the row of a Dictionary data type and click the edit icon. The **Edit** panel opens.
3. Click **Validate Dictionary**. The **Validate Dictionary** panel opens.

![DLP_Validate_Dictionary.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643877854109.png)
4. Upload a test file, and click **Scan File**. The scan results are shown.
5. To download a text file of the content extracted by the DLP engine, click **Export Extracted Text**.

### Best Practices for User Defined Data Types

- When you implement the policy, or add a new application with the Block action:
  - Use the Monitor action for the rule.
  - Review the events that the rule generates and make sure that there are no events for traffic that you want to allow (false positive traffic).
  - If there is false positive traffic, you can make these changes:
    - Refine the scope of the rule to exclude the false positive traffic
    - Create a new allow rule before the block rule, and the scope of the new rule is only for the false positive traffic
    - Refine the regular expression and make sure that you validate it with an accurate example of the content you are scanning for
- Remember that the Application Control policy is an ordered policy, and the final implicit rule is ANY ANY Accept. Add rules to the policy to block the relevant application traffic, activities and criteria.

#### Known Limitations

- For information on the file requirements, see [What is the Cato DLP Service?](/v1/docs/what-is-the-cato-dlp-service)
  - For some downloads compressed in gzip format, the file size for DLP is calculated based on the compressed file. If the compressed file size is less than 1kb it will not be scanned.
- There is a maximum limit of 256 characters for a regular expression.
- Base64 encoded files are not supported, and the DLP engine can't inspect the content in these files.
