# Generated by Django 4.2.3 on 2023-08-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.CharField(choices=[('MCA', 'MCA'), ('MBA', 'MBA'), ('MSC', 'MSC')], max_length=200, null=True),
        ),
    ]
