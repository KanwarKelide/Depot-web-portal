# Generated by Django 3.0.3 on 2020-06-02 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inoutform', '0008_auto_20200601_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrival',
            name='Depot',
            field=models.CharField(choices=[('MIYAPUR', 'MIYAPUR'), ('JBS', 'JBS')], default='SOME STRING', max_length=255),
        ),
        migrations.AlterField(
            model_name='arrival',
            name='Driver_id',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
        migrations.AlterField(
            model_name='arrival',
            name='Route_no',
            field=models.CharField(choices=[('AJ', 'AJ'), ('AB', 'AB'), ('AM', 'AM'), ('AL', 'AL')], default='SOME STRING', max_length=255),
        ),
        migrations.AlterField(
            model_name='arrival',
            name='Service_no',
            field=models.CharField(choices=[('500/1', '500/1'), ('500/2', '500/2'), ('501/1', '501/1'), ('501/2', '501/2'), ('502/1', '502/1'), ('502/2', '502/2'), ('503/1', '503/1'), ('503/2', '503/2'), ('504/1', '504/1'), ('504/2', '504/2'), ('505/1', '505/1'), ('505/2', '505/2'), ('506/1', '506/1'), ('506/2', '506/2'), ('507/1', '507/1'), ('507/2', '507/2'), ('508/1', '508/1'), ('508/2', '508/2'), ('509/1', '509/1'), ('509/2', '509/2'), ('510/1', '510/2'), ('510/2', '510/2'), ('511/1', '511/1'), ('511/2', '511/2'), ('512/1', '512/1'), ('512/2', '512/2'), ('513/1', '513/1'), ('513/2', '513/2'), ('514/1', '514/1'), ('514/2', '514/2'), ('515/1', '515/1'), ('515/2', '515/2'), ('516/1', '516/1'), ('516/2', '516/2'), ('517/1', '517/1'), ('517/2', '517/2'), ('518/1', '518/1'), ('518/2', '518/2'), ('519/1', '519/1'), ('519/2', '519/2')], default='SOME STRING', max_length=255),
        ),
        migrations.AlterField(
            model_name='arrival',
            name='Shift',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd')], default='SOME STRING', max_length=255),
        ),
        migrations.AlterField(
            model_name='arrival',
            name='Vehicle_id',
            field=models.CharField(choices=[('TS 10UB 8168', 'TS 10UB 8168'), ('TS 10UB 8169', 'TS 10UB 8169'), ('TS 10UB 8170', 'TS 10UB 8170'), ('TS 10UB 8171', 'TS 10UB 8171'), ('TS 10UB 8172', 'TS 10UB 8172'), ('TS 10UB 8177', 'TS 10UB 8177'), ('TS 10UB 8178', 'TS 10UB 8178'), ('TS 10UB 8179', 'TS 10UB 8179'), ('TS 10UB 8180', 'TS 10UB 8180'), ('TS 10UB 8181', 'TS 10UB 8181'), ('TS 10UB 8182', 'TS 10UB 8182'), ('TS 10UB 8183', 'TS 10UB 8183'), ('TS 10UB 8184', 'TS 10UB 8184'), ('TS 10UB 8185', 'TS 10UB 8185'), ('TS 10UB 8186', 'TS 10UB 8186'), ('TS 10UB 8187', 'TS 10UB 8187'), ('TS 10UB 8188', 'TS 10UB 8188'), ('TS 10UB 8189', 'TS 10UB 8189'), ('TS 10UB 8190', 'TS 10UB 8190'), ('TS 10UB 8191', 'TS 10UB 8191')], default='SOME STRING', max_length=255),
        ),
    ]
