from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

from apps.course.success_messages import (
    NEW_COURSE_CREATED_MESSAGE,
    COURSE_UPDATED_SUCCESSFULLY_MESSAGE,
    COURSE_WAS_DELETED_SUCCESSFUL,
)
from apps.course.models import Course
from apps.course.serializers import (
    AllCourseSerializer,
)


class CourseListGenericView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllCourseSerializer
    queryset = Course.objects.all()

    def get(self, request: Request, *args, **kwargs):
        courses = self.get_queryset()

        if courses:
            serializer = self.serializer_class(courses, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        else:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "message": NEW_COURSE_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


class RetrieveCourseGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllCourseSerializer

    def get_object(self):
        course_id = self.kwargs.get("course_id")

        course = get_object_or_404(Course, id=course_id)

        return course

    def get(self, request: Request, *args, **kwargs):
        course = self.get_object()

        serializer = self.serializer_class(course)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        course = self.get_object()

        serializer = self.serializer_class(course, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": COURSE_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        course = self.get_object()

        course.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=COURSE_WAS_DELETED_SUCCESSFUL
        )


class CourseListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllCourseSerializer
    queryset = Course.objects.all()

    def get(self, request: Request, *args, **kwargs):
        courses = self.get_queryset()

        if courses:
            serializer = self.serializer_class(courses, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        else:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )
