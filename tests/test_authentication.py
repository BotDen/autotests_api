from http import HTTPStatus

import pytest

from api_client.authentication.authentication_client import get_authentication_client
from api_client.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from api_client.users.public_users_client import get_public_users_client
from api_client.users.user_schema import CreateUserRequestSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.authentication
@pytest.mark.regression
def test_login():
    public_client = get_public_users_client()

    create_request = CreateUserRequestSchema()
    create_response = public_client.create_user_api(create_request)
    assert_status_code(actual=create_response.status_code, expected=HTTPStatus.OK)

    authentication_user = LoginRequestSchema(
        email=create_request.email,
        password=create_request.password
    )
    authentication_client = get_authentication_client()
    auth_response = authentication_client.login_api(authentication_user)
    auth_response_data = LoginResponseSchema.model_validate_json(auth_response.text)

    assert_status_code(actual=auth_response.status_code, expected=HTTPStatus.OK)
    assert_login_response(auth_response_data)

    validate_json_schema(instance=auth_response.json(), schema=auth_response_data.model_json_schema())
