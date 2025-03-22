from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base  # ✅ Import Base AFTER defining it in models.py

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/userdb"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Create tables automatically
Base.metadata.create_all(bind=engine)
