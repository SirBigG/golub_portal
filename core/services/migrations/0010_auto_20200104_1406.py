# Generated by Django 3.0.2 on 2020-01-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20191019_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name="Email (необов'язково)"),
        ),
    ]
