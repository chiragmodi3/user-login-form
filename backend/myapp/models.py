from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name='myapp_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='myapp_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
