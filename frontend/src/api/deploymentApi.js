import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export async function deployTemplate(data) {
  const response = await API.post("/deployment/", data);
  return response.data;
}