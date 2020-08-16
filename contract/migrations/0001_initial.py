# Generated by Django 2.2.15 on 2020-08-16 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=255, verbose_name='Primeiro Nome')),
                ('last_name', models.CharField(max_length=255, verbose_name='Último Nome')),
            ],
            options={
                'verbose_name': 'Cliente',
            },
        ),
    ]