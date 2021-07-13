# Generated by Django 3.2.5 on 2021-07-13 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Update')),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='weather.basemodel')),
                ('location', models.CharField(max_length=20, verbose_name='location')),
                ('loc_time', models.DateTimeField(verbose_name='location time')),
                ('temperature', models.FloatField(verbose_name='temperature')),
                ('weather_icons', models.CharField(max_length=255, verbose_name='weather icons')),
            ],
            options={
                'verbose_name': 'weather',
                'verbose_name_plural': 'weathers',
                'ordering': ('location',),
            },
            bases=('weather.basemodel',),
        ),
    ]