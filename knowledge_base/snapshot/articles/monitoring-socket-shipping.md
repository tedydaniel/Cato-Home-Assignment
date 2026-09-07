---
title: "Monitoring Socket Shipping"
slug: "monitoring-socket-shipping"
updated: 2026-06-28T12:11:18Z
published: 2026-06-28T12:11:18Z
canonical: "knowledge.catonetworks.com/monitoring-socket-shipping"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Socket Shipping

## Overview

Hardware ordered for your Cato account can be tracked and managed directly in the Cato Management Application (CMA). The **Shipping** tab shows order status and delivery details for all your hardware.

To ship an item, fill in the required details and request shipment — you'll see a full pricing breakdown before confirming.

### Shipping Detail Notifications

When customers sign an order form, they are asked to provide a shipping contact. Both the signee and the contact they provide receive an email instructing them to complete the shipping details in the CMA.

If the customer has not provided the shipping details, reminders are sent 30, 14, and 7 days before the license start date, and on the license start date itself. You can control which admins receive these notifications in the [Notification Settings page](/v1/docs/account-level-alerts-and-system-notifications).

## Viewing Hardware Shipping Information

The Socket & Accessories page also lets you easily contact Cato via email, and the message contains a direct link to your Cato account.

**To show the Socket and hardware shipping information:**

1. From the navigation menu, select **Account > Sockets & Accessories**, and select the **Shipping** tab.
2. Click **Contact Logistics** to send an email to Cato regarding hardware shipping.

## Shipping Tab Fields

You can sort, search, and filter the items in the Shipping tab to see the items that interest you.

You can view more information about each item by clicking the drop-down arrow next to that item.

These columns are available in the shipping table:

| Column | Description |
| --- | --- |
| Product | Name of the hardware item |
| Serial Number | Unique identifier of the item being shipped |
| Order Type | Indicates the reason the hardware was ordered: - **Purchase** - Hardware ordered as part of a new purchase or expansion - **Refresh** - Replacement hardware provided through Cato’s Socket hardware refresh program to replace an existing Socket approaching End of Support (EOS) |
| Status | Use this column to track the status of each item. - **Requires Info** - Indicates that the customer must provide further information for the hardware to be shipped. When you purchase a hardware item, it is assigned this status. For more information, see below [Providing Required Shipping Information](/v1/docs/clone-monitoring-socket-shipping#providing-required-shipping-information). - **Requires Confirmation** - Indicates the required shipping details were provided, and the customer should now click **Confirm For Shipping** for this item. - **In Transit** - Indicates that the item delivery data was provided and it is now in the process of being delivered to the requested location. - **Delivered** - Indicates the item has been delivered to the provided address. Cato automatically changes the status to **Delivered** when the item is detected as connected, or 90 days after it was shipped. The customer can manually change the status to **Delivered** in the **Actions** menu. |
| Start Date | License start date for the site the hardware is related to |
| Tracking Number | Identifier used by the carrier. Click to open the carrier's site and view their tracking information. |
| Address | The name of a location as it appears in the [Enterprise Directory](/v1/docs/managing-locations-in-the-enterprise-directory). |
| Quote ID | ID number for the price quote for the item |
| Power Cable | The required power cable according to the location. Possible values include: EU, US, JP, KR, UK, C14, CN (China), CH (Switzerland), IN, and AU. For more information about cable types, see [this article](https://www.worldstandards.eu/electricity/spread-plug-types-map/). For more about C14 couplers, see [this article](https://en.wikipedia.org/wiki/IEC_60320#C13/C14_coupler). |
| Contact Name, Contact Phone, Contact Email | Delivery contact person information |
| Company Name | Name of the company for shipping purposes |
| Incoterms / Shipping Method | Incoterms define the responsibilities of buyers and sellers for the delivery of goods. These are the available options: - **DDU-Economy** (Delivered Duty Unpaid) - Cato delivers goods in economy shipment to the delivery address but does not cover customs duties; you are responsible for paying any import duties. If the delivery is domestic, there will be no duties paid and DDP will cost the same as DDU. - **DDU-Express** (Delivered Duty Unpaid) - Cato delivers goods in express shipment to the delivery address but does not cover customs duties; you are responsible for paying any import duties. If the delivery is domestic, there will be no duties paid, and DDP will cost the same as DDU. - **DDP-Economy** (Delivered Duty Paid) - An economy shipment that Cato takes full responsibility for delivering the goods to the delivery address, including paying all duties and taxes for import. If the delivery is domestic, there will be no duties paid, and DDP will cost the same as DDU. - **DDP-Express** (Delivered Duty Paid) - An express shipment that Cato takes full responsibility for delivering the goods to the delivery address, including paying all duties and taxes for import. If the delivery is domestic, there will be no duties paid, and DDP will cost the same as DDU. - **EXW** (Ex Works) - Cato makes the goods available at their premises, and you are responsible for all transportation costs and risks from that point forward. **Note:** When shipping to the EU or US, select one of the DDU options. Since Cato ships from within these regions, domestic shipments are not subject to duties. |
| Description | Optional description |
| Site Name | Physical location to which the order is connected |
| Shipping Date | Date the item shipped according to the carrier |
| Shipping Carrier | Company that is shipping the hardware |

## Marking Items as Delivered

When you receive Sockets and connect them to the internet, they are automatically marked as delivered. If you received other hardware, did not connect the Socket to the internet, or for any other reason received an item that is still not marked as delivered, you should manually mark items as delivered.

**To mark items as delivered:**

1. Select the relevant item or items from the Shipping list.
2. Click the **Actions** button.
3. Select **Mark as Delivered**.

## Shipping Multiple Completed Items

To save time, you can indicate that you want to ship all items that have the status **Requires Confirmation** at once.

The confirmation window shows the shipping costs that you will be charged.

**To ship all items that require confirmation:**

1. Click the **Actions** button.
2. Select **Ship all Completed Items**.

**To ship a subset of the items displayed:**

1. Select the checkbox for each item you want to ship.
2. Select **Confirm For Shipping**.
3. Review the displayed details and shipping costs. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(18).png)

The costs are based on destination, product type, and shipping conditions.
4. Click **Confirm**.

## Providing Required Shipping Information

You can provide shipping information directly in the Shipping tab for one or more items. Select multiple items and click **Edit Selected** to update shared shipping details for several shipments at once.

### Bulk Editing Shipping Information

Use bulk edit to update shipping information for multiple items at the same time. This is useful when several shipments share the same contact information, address, company name, or other shipping details.

**To bulk edit shipping information directly in the CMA:**

1. From the navigation menu, select **Account > Sockets & Accessories**, and select the **Shipping** tab.
2. Select the items you want to update.
3. Click **Edit Selected**.
4. Enter or update the required shipping information.
5. Click **Save**.

Only fields that you update in the bulk edit form are changed for the selected items.

**To provide the required shipping information using a CSV file:**

For large deployments or when updating many different addresses, you can use CSV export and import to update shipping information in bulk.

To help minimize errors, you export the filtered data on the page to a prefilled CSV, fill in the required fields, and import the CSV back to the CMA.

Addresses are automatically verified to determine if we can locate the address. Unverified addresses are marked with a warning that you can ignore if you are confident that the address is correct.

Make sure there are no spaces before or after values you enter in the CSV or those values may fail when importing. If the CSV contains more than 300 unique address, an error is displayed but the file is uploaded. Refresh the page after importing the file to view the accurate status.

1. From the navigation menu, select **Account > Sockets & Accessories**, and select the **Shipping** tab.
2. Click the **Export** button. A CSV file with the data is downloaded. The export does not include items that have been filtered out.
3. Update the downloaded CSV file with the required details. Updates for items that were already shipped will be ignored, except for changes in the **Comments** column, which will still be updated even if the item was shipped.
4. Update the following fields:
  - Power Cable
  - Contact Name
  - Contact Phone
  - Contact Email
  - Company Name
  - Location Name
  - Incoterms
  - Delivery Instructions

**Note:** Required if the incoterm value is EXW
  - VAT ID: Your company's unique registration number for VAT

**Note:** Required for items shipping to Brazil
  - Comments
5. Click **Import** and select the CSV file. If an error occurs during the import, the CMA provides a detailed log to help you resolve the issue.

### Address Validation

The CMA uses Google Maps API to automatically validate shipping addresses that are from supported countries. Shipping addresses from unsupported countries are not validated and you should make sure the address is correct.

- Validated addresses will be accepted without issue.
- Unvalidated addresses will be marked as **Not Validated** - but you can still proceed with shipping after confirming that the address is correct.

Address validation is supported for the following countries:

Argentina, Austria, Australia, Belgium, Bulgaria, Brazil, Canada, Switzerland, Chile, Colombia, Czechia, Germany, Denmark, Estonia, Spain, Finland, France, United Kingdom, Croatia, Hungary, Ireland, India, Italy, Japan, Lithuania, Luxembourg, Latvia, Mexico, Malaysia, Netherlands, Norway, New Zealand, Poland, Puerto Rico, Portugal, Sweden, Singapore, Slovenia, Slovakia, United States.

### Supported Countries for Shipping

The following is a list of the countries you can ship Cato hardware items to:

Aland Islands, Albania, Algeria, American Samoa, Andorra, Angola, Anguilla, Antigua and Barbuda, Argentina, Armenia, Aruba, Australia, Austria, Azerbaijan, Bahamas, Bahrain, Bangladesh, Barbados, Belgium, Belize, Benin, Bermuda, Bhutan, Bolivia, Bonaire, Sint Eustatius and Saba, Bosnia Herzegovina, Botswana, Bouvet Island, Brazil, British Indian Ocean Territory, Brunei Darussalam, Bulgaria, Bulgaria, Burkina Faso, Burundi, Cambodia, Cameroon, Canada, Cape Verde, Cayman Islands, Chad, Chile, China, Christmas Island, Cocos (Keeling) Islands, Colombia, Comoros, Cook Islands, Costa Rica, Cote d'Ivoire, Croatia, Curacao, Cyprus, Czech Republic, Denmark, Djibouti, Dominica, Dominican Republic, East Timor, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Ethiopia, Falkland Islands (Malvinas), Faroe Islands, Fiji, Finland, France, French Guiana, French Polynesia, French Southern Territories, Gabon, Gambia, Georgia, Germany, Ghana, Gibraltar, Greece, Greenland, Grenada, Guadeloupe, Guam, Guatemala, Guernsey, Guinea, Guinea-Bissau, Guyana, Heard Island and McDonald Islands, Honduras, Hong Kong, Hungary, Iceland, India, Indonesia, Ireland, Isle of Man, Israel, Italy, Jamaica, Japan, Jersey, Jordan, Kazakhstan, Kenya, Kiribati, Kuwait, Kyrgyzstan, Laos, Latvia, Lesotho, Liberia, Liechtenstein, Lithuania, Luxembourg, Macao, Macedonia, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands, Martinique, Mauritania, Mauritius, Mayotte, Mexico, Micronesia, Moldova, Monaco, Mongolia, Montenegro, Montserrat, Morocco, Mozambique, Namibia, Nauru, Nepal, Netherlands, Netherlands Antilles, New Caledonia, New Zealand, Nicaragua, Niger, Nigeria, Niue, Norfolk Island, Northern Mariana Islands, Norway, Oman, Pakistan, Palau, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Pitcairn, Poland, Portugal, Puerto Rico, Qatar, Reunion, Romania, Rwanda, , Saint Barthelemy, Saint Helena, Ascension and Tristan da Cunha, Saint Kitts and Nevis, Saint Lucia, Saint Martin (French part), Saint Pierre and Miquelon, Saint Vincent& the Grenadines, Samoa, San Marino, Sao Tome and Principe, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Sint Maarten (Dutch part), Slovakia, Slovenia, Solomon Islands, South Africa, South Georgia and the South Sandwich Islands, South Korea, Spain, Sri Lanka, Suriname, Svalbard and Jan Mayen, Swaziland, Sweden, Switzerland, Taiwan, Tajikistan, Tanzania, Thailand, Togo, Tokelau, Tonga, Trinidad & Tobago, Tunisia, Turkey, Turkmenistan, Turks and Caicos Islands, Tuvalu, Uganda, Ukraine, United Arab Emirates, United Kingdom, United States, Uruguay, Uzbekistan, Vanuatu, Vatican City, Vietnam, Virgin Islands, British, Virgin Islands, U.S., Wallis and Futuna, Western Sahara, Zambia

### Supported States for Shipping

The following is a list of the states in the US you can ship Cato hardware items to:

**United States:**

AL, AK, AZ, AR, CA, CO, CT, DE, DC, FL, GA, HI, ID, IL, IN, IA, KS, KY, LA, ME, MD, MA, MI, MN, MS, MS, MT, NE, NV, NH, NJ, NM, NY, NC, ND, OH, OK, OR, PA, RI, SC, SD, TN, TX, UT, VT, VA, WA, WV, WI, WY
