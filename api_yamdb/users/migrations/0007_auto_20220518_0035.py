# Generated by Django 2.2.16 on 2022-05-17 17:35

import django.core.validators
from django.db import migrations, models
import users.validator


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20220514_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='moderator status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('admin', 'admin'), ('moderator', 'moderator')], default='user', max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Такой username уже есть'}, max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Поле username может содержать только буквы и цифры', 'invalid'), users.validator.validate_username], verbose_name='username'),
        ),
    ]
