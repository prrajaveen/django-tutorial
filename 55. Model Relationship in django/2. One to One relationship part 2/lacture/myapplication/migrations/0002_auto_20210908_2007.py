# Generated by Django 3.2.5 on 2021-09-08 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapplication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='page_ptr',
        ),
        migrations.AlterField(
            model_name='like',
            name='panna',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapplication.page'),
        ),
    ]
