# Generated by Django 3.0.8 on 2020-07-23 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inputs', '0006_auto_20200723_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='variableset',
            name='goals',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]