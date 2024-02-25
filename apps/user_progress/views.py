from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import (
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status

from apps.user_progress.models import UserProgress
from apps.user_progress.serializers import (
    AllUserProgressSerializer,
)
from rest_framework.permissions import IsAdminUser

from apps.user_progress.success_messages import (
    NEW_PROGRESS_CREATED_MESSAGE,
    PROGRESS_UPDATED_SUCCESSFULLY_MESSAGE,
    PROGRESS_WAS_DELETED_SUCCESSFUL
)


class UserProgressListGenericView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllUserProgressSerializer

    def get_queryset(self):
        queryset = UserProgress.objects.select_related(
            'user',
            'course',
            'module',
        )

        user_obj = self.request.query_params.get("user")
        course = self.request.query_params.get("course")
        module = self.request.query_params.get("module")

        if user_obj:
            queryset = queryset.filter(
                user=user_obj
            )
        if course:
            queryset = queryset.filter(
                course=course
            )
        if module:
            queryset = queryset.filter(
                module=module
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
                "message": NEW_PROGRESS_CREATED_MESSAGE,
                "data": serializer.data
            }
        )


class RetrieveUserProgressGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllUserProgressSerializer

    def get_object(self):
        progress_id = self.kwargs.get("progress_id")

        progress = get_object_or_404(UserProgress, id=progress_id)

        return progress

    def get(self, request: Request, *args, **kwargs):
        progress = self.get_object()

        serializer = self.serializer_class(progress)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        progress = self.get_object()

        serializer = self.serializer_class(progress, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": PROGRESS_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        progress = self.get_object()

        progress.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=PROGRESS_WAS_DELETED_SUCCESSFUL
        )
