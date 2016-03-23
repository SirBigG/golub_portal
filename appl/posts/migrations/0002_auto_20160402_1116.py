# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 11:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classifier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='post publisher'),
        ),
        migrations.AddField(
            model_name='post',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Category', verbose_name='post category'),
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='posts.Post', verbose_name='post of photo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post', verbose_name='post of comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='comment owner'),
        ),
    ]
