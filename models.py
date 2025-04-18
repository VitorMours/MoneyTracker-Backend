from database import Base 
from sqlalchemy import Column, Integer, String, Boolean, Float 


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Float)
    category = Column(String)
    reason = Column(String)
    date = Column(String)