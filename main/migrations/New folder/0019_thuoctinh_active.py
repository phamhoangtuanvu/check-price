# Generated by Django 3.1.3 on 2021-06-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210604_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='thuoctinh',
            name='Active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
