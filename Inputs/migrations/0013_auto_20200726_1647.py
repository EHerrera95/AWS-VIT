# Generated by Django 3.0.8 on 2020-07-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inputs', '0012_auto_20200726_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultset',
            name='assessment_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='assessment_txt_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='goals_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='goals_txt_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='health_concerns_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='health_concerns_txt_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='plan_of_treatment_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='plan_of_treatment_txt_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='reason_for_referral_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='resultset',
            name='reason_for_referral_txt_results',
            field=models.CharField(choices=[('PASS', 'PASS'), ('FAIL - CHECK CONTENTS OF XML', 'FAIL - CHECK CONTENTS OF XML'), ('Not Tested', 'Not Tested')], default='', max_length=32),
        ),
    ]