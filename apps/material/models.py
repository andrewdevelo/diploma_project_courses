from django.db import models
from apps.module.models import Module


class Material(models.Model):
    TYPES = (
        ('video', 'Video'),
        ('text', 'Text'),
        ('pdf', 'PDF'),
    )

    title = models.CharField(max_length=100)

    type_material = models.CharField(
        choices=TYPES)
    content_text = models.TextField(
        blank=True,
        null=True
    )
    content_file = models.FileField(
        upload_to='materials/',
        blank=True,
        null=True
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __str__(self):
        return self.title
