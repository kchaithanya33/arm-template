import { createContext, useContext, useEffect, useState } from "react";

const DeploymentContext = createContext();

const initialDeploymentData = {
  resourceGroup: {},
  storage: {},
  logicApp: {},
  functionApp: {},
};

export function DeploymentProvider({ children }) {
  // Load saved data once
  const [deploymentData, setDeploymentData] = useState(() => {
    const saved = localStorage.getItem("deploymentData");

    return saved
      ? JSON.parse(saved)
      : initialDeploymentData;
  });

  // Save whenever deploymentData changes
  useEffect(() => {
    localStorage.setItem(
      "deploymentData",
      JSON.stringify(deploymentData)
    );
  }, [deploymentData]);

  // Update one section
  function updateSection(section, data) {
    setDeploymentData((previous) => ({
      ...previous,
      [section]: data,
    }));
  }

  // Clear everything after successful deployment
  function clearDeployment() {
    setDeploymentData(initialDeploymentData);
    localStorage.removeItem("deploymentData");
  }

  return (
    <DeploymentContext.Provider
      value={{
        deploymentData,
        updateSection,
        clearDeployment,
      }}
    >
      {children}
    </DeploymentContext.Provider>
  );
}

export function useDeployment() {
  return useContext(DeploymentContext);
}