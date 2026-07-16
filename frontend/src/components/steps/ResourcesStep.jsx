import { useEffect, useState } from "react";

import {
  getStorageAccounts,
  getApplicationInsights,
  getAppServicePlans,
  getFunctionApps,
  getLogicApps,
} from "../../api/azureApi";

function ResourcesStep({ data, setData }) {
  const [storageAccounts, setStorageAccounts] = useState([]);
  const [applicationInsights, setApplicationInsights] = useState([]);
  const [plans, setPlans] = useState([]);
  const [functionApps, setFunctionApps] = useState([]);
  const [logicApps, setLogicApps] = useState([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
  try {

    const [
      storage,
      insights,
      appPlans,
      functions,
      logic
    ] = await Promise.all([
      getStorageAccounts(),
      getApplicationInsights(),
      getAppServicePlans(),
      getFunctionApps(),
      getLogicApps()
    ]);

    setStorageAccounts(storage);
    setApplicationInsights(insights);
    setPlans(appPlans);
    setFunctionApps(functions);
    setLogicApps(logic);

  } catch (err) {
    console.error(err);
  }
};

  const change = (e) => {
    setData({
      ...data,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div>
      <h2>Resources</h2>

      <br />

      <label>Storage Account</label>
      <br />

      <select
        name="storageAccountName"
        value={data.storageAccountName}
        onChange={change}
      >
        <option value="">Select Storage Account</option>

        {storageAccounts.map((item) => (
          <option key={item.name} value={item.name}>
            {item.name}
          </option>
        ))}
      </select>

      <br />
      <br />

      <label>Application Insights</label>
      <br />

      <select
        name="applicationInsightsName"
        value={data.applicationInsightsName}
        onChange={change}
      >
        <option value="">Select Application Insights</option>

        {applicationInsights.map((item) => (
          <option key={item.name} value={item.name}>
            {item.name}
          </option>
        ))}
      </select>

      <br />
      <br />

      <label>App Service Plan</label>
      <br />

      <select
        name="appServicePlanName"
        value={data.appServicePlanName}
        onChange={change}
      >
        <option value="">Select App Service Plan</option>

        {plans.map((item) => (
          <option key={item.name} value={item.name}>
            {item.name}
          </option>
        ))}
      </select>

      <br />
      <br />

      <label>Function App</label>
      <br />

      <select
        name="functionAppName"
        value={data.functionAppName}
        onChange={change}
      >
        <option value="">Select Function App</option>

        {functionApps.map((item) => (
          <option key={item.name} value={item.name}>
            {item.name}
          </option>
        ))}
      </select>

      <br />
      <br />

      <label>Logic App</label>
      <br />

      <select
        name="logicAppName"
        value={data.logicAppName}
        onChange={change}
      >
        <option value="">Select Logic App</option>

        {logicApps.map((item) => (
          <option key={item.name} value={item.name}>
            {item.name}
          </option>
        ))}
      </select>
    </div>
  );
}

export default ResourcesStep;