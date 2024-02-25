from rest_framework import serializers
from apps.user.models import User
from apps.course.models import Course
from apps.module.models import Module
from apps.user_progress.models import UserProgress


class AllUserProgressSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.filter(
            is_instructor=False,
            is_staff=False
        )
    )
    course = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Course.objects.all()
    )
    module = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Module.objects.all()
    )

    class Meta:
        model = UserProgress
        fields = [
            'id',
            'user',
            'course',
            'module',
            'progress',
            'last_update'
        ]


