---
title: "Configuring AI Security Outposts"
slug: "configuring-ai-security-outposts"
updated: 2026-07-12T08:08:15Z
published: 2026-07-12T08:08:15Z
canonical: "knowledge.catonetworks.com/configuring-ai-security-outposts"
excludeFromExternalSearch: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring AI Security Outposts

AI Security Outposts let you inspect AI interaction content in your own environment instead of sending that content to Cato. This deployment model is designed for organizations with strict data residency, privacy, or regulatory requirements.

An Outpost provides the AI Security inspection data plane in your environment, while Cato continues to provide centralized management and visibility. You deploy the Outpost in your own infrastructure and use it to keep AI interaction inspection local.

## What Are Outposts

An Outpost is a customer-hosted deployment of the AI Security inspection services and the AI Security engine. It runs in your environment and processes inspection requests locally, so prompt content stays within your organization.

Even when you use an Outpost, Cato still manages the service configuration and visibility. The Outpost receives its configuration from Cato and sends back only the metadata required for monitoring and management.

## When Should You Use an Outpost

Use an Outpost when your organization must keep prompt content inside its own environment. This is useful for organizations with internal security requirements or external compliance obligations that do not allow prompt data to be sent to a cloud-hosted inspection service. Outposts let you keep the inspection flow local while still using Cato to manage the service.

**Note:** We recommend using Outpost only when necessary because it adds deployment and maintenance complexity in your environment. For customers who want to keep AI interaction data in customer-managed storage, see the documentation for storage integrations, e.g., AWS S3 Storage integration, as a lighter-weight alternative. Outpost also requires a separate license

## Prerequisites

Before you deploy an Outpost, make sure that:

- You have access to a supported Kubernetes cluster GPU nodes are available if required for your deployment
- You can run kubectl and Helm commands against the cluster
- The cluster can pull Outpost images from Docker Hub
- The cluster has the required resources for the Outpost workload
- GPU nodes are available if required for your deployment

## Use Case

Your organization uses AI Security to protect internal AI applications that process sensitive business data, such as employee records, financial information, or proprietary source code. Because your regulatory and internal security requirements do not allow prompt content to leave your environment, you deploy an Outpost in your own infrastructure. You then configure your Guard to use the API Guard type and send prompts to the configured Outpost for inspection. This lets you enforce AI Security controls while keeping sensitive prompt data in-house.

## Deploying an Outpost

Deploy an Outpost from the Cato Management Application. The deployment wizard guides you through creating the Outpost, preparing your Kubernetes environment, and generating the commands and manifest you run in your cluster.

**To deploy an Outpost**

1. Navigate to **AI Security > Outposts** and click **New**.
2. Enter a name to initialize the Outpost.

Cato creates the Outpost and uses this name in the generated deployment configuration.
3. Configure the cluster context and namespace.

If the namespace does not already exist, create it with the command shown in the wizard.
4. Create the service secret.

Copy the generated command and run it in your Kubernetes cluster. This command creates the Kubernetes secret that the Outpost uses to authenticate with Cato.
5. Configure Docker image pull access.

Copy the generated command and run it in your Kubernetes cluster to create the image pull secret in the Outpost namespace.
6. Deploy the operator. Copy the generated Helm commands and run them in this order:

The generated operator command includes values for your deployment, such as the cluster context, namespace, control plane endpoint, image repository, monitoring endpoint, and image pull secret. Wait for the operator deployment to complete before you continue.
  1. Log in to the Helm registry
  2. Install the CRDs in the Kubernetes cluster
  3. Install the Outpost operator
7. Deploy the Outpost. Configure these settings in the wizard:
  - Outpost Namespace - The namespace where the Outpost resources are deployed
  - Release Channel - The software release track for the Outpost, such as Stable, Beta, or Canary

The wizard generates an example Outpost manifest. Copy the manifest and save it as a YAML file. The manifest defines the Outpost deployment settings, such as:

- Outpost name and namespace
- Installation ID
- Probe and monitoring settings
- Replica settings
- Node selector settings
- Resource requests and limits

Apply the manifest to the cluster with the generated kubectl apply command.

### GPU Node Configuration

Before you apply the manifest, review the nodeSelector settings in the manifest.

Make sure that the node selector matches the label used for your GPU nodes. If your environment uses a different label, update the manifest before you deploy it.

Also, verify that the GPU and memory requests match the resources available in your cluster.

### Verify the Deployment

After you apply the manifest:

- Wait for the Outpost resources to be created
- Confirm that the operator finishes the deployment
- Verify that the Outpost workload is running in the correct namespace
- Check that the Outpost can connect to Cato and receive its configuration

After the deployment is complete, the Outpost can begin processing inspection requests in your environment.
