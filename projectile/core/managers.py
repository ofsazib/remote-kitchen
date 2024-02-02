import logging

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

from common.choices import Status
from common.managers import CustomManager
from .choices import UserKind

logger = logging.getLogger(__name__)


class CustomUserManager(BaseUserManager, CustomManager):
    def _create_user(
        self,
        phone,
        email,
        password,
        is_staff,
        is_superuser,
        code=None,
        is_active=True,
        **kwargs
    ):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError("Email must be set!")
        email = self.normalize_email(email)
        user = self.model(
            phone=phone,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email, password=None, **kwargs):
        return self._create_user(phone, email, password, False, False, **kwargs)

    def create_superuser(self, phone, email, password, **kwargs):
        return self._create_user(phone, email, password, True, True, **kwargs)

    def get_status_active(self):
        return self.get_queryset().filter(status=Status.ACTIVE, is_active=True)

    def get_all(self):
        return self.get_queryset()

    def get_active_owners(self):
        return self.get_status_active().filter(kind=UserKind.OWNER)

    def get_active_employees(self):
        return self.get_status_active().filter(kind=UserKind.EMPLOYEE)

    def get_active_customers(self):
        return self.get_status_active().filter(kind=UserKind.CUSTOMER)
