# Generated by Django 1.9.5 on 2016-04-27 15:12
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160402_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='image'),
        ),
    ]
