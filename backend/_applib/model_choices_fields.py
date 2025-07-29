from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import datetime


class TeacherStatus(models.TextChoices):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DELETED = "DELETED"


class GenderChoice(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"


class PhoneValidator(RegexValidator):
    def __init__(self):
        super().__init__(regex=r'^[0-9]{11}$', message="Phone number must be 11 digits.")


class DOBValidator:
    def __init__(self):
        self.min_date = datetime.date(1950, 1, 1)
        self.max_date = datetime.date(2018, 12, 31)

    def __call__(self, value):
        if value < self.min_date or value > self.max_date:
            raise ValidationError("Date of Birth must be between 1950 and 2018.")
