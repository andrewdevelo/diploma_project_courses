from rest_framework import serializers
import datetime
from apps.course.models import Course
from apps.user.models import User

from apps.course.error_messages import (
    TITLE_REQUIRED_ERROR_MESSAGE,
    TITLE_LENGTH_ERROR_MESSAGE,
    DESCRIPTION_LENGTH_ERROR_MESSAGE,
    INCORRECT_DATE_STARTED_ERROR_MESSAGE,
    INCORRECT_END_DATE_ERROR_MESSAGE,
)


def validate_fields(attrs):
    title = attrs.get('title')
    description = attrs.get('description')
    start_date = attrs.get('start_date')
    end_date = attrs.get('end_date')

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
    if start_date and start_date < datetime.date.today():
        raise serializers.ValidationError(
            INCORRECT_DATE_STARTED_ERROR_MESSAGE
        )
    if end_date and end_date < start_date:
        raise serializers.ValidationError(
            INCORRECT_END_DATE_ERROR_MESSAGE
        )

    return attrs


class AllCourseSerializer(serializers.ModelSerializer):
    instructor = serializers.SlugRelatedField(
        slug_field='last_name',
        queryset=User.objects.filter(is_instructor=True)
    )

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'start_date',
            'end_date',
            'instructor'
        ]

        def validate(self, attrs):
            return validate_fields(attrs=attrs)
