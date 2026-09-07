---
title: "Testing User Provisioning (Part 2)"
slug: "testing-user-provisioning-part-2"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/testing-user-provisioning-part-2"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing User Provisioning (Part 2)

## Step 1 - Testing SCIM Provisioning

1. In the LDAP IdP, create a test group (i.e., MS Active Directory group) such as SCIM-TEST on the DC servers that are synced with the CMA.
2. Sync the newly created group to the SCIM IdP (Entra ID).
3. Add the newly created group to the LDAP sync settings:
  1. In the CMA, navigate to **Access > Directory Services** and click the **LDAP** tab.
  2. Select **User Groups**, add the test group from step 1, and click **Save and Close**.
4. Add the test group from step 1 to the following policies:
  1. Client Connectivity Policy
  2. WAN Firewall
  3. Internet Firewall
  4. Always-On Policy
5. Create a test block rule on Internet Firewall to validate the newly created group SCIM-TEST to BLOCK traffic to google.com. Then, verify that one of the test users is blocked from Google.

## Step 2 - Testing Migration from LDAP to SCIM (IdP)

1. Configure the Cato app for the SCIM IdP. For more information, see the relevant article in [SCIM User Provisioning](/v1/docs/scim-user-provisioning).
2. Verify that all the user and user group properties are synced from the LDAP to the SCIM IdP.
3. Assign the SCIM-TEST group to the Cato app for the SCIM IdP.
4. Perform the initial SCIM sync.
5. Ensure test users and the user group (SCIM-TEST) have been updated from LDAP to SCIM in the CMA.
  - For users, go to Access > Users > Users Directory
  - For user groups, go to Access > User Groups, and verify that SCIM-TEST contains all the migrated users
6. Test that the block rule (from the previous section) is still blocking traffic for a user in the SCIM-TEST group.
7. Verify that users can sign out of an SSO app or the Cato Client and then authenticate again.
