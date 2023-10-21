from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField("Address", max_length=300, default='', blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    # Add related_name to groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # Choose a custom related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',  # Choose a custom related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username