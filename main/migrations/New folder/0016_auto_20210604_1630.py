# Generated by Django 3.1.7 on 2021-06-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210602_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='Url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
