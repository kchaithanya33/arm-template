import json
import os

from datetime import datetime



HISTORY_FILE = (
    "logs/deployment_history.json"
)



# ======================================================
# Get Deployment History
# ======================================================

def get_history():


    if not os.path.exists(
        HISTORY_FILE
    ):

        return []


    with open(
        HISTORY_FILE,
        "r"
    ) as file:

        history = json.load(file)



    return history





# ======================================================
# Save Deployment History
# ======================================================

def save_history(
        deployment_data: dict
):


    os.makedirs(
        "logs",
        exist_ok=True
    )


    history = []


    if os.path.exists(
        HISTORY_FILE
    ):

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            history = json.load(file)



    deployment_data["created_at"] = (
        datetime.utcnow().isoformat()
    )



    history.append(
        deployment_data
    )



    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )



    return deployment_data