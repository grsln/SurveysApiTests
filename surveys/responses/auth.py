import allure
from pytest_voluptuous import S

from surveys.responses.base import BaseResponse
from surveys.schemas.schemas import SchemaLoginSuccessful, SchemaLoginUnsuccessful


class AuthSuccessful(BaseResponse):
    def token(self):
        return self.response.json()["access"]

    def assert_(self):
        with allure.step("Проверяем результат"):
            with allure.step("Проверка статус-кода ответа сервера"):
                assert self.status_code() == 200
            with allure.step("Проверка токена пользователя в ответе сервера"):
                assert self.token()
            with allure.step("Проверка схемы ответа сервера"):
                assert self.json == S(SchemaLoginSuccessful)


class AuthUnsuccessful(BaseResponse):
    def error(self):
        return self.response.json()["password"]

    def assert_(self):
        with allure.step("Проверяем результат"):
            with allure.step("Проверка статус-кода ответа сервера"):
                assert self.status_code() == 400
            with allure.step(
                "Проверка отсутствия токена пользователя в ответе сервера"
            ):
                assert self.error() == ["Это поле не может быть пустым."]
            with allure.step("Проверка схемы ответа сервера"):
                assert self.json == S(SchemaLoginUnsuccessful)
