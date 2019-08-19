import json
import unittest

from graphene.test import Client
from alembic import command, config

from app import create_app
from schema import schema
from helpers.database import Base, engine, db_session
from api.user.models import User


class TestConfiguration(unittest.TestCase):
    alembic_configuration = config.Config("./alembic.ini")

    def create_app(self):
        app = create_app('testing')
        self.base_url = 'https://127.0.0.1:5000/api'
        self.headers = {'content-type': 'application/json'}
        self.client = Client(schema)
        return app

    def setUp(self):
        app = self.create_app()
        self.app_test = app.test_client()

        with app.app_context():
            Base.metadata.create_all(bind=engine)
            command.stamp(self.alembic_configuration, 'head')
            command.downgrade(self.alembic_configuration, '-1')
            command.upgrade(self.alembic_configuration, 'head')

            user = User(name="Ken", password="1234567")
            user.save()
            db_session.commit()

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            command.stamp(self.alembic_configuration, 'base')
            db_session.remove()
            Base.metadata.drop_all(bind=engine)


class CommonTestCases(TestConfiguration):
    def get_response(self, query, expected_response):
        response = self.app_test.post(
            '/api?query=' + query)
        actual_response = json.loads(response.data)
        self.assertEqual(actual_response, expected_response)
