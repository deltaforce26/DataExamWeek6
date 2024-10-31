from graphene import ObjectType, Int, String, Field

from app.db.database import session_maker
from app.db.models import Mission, City, TargetType


class TargetGraphQL(ObjectType):
    target_id = Int()
    target_industry = String()
    target_priority = Int()

    mission_id = Int()
    mission = Field("app.gql.types.mission_type.MissionType")

    city_id = Int()
    city = Field("app.gql.types.city_type.CityType")

    target_type_id = Int()
    target_type = Field("app.gql.types.target_type_graphql.TargetTypeGraphQL")


    @staticmethod
    def resolve_mission(root, info):
        with session_maker() as session:
            return session.query(Mission).filter(Mission.mission_id == root.mission_id).first()



    @staticmethod
    def resolve_city(root, info):
        with session_maker() as session:
            return session.query(City).filter(City.city_id == root.city_id).first()


    @staticmethod
    def resolve_target_type(root, info):
        with session_maker() as session:
            return session.query(TargetType).filter(TargetType.target_type_id == root.target_type_id).first()