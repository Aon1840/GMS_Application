# Generated by Django 2.0.3 on 2018-08-26 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Floors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('zone_id', models.AutoField(primary_key=True, serialize=False)),
                ('zone_name', models.CharField(max_length=10)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Floors.Floor')),
            ],
            options={
                'ordering': ('-zone_id',),
            },
        ),
    ]
