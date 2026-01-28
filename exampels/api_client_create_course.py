from api_client.courses.course_schema import CreateCourseRequestSchema
from api_client.courses.courses_client import get_private_courses_client
from api_client.files.files_client import UploadFileRequestSchema, get_private_file_client
from api_client.private_http_builder import AuthenticationUserSchema
from api_client.users.public_users_client import get_public_users_client
from api_client.users.user_schema import CreateUserRequestSchema


public_user_client = get_public_users_client()
create_user_request = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request)
print(create_user_response)


authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
file_client = get_private_file_client(authentication_user)
course_client = get_private_courses_client(authentication_user)


create_file_request = UploadFileRequestSchema(
    upload_file="../test_data/files/chubaka.jpg"
)
create_file_response = file_client.upload_file(create_file_request)


create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id,
)
create_course_response = course_client.create_course(create_course_request)
print(create_course_response)
