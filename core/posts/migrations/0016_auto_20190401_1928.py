# Generated by Django 2.0.8 on 2019-04-01 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author_uk',
        ),
        migrations.RemoveField(
            model_name='post',
            name='source_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='source_uk',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text_uk',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_uk',
        ),
    ]
