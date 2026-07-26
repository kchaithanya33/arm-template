import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  getLocationsApi,
  getResourceGroupsApi,
  getApplicationInsightsApi,
} from "../../api/resourceApi";
import { useDeployment } from "../../context/DeploymentContext";

export default function LogicAppForm() {
  const navigate = useNavigate();
  const { updateSection } = useDeployment();

  /*
  ==========================================
      Azure Data
  ==========================================
  */
  const [locations, setLocations] = useState([]);
  const [resourceGroups, setResourceGroups] = useState([]);
  const [applicationInsightsList, setApplicationInsightsList] = useState([]);

  /*
  ==========================================
      Resource Group Mode
  ==========================================
  */
  const [resourceGroupMode, setResourceGroupMode] = useState("existing");

  /*
  ==========================================
      Application Insights Mode
  ==========================================
  */
  const [applicationInsightsMode, setApplicationInsightsMode] =
    useState("create");

  /*
  ==========================================
      Logic App
  ==========================================
  */
  const [logicApp, setLogicApp] = useState({
    name: "",
    location: "",
    workflowType: "Stateful",
    enableLogAnalytics: true,
  });

  /*
  ==========================================
      Resource Group
  ==========================================
  */
  const [resourceGroup, setResourceGroup] = useState({
    existing: "",
    name: "",
    location: "",
  });

  /*
  ==========================================
      Application Insights
  ==========================================
  */
  const [applicationInsights, setApplicationInsights] = useState({
    existing: "",
    name: "",
    location: "",
    applicationType: "web",
  });

  /*
  ==========================================
      Load Azure Resources
  ==========================================
  */
  useEffect(() => {
    loadAzureResources();
  }, []);

  async function loadAzureResources() {
    try {
      const locationData = await getLocationsApi();
      const rgData = await getResourceGroupsApi();
      const appInsightsData = await getApplicationInsightsApi();

      setLocations(locationData);
      setResourceGroups(rgData);
      setApplicationInsightsList(appInsightsData);
    } catch (error) {
      console.log(error);
    }
  }

  /*
  ==========================================
      Handlers
  ==========================================
  */
  function updateLogicApp(field, value) {
    setLogicApp((prev) => ({
      ...prev,
      [field]: value,
    }));
  }

  function updateResourceGroup(field, value) {
    setResourceGroup((prev) => ({
      ...prev,
      [field]: value,
    }));
  }

  function updateApplicationInsights(field, value) {
    setApplicationInsights((prev) => ({
      ...prev,
      [field]: value,
    }));
  }

  /*
  ==========================================
      Next Button
  ==========================================
  */
  function handleNext() {
    const finalData = {
      ...logicApp,
      resourceGroup: {
        mode: resourceGroupMode,
        ...(resourceGroupMode === "existing"
          ? {
              name: resourceGroup.existing,
            }
          : {
              name: resourceGroup.name,
              location: resourceGroup.location,
            }),
      },
      applicationInsights:
        applicationInsightsMode === "existing"
          ? {
              mode: "existing",
              name: applicationInsights.existing,
            }
          : {
              mode: "create",
              name: applicationInsights.name,
              location: applicationInsights.location,
              applicationType: applicationInsights.applicationType,
            },
    };

    updateSection("logicApp", finalData);
    console.log("Logic App Saved", finalData);

    /*
      Only Create New Application Insights
      needs Workspace page
    */
    if (applicationInsightsMode === "create") {
      navigate("/workspace");
    } else {
      navigate("/");
    }
  }

  return (
    <div className="phone">
      <div className="content">
        {/* Back */}
        <div className="back" onClick={() => navigate("/storage")}>
          ←
        </div>

        <h2 className="logo">
          ARM<span>Flow</span>
        </h2>
        <h1>Create Your Own Template</h1>
        <p className="subtitle">Configure Logic App</p>

        {/* LOGIC APP */}
        <div className="section-card">
          <h2 className="section-title">Logic App</h2>
          <div className="form">
            <div className="field">
              <label>Logic App Name</label>
              <input
                value={logicApp.name}
                placeholder="logic-app-demo"
                onChange={(e) => updateLogicApp("name", e.target.value)}
              />
            </div>

            <div className="field">
              <label>Location</label>
              <select
                value={logicApp.location}
                onChange={(e) => updateLogicApp("location", e.target.value)}
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
              <label>Workflow Type</label>
              <select
                value={logicApp.workflowType}
                onChange={(e) => updateLogicApp("workflowType", e.target.value)}
              >
                <option value="Stateful">Stateful</option>
                <option value="Stateless">Stateless</option>
              </select>
            </div>

            <div className="checkbox">
              <input
                type="checkbox"
                checked={logicApp.enableLogAnalytics}
                onChange={(e) =>
                  updateLogicApp("enableLogAnalytics", e.target.checked)
                }
              />
              <label>Enable Log Analytics</label>
            </div>
          </div>
        </div>

        {/* RESOURCE GROUP */}
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
                <label>Resource Group</label>
                <select
                  value={resourceGroup.existing}
                  onChange={(e) => updateResourceGroup("existing", e.target.value)}
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
                    placeholder="logic-rg"
                    onChange={(e) => updateResourceGroup("name", e.target.value)}
                  />
                </div>
                <div className="field">
                  <label>Location</label>
                  <select
                    value={resourceGroup.location}
                    onChange={(e) => updateResourceGroup("location", e.target.value)}
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

        {/* APPLICATION INSIGHTS */}
        <div className="section-card">
          <h2 className="section-title">Application Insights</h2>
          <div className="toggle">
            <button
              className={applicationInsightsMode === "create" ? "active" : ""}
              onClick={() => setApplicationInsightsMode("create")}
            >
              Create New
            </button>
            <button
              className={applicationInsightsMode === "existing" ? "active" : ""}
              onClick={() => setApplicationInsightsMode("existing")}
            >
              Use Existing
            </button>
          </div>

          <div className="form">
            {applicationInsightsMode === "existing" && (
              <div className="field full">
                <label>Application Insights</label>
                <select
                  value={applicationInsights.existing}
                  onChange={(e) =>
                    updateApplicationInsights("existing", e.target.value)
                  }
                >
                  <option value="">Select Application Insights</option>
                  {applicationInsightsList.map((app) => (
                    <option key={app.name} value={app.name}>
                      {app.name}
                    </option>
                  ))}
                </select>
              </div>
            )}

            {applicationInsightsMode === "create" && (
              <>
                <div className="field">
                  <label>Application Insights Name</label>
                  <input
                    value={applicationInsights.name}
                    placeholder="appi-demo"
                    onChange={(e) =>
                      updateApplicationInsights("name", e.target.value)
                    }
                  />
                </div>

                <div className="field">
                  <label>Location</label>
                  <select
                    value={applicationInsights.location}
                    onChange={(e) =>
                      updateApplicationInsights("location", e.target.value)
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

                <div className="field">
                  <label>Application Type</label>
                  <select
                    value={applicationInsights.applicationType}
                    onChange={(e) =>
                      updateApplicationInsights("applicationType", e.target.value)
                    }
                  >
                    <option value="web">Web</option>
                    <option value="other">Other</option>
                  </select>
                </div>
              </>
            )}
          </div>
        </div>
      </div>

      {/* Footer Buttons */}
      <div className="button-row">
        <button className="next back-button" onClick={() => navigate("/storage")}>
          Back
        </button>
        <button className="next" onClick={handleNext}>
          Next
        </button>
      </div>
    </div>
  );
}