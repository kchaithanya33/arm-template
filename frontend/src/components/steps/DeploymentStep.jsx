import {useEffect,useState} from "react";

import {deployTemplate}
from "../../api/azureApi";


function DeploymentStep({data}){


const [status,setStatus]=useState(
"Starting deployment..."
);



useEffect(()=>{


deployTemplate(data)

.then(()=>{

setStatus(
"Deployment Completed Successfully"
);

})


.catch(()=>{

setStatus(
"Deployment Failed"
);

});


},[]);



return(

<div>

<h2>
Deployment
</h2>


<h3>
{status}
</h3>


</div>


)

}


export default DeploymentStep;