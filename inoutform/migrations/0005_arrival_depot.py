# Generated by Django 3.0.3 on 2020-05-31 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inoutform', '0004_auto_20200531_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrival',
            name='Depot',
            field=models.CharField(choices=[('MIYAPUR', 'MIYAPUR'), ('JBS', 'JBS')], default='SOME STRING', max_length=10),
        ),
    ]
