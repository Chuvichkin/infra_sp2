# Generated by Django 2.2.16 on 2022-05-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',), 'verbose_name': ('Жанр',), 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]