from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as auth_router
from vectorstore.qdrant_store import create_qdrant_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")

# Initialize Qdrant collection
create_qdrant_collection()

@app.get("/")
async def root():
    return {"message": "Seva Portal API running"}

from fastapi import Body

@app.post("/evaluate")
def evaluate(user_payload: dict = Body(...)):
    from vectorstore.qdrant_store import evaluate_schemes
    schemes = evaluate_schemes(user_payload)
    return {"schemes": schemes}
