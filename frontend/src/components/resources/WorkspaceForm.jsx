import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getLocationsApi } from "../../api/resourceApi";
import { useDeployment } from "../../context/DeploymentContext";

export default function WorkspaceForm() {
  const navigate = useNavigate();
  const { updateSection } = useDeployment();

  /*
  ======================================
      Azure Data
  ======================================
  */
  const [locations, setLocations] = useState([]);

  /*
  ======================================
      Workspace Mode
  ======================================
  */
  const [workspaceMode, setWorkspaceMode] = useState("create");

  /*
  ======================================
      Workspace
  ======================================
  */
  const [workspace, setWorkspace] = useState({
    name: "",
    location: "",
    sku: "PerGB2018",
    resourceGroup: {
      mode: "new",
      name: "",
      location: "",
    },
    retentionInDays: 30,
    tags: [],
  });

  /*
  ======================================
      Load Locations
  ======================================
  */
  useEffect(() => {
    loadLocations();
  }, []);

  async function loadLocations() {
    try {
      const data = await getLocationsApi();
      setLocations(data);
    } catch (error) {
      console.log(error);
    }
  }

  /*
  ======================================
      Workspace Update
  ======================================
  */
  function updateWorkspace(field, value) {
    setWorkspace((prev) => ({
      ...prev,
      [field]: value,
    }));
  }

  /*
  ======================================
      Resource Group Update
  ======================================
  */
  function updateResourceGroup(field, value) {
    setWorkspace((prev) => ({
      ...prev,
      resourceGroup: {
        ...prev.resourceGroup,
        [field]: value,
      },
    }));
  }

  /*
  ======================================
      Tags
  ======================================
  */
  function addTag() {
    setWorkspace((prev) => ({
      ...prev,
      tags: [
        ...prev.tags,
        {
          key: "",
          value: "",
        },
      ],
    }));
  }

  function updateTag(index, key, value) {
    setWorkspace((prev) => ({
      ...prev,
      tags: prev.tags.map((tag, i) =>
        i === index
          ? {
              ...tag,
              [key]: value,
            }
          : tag
      ),
    }));
  }

  function removeTag(index) {
    setWorkspace((prev) => ({
      ...prev,
      tags: prev.tags.filter((_, i) => i !== index),
    }));
  }

  /*
  ======================================
      Next
  ======================================
  */
  function next() {
    let finalWorkspace;
    if (workspaceMode === "existing") {
      finalWorkspace = {
        mode: "existing",
        name: workspace.name,
      };
    } else {
      finalWorkspace = {
        mode: "new",
        name: workspace.name,
        location: workspace.location,
        sku: workspace.sku,
        resourceGroup: {
          mode: workspace.resourceGroup.mode,
          name: workspace.resourceGroup.name,
          location:
            workspace.resourceGroup.mode === "create"
              ? workspace.resourceGroup.location
              : "",
        },
        retentionInDays: workspace.retentionInDays,
        tags: workspace.tags,
      };
    }

    updateSection("workspace", finalWorkspace);
    console.log("Workspace Saved", finalWorkspace);
    navigate("/");
  }

  function back() {
    navigate("/logic-app");
  }

  return (
    <div className="phone">
      <div className="back" onClick={back}>
        ←
      </div>

      <div className="content">
        <h2 className="logo">
          ARM<span>Flow</span>
        </h2>
        <h1>Workspace Setup</h1>
        <p className="subtitle">Define your log analytics workspace</p>

        {/* WORKSPACE MODE */}
        <div className="section-card">
          <h2 className="section-title">Workspace</h2>
          <div className="toggle">
            <button
              className={workspaceMode === "create" ? "active" : ""}
              onClick={() => setWorkspaceMode("create")}
            >
              Create New
            </button>
            <button
              className={workspaceMode === "existing" ? "active" : ""}
              onClick={() => setWorkspaceMode("existing")}
            >
              Use Existing
            </button>
          </div>

          <div className="form">
            {/* EXISTING WORKSPACE */}
            {workspaceMode === "existing" && (
              <div className="field">
                <label>Workspace Name</label>
                <input
                  value={workspace.name}
                  placeholder="law-existing"
                  onChange={(e) => updateWorkspace("name", e.target.value)}
                />
              </div>
            )}

            {/* CREATE WORKSPACE */}
            {workspaceMode === "create" && (
              <>
                <div className="field">
                  <label>Workspace Name</label>
                  <input
                    value={workspace.name}
                    placeholder="law-logicapp-01"
                    onChange={(e) => updateWorkspace("name", e.target.value)}
                  />
                </div>

                <div className="field">
                  <label>Location</label>
                  <select
                    value={workspace.location}
                    onChange={(e) => updateWorkspace("location", e.target.value)}
                  >
                    <option value="">Select Location</option>
                    {locations.map((loc, index) => (
                      <option key={index} value={loc.name || loc}>
                        {loc.display_name || loc}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="field">
                  <label>SKU</label>
                  <select
                    value={workspace.sku}
                    onChange={(e) => updateWorkspace("sku", e.target.value)}
                  >
                    <option value="PerGB2018">PerGB2018</option>
                  </select>
                </div>
              </>
            )}
          </div>
        </div>

        {/* WORKSPACE RESOURCE GROUP */}
        {workspaceMode === "create" && (
          <div className="section-card">
            <h2 className="section-title">Resource Group</h2>
            <div className="toggle">
              <button
                className={
                  workspace.resourceGroup.mode === "create" ? "active" : ""
                }
                onClick={() => updateResourceGroup("mode", "create")}
              >
                Create New
              </button>
              <button
                className={
                  workspace.resourceGroup.mode === "existing" ? "active" : ""
                }
                onClick={() => updateResourceGroup("mode", "existing")}
              >
                Use Existing
              </button>
            </div>

            <div className="form">
              {workspace.resourceGroup.mode === "existing" && (
                <div className="field">
                  <label>Existing Resource Group</label>
                  <input
                    value={workspace.resourceGroup.name}
                    placeholder="existing-rg"
                    onChange={(e) => updateResourceGroup("name", e.target.value)}
                  />
                </div>
              )}

              {workspace.resourceGroup.mode === "create" && (
                <>
                  <div className="field">
                    <label>Resource Group Name</label>
                    <input
                      value={workspace.resourceGroup.name}
                      placeholder="workspace-rg"
                      onChange={(e) => updateResourceGroup("name", e.target.value)}
                    />
                  </div>

                  <div className="field">
                    <label>Resource Group Location</label>
                    <select
                      value={workspace.resourceGroup.location}
                      onChange={(e) =>
                        updateResourceGroup("location", e.target.value)
                      }
                    >
                      <option value="">Select Location</option>
                      {locations.map((loc, index) => (
                        <option key={index} value={loc.name || loc}>
                          {loc.display_name || loc}
                        </option>
                      ))}
                    </select>
                  </div>
                </>
              )}
            </div>
          </div>
        )}

        {/* RETENTION */}
        {workspaceMode === "create" && (
          <div className="section-card">
            <h2 className="section-title">Retention</h2>
            <div className="field">
              <label>Retention In Days</label>
              <input
                type="number"
                value={workspace.retentionInDays}
                onChange={(e) =>
                  updateWorkspace("retentionInDays", Number(e.target.value))
                }
              />
            </div>
          </div>
        )}

        {/* TAGS */}
        {workspaceMode === "create" && (
          <div className="section-card">
            <h2 className="section-title">Tags</h2>
            {workspace.tags.map((tag, index) => (
              <div className="form" key={index}>
                <div className="field">
                  <label>Key</label>
                  <input
                    value={tag.key}
                    onChange={(e) => updateTag(index, "key", e.target.value)}
                  />
                </div>
                <div className="field">
                  <label>Value</label>
                  <input
                    value={tag.value}
                    onChange={(e) => updateTag(index, "value", e.target.value)}
                  />
                </div>
                <button type="button" onClick={() => removeTag(index)}>
                  Remove
                </button>
              </div>
            ))}

            <button type="button" className="next" onClick={addTag}>
              Add Tag
            </button>
          </div>
        )}
      </div>

      {/* FOOTER BUTTONS */}
      <div className="button-row">
        <button className="next back-button" onClick={back}>
          Back
        </button>
        <button className="next" onClick={next}>
          Next
        </button>
      </div>
    </div>
  );
}