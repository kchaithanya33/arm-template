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
  const { updateSection } = useDeployment();

  /* ======================================================
      Storage Mode
  ====================================================== */
  const [storageMode, setStorageMode] = useState("create");

  /* ======================================================
      Resource Group Mode
  ====================================================== */
  const [resourceGroupMode, setResourceGroupMode] = useState("existing");

  /* ======================================================
      Azure Data
  ====================================================== */
  const [locations, setLocations] = useState([]);
  const [storageAccounts, setStorageAccounts] = useState([]);
  const [resourceGroups, setResourceGroups] = useState([]);

  /* ======================================================
      Storage Form
  ====================================================== */
  const [storage, setStorage] = useState({
    existingStorage: "",
    name: "",
    location: "",
    kind: "StorageV2",
    sku: "Standard_LRS",
    accessTier: "Hot",
    minimumTlsVersion: "TLS1_2",
    largeFileSharesState: "Disabled",
    publicNetworkAccess: true,
    secureTransferRequired: true,
    allowBlobPublicAccess: false,
    allowSharedKeyAccess: true,
  });

  /* ======================================================
      Resource Group Form
  ====================================================== */
  const [resourceGroup, setResourceGroup] = useState({
    existing: "",
    name: "",
    location: "",
  });

  /* ======================================================
      Load Azure Resources
  ====================================================== */
  useEffect(() => {
    loadAzureResources();
  }, []);

  async function loadAzureResources() {
    try {
      const locationsResult = await getLocationsApi();
      const storageResult = await getStorageAccountsApi();
      const resourceGroupResult = await getResourceGroupsApi();

      setLocations(locationsResult);
      setStorageAccounts(storageResult);
      setResourceGroups(resourceGroupResult);
    } catch (error) {
      console.error(error);
    }
  }

  /* ======================================================
      Storage Handler
  ====================================================== */
  function updateStorage(field, value) {
    setStorage((previous) => ({
      ...previous,
      [field]: value,
    }));
  }

  /* ======================================================
      Resource Group Handler
  ====================================================== */
  function updateResourceGroup(field, value) {
    setResourceGroup((previous) => ({
      ...previous,
      [field]: value,
    }));
  }

  /* ======================================================
      Next Button
  ====================================================== */
  function handleNext() {
 console.log(updateSection);
  updateSection("storage", {
    mode: storageMode,
    ...storage,
  });

  updateSection("resourceGroup", {
    mode: resourceGroupMode,
    ...resourceGroup,
  });

  console.log("Saved");

  navigate("/logic-app");
}

  /* ======================================================
      UI
  ====================================================== */
  return (
    <div className="phone">
      <div className="content">
        <div className="back" onClick={() => navigate("/")}>
          ←
        </div>

        <h2 className="logo">
          ARM<span>Flow</span>
        </h2>

        <h1>Create Your Own Template</h1>
        <p className="subtitle">Configure Storage Account</p>

        {/* ==========================================
            STORAGE ACCOUNT
        =========================================== */}
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
              <label>Storage Account Name</label>
              <select
                value={storage.existingStorage}
                onChange={(e) => updateStorage("existingStorage", e.target.value)}
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
                  placeholder="storage001"
                  onChange={(e) => updateStorage("name", e.target.value)}
                />
              </div>

              <div className="field">
                <label>Location</label>
                <select
                  value={storage.location}
                  onChange={(e) => updateStorage("location", e.target.value)}
                >
                  <option value="">Select</option>
                  {locations.map((location) => (
                    <option key={location.name} value={location.name}>
                      {location.display_name}
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
                  <option>StorageV2</option>
                  <option>BlobStorage</option>
                  <option>FileStorage</option>
                </select>
              </div>

              <div className="field">
                <label>SKU</label>
                <select
                  value={storage.sku}
                  onChange={(e) => updateStorage("sku", e.target.value)}
                >
                  <option>Standard_LRS</option>
                  <option>Standard_GRS</option>
                  <option>Standard_ZRS</option>
                  <option>Premium_LRS</option>
                </select>
              </div>

              <div className="field">
                <label>Access Tier</label>
                <select
                  value={storage.accessTier}
                  onChange={(e) => updateStorage("accessTier", e.target.value)}
                >
                  <option>Hot</option>
                  <option>Cool</option>
                </select>
              </div>

              <div className="field">
                <label>Minimum TLS Version</label>
                <select
                  value={storage.minimumTlsVersion}
                  onChange={(e) => updateStorage("minimumTlsVersion", e.target.value)}
                >
                  <option>TLS1_0</option>
                  <option>TLS1_1</option>
                  <option>TLS1_2</option>
                </select>
              </div>

              <div className="field full">
                <label>Large File Shares</label>
                <select
                  value={storage.largeFileSharesState}
                  onChange={(e) => updateStorage("largeFileSharesState", e.target.value)}
                >
                  <option>Disabled</option>
                  <option>Enabled</option>
                </select>
              </div>

              <div className="checkbox">
                <input
                  type="checkbox"
                  checked={storage.publicNetworkAccess}
                  onChange={(e) => updateStorage("publicNetworkAccess", e.target.checked)}
                />
                <label>Public Network Access</label>
              </div>

              <div className="checkbox">
                <input
                  type="checkbox"
                  checked={storage.secureTransferRequired}
                  onChange={(e) => updateStorage("secureTransferRequired", e.target.checked)}
                />
                <label>Secure Transfer Required</label>
              </div>

              <div className="checkbox">
                <input
                  type="checkbox"
                  checked={storage.allowBlobPublicAccess}
                  onChange={(e) => updateStorage("allowBlobPublicAccess", e.target.checked)}
                />
                <label>Allow Blob Public Access</label>
              </div>

              <div className="checkbox">
                <input
                  type="checkbox"
                  checked={storage.allowSharedKeyAccess}
                  onChange={(e) => updateStorage("allowSharedKeyAccess", e.target.checked)}
                />
                <label>Allow Shared Key Access</label>
              </div>
            </>
          )}
        </div>

        {/* ==========================================
              RESOURCE GROUP - ONLY SHOW WHEN CREATING NEW STORAGE
        ========================================== */}
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
                      placeholder="rg-demo"
                      onChange={(e) => updateResourceGroup("name", e.target.value)}
                    />
                  </div>

                  <div className="field">
                    <label>Location</label>
                    <select
                      value={resourceGroup.location}
                      onChange={(e) => updateResourceGroup("location", e.target.value)}
                    >
                      <option value="">Select</option>
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
          </>
        )}
      </div>

      <button className="next" onClick={handleNext}>
        Next
      </button>
    </div>
  );
}