from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routers import api
from app.intergrations.minio_client import ensure_bucket
from app.core.config import settings


# @asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_bucket(settings.MINIO_BUCKET)
    yield


app = FastAPI(title="Cookbook API", version="1.0", lifespan=lifespan)

app.include_router(api, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
