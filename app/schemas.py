import datetime
from pydantic import BaseModel
import uuid
from typing import Union


class Players(BaseModel):
    player_id: int
    first_name: str
    last_name: str
    name: str
    last_season: int
    current_club_id: int
    player_code: str
    country_of_birth: str
    city_of_birth: str
    country_of_citizenship: str
    date_of_birth: datetime.datetime
    sub_position: str
    position: str
    foot: str
    height_in_cm: int
    image_url: str
    url: str
    current_club_domestic_competition_id: str
    market_value_in_eur: float
    highest_market_value_in_eur: float


class Transfers(BaseModel):
    player_id: int
    transfer_date: datetime.datetime
    transfer_season: str
    from_club_id: int
    to_club_id: int
    from_club_name: str
    to_club_name: str
    transfer_fee: Union[float, None]
    market_value_in_eur: Union[float, None]
    player_name: str
    unique_id: uuid.UUID


class PlayersOut(Players):
    player_id: int

    class Config:
        # orm_mode = True
        from_attribute = True
