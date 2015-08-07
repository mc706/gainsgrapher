# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0002_auto_20150731_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='uuid',
            field=uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='uuid',
            field=uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True),
        ),
    ]
