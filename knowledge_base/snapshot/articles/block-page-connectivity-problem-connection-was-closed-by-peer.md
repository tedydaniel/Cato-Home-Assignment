---
title: "Block Page - Connectivity Problem, Connection was Closed by Peer"
slug: "block-page-connectivity-problem-connection-was-closed-by-peer"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/block-page-connectivity-problem-connection-was-closed-by-peer"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Block Page - Connectivity Problem, Connection was Closed by Peer

## Issue

Users randomly get a block page with the reason being "Connectivity problem, connection was closed by peer"

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/9461411046813.png)

## The Problem

- When TCP proxy is triggered in Cato (see [Accelerating and Optimizing Traffic](/v1/docs/accelerating-and-optimizing-traffic)) it's possible that during a TCP connection, we receive an HTTP request from the client, and at the same time the server side is closing the connection (i.e. received a RST packet). In this case, Cato has no chance to send the request to the server.
- In the above scenario, Cato will reply to the client with the mentioned Block Page stating that it was the server side that closed the connection.

## The Solution

- The issue is likely related to a connection problem with the server.
- Further data can be collected via [Support Self Service](/v1/docs/support-self-service-supportme-portal) which will generate troubleshooting files including packet captures from both the client and server. For better support, please open a [Support ticket](/v1/docs/submitting-a-support-ticket).
