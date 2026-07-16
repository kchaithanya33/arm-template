import { useEffect, useState } from "react";
import { getResourceGroups, getLocations } from "../../api/azureApi";

function BasicsStep({ data, setData }) {
  const [groups, setGroups] = useState([]);
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const rg = await getResourceGroups();
      const loc = await getLocations();

      console.log("RG =", rg);
      console.log("Locations =", loc);

      setGroups(rg);
      setLocations(loc);
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
      <h2>Basics</h2>

      <label>Resource Group</label>
      <br />

      <select
        name="resourceGroup"
        value={data.resourceGroup}
        onChange={change}
      >
        <option value="">Select</option>

        {groups.map((g) => (
          <option key={g.name} value={g.name}>
            {g.name}
          </option>
        ))}
      </select>

      <br />
      <br />

      <label>Location</label>
      <br />

      <select
        name="location"
        value={data.location}
        onChange={change}
      >
        <option value="">Select</option>

        {locations.map((l) => (
          <option key={l.name} value={l.name}>
            {l.display_name}
          </option>
        ))}
      </select>
    </div>
  );
}

export default BasicsStep;