from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
 

# Create engine using DATABASE_URL from settings. If DATABASE_URL is None,
# fall back to a sqlite in-memory database to avoid immediate import errors.
db_url = "postgresql://postgres:AcademyRootPassword@localhost:5432/elder_connect_project" 
engine = create_engine(db_url)
Base = declarative_base()
