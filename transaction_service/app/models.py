from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50))
    category = Column(String(50))
    amount = Column(Float)
    type = Column(String(20))
    date = Column(String(20))
