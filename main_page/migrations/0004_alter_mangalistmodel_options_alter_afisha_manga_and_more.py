# Generated by Django 4.2.7 on 2023-11-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_rename_film_afisha_manga_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mangalistmodel',
            options={'verbose_name': 'Манга', 'verbose_name_plural': 'Манги'},
        ),
        migrations.AlterField(
            model_name='afisha',
            name='manga',
            field=models.CharField(max_length=100, verbose_name='Название манги Афиша'),
        ),
        migrations.AlterField(
            model_name='afisha',
            name='time',
            field=models.TimeField(verbose_name='Дата создания манги'),
        ),
    ]
