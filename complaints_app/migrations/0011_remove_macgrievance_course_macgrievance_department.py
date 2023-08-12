# Generated by Django 4.2.3 on 2023-08-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0010_macgrievance_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='macgrievance',
            name='course',
        ),
        migrations.AddField(
            model_name='macgrievance',
            name='department',
            field=models.CharField(default='d', max_length=200),
            preserve_default=False,
        ),
    ]