# Generated by Django 5.0.2 on 2024-02-22 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type_material', models.CharField(choices=[('video', 'Video'), ('text', 'Text'), ('pdf', 'PDF')], max_length=50)),
                ('content_text', models.TextField(blank=True, null=True)),
                ('content_file', models.FileField(blank=True, null=True, upload_to='materials/')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='module.module')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
            },
        ),
    ]
