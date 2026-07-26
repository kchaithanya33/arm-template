const API_URL = "http://localhost:8000";


// ----------------------------
// Resource Group Create
// ----------------------------
export async function createResourceGroupApi(data) {

  const res = await fetch(
    `${API_URL}/resource-group`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }
  );

  return res.json();
}


// ----------------------------
// Get Resource Groups
// ----------------------------
export async function getResourceGroupsApi(subscriptionId) {

  const res = await fetch(
    `${API_URL}/azure/resource-groups?subscription_id=${subscriptionId}`
  );

  const result = await res.json();

  return result.data;
}


// ----------------------------
// Get Locations
// ----------------------------
export async function getLocationsApi(subscriptionId) {

  const res = await fetch(
    `${API_URL}/azure/locations?subscription_id=${subscriptionId}`
  );

  const result = await res.json();

  return result.data;
}


// ----------------------------
// Get Storage Accounts
// ----------------------------
export async function getStorageAccountsApi(subscriptionId) {

  const res = await fetch(
    `${API_URL}/azure/storage?subscription_id=${subscriptionId}`
  );

  const result = await res.json();

  return result.data;
}


// ----------------------------
// Get Application Insights
// ----------------------------
export async function getApplicationInsightsApi(subscriptionId) {

  const res = await fetch(
    `${API_URL}/azure/application-insights?subscription_id=${subscriptionId}`
  );

  const result = await res.json();

  return result.data;
}


// ----------------------------
// Get Workspaces
// ----------------------------
export async function getWorkspacesApi(subscriptionId) {

  const res = await fetch(
    `${API_URL}/azure/workspaces?subscription_id=${subscriptionId}`
  );

  const result = await res.json();

  return result.data;
}


// ----------------------------
// Get App Service Plans
// ----------------------------
export async function getAppServicePlansApi(subscriptionId) {

  const res = await fetch(
    `${API_URL}/azure/app-service-plans?subscription_id=${subscriptionId}`
  );

  const result = await res.json();

  return result.data;
}


// ----------------------------
// Get Function Apps
// ----------------------------
export async function getFunctionAppsApi(subscriptionId) {

  const res = await fetch(
    `${API_URL}/azure/function-apps?subscription_id=${subscriptionId}`
  );

  const result = await res.json();

  return result.data;
}


// ----------------------------
// Get Logic Apps
// ----------------------------
export async function getLogicAppsApi(subscriptionId) {

  const res = await fetch(
    `${API_URL}/azure/logic-apps?subscription_id=${subscriptionId}`
  );

  const result = await res.json();

  return result.data;
}