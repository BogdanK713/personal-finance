from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/transactiondb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 👇 Model import and table creation after Base is declared
from transaction_service.app.models import Transaction

# 👇 Create all tables
Base.metadata.create_all(bind=engine)
