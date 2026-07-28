import { useDeployment } from "../../context/DeploymentContext";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  getLocationsApi,
  getStorageAccountsApi,
  getResourceGroupsApi,
} from "../../api/resourceApi";

export default function StorageForm() {
  const navigate = useNavigate();
  const { deploymentData, updateSection } = useDeployment();

  // ==============================
  // Modes
  // ==============================
  const [storageMode, setStorageMode] = useState(
    deploymentData.storage?.mode || "create"
  );
  const [resourceGroupMode, setResourceGroupMode] = useState(
    deploymentData.resourceGroup?.mode || "existing"
  );

  // ==============================
  // Azure Data
  // ==============================
  const [locations, setLocations] = useState([]);
  const [storageAccounts, setStorageAccounts] = useState([]);
  const [resourceGroups, setResourceGroups] = useState([]);

  // ==============================
  // Storage
  // ==============================
  const [storage, setStorage] = useState(() => {
    if (deploymentData.storage?.mode === "existing") {
      return {
        existingStorage: deploymentData.storage?.existingStorage || "",
        name: "",
        location: "",
        kind: "StorageV2",
        sku: "Standard_LRS",
        accessTier: "Hot",
        minimumTlsVersion: "TLS1_2",
      };
    }
    return {
      existingStorage: "",
      name: deploymentData.storage?.name || "",
      location: deploymentData.storage?.location || "",
      kind: deploymentData.storage?.kind || "StorageV2",
      sku: deploymentData.storage?.sku || "Standard_LRS",
      accessTier: deploymentData.storage?.accessTier || "Hot",
      minimumTlsVersion: deploymentData.storage?.minimumTlsVersion || "TLS1_2",
    };
  });

  // Clear opposite values when switching modes
  useEffect(() => {
    if (storageMode === "create") {
      setStorage((prev) => ({
        ...prev,
        existingStorage: "",
      }));
    } else {
      setStorage((prev) => ({
        ...prev,
        name: "",
        location: "",
      }));
    }
  }, [storageMode]);

  // ==============================
  // Resource Group
  // ==============================
  const [resourceGroup, setResourceGroup] = useState(() => {
    if (deploymentData.resourceGroup?.mode === "existing") {
      return {
        existing: deploymentData.resourceGroup?.name || "",
        name: "",
        location: "",
      };
    }
    return {
      existing: "",
      name: deploymentData.resourceGroup?.name || "",
      location: deploymentData.resourceGroup?.location || "",
    };
  });

  // ==============================
  // Load Azure Data
  // ==============================
  useEffect(() => {
    loadAzureData();
  }, []);

  async function loadAzureData() {
    try {
      const loc = await getLocationsApi();
      const storageList = await getStorageAccountsApi();
      const rg = await getResourceGroupsApi();

      setLocations(Array.isArray(loc) ? loc : []);
      setStorageAccounts(Array.isArray(storageList) ? storageList : []);
      setResourceGroups(Array.isArray(rg) ? rg : []);
    } catch (error) {
      console.log("Azure loading error", error);
    }
  }

  // ==============================
  // Update Helpers
  // ==============================
  function updateStorage(field, value) {
    setStorage((prev) => ({
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

  // ==============================
  // Next
  // ==============================
  function handleNext() {
    // Save Storage
    if (storageMode === "existing") {
      updateSection("storage", {
        mode: "existing",
        existingStorage: storage.existingStorage,
      });
    } else {
      updateSection("storage", {
        mode: "new",
        name: storage.name,
        location: storage.location,
        kind: storage.kind,
        sku: storage.sku,
        accessTier: storage.accessTier,
        minimumTlsVersion: storage.minimumTlsVersion,
      });
    }

    // Save Resource Group
    if (storageMode === "create") {
      if (resourceGroupMode === "existing") {
        updateSection("resourceGroup", {
          mode: "existing",
          name: resourceGroup.existing,
        });
      } else {
        updateSection("resourceGroup", {
          mode: "new",
          name: resourceGroup.name,
          location: resourceGroup.location,
        });
      }
    }

    navigate("/logic-app");
  }

  return (
    <div className="phone">
      <div className="content">
        <h2 className="logo">
          ARM<span>Flow</span>
        </h2>
        <h1>Create Your Own Template</h1>
        <p className="subtitle">Configure Storage Account</p>

        {/* ==============================
            STORAGE ACCOUNT
        ============================== */}
        <div className="section-title">Storage Account</div>

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
              <label>Storage Account</label>
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
                <label>Storage Name</label>
                <input
                  value={storage.name}
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
                  {locations.map((loc) => (
                    <option key={loc.name} value={loc.name}>
                      {loc.display_name}
                    </option>
                  ))}
                </select>
              </div>

              <div className="field">
                <label>Kind</label>
                <select
                  value={storage.kind}
                  onChange={(e) => updateStorage("kind", e.target.value)}
                >
                  <option value="StorageV2">StorageV2</option>
                  <option value="BlobStorage">BlobStorage</option>
                  <option value="FileStorage">FileStorage</option>
                </select>
              </div>

              <div className="field">
                <label>SKU</label>
                <select
                  value={storage.sku}
                  onChange={(e) => updateStorage("sku", e.target.value)}
                >
                  <option value="Standard_LRS">Standard_LRS</option>
                  <option value="Standard_GRS">Standard_GRS</option>
                  <option value="Standard_ZRS">Standard_ZRS</option>
                  <option value="Premium_LRS">Premium_LRS</option>
                </select>
              </div>

              <div className="field">
                <label>Access Tier</label>
                <select
                  value={storage.accessTier}
                  onChange={(e) => updateStorage("accessTier", e.target.value)}
                >
                  <option value="Hot">Hot</option>
                  <option value="Cool">Cool</option>
                </select>
              </div>

              <div className="field">
                <label>Minimum TLS Version</label>
                <select
                  value={storage.minimumTlsVersion}
                  onChange={(e) =>
                    updateStorage("minimumTlsVersion", e.target.value)
                  }
                >
                  <option value="TLS1_2">TLS1_2</option>
                  <option value="TLS1_1">TLS1_1</option>
                  <option value="TLS1_0">TLS1_0</option>
                </select>
              </div>
            </>
          )}
        </div>

        {storageMode === "create" && (
          <>
            <div className="section-title">Resource Group</div>

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
                    onChange={(e) =>
                      updateResourceGroup("existing", e.target.value)
                    }
                  >
                    <option value="">Select Resource Group</option>
                    {resourceGroups.map((rg) => (
                      <option key={rg.name} value={rg.name}>
                        {rg.name}
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
                      onChange={(e) =>
                        updateResourceGroup("name", e.target.value)
                      }
                    />
                  </div>

                  <div className="field">
                    <label>Resource Group Location</label>
                    <select
                      value={resourceGroup.location}
                      onChange={(e) =>
                        updateResourceGroup("location", e.target.value)
                      }
                    >
                      <option value="">Select Location</option>
                      {locations.map((loc) => (
                        <option key={loc.name} value={loc.name}>
                          {loc.display_name}
                        </option>
                      ))}
                    </select>
                  </div>
                </>
              )}
            </div>
          </>
        )}
      </div>

      <div className="button-row">
        <button className="next back-button" onClick={() => navigate("/")}>
          Back
        </button>
        <button className="next" onClick={handleNext}>
          Next
        </button>
      </div>
    </div>
  );
}