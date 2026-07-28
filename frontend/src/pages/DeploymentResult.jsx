import { useLocation, useNavigate } from "react-router-dom";

export default function DeployResult() {
  const navigate = useNavigate();
  const { state } = useLocation();

  const success =
    state?.success === true ||
    state?.status === "success" ||
    state?.deploymentStatus === "Succeeded";

  const title = success
    ? "Deployment Successful"
    : "Deployment Failed";

  const message = success
    ? state?.message ||
      "Your ARM template has been deployed successfully."
    : state?.detail ||
      state?.message ||
      state?.error ||
      "Something went wrong during deployment.";

  return (
    <div className="phone">
      <div className="content">

        <div
          style={{
            textAlign: "center",
            marginTop: 30,
          }}
        >
          <div
            style={{
              fontSize: 70,
            }}
          >
            {success ? "✅" : "❌"}
          </div>

          <h1>{title}</h1>

          <p
            style={{
              marginTop: 15,
              color: "#666",
              lineHeight: 1.6,
            }}
          >
            {message}
          </p>
        </div>

        {success && (
          <div
            style={{
              marginTop: 30,
              background: "#f4f8ff",
              padding: 15,
              borderRadius: 10,
              border: "1px solid #d8e6ff",
            }}
          >
            <h3>Deployment Summary</h3>

            <p>
              🎉 Your ARM template has been deployed successfully.
            </p>

            <p>
              Azure resources have been created and are ready to use.
            </p>
          </div>
        )}

        {!success && (
          <div
            style={{
              marginTop: 30,
              background: "#fff3f3",
              padding: 15,
              borderRadius: 10,
              border: "1px solid #ffbcbc",
            }}
          >
            <h3>Error Details</h3>

            <pre
              style={{
                whiteSpace: "pre-wrap",
                wordBreak: "break-word",
                fontSize: 13,
                color: "#b00020",
              }}
            >
              {JSON.stringify(state, null, 2)}
            </pre>
          </div>
        )}
      </div>

      <div className="button-row">
        <button
          className="next back-button"
          onClick={() => navigate("/")}
        >
          New Deployment
        </button>

        {!success && (
          <button
            className="next"
            onClick={() => navigate("/payload")}
          >
            Back
          </button>
        )}
      </div>
    </div>
  );
}