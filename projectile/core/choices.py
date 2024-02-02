from django.db import models


class UserGender(models.TextChoices):
    FEMALE = "FEMALE", "Female"
    MALE = "MALE", "Male"
    OTHER = "OTHER", "Other"


class UserKind(models.TextChoices):
    UNDEFINED = "UNDEFINED", "Undefined"
    OWNER = "OWNER", "Owner"
    EMPLOYEE = "EMPLOYEE", "Employee"
    CUSTOMER = "CUSTOMER", "Customer"
