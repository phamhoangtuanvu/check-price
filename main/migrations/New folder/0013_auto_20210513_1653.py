# Generated by Django 3.1.7 on 2021-05-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210513_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='Url',
            field=models.URLField(unique=True),
        ),
    ]
