# Generated by Django 3.2.5 on 2021-08-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
