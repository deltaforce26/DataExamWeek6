from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.models import Base


class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String)
    target_priority = Column(Integer)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))