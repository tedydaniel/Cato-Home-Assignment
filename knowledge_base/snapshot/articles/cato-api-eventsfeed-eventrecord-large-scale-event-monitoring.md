---
title: "Cato API - EventsFeed > EventRecord (Large Scale Event Monitoring)"
slug: "cato-api-eventsfeed-eventrecord-large-scale-event-monitoring"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-eventsfeed-eventrecord-large-scale-event-monitoring"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - EventsFeed > EventRecord (Large Scale Event Monitoring)

## Overview of eventsFeed > EventRecord

The EventRecord fields contain the event data that is returned for the API query.

The explanations for the EventsFields is in [Cato API - EventsFeed (Large Scale Event Monitoring)](/v1/docs/cato-api-eventsfeed-large-scale-event-monitoring).

## Details for the eventsFeedAccountRecord Fields

These are the details that the eventsFeed fields can show for the query:

- ID - ID for the account
- eventRecord - data for the events that the query returned (array with nested queries and fields)

Use the eventRecord > EventFieldName arguments to filter the results of the query.

## eventsFeedAccountRecord ID

The ID field shows the ID for each account.

## eventsFeedAccountRecord > eventRecord

The eventRecord fields show the data for the events.

- eventRecord > time - timestamp for the event
- eventRecord > EventField - each event field that contains specific data for the event, for example source and destination IP address (array with nested fields)
- eventRecord > fieldsMap - event fields and data are key - value pairs in the map format {"key1":"value1", "key2:"value2"}
- eventRecord > flatFields - shows the event field and data as an array of name - value tuples {"name1":"value1", "name2:"value2"}

## eventRecord Time

The Time field shows the timestamp for when the event was generated.

## eventRecord Fields

Fields shows the EventFieldName and EventFieldValue for the specific event data.

### EventFieldName

EventFieldName shows the name for the event field such as source and destination port, IP address, and so on. For more about the values for EventFieldName see [Cato API - EventsFeed (Large Scale Event Monitoring)](/v1/docs/cato-api-eventsfeed-large-scale-event-monitoring).

### EventFieldValue

Shows the data for the eventField. The EventField > Value is a union of these types: string, date, and entity.

- string - event data returned as a string, for example: `"name": "os_type", "value": {"string": "OS_LINUX",}` shows that the operating system for this event was the Linux OS
- date - shows the time stamp when the event was generated
- entity - indicates objects that are used in the Cato Management Application, for example: `"name": "src_isp_ip", "value": {"id": "192.168.1.26","type": "ip","__typename": "Entity"}` shows that the source ISP IP address for this event was 192.168.1.26, and this value is an IP entity in the Cato Management Application

## eventRecord fieldsMap

The fieldsMap fields shows the fields and values for the event as key value pairs object.

## eventRecord flatFields

The flatFields fields shows a simplified output of the fields and values for the event, the data is shown as an array of name value tuples. For example, `[["dest_country":"Australia"], ["src_isp_ip":"192.168.1.26"]]`

## eventRecord > fieldNames Argument

The fieldNames arguments let you filter the API call according to the field names for the different types of events in Event Discovery.

The explanations for the EventFields is in [Cato API - EventsFeed (Large Scale Event Monitoring)](/v1/docs/cato-api-eventsfeed-large-scale-event-monitoring).
