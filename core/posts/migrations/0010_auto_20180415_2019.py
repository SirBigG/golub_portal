# Generated by Django 2.0.3 on 2018-04-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20180318_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsedpost',
            name='hash',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
