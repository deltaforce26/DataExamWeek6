from graphene import ObjectType, Int, String, Float, Field

from app.db.database import session_maker
from app.db.models import Country


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    latitude = Float()
    longitude = Float()

    country_id = Int()
    country = Field("app.gql.types.country_type.CountryType")

    @staticmethod
    def resolve_country(root, info):
        with session_maker() as session:
            return (session
                    .query(Country)
                    .filter(Country.country_id == root.country_id)
                    .first())


