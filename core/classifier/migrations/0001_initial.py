# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 11:16
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, verbose_name='transliteration value')),
                ('value', models.CharField(max_length=250, unique=True, verbose_name='area value')),
                ('value_uk', models.CharField(max_length=250, null=True, unique=True, verbose_name='area value')),
                ('value_en', models.CharField(max_length=250, null=True, unique=True, verbose_name='area value')),
            ],
            options={
                'db_table': 'area',
                'verbose_name': 'area',
                'verbose_name_plural': 'area',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, unique=True, verbose_name='transliteration value')),
                ('value', models.CharField(max_length=250, verbose_name='category value')),
                ('value_uk', models.CharField(max_length=250, null=True, verbose_name='category value')),
                ('value_en', models.CharField(max_length=250, null=True, verbose_name='category value')),
                ('icon', models.CharField(blank=True, max_length=250, null=True, verbose_name='category icon')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='classifier.Category', verbose_name='category parent')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, verbose_name='transliteration value')),
                ('short_slug', models.CharField(max_length=5, verbose_name='short slug')),
                ('value', models.CharField(max_length=250, unique=True, verbose_name='country value')),
                ('value_uk', models.CharField(max_length=250, null=True, unique=True, verbose_name='country value')),
                ('value_en', models.CharField(max_length=250, null=True, unique=True, verbose_name='country value')),
            ],
            options={
                'db_table': 'country',
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, verbose_name='transliteration value')),
                ('value', models.CharField(max_length=250, verbose_name='location value')),
                ('value_uk', models.CharField(max_length=250, null=True, verbose_name='location value')),
                ('value_en', models.CharField(max_length=250, null=True, verbose_name='location value')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Area', verbose_name='area')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Country', verbose_name='country')),
            ],
            options={
                'db_table': 'location',
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, verbose_name='transliteration value')),
                ('value', models.CharField(max_length=250, unique=True, verbose_name='region value')),
                ('value_uk', models.CharField(max_length=250, null=True, unique=True, verbose_name='region value')),
                ('value_en', models.CharField(max_length=250, null=True, unique=True, verbose_name='region value')),
            ],
            options={
                'db_table': 'region',
                'verbose_name': 'region',
                'verbose_name_plural': 'region',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifier.Region', verbose_name='region'),
        ),
    ]
