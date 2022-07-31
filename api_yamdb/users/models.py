from django.db import models
import django.contrib.auth.models as django_auth_models
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.utils.translation import gettext_lazy as _
from django.core import validators
from .validator import validate_username

ROLE_LIST = (
    ('user', 'user'), ('admin', 'admin'), ('moderator', 'moderator')
)


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=30,
        unique=True,
        null=False,
        validators=[
            validators.RegexValidator(
                r"^[\w.@+-]+$",
                _(
                    "Поле username может содержать только буквы и цифры"
                ),
                "invalid",
            ),
            validate_username,
        ],
        error_messages={
            "unique": _("Такой username уже есть"),
        },
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(max_length=50, choices=ROLE_LIST, default='user')
    confirmation_code = models.CharField(
        max_length=128,
        blank=True,
    )
    is_moderator = models.BooleanField(
        _("moderator status"),
        default=False,
    )
    is_admin = models.BooleanField(
        _("staff status"),
        default=False,
    )

    def save(self, *args, **kwargs):
        if self.role == "moderator":
            self.is_moderator = True
        if self.role == "admin":
            self.is_admin = True
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ['username']


class AnonymousUserExtraFields(AnonymousUser):
    is_moderator = False
    is_admin = False


django_auth_models.AnonymousUser = AnonymousUserExtraFields
