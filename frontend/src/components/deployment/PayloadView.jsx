import { useDeployment } from "../../context/DeploymentContext";
import { useNavigate } from "react-router-dom";

export default function PayloadView() {
  const navigate = useNavigate();

  const { deploymentData } = useDeployment();

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
          <pre>
            {JSON.stringify(deploymentData, null, 2)}
          </pre>
        </div>
      </div>

      <div className="button-row">
        <button
          className="next back-button"
          onClick={() => navigate("/function-app")}
        >
          Back
        </button>

        <button
          className="next"
          onClick={() => navigate("/deploy")}
        >
          Deploy
        </button>
      </div>
    </div>
  );
}