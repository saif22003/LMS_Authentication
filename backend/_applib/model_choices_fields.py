from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
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
        super().__init__(regex= r'^01[3-9][0-9]{8}$', message="Enter your valid phone number")


@deconstructible
class DOBValidator:
    def __init__(self, min_date=datetime.date(1950, 1, 1), max_date=datetime.date(2020, 12, 31)):
        self.min_date = min_date
        self.max_date = max_date

    def __call__(self, value):
        if value < self.min_date or value > self.max_date:
            raise ValidationError(f"Enter your valid Birthdate")
        
