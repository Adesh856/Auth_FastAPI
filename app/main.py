from fastapi import FastAPI
from . import models
from .db.database import engine
from .services.auth.controller import router as userRouter
# Create database tables based on models
try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    raise e

# # Initialize FastAPI app
app = FastAPI()

# # Include API router
app.include_router(userRouter)

# Root route
@app.get("/")
def read_items():
    """
    Root route handler.
    """
    return "FastAPI Server is running"