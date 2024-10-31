from sqlalchemy import Column, Integer, String, ForeignKey, Float

from app.db.models import Base


class City(Base):
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey('country.id'))
    latitude = Column(Float)
    longitude = Column(Float)
