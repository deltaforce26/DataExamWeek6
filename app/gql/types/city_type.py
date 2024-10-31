from graphene import ObjectType, Int, String, Float


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    latitude = Float()
    longitude = Float()



