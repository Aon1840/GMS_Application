# Generated by Django 2.0.3 on 2018-10-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Positions', '0003_auto_20180925_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='avg_x',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='position',
            name='avg_y',
            field=models.FloatField(default=0.0),
        ),
    ]
