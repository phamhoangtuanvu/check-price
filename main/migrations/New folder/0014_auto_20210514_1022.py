# Generated by Django 3.1.7 on 2021-05-14 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210513_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguonban',
            name='Domain',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
