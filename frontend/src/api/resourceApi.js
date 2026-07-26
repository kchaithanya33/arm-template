const API_URL = "http://localhost:8000";


// Temporary hardcoded subscription ID
// Later replace this with login user subscription
const SUBSCRIPTION_ID = "cc65e704-15de-4ddc-aa64-56973ac617f8";


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
export async function getResourceGroupsApi() {

  const res = await fetch(
    `${API_URL}/azure/resource-groups?subscription_id=${SUBSCRIPTION_ID}`
  );

  const result = await res.json();

  return result.data || [];
}



// ----------------------------
// Get Locations
// ----------------------------
export async function getLocationsApi() {

  const res = await fetch(
    `${API_URL}/azure/locations?subscription_id=${SUBSCRIPTION_ID}`
  );

  const result = await res.json();

  return result.data || [];
}



// ----------------------------
// Get Storage Accounts
// ----------------------------
export async function getStorageAccountsApi() {

  const res = await fetch(
    `${API_URL}/azure/storage-accounts?subscription_id=${SUBSCRIPTION_ID}`
  );

  const result = await res.json();

  return result.data || [];
}



// ----------------------------
// Get Application Insights
// ----------------------------
export async function getApplicationInsightsApi() {

  const res = await fetch(
    `${API_URL}/azure/application-insights?subscription_id=${SUBSCRIPTION_ID}`
  );

  const result = await res.json();

  return result.data || [];
}



// ----------------------------
// Get Workspaces
// ----------------------------
export async function getWorkspacesApi() {

  const res = await fetch(
    `${API_URL}/azure/workspaces?subscription_id=${SUBSCRIPTION_ID}`
  );

  const result = await res.json();

  return result.data || [];
}



// ----------------------------
// Get App Service Plans
// ----------------------------
export async function getAppServicePlansApi() {

  const res = await fetch(
    `${API_URL}/azure/app-service-plans?subscription_id=${SUBSCRIPTION_ID}`
  );

  const result = await res.json();

  return result.data || [];
}



// ----------------------------
// Get Function Apps
// ----------------------------
export async function getFunctionAppsApi() {

  const res = await fetch(
    `${API_URL}/azure/function-apps?subscription_id=${SUBSCRIPTION_ID}`
  );

  const result = await res.json();

  return result.data || [];
}



// ----------------------------
// Get Logic Apps
// ----------------------------
export async function getLogicAppsApi() {

  const res = await fetch(
    `${API_URL}/azure/logic-apps?subscription_id=${SUBSCRIPTION_ID}`
  );

  const result = await res.json();

  return result.data || [];
}