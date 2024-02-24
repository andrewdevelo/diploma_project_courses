from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAdminUser
)

from apps.module.success_messages import (
    NEW_MODULE_CREATED_MESSAGE,
    MODULE_UPDATED_SUCCESSFULLY_MESSAGE,
    MODULE_WAS_DELETED_SUCCESSFUL,
)
from apps.module.models import Module
from apps.module.serializers import (
    AllModulesSerializer,
)


class ModuleListGenericView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllModulesSerializer
    queryset = Module.objects.all()

    def get(self, request: Request, *args, **kwargs):
        modules = self.get_queryset()

        if modules:
            serializer = self.serializer_class(modules, many=True)

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
                    "message": NEW_MODULE_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


class RetrieveModuleGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllModulesSerializer

    def get_object(self):
        module_id = self.kwargs.get("module_id")

        module = get_object_or_404(Module, id=module_id)

        return module

    def get(self, request: Request, *args, **kwargs):
        module = self.get_object()

        serializer = self.serializer_class(module)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        module = self.get_object()

        serializer = self.serializer_class(module, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": MODULE_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        module = self.get_object()

        module.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=MODULE_WAS_DELETED_SUCCESSFUL
        )
