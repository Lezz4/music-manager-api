from fastapi import FastAPI
from api.routes import router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from db.models import Base
from sqlalchemy import create_engine

# Database setup
DATABASE_URL = "sqlite:///./music_manager.db"  # SQLite for simplicity
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Music Manager API", description="A simple and clean API for managing music tracks.")

# Enable CORS for frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
