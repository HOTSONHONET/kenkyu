from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import router
import json


def create_app():
    """
    
    Function to return a FastAPI instance
    
    """

    # Collecting version info
    version_mapper = json.load(open("version_info.cfg", "r"))

    # Creating an FastAPI Instance
    app = FastAPI(
        title = "kenkyu",
        version = version_mapper["version_num"],
        description = version_mapper["version_description"]
    )

    # Integrating CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )


    # Integrating Router
    app.include_router(router)

    return app