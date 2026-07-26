import React, { useState } from "react";
import useDeployment from "../../hooks/useDeployment";
import { AZURE_REGIONS } from "../../utils/constants";

const ResourceGroupForm = () => {
  const { createResourceGroup, loading, error } = useDeployment();

  const [formData, setFormData] = useState({
    name: "",
    location: "",
  });

  const [success, setSuccess] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSuccess("");

    try {
      await createResourceGroup(formData);
      setSuccess("✅ Resource Group Created Successfully!");
      setFormData({ name: "", location: "" });
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <h3>Create Resource Group</h3>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Resource Group Name</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Location</label>
          <select
            name="location"
            value={formData.location}
            onChange={handleChange}
            required
          >
            <option value="">Select Region</option>
            {AZURE_REGIONS.map((region) => (
              <option key={region} value={region}>
                {region}
              </option>
            ))}
          </select>
        </div>

        <button type="submit" disabled={loading}>
          {loading ? "Creating..." : "Create"}
        </button>
      </form>

      {success && <p style={{ color: "green" }}>{success}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default ResourceGroupForm;