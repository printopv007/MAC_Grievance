# Generated by Django 4.2.3 on 2023-08-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints_app', '0008_macgrievance_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]
