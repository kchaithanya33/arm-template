import { Routes, Route } from "react-router-dom";

import ResourceGroup from "../components/resources/ResourceGroupSelector";
import Storage from "../pages/Storage";
import LogicApp from "../pages/LogicApp";
import FunctionApp from "../pages/FunctionApp";
import Payload from "../pages/Payload";
import Deploy from "../pages/Deploy";

export default function AppRoutes() {
  return (
    <Routes>

      {/* Start Page */}
      <Route
        path="/"
        element={<ResourceGroup />}
      />

      {/* Storage */}
      <Route
        path="/storage"
        element={<Storage />}
      />

      {/* Logic App */}
      <Route
        path="/logic-app"
        element={<LogicApp />}
      />

      {/* Function App */}
      <Route
        path="/function-app"
        element={<FunctionApp />}
      />

      {/* Payload */}
      <Route
        path="/payload"
        element={<Payload />}
      />

      {/* Deploy */}
      <Route
        path="/deploy"
        element={<Deploy />}
      />

    </Routes>
  );
}