from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    adharcard_or_passport = models.ImageField(upload_to='adharcard_or_passport/', blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    preferred_tour_date = models.DateField(blank=True, null=True)

    # Add related_name to groups field
    groups = models.ManyToManyField(
        Group,
        related_name="custom_users",
        related_query_name="custom_user",
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )

    # Add related_name to user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_users",
        related_query_name="custom_user",
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.username
