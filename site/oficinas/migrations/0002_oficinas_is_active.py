# Generated by Django 3.2.7 on 2021-10-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficinas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficinas',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
