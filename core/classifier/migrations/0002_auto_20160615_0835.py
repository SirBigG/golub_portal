# Generated by Django 1.9.7 on 2016-06-15 08:35
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='area_region', to='classifier.Region', verbose_name='area region'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='is_for_user',
            field=models.BooleanField(default=False, verbose_name='user relation for post category'),
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='location latitude'),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='location longitude'),
        ),
        migrations.AddField(
            model_name='region',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='region_country', to='classifier.Country', verbose_name='region country'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='area',
            name='value',
            field=models.CharField(max_length=250, verbose_name='area value'),
        ),
        migrations.AlterField(
            model_name='area',
            name='value_en',
            field=models.CharField(max_length=250, null=True, verbose_name='area value'),
        ),
        migrations.AlterField(
            model_name='area',
            name='value_uk',
            field=models.CharField(max_length=250, null=True, verbose_name='area value'),
        ),
    ]
