# Generated by Django 4.2.3 on 2023-08-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0016_alter_macgrievance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macgrievance',
            name='status',
            field=models.IntegerField(choices=[('Solved', 'Solved'), ('InProgress', 'InProgress'), ('Pending', 'Pending')], default=3),
        ),
    ]