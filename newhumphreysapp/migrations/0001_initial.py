# Generated by Django 4.0.5 on 2023-02-13 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('length', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('latitude', models.DecimalField(decimal_places=7, default=0, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='BusStopLineTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('bus_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newhumphreysapp.busline')),
                ('bus_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='this_stop', to='newhumphreysapp.busstop')),
            ],
        ),
        migrations.CreateModel(
            name='BusStopTimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.CharField(max_length=4)),
                ('day', models.CharField(default='reg', max_length=3)),
                ('bus_stop_line_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newhumphreysapp.busstoplinetable')),
            ],
        ),
    ]
