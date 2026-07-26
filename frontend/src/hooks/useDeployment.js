import { useContext } from "react";
import { DeploymentContext } from "../context/DeploymentContext";

export default function useDeployment() {
  return useContext(DeploymentContext);
}