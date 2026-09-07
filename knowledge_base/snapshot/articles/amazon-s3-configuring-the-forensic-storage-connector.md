---
title: "Amazon S3: Configuring the Forensic Storage Connector"
slug: "amazon-s3-configuring-the-forensic-storage-connector"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/amazon-s3-configuring-the-forensic-storage-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon S3: Configuring the Forensic Storage Connector

This article explains how to configure the connector for Amazon S3, so that data generated from Cato can be securely stored.

## Overview

To minimize data exposure and ensure compliance with regulatory requirements, you can create an integration with a third party for the storage of the evidence files.

This is supported for storing data from DLP policy violations. For more information, see [Investigating DLP Violations with Forensic Evidence](/v1/docs/investigating-dlp-violations-with-forensic-evidence).

To configure the integration, you need to:

1. Configure the integration storage application
2. Create the API connector in the CMA

## Configuring the Amazon S3 Integration

To configure the Amazon S3 integration, create the required configurations in the Amazon S3 Console, then configure the connector within the CMA.

### Step 1: Configure the Integration in the Amazon S3 Console

Create a new S3 bucket and define the policy that allows it to receive data. Then, define the IAM role for the S3 bucket with Cato's role ARN to set the bucket permissions to allow Cato to upload data to the bucket.

> [!NOTE]
> Note:
> 
> - Only regions for S3 buckets where Security Token Service (STS) is active are supported. For more information about enabling STS for a region, see the relevant [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html).
> - The China S3 region is not supported.
> - If access to the third-party service is limited to specific IP addresses, please refer to this [article](https://support.catonetworks.com/hc/en-us/articles/20511945810589) for the list of Cato IP addresses that you need to allow (you must be signed in to view this article).

**To configure the Amazon S3 Integration:**

1. Login to the Amazon S3 Console ([https://console.aws.amazon.com/s3/](http://%20https://console.aws.amazon.com/s3/))

![Bucket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33222713467805.png)
2. Create a new S3 bucket with the appropriate **AWS Region**.

For more information, see the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).
3. Create a new IAM policy for the S3 bucket that allows uploading data to the bucket.
4. In the policy, click the **JSON** tab, and copy the Cato JSON below.

Edit the JSON and add the name for the S3 bucket, and then paste it in the tab.

```plaintext
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::BUCKET-NAME"
            ]
        },
        {
            "Sid": "",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::BUCKET-NAME/*"
            ]
        }
    ]
}
```

![JSON.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33222710617117.png)
5. Review the settings for the policy and click **Create policy**.

![Create_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33222710751901.png)
6. Create a new IAM role with Cato's ARN to allow Cato to upload events for your account to the S3 bucket.
  1. In the **Select trusted entity** screen, add Cato's ARN to the role: `arn:aws:iam::428465470022:role/cato-forensics-integration`

```plaintext
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::428465470022:role/cato-forensics-integration"
            },
            "Condition": {"StringEquals": {"sts:ExternalId": "<CMA Account ID>"}},
            "Action": "sts:AssumeRole"
        }
    ]
}
```

![aws_forensic1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34986800584477.png)
  2. Click **Next**.
  3. In the **Add permissions** screen, attach the policy that you created in step 4 to the role and click **Next**.

![Permissions1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33222713908893.png)
  4. Enter the **Role name** and click **Create role**.

The AWS S3 bucket is ready to integrate with your Cato account. ![aws_done.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34986817050141.png)

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. In the **SaaS Application** drop-down, select Amazon S3.
5. Add these details:
  - Auth: AWS Assume Role
  - Name: The name for this integration
  - Description: (Optional) Add a description
  - Role ARN: The Role ARN for your Amazon account. You can find this in your AWS Management Console under IAM > Roles
  - Region: The region you configured in [Step 1](/v1/docs/amazon-s3-configuring-the-forensic-storage-connector#step-1-configure-the-integration-in-the-amazon-s3-console)
  - Bucket: The name of the Bucked you configured in [Step 1](/v1/docs/amazon-s3-configuring-the-forensic-storage-connector#step-1-configure-the-integration-in-the-amazon-s3-console)
  - Folder Path: Choose the path of the folder. If no folder exists, a new one is created
6. Click **Save**.
7. The app is visible on the **Integrated Apps** table with a **Connected** status.
