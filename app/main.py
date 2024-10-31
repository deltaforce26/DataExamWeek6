from flask import Flask

from app.db.database import session_maker
from app.db.models import City
from app.tests.test_connection import test_connection


app = Flask(__name__)


def get_cities():
    with session_maker() as session:
        cities = session.query(City).all()
        print(cities)

with app.app_context():
    test_connection()
    get_cities()


if __name__ == '__main__':
    app.run(debug=True)
