# Generated by Django 4.0.1 on 2022-01-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
