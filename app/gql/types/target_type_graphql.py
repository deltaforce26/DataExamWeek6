from graphene import ObjectType, Int, String, List
from app.db.database import session_maker
from app.db.models import TargetType, Target
from app.gql.types.target_graphql import TargetGraphQL


class TargetTypeGraphQL(ObjectType):
    target_type_id = Int()
    target_type_name = String()

    targets = List(TargetGraphQL)


    @staticmethod
    def resolve_targets(root, info):
        with session_maker() as session:
            return session.query(Target).filter(Target.target_type_id == root.target_type_id).all()

