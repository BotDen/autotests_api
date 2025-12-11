from http import HTTPStatus

import pytest

from api_client.users.public_users_client import get_public_users_client
from api_client.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.user import assert_create_user_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user_with_valid_data():
    public_client = get_public_users_client()

    request = CreateUserRequestSchema()
    response = public_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_create_user_response(request, response_data)

    validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
