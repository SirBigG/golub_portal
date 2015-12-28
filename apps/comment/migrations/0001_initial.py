# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 09:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(verbose_name='object id')),
                ('text', models.TextField(verbose_name='comment text')),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.IntegerField(choices=[(0, 'Not active'), (1, 'Active')], default=1, verbose_name='comment status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='comment author')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type of object')),
            ],
            options={
                'db_table': 'comments',
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
