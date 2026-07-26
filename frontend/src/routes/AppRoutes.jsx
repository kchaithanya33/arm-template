import { Routes, Route } from "react-router-dom";

import Deploy from "../pages/Deploy";
import Storage from "../pages/Storage";
import LogicApp from "../pages/LogicApp";
import Workspace from "../pages/Workspace";


export default function AppRoutes() {

  return (

    <Routes>


      {/* Resource Group */}
      <Route
        path="/"
        element={<Deploy />}
      />



      {/* Storage Account */}
      <Route
        path="/storage"
        element={<Storage />}
      />



      {/* Logic App */}
      <Route
        path="/logic-app"
        element={<LogicApp />}
      />



      {/* Workspace */}
      <Route
        path="/workspace"
        element={<Workspace />}
      />


    </Routes>

  );

}