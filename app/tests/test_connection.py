from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import session_maker



def test_connection():
    try:
        with session_maker() as session:
            session.execute(text('SELECT 1'))
            print('\n\n----------- Connection successful !')
    except SQLAlchemyError as e:
        print('\n\n----------- Connection failed ! ERROR : ', e)