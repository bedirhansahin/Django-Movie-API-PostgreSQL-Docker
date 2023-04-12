from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from . models_choices import *


class User(AbstractUser):
    birth_date = models.DateField(_("birth date"), null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

