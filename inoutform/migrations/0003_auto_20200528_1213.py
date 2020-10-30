# Generated by Django 3.0.3 on 2020-05-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inoutform', '0002_auto_20200523_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='arrival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shift', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd')], max_length=10)),
                ('Scheduled_departure_time', models.CharField(max_length=100)),
                ('Actual_departure_time', models.CharField(max_length=100)),
                ('Odometer_start_reading', models.CharField(max_length=100)),
                ('SOC_at_departure', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='coming',
        ),
    ]
