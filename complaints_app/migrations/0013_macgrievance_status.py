# Generated by Django 4.2.3 on 2023-08-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0012_feedback_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='macgrievance',
            name='status',
            field=models.CharField(default='Grievance Submitted', max_length=100),
        ),
    ]
