from rest_framework import serializers
from apps.module.models import Module
from apps.course.models import Course

from apps.module.errors_messages import (
    TITLE_REQUIRED_ERROR_MESSAGE,
    TITLE_LENGTH_ERROR_MESSAGE,
    DESCRIPTION_LENGTH_ERROR_MESSAGE
)


def validate_fields(attrs):
    title = attrs.get('title')
    description = attrs.get('description')

    if title is None:
        raise serializers.ValidationError(
            TITLE_REQUIRED_ERROR_MESSAGE
        )
    if title and len(title) > 100:
        raise serializers.ValidationError(
            TITLE_LENGTH_ERROR_MESSAGE
        )
    if description and len(description) > 1499:
        raise serializers.ValidationError(
            DESCRIPTION_LENGTH_ERROR_MESSAGE
        )

    return attrs


class AllModulesSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Course.objects.all()
    )

    class Meta:
        model = Module
        fields = [
            'id',
            'title',
            'description',
            'course'
        ]

    def validate(self, attrs):
        return validate_fields(attrs=attrs)
