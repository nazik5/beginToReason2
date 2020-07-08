# Generated by Django 3.0.8 on 2020-07-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_lesson_lesson_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept_key', models.CharField(max_length=30)),
                ('concept_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_concept',
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_concept',
            field=models.ManyToManyField(blank=True, to='core.Concept'),
        ),
    ]
