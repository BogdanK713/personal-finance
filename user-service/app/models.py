from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)  # ✅ Add length
    email = Column(String(100), unique=True, nullable=False)  # ✅ Add length
    password_hash = Column(String(255), nullable=False)  # ✅ Add length

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
