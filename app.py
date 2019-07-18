from flask import Flask
from flask_graphql import GraphQLView

# from schema import schema
from instance.config import app_config


def create_app(config_name):
    """Factory initialization for the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # app.add_url_rule(
    #     '/api',
    #     view_func=GraphQLView.as_view(
    #         'api',
    #         schema=schema,
    #         graphiql=True   # for having the GraphiQL interface
    #     )
    # )

    return app
