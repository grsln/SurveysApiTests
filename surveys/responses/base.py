from requests import Response


class BaseResponse:
    def __init__(self, response: Response):
        self.response = response
        self.json = response.json()

    def status_code(self):
        return self.response.status_code
