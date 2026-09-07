---
title: "Understanding Cato API Rate Limiting"
slug: "understanding-cato-api-rate-limiting"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/understanding-cato-api-rate-limiting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Cato API Rate Limiting

Rate limits for the Cato API are applied on a per-query, per-account basis. This means that for each query there is an individual counter, but it applies to all the API keys (for different users) querying that account. So two different users calling two separate queries do not impact each other. However, if two different users are calling the same query, then these queries are subject to the same counter (for the purposes of rate limiting) and it is possible that the one user's query impacts the other user.

The Cato API back end is highly available and elastic, so the rate limits are a guaranteed minimum rather than an absolute maximum. For example, the auditFeed query has a rate limit of 5 per minute, this means that an account can call auditFeed at least five times every 60 seconds without being rate limited. In reality, it's possible for customers to call this query more frequently, but the guaranteed minimum rate of unlimited calls is 5 per minute. Nevertheless, there is also an account-wide counter, so if there are five different users all query auditFeed at the same time, to guarantee that they will not be impacted by rate limiting, then each user could only call the query once every 60 seconds.

Cato's Github account contains sample [Python scripts](https://github.com/catonetworks) that gracefully handle rate limiting by waiting for five seconds before retrying. Customers can adopt similar strategies in their own API scripts.

If your query encounters issues related to rate limiting, we recommend that you wait a few minutes and then resume sending additional API queries.

## General API Limiting Rate

API calls are limited to a rate limit of 120/minute, except for the following queries and mutations:

### Query Exceptions

The following query APIs are exceptions and do not have rate limits at 120/minute:

- accountMetrics: 15/minute
- accountSnapshot: 1/second (30/minute)
- appStatsTimeSeries: 80/minute
- auditFeed: 5/minute
- entityLookup: 30/minute (1500/5 hours)
- eventsFeed: 100/minute

### Mutation Exceptions

The following mutation APIs are exceptions and do not have rate limits at 120/minute:

- accountManagement.addAccount: 10/minute
- accountManagement.removeAccount: 5/minute
- policy.appTenantRestriction.publishPolicyRevision: 3/minute (20/hour)
- policy.dynamicIpAllocation.publishPolicyRevision: 3/minute (20/hour)
- policy.internetFirewall.publishPolicyRevision: 3/minute (20/hour)
- policy.pacFile.publishPolicyRevision: 3/minute (20/hour)
- policy.remotePortFwd.publishPolicyRevision: 3/minute (20/hour)
- policy.socketLanFirewall.publishPolicyRevision: 3/minute (20/hour)
- policy.socketLanNetwork.publishPolicyRevision: 3/minute (20/hour)
- policy.wanFirewall.publishPolicyRevision: 3/minute (20/hour)
- policy.wanNetwork.publishPolicyRevision: 3/minute (20/hour)
- policy.ztnaAlwaysOn.publishPolicyRevision: 3/minute (20/hour)
- sandbox.uploadFile: 5/5 minutes
