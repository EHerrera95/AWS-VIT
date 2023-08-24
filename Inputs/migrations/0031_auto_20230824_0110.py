# Generated by Django 3.0.8 on 2023-08-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inputs', '0030_auto_20220510_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curesinputmodel',
            name='criteria',
            field=models.CharField(choices=[('b.1c Amb - Sample 1 (v2)', 'b.1c Amb - Sample 1 (v2)'), ('b.1c Amb - Sample 2 (v2)', 'b.1c Amb - Sample 2 (v2)'), ('b.1c Amb - Sample 3 (v6)', 'b.1c Amb - Sample 3 (v6)'), ('b.1c Inp - Sample 1 (v2)', 'b.1c Inp - Sample 1 (v2)'), ('b.1c Inp - Sample 2 (v2)', 'b.1c Inp - Sample 2 (v2)'), ('b.1c Inp - Sample 3 (v7)', 'b.1c Inp - Sample 3 (v7)'), ('b.2c Amb/Inp - Sample 1 - R1.1 CCD (v6)', 'b.2c Amb/Inp - Sample 1 - R1.1 CCD (v6)'), ('b.2c Amb/Inp - Sample 1 - R2.1 CCD (v8)', 'b.2c Amb/Inp - Sample 1 - R2.1 CCD (v8)'), ('b.2c Amb/Inp - Sample 1 - R2.1 RN (v8)', 'b.2c Amb/Inp - Sample 1 - R2.1 RN (v8)'), ('b.2c Inp - Sample 1 - R2.1 DS (v8)', 'b.2c Inp - Sample 1 - R2.1 DS (v8)'), ('b.7c Amb - Sample 1 (v1)', 'b.7c Amb - Sample 1 (v1)'), ('b.7c Inp - Sample 1 (v1)', 'b.7c Inp - Sample 1 (v1)'), ('b.9c Amb - Sample 1 (v1)', 'b.9c Amb - Sample 1 (v1)'), ('b.9c Inp - Sample 1 (v1)', 'b.9c Inp - Sample 1 (v1)'), ('e.1c Amb - Sample 1 (v3)', 'e.1c Amb - Sample 1 (v3)'), ('e.1c Amb - Sample 2 (v3)', 'e.1c Amb - Sample 2 (v3)'), ('e.1c Amb - Sample 3 (v7)', 'e.1c Amb - Sample 3 (v7)'), ('e.1c Inp - Sample 1 (v4)', 'e.1c Inp - Sample 1 (v4)'), ('e.1c Inp - Sample 2 (v3)', 'e.1c Inp - Sample 2 (v3)'), ('e.1c Inp - Sample 3 (v8)', 'e.1c Inp - Sample 3 (v9)'), ('g.9c Amb - Sample 1 (v2)', 'g.9c Amb - Sample 1 (v2)'), ('g.9c Amb - Sample 2 (v2)', 'g.9c Amb - Sample 2 (v2)'), ('g.9c Amb - Sample 3 (v6)', 'g.9c Amb - Sample 3 (v6)'), ('g.9c Inp - Sample 1 (v2)', 'g.9c Inp - Sample 1 (v2)'), ('g.9c Inp - Sample 2 (v2)', 'g.9c Inp - Sample 2 (v2)'), ('g.9c Inp - Sample 3 (v7)', 'g.9c Inp - Sample 3 (v7)')], max_length=64),
        ),
    ]