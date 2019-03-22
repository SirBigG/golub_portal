# Generated by Django 2.0.8 on 2019-01-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20181104_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.CharField(max_length=255, verbose_name='fingerprint')),
                ('post_id', models.IntegerField(verbose_name='post identifier')),
                ('user_id', models.IntegerField(blank=True, null=True, verbose_name='user identifier')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='classifier.Tag', verbose_name='past tags'),
        ),
    ]