import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useDeployment } from "../../context/DeploymentContext";

import {
  getResourceGroupsApi,
  getLocationsApi,
} from "../../api/resourceApi";

export default function ResourceGroupSelector() {
  const navigate = useNavigate();

  const { deploymentData, updateSection } = useDeployment();

  // ----------------------------
  // Azure Data
  // ----------------------------

  const [resourceGroups, setResourceGroups] = useState([]);
  const [locations, setLocations] = useState([]);

  // ----------------------------
  // Selected Values
  // ----------------------------

  const [mode, setMode] = useState(
    deploymentData.resourceGroup?.mode || "create"
  );

  const [resourceGroupName, setResourceGroupName] = useState(
    deploymentData.resourceGroup?.name || ""
  );

  const [location, setLocation] = useState(
    deploymentData.resourceGroup?.location || ""
  );

  // ----------------------------
  // Load Azure Data
  // ----------------------------

  useEffect(() => {
    loadAzureData();
  }, []);

  async function loadAzureData() {
    try {
      const groups = await getResourceGroupsApi();
      const locationsList = await getLocationsApi();

      setResourceGroups(groups || []);
      setLocations(locationsList || []);
    } catch (error) {
      console.error("Azure loading error:", error);
    }
  }

  // ----------------------------
  // Save helper
  // ----------------------------

  function saveResourceGroup(data) {
    updateSection("resourceGroup", data);
  }

  // ----------------------------
  // Handlers
  // ----------------------------

  function handleModeChange(value) {
    setMode(value);

    saveResourceGroup({
      mode: value,
      name: resourceGroupName,
      location,
    });
  }

  function handleNameChange(value) {
    setResourceGroupName(value);

    saveResourceGroup({
      mode,
      name: value,
      location,
    });
  }

  function handleLocationChange(value) {
    setLocation(value);

    saveResourceGroup({
      mode,
      name: resourceGroupName,
      location: value,
    });
  }

  // ----------------------------
  // Next
  // ----------------------------

  function handleNext() {

  saveResourceGroup({
    mode,
    name: resourceGroupName,
    location,
  });

  navigate("/storage");
}

  return (
    <div className="phone">
      <div className="content">
        

        <h2 className="logo">
          ARM<span>Flow</span>
        </h2>

        <h1>Create Your Own Template</h1>

        <p className="subtitle">
          Define your own parameters
        </p>

        {/* Toggle */}

        <div className="toggle">
          <button
            className={mode === "create" ? "active" : ""}
            onClick={() => handleModeChange("create")}
          >
            Create New
          </button>

          <button
            className={mode === "existing" ? "active" : ""}
            onClick={() => handleModeChange("existing")}
          >
            Use Existing
          </button>
        </div>

        {/* Form */}

        <div className="form">
          <label>Resource Group Name</label>

          {mode === "create" ? (
            <input
              placeholder="rg-armflow-prod"
              value={resourceGroupName}
              onChange={(e) => handleNameChange(e.target.value)}
            />
          ) : (
            <select
              value={resourceGroupName}
              onChange={(e) => handleNameChange(e.target.value)}
            >
              <option value="">
                Select existing group...
              </option>

              {resourceGroups.map((rg) => (
                <option
                  key={rg.name}
                  value={rg.name}
                >
                  {rg.name}
                </option>
              ))}
            </select>
          )}

          {mode === "create" && (
            <>
              <label>Location</label>

              <select
                value={location}
                onChange={(e) => handleLocationChange(e.target.value)}
              >
                <option value="">
                  Select Location
                </option>

                {locations.map((loc) => (
                  <option
                    key={loc.name}
                    value={loc.name}
                  >
                    {loc.display_name}
                  </option>
                ))}
              </select>
            </>
          )}
        </div>
      </div>

      <button
        className="next"
        onClick={handleNext}
      >
        Next
      </button>
    </div>
  );
}