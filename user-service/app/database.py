import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from app.models import Base  # ✅ Make sure this comes after Base is defined in models.py

DATABASE_URL = "mysql+pymysql://root:root@db:3306/userdb"

# Retry connection
for attempt in range(10):
    try:
        engine = create_engine(DATABASE_URL, echo=True)
        connection = engine.connect()
        connection.close()
        print("✅ Connected to MySQL (userdb).")
        break
    except OperationalError:
        print(f"⏳ Attempt {attempt + 1}/10: Waiting for MySQL to be ready...")
        time.sleep(3)
else:
    raise Exception("❌ Could not connect to MySQL (userdb) after 10 attempts.")

# Setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Auto-create tables
Base.metadata.create_all(bind=engine)
