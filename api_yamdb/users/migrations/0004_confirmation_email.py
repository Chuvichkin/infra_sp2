# Generated by Django 2.2.16 on 2022-05-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmation',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
