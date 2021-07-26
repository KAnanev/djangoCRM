import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_token = models.CharField(max_length=16)
    telegram_id = models.CharField(max_length=32,  blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.user_token:
            self.user_token = secrets.token_hex(nbytes=8)
        return super(User, self).save(*args, **kwargs)
