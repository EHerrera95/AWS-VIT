# Generated by Django 3.0.8 on 2021-04-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inputs', '0023_auto_20201021_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputmodel',
            name='criteria',
            field=models.CharField(choices=[('2015E_b1_Ambulatory', '2015E_b1_Ambulatory'), ('2015E_b1_Inpatient', '2015E_b1_Inpatient'), ('2015E_b6_Ambulatory', '2015E_b6_Ambulatory'), ('2015E_b6_Inpatient', '2015E_b6_Inpatient')], max_length=64),
        ),
    ]
