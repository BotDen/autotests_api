import pytest
from pydantic import EmailStr

from api_client.base_pydantic_model import BasePydanticModel
from api_client.private_http_builder import AuthenticationUserSchema
from api_client.users.private_users_client import PrivateUsersClient, get_private_users_client
from api_client.users.public_users_client import PublicUsersClient, get_public_users_client
from api_client.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BasePydanticModel):
    request: CreateUserRequestSchema
    resource: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self):
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def public_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture
def function_user(public_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_client.create_user(request)
    return UserFixture(request=request, resource=response)


@pytest.fixture
def private_user_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)
