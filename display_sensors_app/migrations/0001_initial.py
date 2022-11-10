# Generated by Django 4.1.3 on 2022-11-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pressure', models.CharField(max_length=50)),
                ('temperature', models.CharField(max_length=50)),
                ('depth', models.CharField(max_length=50)),
            ],
        ),
    ]