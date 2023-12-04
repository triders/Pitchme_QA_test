from typing import Optional, Union

import requests


class SocialMediaAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.default_headers = {"Content-type": "application/json; charset=UTF-8"}

    def get(
        self, endpoint: str, expected_status_code: Optional[int] = None
    ) -> Union[dict, list]:
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint

        response = requests.get(
            url=self.base_url + endpoint, headers=self.default_headers
        )

        if expected_status_code:
            assert (
                response.status_code == expected_status_code
            ), f"Expected status code ='{expected_status_code}', but request to '{self.base_url + endpoint}' returned '{response.status_code}', response body: \n'{response.text}'"

        result_json = response.json()
        return result_json


class Users(SocialMediaAPI):

    GET_USERS = "/users"
    GET_USER_BY_ID = "/user/{user_id}"

    def __init__(self, social_media_api: SocialMediaAPI):
        super().__init__(base_url=social_media_api.base_url)

    def get_user(
        self, user_id: int, expected_status_code: Optional[int] = None
    ) -> dict:
        return self.get(
            self.GET_USER_BY_ID.format(user_id=user_id),
            expected_status_code=expected_status_code,
        )

    def get_users(self, expected_status_code: Optional[int] = None) -> list[dict]:
        return self.get(self.GET_USERS, expected_status_code=expected_status_code)
