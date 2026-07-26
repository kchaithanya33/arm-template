from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import deployment
from app.api import azure_resources
from app.api import delete
from app.api import history



# ======================================================
# Create FastAPI Application
# ======================================================

app = FastAPI(

    title="Azure ARM Deployment API",

    description=
    "API for deploying Azure resources using ARM templates",

    version="1.0.0"

)



# ======================================================
# CORS Configuration
# ======================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ],

)



# ======================================================
# Register Routers
# ======================================================


app.include_router(
    deployment.router
)


app.include_router(
    azure_resources.router
)


app.include_router(
    delete.router
)


app.include_router(
    history.router
)



# ======================================================
# Health Check
# ======================================================

@app.get("/")
def health_check():

    return {

        "status": "running",

        "message":
        "Azure Deployment Backend API is running"

    }



# ======================================================
# Application Startup
# ======================================================

@app.on_event("startup")
def startup_event():

    print(
        "================================"
    )

    print(
        "Azure Deployment API Started"
    )

    print(
        "================================"
    )



# ======================================================
# Application Shutdown
# ======================================================

@app.on_event("shutdown")
def shutdown_event():

    print(
        "Azure Deployment API Stopped"
    )