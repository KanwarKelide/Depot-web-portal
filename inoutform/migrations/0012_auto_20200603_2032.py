# Generated by Django 3.0.3 on 2020-06-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inoutform', '0011_auto_20200603_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrival',
            name='Service_no',
            field=models.CharField(choices=[('500', '500'), ('501', '501'), ('502', '502'), ('503', '503'), ('504', '504'), ('505', '505'), ('506', '506'), ('507', '507'), ('508', '508'), ('509', '509'), ('510', '510'), ('511', '511'), ('512', '512'), ('513', '513'), ('514', '514'), ('515', '515'), ('516', '516'), ('517', '517'), ('518', '518'), ('519', '519'), ('501', '501'), ('502', '502'), ('503', '503'), ('504', '504'), ('505', '505'), ('506', '506'), ('507', '507'), ('508', '508'), ('509', '509'), ('510', '510'), ('521', '521'), ('522', '522'), ('511', '511'), ('512', '512'), ('513', '513'), ('514', '514'), ('515', '515'), ('516', '516'), ('517', '517'), ('518', '518')], default='SOME STRING', max_length=255),
        ),
    ]
