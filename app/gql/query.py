from graphene import ObjectType, Field, Int, List, Date, String
from sqlalchemy import and_
from app.db.database import session_maker
from app.db.models import Mission, Target, City, Country
from app.gql.types.mission_type import MissionType



class Query(ObjectType):
    mission_by_id = Field(MissionType, mission_id=Int())
    missions_by_date_range = List(MissionType, start_date=Date(), end_date=Date())
    missions_by_target_industry = List(MissionType, target_industry=String())
    mission_by_country = List(MissionType, country=String())


    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        with session_maker() as session:
            return (session
                    .query(Mission)
                    .filter(Mission.mission_id == mission_id)
                    .first())



    @staticmethod
    def resolve_missions_by_date_range(root, info, start_date, end_date):
        with session_maker() as session:
            return (session
                    .query(Mission)
                    .filter(and_(Mission.mission_date >= start_date, Mission.mission_date <= end_date))
                    .all())



    @staticmethod
    def resolve_missions_by_target_industry(root, info, target_industry):
        with session_maker() as session:
            return (session
                    .query(Mission)
                    .join(Target, Target.mission_id == Mission.mission_id)
                    .filter(Target.target_industry == target_industry)
                    .all())


    @staticmethod
    def resolve_mission_by_country(root, info, country):
        with session_maker() as session:
            return (session
                    .query(Mission)
                    .join(Target, Target.mission_id == Mission.mission_id)
                    .join(City, City.city_id == Target.city_id)
                    .join(Country, Country.country_id == City.country_id)
                    .filter(Country.country_name == country)
                    .all())
