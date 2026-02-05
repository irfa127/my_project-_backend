from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

# Create engine using DATABASE_URL from settings.
# If DATABASE_URL is None (e.g. build step), we can optionaly fallback or let it fail.
# On Render, DATABASE_URL will be set.
db_url = settings.DATABASE_URL
if not db_url:
    # Fallback for local testing if env var not set, or raise error. 
    # For now, let's allow a fallback but warn, or just use sqlite for safety if really needed.
    # But usually locally users have .env.
    print("Warning: DATABASE_URL not found in settings.")
    db_url = "sqlite:///./test.db"

engine = create_engine(db_url)
Base = declarative_base()
