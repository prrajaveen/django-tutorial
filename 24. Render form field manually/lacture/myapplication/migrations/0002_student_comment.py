# Generated by Django 3.2.5 on 2021-08-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='not abliable', max_length=70),
        ),
    ]
