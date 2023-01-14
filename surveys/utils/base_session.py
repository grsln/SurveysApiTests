from allure import step
from requests import Response, Session


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop("base_url")
        super().__init__()

    @step("Выполнен запрос {method} {url}")
    def request(self, method, url, **kwargs) -> Response:
        response = super().request(method, url=f"{self.base_url}{url}", **kwargs)
        return response
