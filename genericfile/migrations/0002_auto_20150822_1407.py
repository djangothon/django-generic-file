# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genericfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filestore',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', null=True),
        ),
        migrations.AlterField(
            model_name='filestore',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
