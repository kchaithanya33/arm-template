import { createContext, useContext, useState } from "react";


const DeploymentContext = createContext();



const getInitialState = () => ({

  resourceGroup: {},

  storage: {},

  logicApp: {},

  applicationInsights: {},

  workspace: {},

  appServicePlan: {},

  functionApp: {},

});





export function DeploymentProvider({children}) {


  const [
    deploymentData,
    setDeploymentData
  ] = useState(
    getInitialState()
  );




  function updateSection(section,data){


    setDeploymentData(previous => ({

      ...previous,

      [section]: data,

    }));

  }





  function resetDeployment(){


    setDeploymentData(
      getInitialState()
    );


  }





  return (

    <DeploymentContext.Provider

      value={{

        deploymentData,

        updateSection,

        resetDeployment,

      }}

    >

      {children}

    </DeploymentContext.Provider>

  );

}





export function useDeployment(){

  return useContext(
    DeploymentContext
  );

}