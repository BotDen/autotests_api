from api_client.private_http_builder import AuthenticationUserSchema
from api_client.users.private_users_client import get_private_users_client
from api_client.users.public_users_client import get_public_users_client
from api_client.users.user_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema


public_user_client = get_public_users_client()
create_user_request = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request)


login_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

private_user_client = get_private_users_client(login_user)

get_user = private_user_client.get_user_api(create_user_response.user.id)
get_user_json = GetUserResponseSchema.model_json_schema()
validate_json_schema(instance=get_user.json(), schema=get_user_json)

