# Generated by Django 3.1.7 on 2021-05-07 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210507_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanpham',
            name='TenSP',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='thuoctinh',
            name='GiaGoc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.giagoc'),
        ),
        migrations.AlterField(
            model_name='thuoctinh',
            name='GiaMoi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.giamoi'),
        ),
    ]
