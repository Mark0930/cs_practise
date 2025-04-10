from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@db:5432/sampledb"

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/sampledb"

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@postgres-service:5432/sampledb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# if __name__ == "__main__":
#     db = get_db()
#     print(db)
    
