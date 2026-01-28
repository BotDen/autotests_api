from api_client.users.public_users_client import get_public_users_client
from api_client.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema


public_user_client = get_public_users_client()
create_user_request = CreateUserRequestSchema()

create_user_response = public_user_client.create_user_api(create_user_request)
create_user_json_schema = CreateUserResponseSchema.model_json_schema()
validate_json_schema(instance=create_user_response.json(), schema=create_user_json_schema)
