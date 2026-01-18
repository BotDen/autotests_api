from http import HTTPStatus

from fixtures.users import UserFixture
from tools.fakers import fake

import pytest

from api_client.users.private_users_client import PrivateUsersClient
from api_client.users.public_users_client import PublicUsersClient
from api_client.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.user import assert_create_user_response, assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
class TestUser:
    @pytest.mark.parametrize("email", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user_with_valid_data(self, email: str, public_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.get_email(domain=email))
        response = public_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


    def test_get_user_me(
        self,
        private_user_client: PrivateUsersClient,
        function_user: UserFixture,
    ):
        response = private_user_client.get_user_me_api()
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        response_schema = GetUserResponseSchema.model_validate_json(response.text)
        assert_get_user_response(response_schema, function_user.response)

        validate_json_schema(instance=response.json(), schema=response_schema.model_json_schema())
