# Generated by Django 3.2.8 on 2021-10-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='additional_img',
            field=models.URLField(blank=True, null=True, verbose_name='Доп изображение 1'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='additional_img_2',
            field=models.URLField(blank=True, null=True, verbose_name='Доп изображение 2'),
        ),
    ]
