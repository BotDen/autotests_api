from api_client.courses.course_schema import CreateCourseRequestSchema
from api_client.courses.courses_client import get_private_courses_client
from api_client.exercises.exercise_schema import CreateExerciseRequestSchema
from api_client.exercises.exercises_client import get_private_exercises_client
from api_client.files.file_schema import UploadFileRequestSchema
from api_client.files.files_client import get_private_file_client
from api_client.private_http_builder import AuthenticationUserSchema
from api_client.users.public_users_client import get_public_users_client
from api_client.users.user_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    first_name="string",
    last_name="string",
    middle_name="string"
)

create_user_response = public_user_client.create_user(create_user_request)
print(create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

file_client = get_private_file_client(authentication_user)
course_client = get_private_courses_client(authentication_user)
exercise_client = get_private_exercises_client(authentication_user)

create_file_request = UploadFileRequestSchema(
    filename="chubaka.jpg",
    directory="courses",
    upload_file="./test_data/files/chubaka.jpg"
)
create_file_response = file_client.upload_file(create_file_request)

create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,
    min_score=10,
    description="Course about Python by Chubaka",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id,
    estimated_time="2 weeks"
)
create_course_response = course_client.create_course(create_course_request)
print(create_course_response)

create_exercise_request = CreateExerciseRequestSchema(
    title="Pyton",
    course_id=create_course_response.course.id,
    max_score=100,
    min_score=10,
    order_index=1,
    description="Pyton by Chubaka",
    estimated_time="2 weeks",
)
create_exercise_request = exercise_client.create_exercise(create_exercise_request)
print(create_exercise_request)
