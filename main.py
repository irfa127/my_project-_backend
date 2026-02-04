import sys
import os

# Add parent directory to path to ensure 'app' package is resolvable
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import Base, engine
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
frontend_path = os.path.join(project_root, "frontend")


if os.path.exists(frontend_path):
   
    print(f"Mounting frontend from: {frontend_path}")
else:
    print(f"Frontend directory not found at: {frontend_path}") 




from routers import (
    auth, 
    users,
    appointments,
    vitals,
    communities,
    inquiries,
    reviews,
)

app = FastAPI(title="ElderConnect API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if os.path.exists(frontend_path):
    app.mount("/frontend", StaticFiles(directory=frontend_path, html=True), name="frontend")


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(appointments.router)
app.include_router(vitals.router)
app.include_router(communities.router)
app.include_router(inquiries.router)
app.include_router(reviews.router)


@app.get("/")
async def root():
    return {"message": "Welcome to ElderConnect API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


