from django.db import models

from django.contrib.auth.models import AbstractBaseUser

from .manager import UserManager


class User(AbstractBaseUser):
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    grade   = models.CharField(default='', max_length=100, null=False, blank=False)
    ability = models.CharField(default='', max_length=100, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin  = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD  = 'name'
    REQUIRED_FIELDS = ['name', 'grade']

    def __str__(self):
        return self.name
