# Generated by Django 4.2.3 on 2023-08-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0015_alter_macgrievance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macgrievance',
            name='status',
            field=models.IntegerField(choices=[(1, 'Solved'), (2, 'InProgress'), (3, 'Pending')], default=3),
        ),
    ]
