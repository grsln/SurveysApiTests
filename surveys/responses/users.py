import allure
from pytest_voluptuous import S

from surveys.responses.base import BaseResponse
from surveys.schemas.schemas import SchemaCreateUser, SchemaUpdateUser


class CreatedUser(BaseResponse):
    def username(self):
        return self.response.json()["username"]

    def email(self):
        return self.response.json()["email"]

    def assert_(self, username, email):
        with allure.step("Проверка результата"):
            with allure.step("Проверка статус-кода ответа сервера"):
                assert self.status_code() == 201, "Статус код создания не 201"
            with allure.step("Проверка имени пользователя в ответе сервера"):
                assert self.username() == username, "username не поменялся"
            with allure.step("Проверка email пользователя в ответе сервера"):
                assert self.email() == email, "email не поменялся"
            with allure.step("Проверка схемы ответа сервера"):
                assert self.json == S(
                    SchemaCreateUser
                ), "Ошибка проверки схемы SchemaCreateUser"


class UpdatedUser(BaseResponse):
    def username(self):
        return self.response.json()["username"]

    def assert_(self, new_username):
        with allure.step("Проверяем результат"):
            with allure.step("Проверка статус-кода ответа сервера"):
                assert self.status_code() == 200, "Статус код обновления не 200"
            with allure.step("Проверка имени пользователя в ответе сервера"):
                assert self.username() == new_username, "username не поменялся"
            with allure.step("Проверка схемы ответа сервера"):
                assert self.json == S(
                    SchemaUpdateUser
                ), "Ошибка проверки схемы SchemaUpdateUser"


class DeletedUser(BaseResponse):
    def assert_(self):
        with allure.step("Проверяем результат"):
            with allure.step("Проверка статус-кода ответа сервера"):
                assert self.status_code() == 200, "Статус код удаления не 200"
