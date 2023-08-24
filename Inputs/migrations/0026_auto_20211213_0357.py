# Generated by Django 3.0.8 on 2021-12-13 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inputs', '0025_auto_20210603_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputmodel',
            name='criteria',
            field=models.CharField(choices=[('b.1 Amb: Sample 1 - 2015e', 'b.1 Amb: Sample 1 - 2015e'), ('b.1 Amb: Sample 2 - 2015e', 'b.1 Amb: Sample 2 - 2015e'), ('b.1 Amb: Sample 1 - 2015e (Cures Update)', 'b.1 Amb: Sample 1 - 2015e (Cures Update)'), ('b.1 Amb: Sample 2 - 2015e (Cures Update)', 'b.1 Amb: Sample 2 - 2015e (Cures Update)'), ('b.1 Amb: Sample 3 - 2015e (Cures Update)', 'b.1 Amb: Sample 3 - 2015e (Cures Update)'), ('b.1 Inp: Sample 1 - 2015e', 'b.1 Inp: Sample 1 - 2015e'), ('b.1 Inp: Sample 2 - 2015e', 'b.1 Inp: Sample 2 - 2015e'), ('b.1 Inp: Sample 1 - 2015e (Cures Update)', 'b.1 Inp: Sample 1 - 2015e (Cures Update)'), ('b.1 Inp: Sample 2 - 2015e (Cures Update)', 'b.1 Inp: Sample 2 - 2015e (Cures Update)'), ('b.1 Inp: Sample 3 - 2015e (Cures Update)', 'b.1 Inp: Sample 3 - 2015e (Cures Update)'), ('b.2 Amb: Sample 1 - R1.1 CCD - 2015e (Cures Update)', 'b.2 Amb: Sample 1 - R1.1 CCD - 2015e (Cures Update)'), ('b.2 Amb: Sample 1 - R2.1 CCD - 2015e (Cures Update)', 'b.2 Amb: Sample 1 - R2.1 CCD - 2015e (Cures Update)'), ('b.2 Amb: Sample 1 - R2.1 RN - 2015e (Cures Update)', 'b.2 Amb: Sample 1 - R2.1 RN - 2015e (Cures Update)'), ('b.2 Inp: Sample 1 - R2.1 DS - 2015e (Cures Update)', 'b.2 Inp: Sample 1 - R2.1 DS - 2015e (Cures Update)'), ('b.7 Amb: Sample 1 - 2015e', 'b.7 Amb: Sample 1 - 2015e'), ('b.7 Inp: Sample 1 - 2015e', 'b.7 Inp: Sample 1 - 2015e'), ('b.7 Amb: Sample 1 - 2015e (Cures Update)', 'b.7 Amb: Sample 1 - 2015e (Cures Update)'), ('b.7 Inp: Sample 1 - 2015e (Cures Update)', 'b.7 Inp: Sample 1 - 2015e (Cures Update)'), ('b.9 Amb: Sample 1 - 2015e', 'b.9 Amb: Sample 1 - 2015e'), ('b.9 Inp: Sample 1 - 2015e', 'b.9 Inp: Sample 1 - 2015e'), ('b.9 Amb: Sample 1 - 2015e (Cures Update)', 'b.9 Amb: Sample 1 - 2015e (Cures Update)'), ('b.9 Inp: Sample 1 - 2015e (Cures Update)', 'b.9 Inp: Sample 1 - 2015e (Cures Update)'), ('e.1 Amb: Sample 1 - 2015e', 'e.1 Amb: Sample 1 - 2015e'), ('e.1 Amb: Sample 2 - 2015e', 'e.1 Amb: Sample 2 - 2015e'), ('e.1 Amb: Sample 1 - 2015e (Cures Update)', 'e.1 Amb: Sample 1 - 2015e (Cures Update)'), ('e.1 Amb: Sample 2 - 2015e (Cures Update)', 'e.1 Amb: Sample 2 - 2015e (Cures Update)'), ('e.1 Amb: Sample 3 - 2015e (Cures Update)', 'e.1 Amb: Sample 3 - 2015e (Cures Update)'), ('e.1 Inp: Sample 1 - 2015e', 'e.1 Inp: Sample 1 - 2015e'), ('e.1 Inp: Sample 2 - 2015e', 'e.1 Inp: Sample 2 - 2015e'), ('e.1 Inp: Sample 1 - 2015e (Cures Update)', 'e.1 Inp: Sample 1 - 2015e (Cures Update)'), ('e.1 Inp: Sample 2 - 2015e (Cures Update)', 'e.1 Inp: Sample 2 - 2015e (Cures Update)'), ('e.1 Inp: Sample 3 - 2015e (Cures Update)', 'e.1 Inp: Sample 3 - 2015e (Cures Update)'), ('g.9 Amb: Sample 1 - 2015e', 'g.9 Amb: Sample 1 - 2015e'), ('g.9 Amb: Sample 2 - 2015e', 'g.9 Amb: Sample 2 - 2015e'), ('g.9 Amb: Sample 1 - 2015e (Cures Update)', 'g.9 Amb: Sample 1 - 2015e (Cures Update)'), ('g.9 Amb: Sample 2 - 2015e (Cures Update)', 'g.9 Amb: Sample 2 - 2015e (Cures Update)'), ('g.9 Amb: Sample 3 - 2015e (Cures Update)', 'g.9 Amb: Sample 3 - 2015e (Cures Update)'), ('g.9 Inp: Sample 1 - 2015e', 'g.9 Inp: Sample 1 - 2015e'), ('g.9 Inp: Sample 2 - 2015e', 'g.9 Inp: Sample 2 - 2015e'), ('g.9 Inp: Sample 1 - 2015e (Cures Update)', 'g.9 Inp: Sample 1 - 2015e (Cures Update)'), ('g.9 Inp: Sample 2 - 2015e (Cures Update)', 'g.9 Inp: Sample 2 - 2015e (Cures Update)'), ('g.9 Inp: Sample 3 - 2015e (Cures Update)', 'g.9 Inp: Sample 3 - 2015e (Cures Update)')], max_length=64),
        ),
        migrations.CreateModel(
            name='AllLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]