from typing import List
from fastapi import FastAPI, Depends, HTTPException
import crud
import schemas
import models
import database
from database import get_db, engine
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/get_transfers/{player_name}", response_model=schemas.PlayersOut)
def get_transfers(player_name: str, db: Session = Depends(get_db)):
    transfers = crud.get_player(db, player_name)
    return transfers


@app.get("/all_transfers/{player_name}", response_model=List[schemas.Transfers])
def get_transfers(player_name: str, db: Session = Depends(get_db)):
    transfers = crud.get_transfers(db, player_name)
    return transfers
