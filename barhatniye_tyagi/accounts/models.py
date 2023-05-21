# from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Custom user model
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"),unique=True)
    phone_number = PhoneNumberField(_("phone number"))
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.webp')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
