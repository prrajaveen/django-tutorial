# Generated by Django 3.2.5 on 2021-09-08 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('page_name', models.CharField(max_length=70)),
                ('page_cat', models.CharField(max_length=70)),
                ('page_publish_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myapplication.page')),
                ('panna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('likes', models.IntegerField()),
            ],
            bases=('myapplication.page',),
        ),
    ]
