# Generated by Django 4.2.6 on 2023-10-09 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swapImg', '0005_images_delete_capturedimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
    ]
