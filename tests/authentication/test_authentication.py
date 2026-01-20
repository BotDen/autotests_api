from http import HTTPStatus

import allure
import pytest

from api_client.authentication.authentication_client import AuthenticationClient
from api_client.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.title("Login with valid credentials")
    @allure.tag(AllureTag.VALIDATE_ENTITY)
    @allure.story(AllureStory.LOGIN)
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        authentication_user = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password,
        )
        response = authentication_client.login_api(authentication_user)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
