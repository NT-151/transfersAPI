from sqlalchemy import Column, Integer, String, BOOLEAN, BigInteger, VARCHAR, ForeignKey, Float, Date, Uuid
from database import Base


class Competitions(Base):
    __tablename__ = "competitions"

    competition_id = Column(VARCHAR(20), primary_key=True, nullable=False)
    competition_code = Column(VARCHAR(100), nullable=False)
    name = Column(VARCHAR(100), nullable=False)
    sub_type = Column(
        VARCHAR(100), nullable=False)
    country_id = Column(BigInteger, nullable=False)
    country_name = Column(VARCHAR(50))
    domestic_league_code = Column(VARCHAR(50))
    confederation = Column(VARCHAR(50), nullable=False)
    is_major_national_league = Column(BOOLEAN)


class Clubs(Base):
    __tablename__ = "clubs"

    club_id = Column(BigInteger, primary_key=True, nullable=False)
    club_code = Column(VARCHAR(100))
    name = Column(VARCHAR(100), unique=True)
    domestic_competition = Column(
        VARCHAR(20), ForeignKey('competitions.competition_id'))
    squad_size = Column(Integer)
    average_age = Column(Float)
    foreigners_number = Column(Float)
    foreigners_percentage = Column(Float)
    national_team_players = Column(Integer)
    stadium_name = Column(VARCHAR(100))
    stadium_seats = Column(Integer)
    net_transfer_record = VARCHAR(20)


class Player(Base):
    __tablename__ = 'players'
    player_id = Column(BigInteger, primary_key=True, nullable=False)
    first_name = Column(VARCHAR(100))
    last_name = Column(VARCHAR(100))
    name = Column(VARCHAR(100))
    last_season = Column(Integer)
    current_club_id = Column(BigInteger, ForeignKey('clubs.club_id'))
    player_code = Column(VARCHAR(100))
    country_of_birth = Column(VARCHAR(100))
    city_of_birth = Column(VARCHAR(100))
    country_of_citizenship = Column(VARCHAR(100))
    date_of_birth = Column(Date)
    sub_position = Column(VARCHAR(100))
    position = Column(VARCHAR(100))
    foot = Column(VARCHAR(100))
    height_in_cm = Column(Integer)
    image_url = Column(VARCHAR(500))
    url = Column(VARCHAR(500))
    current_club_domestic_competition_id = Column(
        VARCHAR(50), ForeignKey('competitions.competition_id'))
    market_value_in_eur = Column(Float)
    highest_market_value_in_eur = Column(Float)


class Transfers(Base):
    __tablename__ = 'transfers'

    player_id = Column(BigInteger, ForeignKey('players.player_id'))
    transfer_date = Column(Date)
    transfer_season = Column(VARCHAR(10))
    from_club_id = Column(BigInteger)
    to_club_id = Column(BigInteger)
    from_club_name = Column(VARCHAR(100))
    to_club_name = Column(VARCHAR(100))
    transfer_fee = Column(Float)
    market_value_in_eur = Column(Float)
    player_name = Column(VARCHAR(100))
    unique_id = Column(Uuid, primary_key=True, nullable=False)
