# Generated by Django 3.1.7 on 2021-03-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('violation', '0002_auto_20200625_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violation',
            name='place',
            field=models.CharField(choices=[(1, 'Склад'), (2, 'Цех')], max_length=100),
        ),
    ]
