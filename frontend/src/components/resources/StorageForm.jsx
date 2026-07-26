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



  // ==============================
  // Modes
  // ==============================

  const [storageMode,setStorageMode] =
    useState("create");


  const [resourceGroupMode,setResourceGroupMode] =
    useState("existing");




  // ==============================
  // Azure Data
  // ==============================

  const [locations,setLocations] =
    useState([]);


  const [storageAccounts,setStorageAccounts] =
    useState([]);


  const [resourceGroups,setResourceGroups] =
    useState([]);




  // ==============================
  // Storage
  // ==============================

  const [storage,setStorage] = useState({

    existingStorage:"",

    name:"",

    location:"",

    kind:"StorageV2",

    sku:"Standard_LRS",

    accessTier:"Hot",

    minimumTlsVersion:"TLS1_2",

  });




  // ==============================
  // Resource Group
  // ==============================

  const [resourceGroup,setResourceGroup] =
    useState({

      existing:"",

      name:"",

      location:""

    });





  // ==============================
  // Load Azure Data
  // ==============================

  useEffect(()=>{

    loadAzureData();

  },[]);




  async function loadAzureData(){


    try{


      const loc =
        await getLocationsApi();


      const storage =
        await getStorageAccountsApi();


      const rg =
        await getResourceGroupsApi();




      console.log("LOCATIONS",loc);

      console.log("STORAGE",storage);

      console.log("RESOURCE GROUPS",rg);



      setLocations(
        Array.isArray(loc)
        ? loc
        : []
      );



      setStorageAccounts(
        Array.isArray(storage)
        ? storage
        : []
      );



      setResourceGroups(
        Array.isArray(rg)
        ? rg
        : []
      );


    }

    catch(error){

      console.log(
        "Azure loading error",
        error
      );

    }

  }





  function updateStorage(field,value){


    setStorage(prev=>({

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





  function handleNext(){


    updateSection(
      "storage",
      {
        mode:storageMode,
        ...storage
      }
    );



    updateSection(
      "resourceGroup",
      {
        mode:resourceGroupMode,
        ...resourceGroup
      }
    );



    navigate("/logic-app");

  }






  return (

<div className="phone">


<div className="content">


<h2 className="logo">
ARM<span>Flow</span>
</h2>


<h1>
Create Your Own Template
</h1>


<p className="subtitle">
Configure Storage Account
</p>





{/* ==============================
 STORAGE ACCOUNT
================================ */}


<div className="section-title">
Storage Account
</div>



<div className="toggle">


<button

className={
storageMode==="create"
?"active":""
}

onClick={()=>setStorageMode("create")}

>

Create New

</button>



<button

className={
storageMode==="existing"
?"active":""
}

onClick={()=>setStorageMode("existing")}

>

Use Existing

</button>


</div>






<div className="form">





{
storageMode==="existing" &&

<div className="field full">

<label>
Storage Account
</label>


<select

value={storage.existingStorage}

onChange={
e=>
updateStorage(
"existingStorage",
e.target.value
)
}

>


<option value="">
Select Storage Account
</option>



{
storageAccounts.map(
(account)=>(

<option

key={account.name}

value={account.name}

>

{account.name}

</option>

)

)

}


</select>


</div>

}








{
storageMode==="create" &&

<>


<div className="field">

<label>
Storage Name
</label>


<input

value={storage.name}

onChange={
e=>
updateStorage(
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

value={storage.location}

onChange={
e=>
updateStorage(
"location",
e.target.value
)
}

>


<option>
Select Location
</option>


{
locations.map(
(loc)=>(

<option

key={loc.name}

value={loc.name}

>

{loc.display_name}

</option>

)

)

}


</select>


</div>






<div className="field">

<label>
Kind
</label>


<select

value={storage.kind}

onChange={
e=>
updateStorage(
"kind",
e.target.value
)
}

>


<option>
StorageV2
</option>


<option>
BlobStorage
</option>


<option>
FileStorage
</option>


</select>


</div>






<div className="field">


<label>
SKU
</label>


<select

value={storage.sku}

onChange={
e=>
updateStorage(
"sku",
e.target.value
)
}

>

<option>
Standard_LRS
</option>


<option>
Standard_GRS
</option>


<option>
Standard_ZRS
</option>


<option>
Premium_LRS
</option>


</select>


</div>






<div className="field">


<label>
Access Tier
</label>


<select

value={storage.accessTier}

onChange={
e=>
updateStorage(
"accessTier",
e.target.value
)
}

>

<option>
Hot
</option>


<option>
Cool
</option>


</select>


</div>






<div className="field">


<label>
Minimum TLS Version
</label>


<select

value={storage.minimumTlsVersion}

onChange={
e=>
updateStorage(
"minimumTlsVersion",
e.target.value
)
}

>

<option>
TLS1_2
</option>


<option>
TLS1_1
</option>


<option>
TLS1_0
</option>


</select>


</div>


</>

}


</div>









{/* ==============================
RESOURCE GROUP
================================ */}



{
storageMode==="create" &&


<>


<div className="section-title">

Resource Group

</div>




<div className="toggle">


<button

className={
resourceGroupMode==="create"
?"active":""
}

onClick={
()=>setResourceGroupMode("create")
}

>

Create New

</button>



<button

className={
resourceGroupMode==="existing"
?"active":""
}

onClick={
()=>setResourceGroupMode("existing")
}

>

Use Existing

</button>


</div>







<div className="form">


{

resourceGroupMode==="existing" &&


<div className="field full">


<label>
Resource Group
</label>


<select

value={resourceGroup.existing}

onChange={
e=>
updateResourceGroup(
"existing",
e.target.value
)
}

>


<option>
Select Resource Group
</option>



{

resourceGroups.map(
(rg)=>(

<option

key={rg.name}

value={rg.name}

>

{rg.name}

</option>


)

)

}


</select>


</div>


}








{

resourceGroupMode==="create" &&

<>


<div className="field">


<label>
Resource Group Name
</label>


<input

value={resourceGroup.name}

onChange={
e=>
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

onChange={
e=>
updateResourceGroup(
"location",
e.target.value
)
}

>


<option>
Select Location
</option>



{

locations.map(
(loc)=>(

<option

key={loc.name}

value={loc.name}

>

{loc.display_name}

</option>

)

)

}


</select>


</div>


</>


}



</div>


</>

}



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