const API_URL = "http://localhost:8000";


// Temporary hardcoded subscription ID
// Later replace this with logged-in user's subscription
const SUBSCRIPTION_ID = "cc65e704-15de-4ddc-aa64-56973ac617f8";



// ======================================================
// RESOURCE GROUP
// ======================================================


// Create Resource Group
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





// Get Existing Resource Groups
export async function getResourceGroupsApi() {


  const res = await fetch(

    `${API_URL}/azure/resource-groups?subscription_id=${SUBSCRIPTION_ID}`

  );


  const result = await res.json();


  return result.data || [];

}






// ======================================================
// LOCATIONS
// ======================================================


// Get Azure Locations
export async function getLocationsApi() {


  const res = await fetch(

    `${API_URL}/azure/locations?subscription_id=${SUBSCRIPTION_ID}`

  );


  const result = await res.json();


  return result.data || [];

}






// ======================================================
// STORAGE ACCOUNT
// ======================================================


// Get Existing Storage Accounts
export async function getStorageAccountsApi() {


  const res = await fetch(

    `${API_URL}/azure/storage-accounts?subscription_id=${SUBSCRIPTION_ID}`

  );


  const result = await res.json();


  return result.data || [];

}







// ======================================================
// APPLICATION INSIGHTS
// ======================================================


// Get Existing Application Insights
export async function getApplicationInsightsApi() {


  const res = await fetch(

    `${API_URL}/azure/application-insights?subscription_id=${SUBSCRIPTION_ID}`

  );


  const result = await res.json();


  return result.data || [];

}







// ======================================================
// LOG ANALYTICS WORKSPACE
// ======================================================


// Get Existing Workspaces
export async function getWorkspacesApi() {


  const res = await fetch(

    `${API_URL}/azure/workspaces?subscription_id=${SUBSCRIPTION_ID}`

  );


  const result = await res.json();


  return result.data || [];

}







// ======================================================
// APP SERVICE PLAN
// ======================================================


// Get Existing App Service Plans
export async function getAppServicePlansApi() {


  const res = await fetch(

    `${API_URL}/azure/app-service-plans?subscription_id=${SUBSCRIPTION_ID}`

  );


  const result = await res.json();


  return result.data || [];

}







// ======================================================
// FUNCTION APP
// ======================================================


// Get Existing Function Apps
export async function getFunctionAppsApi() {


  const res = await fetch(

    `${API_URL}/azure/function-apps?subscription_id=${SUBSCRIPTION_ID}`

  );


  const result = await res.json();


  return result.data || [];

}







// ======================================================
// LOGIC APP
// ======================================================


// Get Existing Logic Apps
export async function getLogicAppsApi() {


  const res = await fetch(

    `${API_URL}/azure/logic-apps?subscription_id=${SUBSCRIPTION_ID}`

  );


  const result = await res.json();


  return result.data || [];

}