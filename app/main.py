from typing import List
from fastapi import FastAPI, Depends
import crud
import schemas
from database import get_db
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/all_transfers/{player_name}", response_model=List[schemas.Transfers])
def get_transfers(player_name: str, db: Session = Depends(get_db)):
    transfers = crud.get_transfers(db, player_name)
    return transfers
