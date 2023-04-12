from datetime import datetime

# To select a gender
GENDER_CHOICES = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER')
)


# To select a year
YEAR_CHOICES = []
for i in range(1890, datetime.now().year+1):
    YEAR_CHOICES.append(i)
