from rest_framework import serializers
from apps.user.models import User
from apps.course.models import Course
from apps.enrollment.models import Enrollment


class AllEnrollmentSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Enrollment
        fields = [
            'id',
            'user',
            'course',
            'enrollment_date',
            'status'
        ]