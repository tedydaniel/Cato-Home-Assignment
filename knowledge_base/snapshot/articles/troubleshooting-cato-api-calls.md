---
title: "Troubleshooting Cato API Calls"
slug: "troubleshooting-cato-api-calls"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/troubleshooting-cato-api-calls"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Cato API Calls

This article provides troubleshooting suggestions for common errors that can occur when you use the Cato to run an API query with API tools and software. For example, Altair and Postman.

Issues related to API scripts and coding aren't supported.

## Required API Arguments

These are the arguments that you must include in the API query. When you remove an optional argument from the API query, the default value is used.

- accountMetrics query
  - id - account ID
  - timeframe - time frame of data that the query returns
  - groupDevices - For multiple sites, and sites with multiple Sockets, combine the analytics into a single Socket (for boolean value **true**)
- accountSnapshot query
  - id - account ID

## Common GRAPHQL_PARSE_FAILED Errors

This section explains some common examples for error messages related to the Cato GraphQL schema.

### Message: Unexpected )

There is an extra parenthesis in the query. Often this error is caused when you don't provide a Boolean value for an argument. For example, `groupInterfaces: ,` instead of `groupInterfaces: true,`

### Message: Expected Name, found <character>

The JSON file isn't formatted correctly. The message shows a character that is related to the missing or extra character. For example, **Expected Name, found (** for the argument `accountSnapshot((id: 42)`. The correct format for this argument is `accountSnapshot(id: 1941)`

### Message: Expected Name, found <Invalid>

The error message indicates that there is an with an invalid value.

For example, the **timeFrame** argument (**accountMetrics**) in the Cato API uses quotation marks for the ISO 8601 date and time standard, `timeFrame: "last.P1D"` is correct and `timeFrame: last.P1D` produces this error.

## Common GRAPH_QL_VALIDATION_FAILED Errors

This section explains some common examples for error messages related to the incorrect format for arguments in the query.

### Message: Expected type String!, found <number>

The error message indicates that an argument has an invalid value, usually related to the argument format.

For example, the **sites ids** argument (**accountMetrics > sites**) is a STRING, so you must use quotation marks for the value, `ids: ["4242"]` is correct and `ids:[4242]` produces this error.

### Message: Expected type Int!, found \"<number>\"

The error message indicates that an argument has an invalid value, usually related to the argument format.

For example, the **sites ids** argument (**accountSnapshot > sites**) is an INT, so you must NOT use quotation marks for the value, `ids: [2626]` is correct and `ids:["2626"]` produces this error.

## API Error Messages

This section explains common error messages that aren't specifically related to Cato GraphQL schema or format.

### Message: authentication error or 403

There is a problem with the API key for your account. Suggested solutions:

- In the Cato Management Application (**System > API Access Management**), make sure that:
  - The API key you are using is still valid (exists and has not expired)
  - If the **Allow access from IPs** option is set, the API client is making the call from a specific allowed IP address or range
- Confirm that the key is configured correctly in the HTTP header settings for the API query software: `x-api-key: &lt;key value&gt;`, for example, `x-api-key: abcdef12345`
- If the problem continues, generate a new API key and add it to the API query software

This is an example of a valid HTTP header for the API Client:

```plaintext
POST /api/v1/graphql2 HTTP/2
Host: api.catonetworks.com
User-Agent: curl/8.7.1
Accept: */*
Content-Type:application/json
x-api-key: abcdef123456789
```

### Message: cannot separate devices (groupDevices = false) when multiple sites are selected

The value for the **groupDevices** argument (**accountMetrics**) must be **true** when the query includes multiple sites.

## Converting API Analytics Data

The Cato API returns traffic data in bytes. To convert the data to larger units (such as MB or GB), you need to divide by exponential values of 1024: 10242 for MB, and 10243 for GB.

For example, to convert 536,870,912,000 bytes to GB, divide by 10243 to show 500GB of data.
