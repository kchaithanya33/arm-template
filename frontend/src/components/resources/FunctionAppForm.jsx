import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  getLocationsApi,
  getResourceGroupsApi,
  getStorageAccountsApi,
} from "../../api/resourceApi";
import { useDeployment } from "../../context/DeploymentContext";

export default function FunctionAppForm() {
  const navigate = useNavigate();
  const { deploymentData, updateSection } = useDeployment();

  /* ==========================================
      Azure Resources
  ========================================== */
  const [locations, setLocations] = useState([]);
  const [storageAccounts, setStorageAccounts] = useState([]);
  const [resourceGroups, setResourceGroups] = useState([]);

  /* ==========================================
      Modes
  ========================================== */
  const [storageMode, setStorageMode] = useState(
  deploymentData.functionApp?.storage?.mode || "existing"
);
  const [resourceGroupMode, setResourceGroupMode] = useState(() => {
  if (deploymentData.functionApp?.resourceGroup?.mode === "new") {
    return "create";
  }

  return deploymentData.functionApp?.resourceGroup?.mode || "existing";
});

  /* ==========================================
      Function App
  ========================================== */
  const [functionApp, setFunctionApp] = useState({
  name: deploymentData.functionApp?.name || "",
  location: deploymentData.functionApp?.location || "",
  runtimeStack:
    deploymentData.functionApp?.runtimeStack || "python",
  runtimeVersion:
    deploymentData.functionApp?.runtimeVersion || "3.12",
  hostingPlan:
    deploymentData.functionApp?.hostingPlan ||
    "Flex Consumption",
});

  /* ==========================================
      Storage
  ========================================== */
  const [storage, setStorage] = useState({
  existingStorage:
    deploymentData.functionApp?.storage?.existingStorage || "",

  name:
    deploymentData.functionApp?.storage?.name || "",

  location:
    deploymentData.functionApp?.storage?.location || "",
});

  /* ==========================================
      Resource Group
  ========================================== */
  const [resourceGroup, setResourceGroup] = useState({
  existing:
    deploymentData.functionApp?.resourceGroup?.existing || "",

  name:
    deploymentData.functionApp?.resourceGroup?.name || "",

  location:
    deploymentData.functionApp?.resourceGroup?.location || "",
});

  /* ==========================================
      Runtime Versions
  ========================================== */
  const runtimeVersions = {
    python: ["3.10", "3.11", "3.12", "3.13"],
    node: ["18", "20", "22"],
    dotnet: ["6", "8", "9"],
    java: ["8", "11", "17", "21"],
    powershell: ["7.2", "7.4"],
  };

  /* ==========================================
      Load Azure Resources
  ========================================== */
  useEffect(() => {
    loadAzureResources();
  }, []);

  async function loadAzureResources() {
    try {
      const locationData = await getLocationsApi();
      const storageData = await getStorageAccountsApi();
      const resourceGroupData = await getResourceGroupsApi();

      setLocations(locationData || []);
      setStorageAccounts(storageData || []);
      setResourceGroups(resourceGroupData || []);
    } catch (error) {
      console.log(error);
    }
  }

  /* ==========================================
      Update Handlers
  ========================================== */
  function updateFunctionApp(field, value) {
    setFunctionApp((previous) => ({
      ...previous,
      [field]: value,
    }));
  }

  function updateStorage(field, value) {
    setStorage((previous) => ({
      ...previous,
      [field]: value,
    }));
  }

  function updateResourceGroup(field, value) {
    setResourceGroup((previous) => ({
      ...previous,
      [field]: value,
    }));
  }


  /* ==========================================
      Next
  ========================================== */
  function handleNext() {
    updateSection("functionApp", {
      ...functionApp,
      storage: {
        mode: storageMode === "create" ? "new" : "existing",
        ...storage,
      },
      resourceGroup:
  resourceGroupMode === "existing"
    ? {
        mode: "existing",
        name: resourceGroup.existing,
      }
    : {
        mode: "new",
        name: resourceGroup.name,
        location: resourceGroup.location,
      },
    });
    console.log("Function App Saved");
    navigate("/payload");
  }

  return (
    <div className="phone">
      <div className="content">
        

        <h2 className="logo">
          ARM<span>Flow</span>
        </h2>

        <h1>Function App</h1>
        <p className="subtitle">Define your function app parameters</p>

        {/* ==========================================
              FUNCTION APP
        ========================================== */}
        <div className="section-card">
          <h2 className="section-title">Function App</h2>
          <div className="form">
            <div className="field">
              <label>Function App Name</label>
              <input
                value={functionApp.name}
                placeholder="demo-function-app-001"
                onChange={(e) => updateFunctionApp("name", e.target.value)}
              />
            </div>

            <div className="field">
              <label>Location</label>
              <select
                value={functionApp.location}
                onChange={(e) => updateFunctionApp("location", e.target.value)}
              >
                <option value="">Select Location</option>
                {locations.map((location) => (
                  <option key={location.name} value={location.name}>
                    {location.display_name}
                  </option>
                ))}
              </select>
            </div>

            <div className="field">
              <label>Runtime Stack</label>
              <select
                value={functionApp.runtimeStack}
                onChange={(e) => {
                  updateFunctionApp("runtimeStack", e.target.value);
                  const versions = runtimeVersions[e.target.value];
                  updateFunctionApp("runtimeVersion", versions[0]);
                }}
              >
                <option value="python">Python</option>
                <option value="node">Node.js</option>
                <option value="dotnet">.NET</option>
                <option value="java">Java</option>
                <option value="powershell">PowerShell</option>
              </select>
            </div>

            <div className="field">
              <label>Runtime Version</label>
              <select
                value={functionApp.runtimeVersion}
                onChange={(e) =>
                  updateFunctionApp("runtimeVersion", e.target.value)
                }
              >
                {runtimeVersions[functionApp.runtimeStack].map((version) => (
                  <option key={version} value={version}>
                    {version}
                  </option>
                ))}
              </select>
            </div>

            <div className="field full">
              <label>Hosting Plan</label>
              <select
                value={functionApp.hostingPlan}
                onChange={(e) =>
                  updateFunctionApp("hostingPlan", e.target.value)
                }
              >
                <option>Flex Consumption</option>
                <option>Consumption</option>
                <option>Premium</option>
                <option>App Service Plan</option>
              </select>
            </div>
          </div>
        </div>

        {/* ==========================================
              STORAGE ACCOUNT
        ========================================== */}
        <div className="section-card">
          <h2 className="section-title">Storage Account</h2>
          <div className="toggle">
            <button
              className={storageMode === "create" ? "active" : ""}
              onClick={() => setStorageMode("create")}
            >
              Create New
            </button>
            <button
              className={storageMode === "existing" ? "active" : ""}
              onClick={() => setStorageMode("existing")}
            >
              Use Existing
            </button>
          </div>

          <div className="form">
            {storageMode === "existing" && (
              <div className="field full">
                <label>Existing Storage Account</label>
                <select
                  value={storage.existingStorage}
                  onChange={(e) =>
                    updateStorage("existingStorage", e.target.value)
                  }
                >
                  <option value="">Select Storage Account</option>
                  {storageAccounts.map((account) => (
                    <option key={account.name} value={account.name}>
                      {account.name}
                    </option>
                  ))}
                </select>
              </div>
            )}

            {storageMode === "create" && (
              <>
                <div className="field">
                  <label>Storage Account Name</label>
                  <input
                    value={storage.name}
                    placeholder="storageaccount001"
                    onChange={(e) => updateStorage("name", e.target.value)}
                  />
                </div>
                <div className="field">
                  <label>Location</label>
                  <select
                    value={storage.location}
                    onChange={(e) => updateStorage("location", e.target.value)}
                  >
                    <option value="">Select Location</option>
                    {locations.map((location) => (
                      <option key={location.name} value={location.name}>
                        {location.display_name}
                      </option>
                    ))}
                  </select>
                </div>
              </>
            )}
          </div>
        </div>

        {/* ==========================================
              RESOURCE GROUP
        ========================================== */}
        <div className="section-card">
          <h2 className="section-title">Resource Group</h2>
          <div className="toggle">
            <button
              className={resourceGroupMode === "create" ? "active" : ""}
              onClick={() => setResourceGroupMode("create")}
            >
              Create New
            </button>
            <button
              className={resourceGroupMode === "existing" ? "active" : ""}
              onClick={() => setResourceGroupMode("existing")}
            >
              Use Existing
            </button>
          </div>

          <div className="form">
            {resourceGroupMode === "existing" && (
              <div className="field full">
                <label>Existing Resource Group</label>
                <select
                  value={resourceGroup.existing}
                  onChange={(e) =>
                    updateResourceGroup("existing", e.target.value)
                  }
                >
                  <option value="">Select Resource Group</option>
                  {resourceGroups.map((group) => (
                    <option key={group.name} value={group.name}>
                      {group.name}
                    </option>
                  ))}
                </select>
              </div>
            )}

            {resourceGroupMode === "create" && (
              <>
                <div className="field">
                  <label>Resource Group Name</label>
                  <input
                    value={resourceGroup.name}
                    placeholder="rg-demo"
                    onChange={(e) =>
                      updateResourceGroup("name", e.target.value)
                    }
                  />
                </div>
                <div className="field">
                  <label>Location</label>
                  <select
                    value={resourceGroup.location}
                    onChange={(e) =>
                      updateResourceGroup("location", e.target.value)
                    }
                  >
                    <option value="">Select Location</option>
                    {locations.map((location) => (
                      <option key={location.name} value={location.name}>
                        {location.display_name}
                      </option>
                    ))}
                  </select>
                </div>
              </>
            )}
          </div>
        </div>
      </div>

      {/* ==========================================
            FOOTER BUTTONS
      ========================================== */}
      <div className="button-row">
        <button
          className="next back-button"
          onClick={() => navigate("/logic-app")}
        >
          Back
        </button>
        <button className="next" onClick={handleNext}>
          Next
        </button>
      </div>
    </div>
  );
}