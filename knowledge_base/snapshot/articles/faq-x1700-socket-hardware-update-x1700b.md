---
title: "FAQ - X1700 Socket Hardware Update (X1700B)"
slug: "faq-x1700-socket-hardware-update-x1700b"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/faq-x1700-socket-hardware-update-x1700b"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQ - X1700 Socket Hardware Update (X1700B)

Cato recently certified the updated **X1700B** Socket as a second hardware platform for X1700 Socket sites. This article addresses frequently asked questions relating to the update.

**Does Cato plan to announce End-of-Life or End-of-Support for the existing X1700 Socket model?**

No. Cato will continue to support all existing Socket models.

**Can the existing X1700 and the new X1700B Socket models be used in the same Socket HA cluster?**

Yes. There is full interoperability between the X1700 and X1700B Socket models. The first Socket assigned to the site is the Primary Socket, irrespective of the Socket model.

**Are there performance differences between the Socket models?**

Yes, the X1700B Socket model has stronger hardware. This is the supported throughput for each model:

- X1700 - up to 3 Gbps
- X1700B - up to 10 Gbps

**When will we start shipping the X1700B Socket to customers?**

Cato has already started shipping the X1700B Socket.

**Will Cato replace the existing X1700 Socket model with the X1700B?**

No. Cato will continue to support the existing X1700 model.

**Does the X1700B Socket require a different site type in the Cato Management Application?**

No. The site type **X1700** covers both models.

**Can the X1700B Socket model be mounted using the existing X1700 rack mount?**

No. The X1700B is shipped with its own rack mount kit.

**Do we need a different USB image to reset/reimage the x1700B Socket?**

Yes. Each Socket hardware model requires a separate image. For more about resetting sockets, see [Overview of Reimaging Cato Sockets](/v1/docs/overview-of-reimaging-cato-sockets).

**Is there a pricing difference between the two X1700 hardware models?**

No. The pricing is the same for both hardware models and the add-ons.

**Can we take add-on cards from the X1700 Socket, and install them on the X1700B Socket?**

No. add-on cards for each Socket model are not interchangeable. There are separate add-on cards for the X1700 and for the X1700B Socket.
