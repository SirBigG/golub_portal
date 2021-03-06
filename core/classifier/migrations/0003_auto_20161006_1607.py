# Generated by Django 1.9.9 on 2016-10-06 16:07
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_metadata'),
        ('classifier', '0002_auto_20160615_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='for feel on off'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category-meta-data+', to='services.MetaData', verbose_name='category meta data'),
        ),
    ]
