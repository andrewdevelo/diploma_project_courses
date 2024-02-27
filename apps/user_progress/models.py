from django.db import models
from apps.user.models import User
from apps.course.models import Course
from apps.module.models import Module
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)


class UserProgress(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    progress = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    last_update = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'UserProgress'
        verbose_name_plural = 'UserProgresses'


