import logging

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from autoslug import AutoSlugField
from dirtyfields import DirtyFieldsMixin
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from common.lists import COUNTRIES
from common.models import BaseModel, NameSlugDescriptionBaseModel

from .choices import UserGender, UserKind
from .managers import CustomUserManager

from .utils import get_user_slug

logger = logging.getLogger(__name__)


class EmployeeDesignation(NameSlugDescriptionBaseModel):
    """Employee Designation model for storing and managing different kind of employee designations
    """

    class Meta:
        verbose_name_plural = "Employee Designations"

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class User(
    DirtyFieldsMixin,
    BaseModel,
    AbstractUser,
    PermissionsMixin,
):
    """User model for storing and managing different kind of users
    """
    phone = PhoneNumberField(db_index=True, unique=True, blank=False, null=False)
    email = models.EmailField(db_index=True, unique=True, blank=False, null=False)
    country = models.CharField(
        max_length=2, choices=COUNTRIES, default="bd", db_index=True
    )
    language = models.CharField(max_length=2, default="en")
    slug = AutoSlugField(
        populate_from=get_user_slug, unique=True, null=True, db_index=True
    )
    gender = models.CharField(
        max_length=20,
        blank=True,
        choices=UserGender.choices,
        db_index=True,
    )
    profile_image = VersatileImageField(
        "Profile Image", upload_to="profile/images", blank=True, null=True
    )
    kind = models.CharField(
        max_length=50,
        choices=UserKind.choices,
        db_index=True,
        default=UserKind.UNDEFINED,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    designation = models.ForeignKey(
        EmployeeDesignation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Designation of an employee, only valid for employee kind user",
    )
    owner = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees'
    )

    # Hack: Do not use username field, we are using phone as the unique id
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", ]

    class Meta:
        ordering = ("-pk",)

    def __str__(self):
        return f"ID: {self.id}, Kind: {self.kind}, Name: {self.first_name} {self.last_name}, Phone: {self.phone}"

