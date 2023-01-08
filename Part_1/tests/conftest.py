""" import pytest
from app import app as test_app

@pytest.fixture()
def app():
        yield test_app

@pytest.fixture()
def client(app):
     return app.test_client() """


import pytest
import connexion

flask_app = connexion.FlaskApp(__name__)
flask_app.add_api("../swagger.yml")

@pytest.fixture(scope='module')
def client():
        with flask_app.app.test_client() as x:
                yield x
