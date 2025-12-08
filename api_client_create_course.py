from api_client.courses.courses_client import CreateCourseRequestDict, get_private_courses_client
from api_client.files.files_client import UploadFileRequestDict, get_private_file_client
from api_client.private_http_builder import AuthenticationUserDict
from api_client.users.public_users_client import CreateUserRequestDict, get_public_users_client
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    firstName="string",
    lastName="string",
    middleName="string"
)

create_user_response = public_user_client.create_user(create_user_request)
print(create_user_response)

authentication_user = AuthenticationUserDict(
    email=create_user_request["email"],
    password=create_user_request["password"]
)
file_client = get_private_file_client(authentication_user)
course_client = get_private_courses_client(authentication_user)

create_file_request = UploadFileRequestDict(
    filename="chubaka.jpg",
    directory="courses",
    upload_file="./test_data/files/chubaka.jpg"
)
create_file_response = file_client.upload_file(create_file_request)

create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Course about Python by Chubaka",
    previewFileId=create_file_response["file"]["id"],
    createdByUserId=create_user_response["user"]["id"],
    estimatedTime="2 weeks"
)
create_course_response = course_client.create_course(create_course_request)
print(create_course_response)
