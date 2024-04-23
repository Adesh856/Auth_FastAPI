from fastapi import FastAPI
import app
from . import models
from .db.database import engine
from .services.user.controller import router as userRouter  
# Create database tables based on models
try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    raise e


# # Initialize FastAPI app
app = FastAPI(
    title="Auth-App",  # Update with your desired title
    description="This is a custom API built with FastAPI.",
    version="1.0.0",
)



# Configure OAuth2 flow for Swagger UI

# # Include API router
app.include_router(userRouter)

# Root route
@app.get("/")
def read_items():
    """
    Root route handler.
    """
    return "FastAPI Server is running"