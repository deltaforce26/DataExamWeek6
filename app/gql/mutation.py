from graphene import ObjectType
from app.gql.mutations.mission_mutations import CreateMission


class Mutation(ObjectType):
    create_mission = CreateMission.Field()