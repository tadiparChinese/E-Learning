# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 13:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20171012_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
