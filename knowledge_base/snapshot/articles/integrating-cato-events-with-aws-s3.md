---
title: "Integrating Cato Events with AWS S3"
slug: "integrating-cato-events-with-aws-s3"
updated: 2026-08-13T06:51:05Z
published: 2026-08-13T06:51:05Z
canonical: "knowledge.catonetworks.com/integrating-cato-events-with-aws-s3"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Cato Events with AWS S3

## Overview of the Amazon S3 Events Integration

Organizations that store and manage event data in an AWS S3 bucket can configure their Cato account to automatically and continuously upload events to it.

This integration continuously pushes events directly from the Cato Cloud to the S3 bucket, unlike the [eventsFeed](https://api.catonetworks.com/documentation/#query-eventsFeed) API, which requires pulling data from Cato and can be affected by rate limiting.

The Cato Cloud uploads data to the S3 bucket every 60 seconds, or whenever more than 9.5 MB of uncompressed data is accumulated. Data is transferred securely over HTTPS.

Events are uploaded in a compressed .GZ format. Some clients, such as certain browsers, may automatically decompress these files without removing the .GZ extension. If this occurs, changing the file extension to LOG or TXT will correctly align the file's format with its extension.

### Events Integration Use Case

Sample Company uses the [IPS Suspicious Activity Monitoring feature](/v1/docs/monitoring-suspicious-activity-with-ips-sam), which generates a high volume of security events. They decide to create an AWS S3 bucket to store all the event data, which they can then integrate with their SIEM solution. Sample Company enables Events Integration and adds the S3 bucket as an integration to their Cato account so that all IPS events are automatically uploaded to the S3 bucket.

### Prerequisites

- Review the prerequisites for all Cato event integrations in [Getting Started with Event Integrations](/v1/docs/getting-started-with-event-integrations)

## Configuring the AWS S3 Bucket

Create an S3 bucket and define an IAM policy that allows Cato to upload event data to it. Then, create an IAM role with Cato’s role ARN and attach the policy to the role.

The Cato Cloud uploads data to the S3 bucket every 60 seconds, or when more than 9.5 MB of uncompressed data is accumulated. Depending on different factors, data can sometimes be uploaded before it reaches 9.5 MB.

Cato uses HTTPS to upload data to the S3 bucket.

**Notes:**

- Only regions for S3 buckets where Security Token Service (STS) is active are supported. For more information about enabling STS for a region, see the relevant [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html).
- The China S3 region is not supported.

**To configure an S3 bucket in AWS to receive Cato event data:**

1. Create a new S3 bucket with the appropriate **AWS Region**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_aws_events.png)
2. Create a new IAM policy for the S3 bucket that allows uploading data to the bucket.
3. In the policy, click the **JSON** tab, and copy the Cato JSON below.

Edit the JSON and add the name for the S3 bucket, and then paste it in the tab.

```json
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
                "arn:aws:s3:::<bucket name>"
            ]
        },
        {
            "Sid": "",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket name>/*"
            ]
        }
    ]
}
```

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_aws_events.png)
4. Review the settings for the policy and click **Create policy**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_aws_events.png)
5. Create a new IAM role with Cato's ARN to allow Cato to upload events for your account to the S3 bucket.

The AWS S3 bucket is ready to integrate with your Cato account.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/06_aws_events.png)
  1. In the **Select trusted entity** page, add Cato's ARN to the role: `arn:aws:iam::428465470022:role/cato-events-integration`

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::428465470022:role/cato-events-integration"
            },
            "Condition": {"StringEquals": {"sts:ExternalId": "<CMA Account ID>"}},
            "Action": "sts:AssumeRole"
        }
    ]
}
```

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/04_aws_events.png)

Click **Next**.
  2. In the **Add permissions** page, attach the policy that you created earlier to the role.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/05_aws_events.png)

Click **Next**.
  3. Enter the **Role name** and click **Create role**.

## Adding an Event Integration for Amazon S3

Create a new integration for the AWS S3 bucket in the **Integrations** page, and add the Role ARN to the integration. This ARN permits Cato to upload the event data to the S3 bucket.

After you define and enable the AWS S3 integration, it takes a few minutes for Cato to start uploading events to the S3 bucket.

You can filter the events that are uploaded to the S3 bucket by event type or subtype. For example, you can upload only IPS events for your account. By default, no filter is applied, and all events are uploaded to the S3 bucket.

**To add an AWS S3 bucket integration to upload events for your account:**

1. From the navigation menu, select **Resources > Integrations > Configured Integrations**.
2. Click **New**. The **New Integration** panel opens.
3. Select the integration type: **Amazon S3.**
4. Configure the settings for the S3 bucket integration:
  1. Enter the **Name** for the integration.
  2. Enter these **Connection Details** for the integration based on the settings in AWS:
    - **Bucket Name** - Exact name of the S3 bucket
    - **Folder** - Folder path within the S3 bucket, if necessary
    - **Region** - Region where the S3 bucket is hosted

**Note:** Only regions for S3 buckets where the Security Token Service (STS) is active are supported.
    - **Role ARN** - Copy and paste the ARN for the role for the S3 bucket

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/07_aws_events.png)
  3. **(Optional)** Define the filter settings for events that are uploaded to the S3 bucket.

When you define multiple filters, there is an AND relationship, and the events that match all filters are uploaded.
5. Click **Apply**. The AWS S3 bucket is now integrated with your account.

**Note:** You can define up to three Event Integrations for your account.
