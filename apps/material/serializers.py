from rest_framework import serializers
from apps.material.models import Material
from apps.module.models import Module

from apps.material.error_messages import (
    TITLE_REQUIRED_ERROR_MESSAGE,
    TITLE_LENGTH_ERROR_MESSAGE,
    CONTENT_TEXT_LENGTH_ERROR_MESSAGE
)


def validate_fields(attrs):
    title = attrs.get('title')
    content_text = attrs.get('content_text')

    if title is None:
        raise serializers.ValidationError(
            TITLE_REQUIRED_ERROR_MESSAGE
        )
    if title and len(title) > 100:
        raise serializers.ValidationError(
            TITLE_LENGTH_ERROR_MESSAGE
        )
    if content_text and len(content_text) > 1499:
        raise serializers.ValidationError(
            CONTENT_TEXT_LENGTH_ERROR_MESSAGE
        )

    return attrs


class AllMaterialSerializer(serializers.ModelSerializer):
    module = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Module.objects.all()
    )

    class Meta:
        model = Material
        fields = [
            'id',
            'title',
            'type_material',
            'content_text',
            'module'
        ]

    def validate(self, attrs):
        return validate_fields(attrs=attrs)
