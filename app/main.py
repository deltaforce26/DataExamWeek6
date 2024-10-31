from flask import Flask
from app.tests.test_connection import test_connection

app = Flask(__name__)




with app.app_context():
    test_connection()


if __name__ == '__main__':
    app.run(debug=True)
