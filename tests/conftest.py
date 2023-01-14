import os

import pytest
from dotenv import load_dotenv
from faker import Faker

from surveys.requests.surveys import Surveys

load_dotenv()
ADMIN = os.getenv("SURVEYS_API_ADMIN")
PASSWORD = os.getenv("SURVEYS_API_PASSWORD")


@pytest.fixture(scope="session")
def surveys():
    yield Surveys()


@pytest.fixture()
def admin_token(surveys):
    token = surveys.get_token(ADMIN, PASSWORD)
    return token


@pytest.fixture()
def fake_user():
    fake = Faker()
    username = fake.name()
    email = fake.email()
    password = fake.password()
    return {"username": username, "email": email, "password": password}


@pytest.fixture()
def new_user(surveys, fake_user):
    response = surveys.create_user(**fake_user)
    user_id = response.json()["id"]
    yield {**fake_user, "id": user_id}
    token = surveys.get_token(ADMIN, PASSWORD)
    surveys.delete_user(user_id, token)
