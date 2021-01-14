from django.db import models
import re
import phonenumbers
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def validate_phonenumber(phone):
    """
    Validate if input is a phone number
    """
    try:
        formatted_phone = phonenumbers.parse(phone)
        assert phonenumbers.is_valid_number(formatted_phone)
    except (phonenumbers.NumberParseException, AssertionError):
        raise ValidationError(
            'Enter a valid phone number (e.g. +12125552368).')


# Create your models here.
class Contact(models.Model):
    name = models.CharField("Full Name",max_length=1024)
    email = models.EmailField("Email")
    phone = models.CharField("Phone",
        validators=[validate_phonenumber], max_length=17)
    message = models.TextField("Message")

    def __str__(self):
        return self.name