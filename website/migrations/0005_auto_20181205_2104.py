# Generated by Django 2.1.3 on 2018-12-05 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20181205_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menclothes',
            name='accessory1',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory10',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory11',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory12',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory13',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory2',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory3',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory4',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory5',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory6',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory7',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory8',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='menclothes',
            name='accessory9',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color1',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color10',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color2',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color3',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color4',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color5',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color6',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color7',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color8',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='mencolor',
            name='color9',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory1',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory10',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory11',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory12',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory13',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory2',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory3',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory4',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory5',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory6',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory7',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory8',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='accessory9',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color1',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color10',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color2',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color3',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color4',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color5',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color6',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color7',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color8',
            field=models.CharField(default=None, max_length=7),
        ),
        migrations.AlterField(
            model_name='womencolor',
            name='color9',
            field=models.CharField(default=None, max_length=7),
        ),
    ]
