from graphene import Mutation, Int, String, Field, InputObjectType, Boolean
from sqlalchemy import func
from app.db.database import session_maker
from app.db.models import  Target
from app.gql.types.target_graphql import TargetGraphQL


class DeleteTarget(Mutation):
    class Arguments:
        target_id = Int(required=True)

    success = Boolean()
    target = Field(TargetGraphQL)


    @staticmethod
    def mutate(root, info, target_id):
        with session_maker() as session:
            deleted_target = (session
                              .query(Target)
                              .filter_by(id=target_id)
                              .delete())
            return DeleteTarget(success=True, target=deleted_target)



class TargetInput(InputObjectType):
    target_id = Int()
    target_industry = String()
    target_priority = Int()
    mission_id = Int()
    city_id = Int()
    target_type_id = Int()


class CreateTarget(Mutation):
    class Arguments:
        target_input = TargetInput()

    success = Boolean()
    target = Field(TargetGraphQL)


    @staticmethod
    def mutate(root, info, target_input):
        with session_maker() as session:
            new_target = Target(
                target_id = session.query(func.max(Target.target_id)).scalar() + 1,
                target_industry = target_input.target_industry,
                target_priority = target_input.target_priority,
                mission_id = target_input.mission_id,
                city_id = target_input.city_id,
                target_type_id = target_input.target_type_id
            )
            session.add(new_target)
            session.commit()
            session.refresh(new_target)
            return CreateTarget(success=True, target=new_target)
