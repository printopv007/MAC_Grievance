# Generated by Django 4.2.3 on 2023-08-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0007_remove_macgrievance_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='macgrievance',
            name='name',
            field=models.CharField(default='dsd', max_length=100),
            preserve_default=False,
        ),
    ]
