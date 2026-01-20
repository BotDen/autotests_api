from enum import Enum

class AllureFeature(str, Enum):
    USERS = "users"
    FILES = "files"
    COURSES = "courses"
    EXERCISES = "exercises"
    AUTHENTICATION = "authentication"
