from concurrent import futures

import grpc

from exampels import course_service_pb2, course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):

    def GetCourse(self, request, context):
        title = "Автотесты API"
        description = "Будем изучать написание API автотестов"
        print(f"Получен запрос к методу GetCourses о курсе {request.course_id}")

        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title=title,
            description=description
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Сервер gRPC успешно запущен на порту 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
