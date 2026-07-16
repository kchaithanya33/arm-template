import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

export const getResourceGroups = async () => {
    const res = await api.get("/azure/resource-groups");
    return res.data;
};

export const getLocations = async () => {
    const res = await api.get("/azure/locations");
    return res.data;
};

export const getStorageAccounts = async () => {
    const res = await api.get("/azure/storage-accounts");
    return res.data;
};

export const getAppServicePlans = async () => {
    const res = await api.get("/azure/app-service-plans");
    return res.data;
};

export const getFunctionApps = async () => {
    const res = await api.get("/azure/function-apps");
    return res.data;
};

export const getLogicApps = async () => {
    const res = await api.get("/azure/logic-apps");
    return res.data;
};

export const deployTemplate = async (data) => {
    const res = await api.post("/deploy", data);
    return res.data;
};

export const getApplicationInsights = async () => {
    const res = await api.get("/azure/application-insights");
    return res.data;
};

export default api;