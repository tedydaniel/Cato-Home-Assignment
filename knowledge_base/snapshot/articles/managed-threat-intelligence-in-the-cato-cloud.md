---
title: "Managed Threat Intelligence in the Cato Cloud"
slug: "managed-threat-intelligence-in-the-cato-cloud"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/managed-threat-intelligence-in-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managed Threat Intelligence in the Cato Cloud

This article describes Cato's managed threat intelligence service that is included in the Threat Prevention license.

For more about purchasing a Threat Prevention license, please contact your Cato representative.

## What is Threat Intelligence?

Threat Intelligence is the process of collecting and analyzing information about potential or existing threats to an organization's assets, systems, or operations. You can use this information to help identify and assess risks, anticipate threats, and develop strategies to prevent or mitigate potential attacks.

## Advantages of Cato Managed Threat Intelligence

Cato offers a managed operational threat intelligence service that is a tailored cybersecurity solution delivering threat intelligence feeds for IOCs such as IP addresses, domains, and URLs. Our cybersecurity experts meticulously analyze and monitor these feeds to ensure their accuracy, and then deploy them in Cato Security services such as [IPS](/v1/docs/configuring-the-ips-policy) and [XDR](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench). For example, many of the Cato IPS threat signatures are designed to block traffic that matches the IOCs in threat intelligence feeds. Cato's extensive expertise and resources for managing threat intelligence provide the following advantages:

- **Expertise and Resources**

Cato features specialized security experts and an internal threat intelligence system equipped with advanced mechanisms that provide comprehensive threat intelligence solutions. This lets organizations leverage Cato's expertise and infrastructure without the need for in-house investment in building and maintaining such capabilities.
- **Responsiveness and Timeliness**

Cato provides real-time monitoring, mitigation, and analysis capabilities, delivering customers immediate notifications for active threats detected through its Threat Intelligence functionality. This ensures organizations stay updated on emerging threats and empowers them to proactively mitigate risks.
- **Ownership and Control**

Cato assumes responsibility and ownership of the customer's threat intelligence platform. This involves staying informed about cybersecurity trends, different attacker groups, and IOCs through diverse intelligence sources. Additionally, Cato performs continuous maintenance of the existing platform and conducts regular, comprehensive examinations of the data.
- **Cost and Scalability**

Cato's model lets organizations benefit from a broader spectrum of threat intelligence sources, with continuous improvement and enhancement of the Cato module. Cato constantly adds new features and they are included as part of the package without any additional cost.

## Cato's Threat Intelligence Deployment Cycle

As of 2024, Cato ingests approximately 250 different threat intelligence sources containing some 20 million IOCs. Since feeds coming from open source communities and commercial providers vary greatly in quality, they often contain false positives. Too many false positives result in unnecessary alerts that overwhelm security teams, preventing them from spotting legitimate threats. False positives also disrupt the business, preventing users from accessing legitimate resources. Cato's managed service improves business outcomes by continuously evaluating threat intelligence feeds and eliminating false positives. On average, Cato identifies 10% of the IOCs as false positives. This means that after the process of evaluation and elimination, approximately 18 million remaining IOCs are deployed to the security services in the Cato Cloud to provide protection for all customers. This deployment cycle for new threat intelligence content to the Cato Cloud takes approximately 3 hours end to end.

The following figure summarizes the deployment cycle for new threat intelligence content:

![Threat_Intelligence_Deployment_Cycle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303142801309.png)

## How Cato Assesses Threat Intelligence Feeds

This section describes the different methods Cato uses to assess and refine threat intelligence feeds.

### Ad Hoc Human Analysis

The Cato feed assessment process follows an internal protocol to gauge feed quality and facilitate integration seamlessly. Led by a security analyst, this entails a manual examination of each feed to ensure high quality and reduce the incidence of false positives. The process involves verifying the reliability of the feed source, configuring it within the internal threat intelligence system, and meticulously checking IOCs while employing tailored filters to amplify true positives and minimize false positives.

### Data Driven Refinement

Cato leverages the vast amounts of information collected from traffic across our network to improve its threat intelligence. Machine learning algorithms can be run against the data in the Cato data warehouse, which is built from the metadata for traffic flows across the Cato Cloud. These are some of the ways this data is used for better threat intelligence:

- **Popularity Models to Assess Threat Frequency and Significance** - These models help us gauge threat relevance based on how often they're encountered by customers. Popularity models assign scores to threats indicating their frequency. A higher score suggests a higher likelihood of a genuine threat. To build the popularity models, we collect data on internet traffic, and examine customer interactions with websites and IP addresses. The popularity score reflects the level of interest in a target across our network.
- **Evaluation of IPS Threat Signatures** - We constantly gauge the accuracy of IPS signatures based on data retrieved from customer environments where signatures were detected. This feedback loop refines our monitoring and improves IPS quality without customer input.

### AI Classification

A sophisticated AI model assesses each IOC and gives it a classification score. Cato stores IOCs in a database to collect related reputation data, and uses AI to continuously update the classification score. This score determines whether IPS blocks an IOC and if it is marked as malicious in [XDR stories](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench). These database entries are maintained long-term and the data is enhanced based on many external sources and our own threat intelligence feeds.

### Additional Resources

For more about Cato threat intelligence, see the following articles:

- [An Overview of Threat Intelligence](/v1/docs/an-overview-of-threat-intelligence)
- [Cato Automates Threat Intelligence Feed Assessment, Eliminating False Positives](https://www.catonetworks.com/news/cato-automates-threat-intelligence-feed-assessment-eliminating-false-positives/)
