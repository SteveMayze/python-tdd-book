# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_auto_20190202_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_with', to=settings.AUTH_USER_MODEL),
        ),
    ]