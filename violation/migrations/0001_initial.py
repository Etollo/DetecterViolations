# Generated by Django 2.2.5 on 2020-06-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Violations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='')),
                ('time', models.DateTimeField()),
                ('place', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
