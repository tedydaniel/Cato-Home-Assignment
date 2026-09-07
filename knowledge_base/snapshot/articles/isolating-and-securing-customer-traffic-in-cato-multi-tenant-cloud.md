---
title: "Isolating and Securing Customer Traffic in Cato Multi-Tenant Cloud"
slug: "isolating-and-securing-customer-traffic-in-cato-multi-tenant-cloud"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/isolating-and-securing-customer-traffic-in-cato-multi-tenant-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Isolating and Securing Customer Traffic in Cato Multi-Tenant Cloud

This article provides an explanation of how to isolate and secure customer traffic in the Cato Multi-Tenant Cloud

## Introduction to Cato Multi-tenant Cloud

Cato offers a true multi-tenant platform that eliminates the need for hardware appliances by delivering functions as a cloud-native, multi-tenant platform. Neither the enterprise nor the provider incurs the operational overhead of managing appliances.

## Isolation and Security in the Cato Multi-Tenant Cloud

### End-to-End Traffic Encryption

Cato employs end to end encryption. All customer traffic is encrypted at every hop in both directions.

### End-to-End Traffic Isolation

Cato has developed a unique routing algorithm that incorporates global routing optimization and flow isolation based on customer accounts through a tagging technique. This technique involves layering a packet tagging mechanism onto the existing global routing system. Cato's approach to isolating traffic using packet tagging is a well-established and widely accepted industry practice. Cato assigns a unique identifier to tag packets belonging to individual customers, which enables the identification of traffic at a granular level. This identifier is exclusive to each customer and serves to distinguish their traffic from other customers. At every stage of the traffic flow, Cato verifies the unique identifier assigned to each customer's account, ensuring that their traffic remains isolated and secure from that of other customers.
