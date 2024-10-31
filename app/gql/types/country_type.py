from graphene import ObjectType, Int, String, List
from app.db.database import session_maker
from app.db.models import City


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()

    cities = List("app.gql.types.city_type.CityType")


    @staticmethod
    def resolve_cities(root, info):
        with session_maker() as session:
            cities = (session
                      .query(City)
                      .filter(City.country_id == root.country_id)
                      .all())
            return cities