from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import solvers,dashboard

# internal package
from database import engine
import models

app = FastAPI(title="CAPTCHA Solver")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}\

app.include_router(solvers.router)
app.include_router(dashboard.router)


