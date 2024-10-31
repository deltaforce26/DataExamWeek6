from graphene import Mutation, Date, Float, Field, Boolean, InputObjectType, String, Int
from sqlalchemy import func
from app.db.database import session_maker
from app.db.models import Mission
from app.gql.types.mission_type import MissionType


class MissionInput(InputObjectType):
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()


class CreateMission(Mutation):
    class Arguments:
        mission_input = MissionInput()


    success = Boolean()
    mission = Field(MissionType)



    @staticmethod
    def mutate(root, info, mission_input):
        with session_maker() as session:
            new_mission = Mission(
                mission_id=session.query(func.max(Mission.mission_id)).scalar() + 1,
                mission_date=mission_input.mission_date,
                airborne_aircraft=mission_input.airborne_aircraft,
                attacking_aircraft=mission_input.attacking_aircraft,
                bombing_aircraft=mission_input.bombing_aircraft,
                aircraft_returned=mission_input.aircraft_returned,
                aircraft_failed=mission_input.aircraft_failed,
                aircraft_damaged=mission_input.aircraft_damaged,
                aircraft_lost=mission_input.aircraft_lost
            )
            session.add(new_mission)
            session.commit()
            session.refresh(new_mission)
            return CreateMission(success=True, mission=new_mission)


class UpdateMissionResult(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        mission_input = MissionInput()

    success = Boolean()
    mission = Field(MissionType)

    @staticmethod
    def mutate(info, mission_id, mission_input):
        with session_maker() as session:
            mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            if not mission:
                raise Exception("Mission not found")
            if mission_input.aircraft_damaged:
                mission.aircraft_damaged = mission_input.aircraft_damaged
            if mission_input.aircraft_lost:
                mission.aircraft_lost = mission_input.aircraft_lost
            if mission_input.aircraft_failed:
                mission.aircraft_failed = mission_input.aircraft_failed
            if mission_input.aircraft_returned:
                mission.aircraft_returned = mission_input.aircraft_returned
            session.commit()
            session.refresh(mission)
            return UpdateMissionResult(success=True, mission=mission)

