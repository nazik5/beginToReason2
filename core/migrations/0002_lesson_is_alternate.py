# Generated by Django 3.1.1 on 2020-10-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='is_alternate',
            field=models.BooleanField(default=False),
        ),
    ]