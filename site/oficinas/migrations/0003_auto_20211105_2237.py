# Generated by Django 3.2.7 on 2021-11-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficinas', '0002_oficinas_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficinaaluno',
            name='deleted',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='oficinas',
            name='deleted',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='oficinas',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='oficinas',
            name='link',
            field=models.CharField(blank=True, db_index=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='oficinas',
            name='local',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='oficinas',
            name='nome',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]