# Generated by Django 4.2.5 on 2023-09-07 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost_per_day', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('cheap', 'Дешёвые'), ('comfortable', 'Комфортные'), ('vip', 'V.I.P.')], max_length=20)),
                ('number', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField()),
                ('is_booked', models.BooleanField(default=False)),
                ('price_per_day', models.PositiveIntegerField(default=0)),
                ('features', models.ManyToManyField(blank=True, to='hotel_app.roomfeature')),
            ],
        ),
        migrations.CreateModel(
            name='BookingApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('is_approved', models.BooleanField(default=False)),
                ('stay_duration', models.PositiveIntegerField(blank=True, null=True)),
                ('final_price', models.PositiveIntegerField(blank=True, null=True)),
                ('additional_services', models.ManyToManyField(blank=True, to='hotel_app.roomfeature')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.client')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.room')),
            ],
        ),
    ]
