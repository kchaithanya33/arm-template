import { useState } from "react";

import BasicsStep from "./steps/BasicsStep";
import ResourcesStep from "./steps/ResourcesStep";
import ReviewStep from "./steps/ReviewStep";
import DeploymentStep from "./steps/DeploymentStep";

function DeploymentWizard() {
  const [step, setStep] = useState(1);

  const [data, setData] = useState({
    resourceGroup: "",
    location: "",

    storageAccountName: "",
    applicationInsightsName: "",
    appServicePlanName: "",
    functionAppName: "",
    logicAppName: "",
  });

  return (
    <div>
      <h2>Create Deployment</h2>

      <hr />

      {step === 1 && (
        <BasicsStep
          data={data}
          setData={setData}
        />
      )}

      {step === 2 && (
        <ResourcesStep
          data={data}
          setData={setData}
        />
      )}

      {step === 3 && (
        <ReviewStep
          data={data}
        />
      )}

      {step === 4 && (
        <DeploymentStep
          data={data}
        />
      )}

      <br />
      <br />

      {step > 1 && (
        <button onClick={() => setStep(step - 1)}>
          Back
        </button>
      )}

      {" "}

      {step < 3 && (
        <button onClick={() => setStep(step + 1)}>
          Next
        </button>
      )}

      {" "}

      {step === 3 && (
        <button onClick={() => setStep(4)}>
          Create
        </button>
      )}
    </div>
  );
}

export default DeploymentWizard;