from fastapi import FastAPI

from .config import AppConfig

config = AppConfig()
app = FastAPI(root_path=config.URL_PREFIX)
