from typing import TYPE_CHECKING, cast
from django.db import models

if TYPE_CHECKING:
    from datetime import datetime


class User(models.Model):
    name = cast(
        str,
        models.CharField(max_length=120)
    )

    address = cast(
        str,
        models.CharField(max_length=120)
    )

    birthday = cast(
        datetime,
        models.DateTimeField()
    )

    class Meta:  # type: ignore
        db_table = 'usuarios'
