# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=128, unique=True, serialize=False, primary_key=True)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
