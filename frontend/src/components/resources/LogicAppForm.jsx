
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getLocationsApi,
  getResourceGroupsApi,
} from "../../api/resourceApi";

import { useDeployment } from "../../context/DeploymentContext";


export default function LogicAppForm() {


  const navigate = useNavigate();

  const { deploymentData, updateSection } = useDeployment();



  /*
  ==========================================
      Azure Data
  ==========================================
  */

  const [locations, setLocations] = useState([]);

  const [resourceGroups, setResourceGroups] = useState([]);



  /*
  ==========================================
      Resource Group Mode
  ==========================================
  */

  const [resourceGroupMode, setResourceGroupMode] = useState(() => {
  if (deploymentData.logicApp?.resourceGroup?.mode === "new") {
    return "create";
  }
  return deploymentData.logicApp?.resourceGroup?.mode || "existing";
});


  /*
  ==========================================
      Logic App
  ==========================================
  */

  const [logicApp, setLogicApp] = useState(
  deploymentData.logicApp || {
    mode: "new",
    name: "",
    location: "",
  }
);



  /*
  ==========================================
      Resource Group
  ==========================================
  */

  const [resourceGroup, setResourceGroup] = useState({
  existing:
    deploymentData.logicApp?.resourceGroup?.mode === "existing"
      ? deploymentData.logicApp?.resourceGroup?.name || ""
      : "",

  name:
  deploymentData.logicApp?.resourceGroup?.mode !== "existing"
  ? deploymentData.logicApp?.resourceGroup?.name || ""
  : "",

  location:
    deploymentData.logicApp?.resourceGroup?.location || "",
});



  /*
  ==========================================
      Load Azure Data
  ==========================================
  */


  useEffect(() => {

    loadAzureResources();

  }, []);



  async function loadAzureResources(){

    try{


      const locationData =
        await getLocationsApi();


      const rgData =
        await getResourceGroupsApi();



      setLocations(locationData);

      setResourceGroups(rgData);



    }
    catch(error){

      console.log(error);

    }

  }




  /*
  ==========================================
      Update Handlers
  ==========================================
  */


  function updateLogicApp(field,value){

    setLogicApp(prev=>({

      ...prev,

      [field]:value

    }));

  }



  function updateResourceGroup(field,value){

    setResourceGroup(prev=>({

      ...prev,

      [field]:value

    }));

  }

  /*
==========================================
    Preserve Data Until Deploy
==========================================
*/




  /*
  ==========================================
      Next
  ==========================================
  */


  function handleNext() {

  const finalData = {

    mode: "new",

    name: logicApp.name,

    location: logicApp.location,

    resourceGroup: {

      mode:
        resourceGroupMode === "create"
          ? "new"
          : "existing",

      ...(resourceGroupMode === "existing"
        ? {
            name: resourceGroup.existing,
          }
        : {
            name: resourceGroup.name,
            location: resourceGroup.location,
          }),
    },
  };

  updateSection(
    "logicApp",
    finalData
  );

  console.log(
    "Logic App Saved",
    finalData
  );

  navigate("/function-app");
}





return (

<div className="phone">


<div className="content">







<h2 className="logo">

ARM<span>Flow</span>

</h2>


<h1>Create Your Own Template</h1>


<p className="subtitle">

Configure Logic App

</p>





{/* ==================================
        LOGIC APP
================================== */}


<div className="section-card">


<h2 className="section-title">

Logic App

</h2>



<div className="form">



<div className="field">


<label>

Logic App Name

</label>



<input

value={logicApp.name}

placeholder="logic-demo"

onChange={(e)=>
updateLogicApp(
"name",
e.target.value
)
}

/>


</div>





<div className="field">


<label>

Location

</label>



<select


value={logicApp.location}


onChange={(e)=>
updateLogicApp(
"location",
e.target.value
)
}

>


<option value="">

Select Location

</option>



{
locations.map(location=>(

<option

key={location.name}

value={location.name}

>

{location.display_name}

</option>


))

}


</select>


</div>



</div>


</div>









{/* ==================================
        RESOURCE GROUP
================================== */}



<div className="section-card">


<h2 className="section-title">

Resource Group

</h2>




<div className="toggle">


<button

className={
resourceGroupMode==="create"
?
"active"
:
""
}


onClick={()=>
setResourceGroupMode("create")
}

>

Create New

</button>





<button

className={
resourceGroupMode==="existing"
?
"active"
:
""
}


onClick={()=>
setResourceGroupMode("existing")
}

>

Use Existing

</button>



</div>





<div className="form">





{
resourceGroupMode==="existing"

&&

<div className="field">


<label>

Resource Group

</label>



<select


value={resourceGroup.existing}


onChange={(e)=>

updateResourceGroup(
"existing",
e.target.value
)

}


>


<option value="">

Select Resource Group

</option>



{

resourceGroups.map(group=>(


<option

key={group.name}

value={group.name}

>


{group.name}


</option>


))

}



</select>



</div>


}







{
resourceGroupMode==="create"

&&

<>


<div className="field">


<label>

Resource Group Name

</label>


<input


value={resourceGroup.name}


placeholder="logic-rg"


onChange={(e)=>

updateResourceGroup(
"name",
e.target.value
)

}


/>


</div>





<div className="field">


<label>

Resource Group Location

</label>



<select


value={resourceGroup.location}


onChange={(e)=>

updateResourceGroup(
"location",
e.target.value
)

}


>


<option value="">

Select Location

</option>


{

locations.map(location=>(


<option

key={location.name}

value={location.name}

>

{location.display_name}

</option>


))

}



</select>



</div>


</>



}





</div>


</div>




</div>





<div className="button-row">


<button

className="next back-button"

onClick={()=>navigate("/storage")}

>

Back

</button>




<button

className="next"

onClick={handleNext}

>

Next

</button>



</div>



</div>


);


}