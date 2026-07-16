from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.azure_routes import router as azure_router
from app.api.deploy_routes import router as deploy_router

app = FastAPI(
    title="ARM Deployment Portal API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Azure APIs
app.include_router(azure_router)

# Deployment APIs
app.include_router(deploy_router)

@app.get("/")
def root():
    return {
        "message": "ARM Deployment Portal API is running"
    }