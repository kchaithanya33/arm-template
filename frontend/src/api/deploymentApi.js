const BASE_URL = "http://localhost:5000/api"; // change if needed

export const createResourceGroupApi = async (data) => {
  try {
    const response = await fetch(`${BASE_URL}/resource-group`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Failed to create resource group");
    }

    return await response.json();
  } catch (error) {
    throw error;
  }
};