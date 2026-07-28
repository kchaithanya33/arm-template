import { useDeployment } from "../../context/DeploymentContext";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

export default function PayloadView() {
  const navigate = useNavigate();

  const { deploymentData, clearDeployment } = useDeployment();

  const [loading, setLoading] = useState(false);

  async function handleDeploy() {
    try {
      setLoading(true);

      // Build payload expected by FastAPI
      const payload = {
        subscriptionId: "cc65e704-15de-4ddc-aa64-56973ac617f8",

        resourceGroup: {
          mode: deploymentData.resourceGroup.mode,
          name: deploymentData.resourceGroup.name,
          location: deploymentData.resourceGroup.location || null,
        },

        storage: {
          mode: deploymentData.storage.mode,

          name:
            deploymentData.storage.mode === "existing"
              ? deploymentData.storage.existingStorage
              : deploymentData.storage.name,

          location: deploymentData.storage.location || null,
          kind: deploymentData.storage.kind,
          sku: deploymentData.storage.sku,
          accessTier: deploymentData.storage.accessTier,
          minimumTlsVersion:
            deploymentData.storage.minimumTlsVersion,

          resourceGroup: {
            mode: deploymentData.resourceGroup.mode,
            name: deploymentData.resourceGroup.name,
            location:
              deploymentData.resourceGroup.location || null,
          },
        },

        logicApp: {
          mode: "new",
          name: deploymentData.logicApp.name,
          location: deploymentData.logicApp.location,

          resourceGroup: {
            mode:
              deploymentData.logicApp.resourceGroup.mode,

            name:
              deploymentData.logicApp.resourceGroup.name,

            location:
              deploymentData.logicApp.resourceGroup
                .location || null,
          },
        },

        functionApp: {
          name: deploymentData.functionApp.name,

          location: deploymentData.functionApp.location,

          runtimeStack:
            deploymentData.functionApp.runtimeStack,

          runtimeVersion:
            deploymentData.functionApp.runtimeVersion,

          functionPlanName:
            deploymentData.functionApp.hostingPlan,

          storageAccount: {
            mode:
              deploymentData.functionApp.storage.mode,

            name:
              deploymentData.functionApp.storage.mode ===
              "existing"
                ? deploymentData.functionApp.storage
                    .existingStorage
                : deploymentData.functionApp.storage.name,

            location:
              deploymentData.functionApp.storage.location ||
              null,
          },

          resourceGroup: {
            mode:
              deploymentData.functionApp.resourceGroup
                .mode,

            name:
              deploymentData.functionApp.resourceGroup
                .mode === "existing"
                ? deploymentData.functionApp
                    .resourceGroup.existing
                : deploymentData.functionApp
                    .resourceGroup.name,

            location:
              deploymentData.functionApp.resourceGroup
                .location || null,
          },
        },
      };

      console.log("Final Payload");
      console.log(JSON.stringify(payload, null, 2));

      const response = await axios.post(
        "http://localhost:8000/deployment/",
        payload
      );

      console.log(response.data);
      clearDeployment();
      navigate("/deploy", {
        state: {
    success: true,
    message:
      response.data?.message ||
      "Your ARM template has been deployed successfully.",
    data: response.data,
  },
});
    } catch (error) {
  console.error(error);

  const errorMessage =
    error.response?.data?.detail ||
    error.response?.data?.message ||
    error.message ||
    "Deployment Failed";

  navigate("/deploy", {
    state: {
      success: false,
      message: errorMessage,
      data: error.response?.data,
    },
  });
} finally {
      setLoading(false);
    }
  }

  return (
    <div className="phone">
      <div className="content">
        <div
          className="back"
          onClick={() => navigate("/function-app")}
        >
          ←
        </div>

        <h2 className="logo">
          ARM<span>Flow</span>
        </h2>

        <h1>Deployment Payload</h1>

        <p className="subtitle">
          Review all selected values before deployment.
        </p>

        <div
          style={{
            marginTop: 20,
            background: "#1f1f1f",
            color: "#fff",
            borderRadius: 8,
            padding: 15,
            maxHeight: "60vh",
            overflow: "auto",
            fontSize: 13,
          }}
        >
          <pre>{JSON.stringify(payloadPreview(), null, 2)}</pre>
        </div>
      </div>

      <div className="button-row">
        <button
          className="next back-button"
          onClick={() => navigate("/function-app")}
          disabled={loading}
        >
          Back
        </button>

        <button
          className="next"
          onClick={handleDeploy}
          disabled={loading}
        >
          {loading ? "Deploying..." : "Deploy"}
        </button>
      </div>
    </div>
  );

  function payloadPreview() {
    return {
      subscriptionId: "cc65e704-15de-4ddc-aa64-56973ac617f8",

      resourceGroup: deploymentData.resourceGroup,

      storage: {
        ...deploymentData.storage,
        name:
          deploymentData.storage.mode === "existing"
            ? deploymentData.storage.existingStorage
            : deploymentData.storage.name,
      },

      logicApp: {
        mode: "new",
        ...deploymentData.logicApp,
      },

      functionApp: {
        ...deploymentData.functionApp,

        functionPlanName:
          deploymentData.functionApp.hostingPlan,

        storageAccount: {
          ...deploymentData.functionApp.storage,

          name:
            deploymentData.functionApp.storage?.mode ===
            "existing"
              ? deploymentData.functionApp.storage
                  ?.existingStorage
              : deploymentData.functionApp.storage?.name,
        },
      },
    };
  }
}