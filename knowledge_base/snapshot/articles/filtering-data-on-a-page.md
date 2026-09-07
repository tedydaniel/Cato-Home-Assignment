---
title: "Filtering Data on a Page"
slug: "filtering-data-on-a-page"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/filtering-data-on-a-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filtering Data on a Page

The filter bar lets you filter data in several pages of the Cato Mangement Application (CMA).

## Using the Select Preset Filters

The **Select Presets** drop-down menu contains predefined filters for common analytics scenarios. When you select a preset option, the filters are automatically added to the filter bar, and the page is updated to show the items that match the filter.

## Creating Custom Presets

In addition to the predefined presets you can create a custom preset to filter the page and set the time frame that is displayed. When you save the custom preset, all the filters and the time frame are saved to the **Select Preset** drop-down menu for that user. The time frame can be dynamic, such as **Last Week**, or with exact **From** and **To** dates.

- The custom presets are saved for each admin’s account and are only available to that admin
- Custom presets are available for Cato Management Application users with editor permissions

![alerts_custom_preset.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896280398109.jpeg)

**To create a custom preset:**

1. Set the filters and time frame for your query.
2. Click the bookmark icon.

The **Custom Preset** panel opens.

![CustomPreset.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896287306525.png)
3. Enter the **Name** for the preset.
4. The **Details** section shows the filters, fields, and time frame that are included in the custom preset.
5. Click **Apply**.

The preset is added to the **Custom Presets** drop-down menu.

## Manually Configuring a Filter

You can manually configure the filter for greater granularity. After you configure the filter, it is added to the filter bar and the page is automatically updated to show the items that match the new filter. You can create filters with up to 2048 characters.

​When there are multiple ​**Fields**​​, there is an AND relationship between them. When there are multiple ​**Operators**​​ for a single Field, there is an OR relationship between the Operators. The same value for a field can only be included one time in each filter.

The following table explains the sections in the **Add Filter** pop-up window:

![Events_ManualFilter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896280450333.png)

| Name | Description |
| --- | --- |
| Field | Select the field for this filter. The available fields are based on the filtered items in the selected time range. |
| Operator | Select the operator that defines the filter. For multiple values within the same **Field**, use the IN operator (this applies an OR logic). The **Approximate Match** and **Contains** operators only apply to fields with textual values. The **Approximate Match** operator helps you locate an item even if you don't remember the exact name or spelling. For example, you might filter for “Microsoft Azure Cloud Security” instead of the correct name, “Microsoft Azure Cloud App Security,” or type “Micheal” instead of “Michael.” |
| Value | After you select the operators, you can choose the value for the filter. Values are not case sensitive. |

**To create a manual filter:**

1. In the filter bar, click the **Add** icon.

The **Add Filter** window opens.
2. From **Field**, select the field for this filter. You can enter the name of the field and the options in the drop-down menu are dynamically updated.
3. From **Operator**, select the operator for the filter.
4. If necessary, from **Value** select the value for the filter. The **in** and **not in** operators support selecting multiple values.
5. Click **OK**. The filter is added to the filter bar.

> [!NOTE]
> **Note:**
> 
> When you are creating a manual filter for a **Field**, the **Value** drop-down menu shows a maximum of 99 results. You can enter the entire name of a **Value**, and it is added to the filter.

## Defining the Default Page Filter (Default Preset)

Use the preset drop-down to set any of the preset filters to be the **Default** preset filter. The **Default** preset determines the filters applied when the page is first opened, and can also be selected from the preset drop-down menu.

![Events_Default_preset.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896256821405.png)

**To define the Default preset filter:**

1. Click ![Events_preset_button.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896268990365.png) to open the presets drop-down menu.
2. Hover the mouse over a preset and click ![star.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896270806685.png). The preset is defined as the **Default** preset.

## Filtering by Type

Use the quick filter buttons under the timeline to exclude a type of data, and then automatically update the filter bar.

This is currently supported for the Events and Audit trail pages.

![Events_QuickFilter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896256917789.png)

**To filter by type:**

1. From the timeline, click the type of data under the timeline. The type is excluded from the filter and from the results.
2. To clear the filter:
  - Click the **X** for the filter icon.
  - Click the name of the quick filter type.

(The filter icon in the above example is **event type is Connectivity**)
