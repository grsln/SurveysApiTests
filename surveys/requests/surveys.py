import os

from allure import step
from requests import Response

from surveys.utils import attach
from surveys.utils.base_session import BaseSession


class Surveys:
    def __init__(self):
        self.surveys = BaseSession(base_url=os.getenv("API_URL"))

    @step("Выполнение авторизации")
    def login(self, login, password) -> Response:
        response = self.surveys.post(
            url="/auth/", json={"email": login, "password": password}
        )
        attach.add_body_request(response)
        attach.add_curl(response)
        attach.add_response(response)
        return response

    @step("Получаем токен авторизации")
    def get_token(self, login, password) -> str:
        response = self.surveys.post(
            url="/auth/", json={"email": login, "password": password}
        )
        attach.add_comment("Получен token", f'{response.json()["access"]}')
        return f'{response.json()["access"]}'

    @step("Добавление нового пользователя")
    def create_user(self, username, email, password) -> Response:
        response = self.surveys.post(
            url="/users/create/",
            json={"username": username, "email": email, "password": password},
        )
        attach.add_body_request(response)
        attach.add_curl(response)
        attach.add_response(response)
        return response

    @step("Выполняем изменение данных пользователя")
    def update_user(self, user_id, username, password, token) -> Response:
        response = self.surveys.patch(
            url=f"/users/{user_id}/",
            json={"username": username, "password": password},
            headers={"Authorization": f"JWT {token}"},
        )
        attach.add_body_request(response)
        attach.add_curl(response)
        attach.add_response(response)
        return response

    @step("Выполняем удаление пользователя")
    def delete_user(self, user_id, token) -> Response:
        response = self.surveys.delete(
            f"/users/{user_id}/", headers={"Authorization": f"JWT {token}"}
        )
        attach.add_curl(response)
        return response
