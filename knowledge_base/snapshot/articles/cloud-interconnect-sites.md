---
title: "Getting Started with Cloud Interconnect Sites"
slug: "getting-started-with-cloud-interconnect-sites"
updated: 2026-09-02T06:57:35Z
published: 2026-09-02T06:57:35Z
canonical: "knowledge.catonetworks.com/getting-started-with-cloud-interconnect-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with Cloud Interconnect Sites

This article helps you get started with Cloud Interconnect sites that natively connect with AWS, Microsoft Azure, GCP, and OCI cloud platforms.

## Overview of Cloud Interconnect with Cato

A Cloud Interconnect is a site type option that can be used for cloud environment integration with Cato among other options such as an IPsec or vSocket site type. Cloud Interconnect is a dedicated connection between two peers, such as a cloud provider and a customer's on-premises infrastructure. This private connection type allows for lower latency and higher bandwidth than public internet use.

In cloud computing environments, Cloud Interconnect allows one network to connect directly to another network using a data center cloud exchange via a service provider partner (such as Equinix’s Cloud Exchange Fabric or Megaport SDCI). This can provide customers with more flexibility in how they use and manage their cloud resources in a multi-cloud environment and improve performance for workloads that need to communicate between them. With Cato, Cloud Interconnect data traverses Layer2 virtual circuits, resulting in high performance and low latency due to no encryption overhead.

Use the Cato Management Application (CMA) as part of Cato's turnkey solution to orchestrate and integrate with the cloud service provider. When you create a new Cloud Interconnect, you are guided through the steps and settings to automate connecting the public cloud via a service provider to the Cato Cloud. The following diagram shows an example of connecting the AWS data center to the Cloud Interconnect site in your account via the Equinix Cloud Exchange Fabric.

| ![image1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247847157789.png) |
| --- |

### Why Use Cloud Interconnect?

There are several reasons why a Cloud Interconnect site may be the preferred option for your site deployment:

- Security – Cloud Interconnect is considered more secure as it does not transmit data over the public internet.
- Cost – Cloud Interconnect may be a less expensive solution for high-throughput sites. Many cloud providers provide fixed-price options which allow for cost predictability.
- Simplicity – Setting up Cloud Interconnect involves limited configuration steps.
- Performance & Reliability – Cloud Interconnect sites benefit from better performance due to lack of encryption/decryption overhead, guaranteed bandwidth, and close-to-zero latency due to its Layer 2 connectivity in a data center alongside the Cato PoP. (A private connection is more reliable than internet transport)

## Preparing for a Cloud Interconnect Site

Before deploying a Cloud Interconnect site, verify that the Cato PoP location, cloud provider, and fabric provider support the use case. For example, for an Azure Cloud Interconnect site located in Chicago, with a primary location in Chicago and a secondary location in New York. Make sure that both the Cato Chicago and New York PoPs and the Azure ExpressRoute locations support a dedicated connection between two peers. In addition, verify that Equinix, the fabric provider for the Chicago and New York PoP locations, is also supported in the relevant Azure peering location.

Cato has two categories of lead time for Cloud Interconnect sites: immediate or at a future date (between a few weeks and several months). PoP locations that are immediately available can be provisioned on demand from the CMA. If your use case is not supported by the automated provisioning in the CMA (e.g., Ali Cloud) but is supported by the fabric and the PoP location, Cato can create the connection using manual backend provisioning. PoP locations that are available at a future date require manual back-end configurations and need to be coordinated with your Cato representative.

For more information about the availability of supported PoP locations, see [Cloud Interconnect Availability](/v1/docs/cloud-interconnect-availability).

> [!NOTE]
> Notes:
> 
> Cato account licenses use one of two models.
> 
> - If your account is on an Enforcement Model license, the minimum bandwidth for a Cloud Interconnect site is 500 Mbps.
> - If your account is on a [**Bursting** **Model**](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) **license**, there is no minimum requirement.
> 
> To learn more about the differences between Bursting and Enforcement, and to identify which license model your account uses, see [here](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

For more information, contact your authorized Cato representative.

For more information about the available Cloud Interconnect location for each cloud provider, see the relevant documentation for that third-party service:

- [Microsoft Azure](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-locations)
- [Amazon Web Services](https://aws.amazon.com/directconnect/locations/)
- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/networking/fastconnect/providers/)
- [Google Cloud Platform](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers)

### Immediate Cloud Interconnect Sites

If Cato supports immediate availability for a Cloud Interconnect site, you need to confirm that the cloud provider also supports the relevant cloud region for the Primary and Secondary PoP locations. If a PoP location is not immediately available, you need to contact Cato to manually configure back-end settings in the Cato Cloud to support the site.

If the PoP locations are supported for immediate availability by Cato and supported by the cloud provider, you can start provisioning the site in the CMA. For more information, see the documentation for the relevant cloud provider below, [Related Cloud Interconnect Site Resources](/v1/docs/getting-started-with-cloud-interconnect-sites#related-cloud-interconnect-site-resources).

### Future Date Cloud Interconnect Sites

Cato PoP locations that are available at a future date require manual back-end configurations to connect the Cloud Interconnect site to the cloud provider. Contact your authorized Cato representative to add a new Cloud Interconnect site with the following criteria for each circuit:

- Cloud Provider environment (Azure, AWS, GCP, or OCI)
- Cloud Provider region (i.e., US-EAST-1)
- Required bandwidth
- Cato PoP location
- Circuit ID and Account ID

After you receive confirmation that the settings for the site are ready, you can start provisioning the site.

### Example of Preparing for a Cloud Interconnect Site for AWS Data Center

A company wants to connect AWS VPC resources located in the US East (Virginia) region to Cato using a Cloud Interconnect site. The closest Cato PoPs that are immediately available are located in New York and Ashburn. The customer reviews the supported [AWS Direct Connect locations](https://aws.amazon.com/directconnect/locations/) and sees that New York and Ashburn are supported for 10G throughput for both locations.

![PoP Locations](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247870022429.png)

The customer can start provisioning the Cloud Interconnect site for the Primary and Secondary PoP locations.

## Cloud Interconnect Site Architecture

Cloud Interconnect is a physical layer 2 connection to your cloud environment via one of Cato’s supported partner data center locations, such as Equinix. The Cloud Interconnect provider partner data center may be in the physical location where the Cato PoP is hosted alongside a Cloud provider connector. However, in some cases, all of the resources involved might be in different locations, where the Cloud provider and Cato PoP are not in the same physical location as the Cloud Interconnect provider. For example, the PoP and Data Center might be located in New York, and the Cloud Interconnect Provider is in Washington, D.C.

Cloud Interconnect can be deployed as a single link or as high availability (HA). In HA, Cato provides PoP-level resiliency for the redundant Cloud Interconnect links. The two links work in an Active/Passive manner with the Active link connected to one Cato PoP and the Passive link connected to a different Cato PoP.

Cloud Interconnect relies on BGP to mandate the primary location with preferred metrics and the secondary location with less preferred metrics by prepending the AS-PATH attribute behind the scenes. BGP is also used to manage connectivity to the Cato PoPs and exchange routing information between the Cato PoPs and the cloud environment to determine the active circuit for the site in case of a failover.

BGP MD5 authentication is a mandatory configuration for a Cloud Interconnect site.

BGP neighbors status is the indicator for site connectivity. As long as **at least one** BGP peer is reporting connectivity, the site is considered connected.

The following table describes the site connectivity status based on each BGP neighbor scenario:

| ![image2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247847362205.png) |
| --- |

This is a high-level description of connecting two cloud environments:

1. Prepare for the Cloud Interconnect site and verify the availability of the Cato and cloud provider locations:
  1. The Cato PoP location supports Cloud Interconnect as follows:
    - Immediately available - Configure the site in the CMA
    - Future date - Contact your Cato representative, lead time is from a few weeks to several months
  2. The cloud provider supports the same geographic location as the Cato PoP
2. Create the Cloud Interconnect circuits on the Cloud Provider and select the relevant Cloud Interconnect Provider partner location (such as Equinix or Megaport SDCI).
3. Configure IP and BGP settings for each Cloud Interconnect circuit in the Cloud Provider platform.
4. Create a Cloud Interconnect site in the CMA and configure the IP and BGP settings from the previous step. Cato now provisions the Cloud Interconnect site and will notify you upon completion.
5. Connect your cloud environment VPC via a linked Gateway to the Cloud Interconnect circuits in the cloud environment.
6. Verify the site connectivity.

| ![image3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247886625437.png) |
| --- |

## Related Cloud Interconnect Site Resources

These are the cloud providers that Cato supports to integrate with Cloud Interconnect sites and the relevant configuration articles:

- [Cloud Interconnect for AWS Public Cloud](/v1/docs/cloud-interconnect-for-aws-public-cloud)
- [Cloud Interconnect for Azure Public Cloud](/v1/docs/cloud-interconnect-for-azure-public-cloud)
- [Cloud Interconnect for GCP Public Cloud](/v1/docs/cloud-interconnect-for-gcp-public-cloud)
- [Cloud Interconnect for Oracle Public Cloud](/v1/docs/cloud-interconnect-for-oracle-public-cloud)
