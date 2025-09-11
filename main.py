from fastapi import FastAPI , HTTPException , status
from routers import solvers
app = FastAPI(title="CAPTCHA Solver")

@app.get("/")
async def root():
    return {"message": "Hello World"}\

app.include_router(solvers.router)


