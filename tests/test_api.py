import allure
from allure_commons.types import Severity

from surveys.responses.auth import AuthSuccessful, AuthUnsuccessful
from surveys.responses.users import CreatedUser, DeletedUser, UpdatedUser


@allure.feature("Тесты Surveys API (https://surveys-biof.onrender.com)")
class TestUsers:
    @allure.tag("critical")
    @allure.severity(Severity.CRITICAL)
    @allure.story("Действия с пользователем")
    @allure.title("Добавление нового пользователя")
    def test_create_user(self, surveys, fake_user):
        username = fake_user["username"]
        email = fake_user["email"]
        password = fake_user["password"]
        response = surveys.create_user(username, email, password)
        CreatedUser(response).assert_(username, email)

    @allure.tag("critical")
    @allure.severity(Severity.BLOCKER)
    @allure.story("Авторизация пользователя")
    @allure.title("Успешная авторизация")
    def test_login_user(self, surveys, new_user):
        response = surveys.login(new_user["email"], new_user["password"])
        AuthSuccessful(response).assert_()

    @allure.tag("critical")
    @allure.severity(Severity.CRITICAL)
    @allure.story("Авторизация пользователя")
    @allure.title("Неуспешная авторизация. Не указан пароль")
    def test_login_unsuccessful(self, surveys, new_user):
        response = surveys.login(new_user["email"], "")
        AuthUnsuccessful(response).assert_()

    @allure.tag("critical")
    @allure.severity(Severity.CRITICAL)
    @allure.story("Действия с пользователем")
    @allure.title("Изменение данных пользователя")
    def test_update_user(self, surveys, admin_token, new_user):
        user_id = new_user["id"]
        username = f't_e_s_t_{new_user["username"]}'
        password = new_user["password"]
        response = surveys.update_user(user_id, username, password, admin_token)
        UpdatedUser(response).assert_(username)

    @allure.tag("critical")
    @allure.severity(Severity.CRITICAL)
    @allure.story("Действия с пользователем")
    @allure.title("Удаление пользователя")
    def test_delete_user(self, surveys, admin_token, new_user):
        user_id = new_user["id"]
        response = surveys.delete_user(user_id, admin_token)
        DeletedUser(response).assert_()
