from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
from django_countries import Countries


# To select a gender
GENDER_CHOICES = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER')
)


# To select a year
YEAR_CHOICES = []
for i in range(1890, datetime.now().year+1):
    YEAR_CHOICES.append((i, i))


# To select a country
class SomeCountries(Countries):
    only = [
        "TR", "CA", "FR", "DE", "IT", "JP", "RU", "GB",
        "US", "AT", "SE", "ES", "KR", "CN", "BE", "IR",

    ]

