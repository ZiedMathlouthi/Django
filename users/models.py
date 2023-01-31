from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.validators import RegexValidator
from  django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def is_mail_esprit(value):
    if str(value).endswith('@esprit.tn') == False:
        raise ValidationError(
            "Your email must be @esprit.tn"
        )


# Create your models here.
class Person(AbstractUser):
    cin = models.CharField(
        "CIN",
        primary_key=True,
        max_length=8,
        validators=[
            MaxLengthValidator(8, message="Verify length"),
            MinLengthValidator(8, message="Verify length"),
            RegexValidator(r'^[0-9]$' , message="Just number")
        ]
    )
    username = models.CharField("Username", max_length=255, unique=True)
    email = models.EmailField(
        unique=True, validators=[is_mail_esprit]
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "users"
