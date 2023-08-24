# Generated by Django 3.0.8 on 2022-04-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inputs', '0028_auto_20220427_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='igmodel',
            name='criteria',
            field=models.CharField(choices=[('b.1 Amb: Sample 1 - 2015e', 'b.1 Amb: Sample 1 - 2015e'), ('b.1 Amb: Sample 2 - 2015e', 'b.1 Amb: Sample 2 - 2015e'), ('b.1 Inp: Sample 1 - 2015e', 'b.1 Inp: Sample 1 - 2015e'), ('b.1 Inp: Sample 2 - 2015e', 'b.1 Inp: Sample 2 - 2015e'), ('b.2 Amb: Sample 1 - R1.1 CCD - 2015e', 'b.2 Amb: Sample 1 - R1.1 CCD - 2015e'), ('b.2 Amb: Sample 1 - R2.1 CCD - 2015e', 'b.2 Amb: Sample 1 - R2.1 CCD - 2015e'), ('b.2 Amb: Sample 1 - R2.1 RN - 2015e', 'b.2 Amb: Sample 1 - R2.1 RN - 2015e'), ('b.2 Inp: Sample 1 - R2.1 DS - 2015e', 'b.2 Inp: Sample 1 - R2.1 DS - 2015e'), ('b.7 Amb: Sample 1 - 2015e', 'b.7 Amb: Sample 1 - 2015e'), ('b.7 Inp: Sample 1 - 2015e', 'b.7 Inp: Sample 1 - 2015e'), ('b.9 Amb: Sample 1 - 2015e', 'b.9 Amb: Sample 1 - 2015e'), ('b.9 Inp: Sample 1 - 2015e', 'b.9 Inp: Sample 1 - 2015e'), ('e.1 Amb: Sample 1 - 2015e', 'e.1 Amb: Sample 1 - 2015e'), ('e.1 Amb: Sample 2 - 2015e', 'e.1 Amb: Sample 2 - 2015e'), ('e.1 Inp: Sample 1 - 2015e', 'e.1 Inp: Sample 1 - 2015e'), ('e.1 Inp: Sample 2 - 2015e', 'e.1 Inp: Sample 2 - 2015e'), ('g.9 Amb: Sample 1 - 2015e', 'g.9 Amb: Sample 1 - 2015e'), ('g.9 Amb: Sample 2 - 2015e', 'g.9 Amb: Sample 2 - 2015e'), ('g.9 Inp: Sample 1 - 2015e', 'g.9 Inp: Sample 1 - 2015e'), ('g.9 Inp: Sample 2 - 2015e', 'g.9 Inp: Sample 2 - 2015e')], max_length=64),
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='criteria',
            field=models.CharField(choices=[('b.1 Amb: Sample 1 - 2015e', 'b.1 Amb: Sample 1 - 2015e'), ('b.1 Amb: Sample 2 - 2015e', 'b.1 Amb: Sample 2 - 2015e'), ('b.1 Inp: Sample 1 - 2015e', 'b.1 Inp: Sample 1 - 2015e'), ('b.1 Inp: Sample 2 - 2015e', 'b.1 Inp: Sample 2 - 2015e'), ('b.2 Amb: Sample 1 - R1.1 CCD - 2015e', 'b.2 Amb: Sample 1 - R1.1 CCD - 2015e'), ('b.2 Amb: Sample 1 - R2.1 CCD - 2015e', 'b.2 Amb: Sample 1 - R2.1 CCD - 2015e'), ('b.2 Amb: Sample 1 - R2.1 RN - 2015e', 'b.2 Amb: Sample 1 - R2.1 RN - 2015e'), ('b.2 Inp: Sample 1 - R2.1 DS - 2015e', 'b.2 Inp: Sample 1 - R2.1 DS - 2015e'), ('b.7 Amb: Sample 1 - 2015e', 'b.7 Amb: Sample 1 - 2015e'), ('b.7 Inp: Sample 1 - 2015e', 'b.7 Inp: Sample 1 - 2015e'), ('b.9 Amb: Sample 1 - 2015e', 'b.9 Amb: Sample 1 - 2015e'), ('b.9 Inp: Sample 1 - 2015e', 'b.9 Inp: Sample 1 - 2015e'), ('e.1 Amb: Sample 1 - 2015e', 'e.1 Amb: Sample 1 - 2015e'), ('e.1 Amb: Sample 2 - 2015e', 'e.1 Amb: Sample 2 - 2015e'), ('e.1 Inp: Sample 1 - 2015e', 'e.1 Inp: Sample 1 - 2015e'), ('e.1 Inp: Sample 2 - 2015e', 'e.1 Inp: Sample 2 - 2015e'), ('g.9 Amb: Sample 1 - 2015e', 'g.9 Amb: Sample 1 - 2015e'), ('g.9 Amb: Sample 2 - 2015e', 'g.9 Amb: Sample 2 - 2015e'), ('g.9 Inp: Sample 1 - 2015e', 'g.9 Inp: Sample 1 - 2015e'), ('g.9 Inp: Sample 2 - 2015e', 'g.9 Inp: Sample 2 - 2015e')], max_length=64),
        ),
    ]
