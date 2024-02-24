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

from apps.material.success_messages import (
    NEW_MATERIAL_CREATED_MESSAGE,
    MATERIAL_UPDATED_SUCCESSFULLY_MESSAGE,
    MATERIAL_WAS_DELETED_SUCCESSFUL,
)
from apps.material.models import Material
from apps.material.serializers import (
    AllMaterialSerializer,
)


class MaterialListGenericView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllMaterialSerializer
    queryset = Material.objects.all()

    def get(self, request: Request, *args, **kwargs):
        materials = self.get_queryset()

        if materials:
            serializer = self.serializer_class(materials, many=True)

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
                    "message": NEW_MATERIAL_CREATED_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )


class RetrieveMaterialGenericView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AllMaterialSerializer

    def get_object(self):
        material_id = self.kwargs.get("material_id")

        material = get_object_or_404(Material, id=material_id)

        return material

    def get(self, request: Request, *args, **kwargs):
        material = self.get_object()

        serializer = self.serializer_class(material)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        material = self.get_object()

        serializer = self.serializer_class(material, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data={
                    "message": MATERIAL_UPDATED_SUCCESSFULLY_MESSAGE,
                    "data": serializer.data
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )

    def delete(self, request, *args, **kwargs):
        material = self.get_object()

        material.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=MATERIAL_WAS_DELETED_SUCCESSFUL
        )
