import time
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = "mysql+pymysql://root:root@db:3306/transactiondb"

# Retry loop
for attempt in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("✅ Connected to MySQL.")
        break
    except OperationalError:
        print(f"⏳ Attempt {attempt + 1}/10: Waiting for MySQL to be ready...")
        time.sleep(3)
else:
    raise Exception("❌ Could not connect to MySQL after 10 attempts.")

# Continue setup
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from models import Transaction
Base.metadata.create_all(bind=engine)
