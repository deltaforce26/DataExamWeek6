from graphene import ObjectType, Int, Date, Float, List
from app.db.database import session_maker
from app.db.models import Target
from app.gql.types.target_graphql import TargetGraphQL



class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()

    targets = List(TargetGraphQL)



    @staticmethod
    def resolve_targets(root, info):
        with session_maker() as session:
            return session.query(Target).filter(Target.mission_id == root.mission_id).all()

