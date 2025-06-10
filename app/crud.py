from sqlalchemy.orm import Session
from models import Player, Transfers


def get_transfers(db: Session, name: str):
    player_info = db.query(Player).filter(
        Player.name == name).first()
    if player_info:
        all_transfers = db.query(Transfers).filter(
            Transfers.player_id == player_info.player_id).all()
        return all_transfers
    return []
