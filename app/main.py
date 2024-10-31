from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from app.tests.test_connection import test_connection


app = Flask(__name__)

schema = Schema(query=Query)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
    )
)

with app.app_context():
    test_connection()



if __name__ == '__main__':
    app.run(debug=True)
