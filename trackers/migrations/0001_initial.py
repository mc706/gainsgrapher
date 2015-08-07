# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('value', models.DecimalField(max_digits=9, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('description', models.TextField(help_text=b'How to take track', max_length=255)),
                ('units', models.CharField(max_length=64, choices=[(b'in', b'Inches'), (b'lbs', b'Pounds'), (b'ft', b'Feet'), (b's', b'Seconds'), (b'u', b'Units')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='tracker',
            field=models.ForeignKey(to='trackers.Tracker'),
        ),
    ]
