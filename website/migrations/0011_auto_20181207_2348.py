# Generated by Django 2.1.3 on 2018-12-07 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20181207_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='mencolor',
            name='color10',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='mencolor',
            name='color9',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='womencolor',
            name='color10',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='womencolor',
            name='color9',
            field=models.CharField(default='', max_length=7),
        ),
    ]