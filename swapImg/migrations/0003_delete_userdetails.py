# Generated by Django 4.2.6 on 2023-10-09 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swapImg', '0002_userdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]