---
title: "Configuring AWS IAM Role Authentication for Proxy Guards"
slug: "configuring-aws-iam-role-authentication-for-proxy-guards"
updated: 2026-07-21T13:46:54Z
published: 2026-07-21T13:46:54Z
canonical: "knowledge.catonetworks.com/configuring-aws-iam-role-authentication-for-proxy-guards"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring AWS IAM Role Authentication for Proxy Guards

Cato's AI Security Proxy Guard can authenticate to Amazon Bedrock with an AWS IAM role instead of a static API key. This lets you use short-lived AWS credentials and avoid storing long-term Bedrock API credentials in the Guard configuration.

## Prerequisites

- Access to the Amazon Bedrock models you want to use in the selected region
- Permission to create and edit IAM roles and policies in your AWS account

## Choose the Guard Hosting Type

The configuration depends on where the Proxy Guard is hosted:

- **Cloud-hosted Guards**: Cato uses cross-account role assumption. You create an IAM role in your AWS account that trusts Cato's AWS account, and Cato assumes that role to sign Bedrock requests on your behalf. Credentials are cached and refreshed automatically before they expire.
- **Outpost-hosted Guards**: The Guard uses the AWS credentials available to the Outpost pods, such as credentials provided through EKS Pod Identity or IAM Roles for Service Accounts (IRSA). No cross-account trust with Cato or External ID is required.

## Configuring IAM Authentication for Cloud-Hosted Guards

Use this procedure when your Proxy Guard runs on Cato's cloud infrastructure and you aren't using a Cato Outpost.

### Configure the Guard in the CMA

In the Guard's model connection settings, select **Amazon Bedrock** as the AI service, configure the **Amazon Bedrock Region**, and set **Choose Authentication Method** to **AWS IAM**.

### Create the IAM Role with CloudFormation

After you select **AWS IAM**, the CMA shows the **Create the Amazon Bedrock IAM role** panel.

Click **Install with CloudFormation** to open the AWS CloudFormation console in a new tab with a Cato-provided template and stack name. To review the template before creating the stack, click **See stack content**.

Create the stack in your AWS account. The stack creates a correctly named IAM role with the required trust policy and permissions. When the stack finishes, copy its `RoleArn` and `ExternalId` outputs into the **AWS Role ARN** and **External ID** fields in the CMA.

### Manually Create the IAM Role

Use manual setup to customize the policy, scope access to specific model ARNs, or create the role without CloudFormation.

#### Trust Policy

The trust policy allows Cato's AWS account to assume the role.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::428465470022:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "<YOUR_EXTERNAL_ID>"
        }
      }
    }
  ]
}
```

- `428465470022` is Cato's AWS account ID
- Replace `<YOUR_EXTERNAL_ID>` with a string you choose, such as your CMA account ID or a random string. Enter the same value in the **External ID** field in the Guard configuration to help prevent confused-deputy attacks
- The role name must contain the string `AiSecurityBedrockInvocationRole`, for example `my-app-AiSecurityBedrockInvocationRole`. The CMA validates this pattern and rejects a Role ARN that doesn't match it

#### Permissions Policy

The permissions policy grants the actions Cato needs to validate the connection and invoke models.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListFoundationModels"
      ],
      "Resource": "*"
    }
  ]
}
```

`bedrock:ListFoundationModels` is used by the **Validate** action in the Guard configuration page. It checks the role and region by listing available models and doesn't invoke a model. The `InvokeModel` actions are used for actual traffic.

You can scope `Resource` to specific model ARNs, for example `arn:aws:bedrock:<region>::foundation-model/*`, instead of `"*"` to restrict which models Cato can invoke.

### Validate the Configuration

1. Enter the **AWS Role ARN** from the CloudFormation stack output or from the role you created manually.
2. Enter the **External ID** from the CloudFormation stack output or the value you chose manually.
3. Click **Validate** to confirm Cato can assume the role and list Bedrock foundation models in the selected region.

## Configuring IAM Authentication for Outpost-Hosted Guards

Use this procedure when the Guard is hosted on a Cato Outpost running in your environment. The Guard uses the AWS credentials available to the Outpost pods, so there is no cross-account trust with Cato or External ID to configure.

### Create the IAM Role

Create an IAM role with the Bedrock permissions policy from the Cloud-hosted Guards procedure. You don't need a Cato trust policy or External ID. The role must be available to the Outpost's Kubernetes service account.

### Create the Kubernetes Service Account

Enable a dedicated Kubernetes service account for the Outpost's relevant pods:

```bash
kubectl --kube-context '<your-context>' -n <outpost-namespace> patch outpost <outpost-name> \
  --type merge \
  -p '{"spec":{"firewallServiceOverrides":{"serviceAccount":{"enabled":true,"annotations":{}}}}}'
```

This creates a service account named `<outpost-name>-firewall-service` in the Outpost namespace and binds the firewall pods to it.

### Allow the Service Account to Assume the IAM Role

Grant the `<outpost-name>-firewall-service` service account permission to assume the IAM role. Cato doesn't require a specific mechanism. Use the method your platform supports.

Common options include:

- **EKS Pod Identity**: Create a Pod Identity association for the Outpost namespace and service account. Configure the IAM role according to AWS EKS Pod Identity requirements, including trust for the `pods.eks.amazonaws.com` service principal.
- **IRSA (IAM Roles for Service Accounts)**: Trust your cluster's OIDC provider scoped to the service account, and set the role ARN as the `eks.amazonaws.com/role-arn` annotation on the service account. You can add this annotation directly in the service account patch instead of `{}`.

For IRSA, the role trust policy must reference `system:serviceaccount:<outpost-namespace>:<outpost-name>-firewall-service`. For EKS Pod Identity, create the association for the same Outpost namespace and service account.

In both cases, the IAM role must include the Bedrock permissions policy from the Cloud-hosted Guards procedure.

## Troubleshooting IAM Authentication for Bedrock

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `403` or `AccessDeniedException` on Bedrock calls | The AWS account doesn't have access to the selected model, or the role is missing `bedrock:InvokeModel` | Confirm the account can access the model in the selected region. Some models may require AWS Marketplace permissions, provider terms, or additional access steps. Confirm the role includes the Bedrock permissions policy from this article. |
| STS `AssumeRole` failures for cloud-hosted Guards | Trust policy or External ID mismatch | Confirm the trust policy Principal is Cato's account ID (`428465470022`) exactly, and the External ID in the trust policy matches the value entered in the Guard configuration. |
| "Validation failed. Please check the Role ARN, External ID and region." for cloud-hosted Guards | Mismatched trust policy, wrong External ID, wrong Role ARN, or wrong region | Double-check all values. If you used CloudFormation, confirm that you copied the stack outputs exactly. |
| "Validation failed. The outpost couldn't list Bedrock foundation models." for Outpost-hosted Guards | IAM role lacks permissions, the Outpost can't reach AWS, or the pod can't assume the role | Verify network connectivity from the Outpost to AWS first, then confirm the role includes `bedrock:ListFoundationModels`. For IRSA, also verify the OIDC provider and the `system:serviceaccount:<namespace>:<name>` string in the trust policy. For EKS Pod Identity, verify the Pod Identity association and role trust policy. |
| `Could not load credentials` for Outpost-hosted Guards | Service account isn't associated with the IAM role, or the role ARN is incorrect | Confirm the role is associated with `<outpost-name>-firewall-service` using EKS Pod Identity or IRSA, and verify that the role ARN is correct. |
