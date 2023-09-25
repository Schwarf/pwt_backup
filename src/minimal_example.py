from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configure your database connection string


# Create a FastAPI app
app = FastAPI()

# Define your SQLAlchemy model
Base = declarative_base()

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

# Create the database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# Create API endpoints to push entries into the database
@app.post("/entries/", response_model=Entry)
async def create_entry(entry: Entry):
    db_entry = Entry(**entry.dict())
    db = SessionLocal()
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    db.close()
    return db_entry

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
