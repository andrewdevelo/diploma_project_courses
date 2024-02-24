from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import (
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status

from apps.enrollment.models import Enrollment
from apps.enrollment.serializers import (
    AllEnrollmentSerializer,
)

from apps.enrollment.success_messages import (
    NEW_ENROLLMENT_CREATED_MESSAGE,
    ENROLLMENT_UPDATED_SUCCESSFULLY_MESSAGE,
    ENROLLMENT_WAS_DELETED_SUCCESSFUL
)


class EnrollmentListGenericView(ListCreateAPIView):
    serializer_class = AllEnrollmentSerializer

    def get_queryset(self):
        queryset = Enrollment.objects.select_related(
            'user',
            'course'
        )

        user_obj = self.request.query_params.get("user")
        course = self.request.query_params.get("course")

        if user_obj:
            queryset = queryset.filter(
                user=user_obj
            )
        if course:
            queryset = queryset.filter(
                course=course
            )

        return queryset

    def get(self, request: Request, *args, **kwargs):
        filtered_data = self.get_queryset()

        if filtered_data.exists():
            serializer = self.serializer_class(
                instance=filtered_data,
                many=True
            )

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "message": NEW_ENROLLMENT_CREATED_MESSAGE,
                "data": serializer.data
            }
        )


class RetrieveEnrollmentGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = AllEnrollmentSerializer

    def get_object(self):
        enrollment_id = self.kwargs.get("enrollment_id")

        enrollment = get_object_or_404(Enrollment, id=enrollment_id)

        return enrollment

    def get(self, request: Request, *args, **kwargs):
        enrollment = self.get_object()

        serializer = self.serializer_class(enrollment)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        enrollment = self.get_object()

        serializer = self.serializer_class(enrollment, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": ENROLLMENT_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        enrollment = self.get_object()

        enrollment.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=ENROLLMENT_WAS_DELETED_SUCCESSFUL
        )
