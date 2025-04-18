from fastapi import FastAPI, Depends, HTTPException 
from typing import Annotated, List
from sqlalchemy.orm import Session 
from pydantic import BaseModel 
from database import SessionLocal, engine 
from fastapi.middleware.cors import CORSMiddleware
import models


app = FastAPI()

origins = [
    "http://localhost:3000"
]


app.add_middleware(CORSMiddleware, allow_origins=origins)

class TransactionBase(BaseModel):
    name: str
    value: float
    category: str
    reason: str
    date: str

class TransactionModel(TransactionBase):
    id: int 

def get_db():
    db = SessionLocal()
    try: 
        yield db 
    finally:
        db.close()



db_dependecy = Annotated[Session, Depends(get_db)]
models.Base.metadata.create_all(bind=engine)

@app.post("/transactions/", response_model = TransactionModel)
async def transactions(transaction: TransactionBase, db: db_dependecy):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get("/transactions/", response_model=List[TransactionModel])
async def read_transactions(db: db_dependecy, skip:int = 0, limit:int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions
