from fastapi import FastAPI
from api.routes.router import router
from api.routes.administration import administration_router

app = FastAPI()

app.include_router(router)
app.include_router(administration_router)