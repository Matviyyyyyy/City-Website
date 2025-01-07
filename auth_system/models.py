from django.db import models
from django.contrib.auth.models import AbstractUser
from auth_system.validators import validate_image_size
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=[
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    ], default="user")
    media = CloudinaryField("media",  blank=True, null=True,  validators=[validate_image_size])

    def admin_or_moder(self):
        if self.role == 'admin' or self.role == 'moderator':
            return True
        return False




