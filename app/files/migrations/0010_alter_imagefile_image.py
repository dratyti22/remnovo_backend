# Generated by Django 4.2.11 on 2024-06-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0009_descriptionfile_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='file_image', verbose_name='Изображение'),
        ),
    ]
