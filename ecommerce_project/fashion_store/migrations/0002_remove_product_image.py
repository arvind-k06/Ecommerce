# Generated by Django 4.2.3 on 2023-07-24 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashion_store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
