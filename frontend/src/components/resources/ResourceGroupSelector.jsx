import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getResourceGroupsApi,
  getLocationsApi,
} from "../../api/resourceApi";


export default function ResourceGroupSelector() {

  const [mode, setMode] = useState("create");

  const navigate = useNavigate();


  // ----------------------------
  // Azure Data
  // ----------------------------

  const [resourceGroups, setResourceGroups] = useState([]);

  const [locations, setLocations] = useState([]);


  // ----------------------------
  // Selected Values
  // ----------------------------

  const [resourceGroupName, setResourceGroupName] =
    useState("");

  const [location, setLocation] =
    useState("");


  // ----------------------------
  // Load Azure Data
  // ----------------------------

  useEffect(() => {

    loadAzureData();

  }, []);



  async function loadAzureData() {

    try {

      // temporary subscription id
      // later we will take this from login context

      const subscriptionId =
        "cc65e704-15de-4ddc-aa64-56973ac617f8";


      const groups =
        await getResourceGroupsApi(subscriptionId);


      const locationsList =
        await getLocationsApi(subscriptionId);



      setResourceGroups(groups);

      setLocations(locationsList);


    } catch(error) {

      console.error(
        "Azure loading error:",
        error
      );

    }

  }



  return (

    <div className="phone">


      <div className="back">
        ←
      </div>



      <div className="content">


        <h2 className="logo">
          ARM<span>Flow</span>
        </h2>


        <h1>
          Create Your Own Template
        </h1>


        <p className="subtitle">
          Define your own parameters
        </p>



        {/* Toggle */}

        <div className="toggle">


          <button
            className={
              mode === "create"
              ? "active"
              : ""
            }

            onClick={() =>
              setMode("create")
            }
          >
            Create New
          </button>



          <button
            className={
              mode === "existing"
              ? "active"
              : ""
            }

            onClick={() =>
              setMode("existing")
            }
          >
            Use Existing
          </button>


        </div>





        {/* Form */}

        <div className="form">


          <label>
            Resource Group Name
          </label>



          {
            mode === "create" ?


            (
              <input

                placeholder="rg-armflow-prod"

                value={resourceGroupName}

                onChange={(e)=>
                  setResourceGroupName(
                    e.target.value
                  )
                }

              />

            )


            :


            (

              <select

                value={resourceGroupName}

                onChange={(e)=>
                  setResourceGroupName(
                    e.target.value
                  )
                }

              >

                <option value="">
                  Select existing group...
                </option>


                {
                  resourceGroups.map((rg)=>(

                    <option
                      key={rg.name}
                      value={rg.name}
                    >
                      {rg.name}
                    </option>

                  ))
                }


              </select>

            )

          }





          {
            mode === "create" &&

            <>

              <label>
                Location
              </label>



              <select

                value={location}

                onChange={(e)=>
                  setLocation(
                    e.target.value
                  )
                }

              >

                <option value="">
                  Select Location
                </option>



                {
                  locations.map((loc)=>(

                    <option
                      key={loc.name}
                      value={loc.name}
                    >
                      {loc.display_name}
                    </option>

                  ))
                }


              </select>


            </>

          }


        </div>


      </div>





      <button

        className="next"

        onClick={() =>
          navigate("/storage")
        }

      >

        Next

      </button>


    </div>

  );

}