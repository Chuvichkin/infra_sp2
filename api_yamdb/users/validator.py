from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username(username):
    if username.lower() == "me":
        raise ValidationError(
            _("Поле %(username)s не корректно"),
            params={"username": username},
        )
