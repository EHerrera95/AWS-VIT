# Generated by Django 3.0.8 on 2020-07-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inputs', '0009_resultset_goals_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultset',
            name='health_concerns_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL', 'FAIL')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='resultset',
            name='plan_of_treatment_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL', 'FAIL')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='resultset',
            name='reason_for_referral_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL', 'FAIL')], default='', max_length=10),
        ),
    ]
