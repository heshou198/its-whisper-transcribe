import src.connectors
from fastapi import FastAPI, UploadFile, File

app = FastAPI()
app.include_router(src.connectors.router)