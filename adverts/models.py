from django.db import models
from auth_system.models import *
from adverts.validators import validate_image_size
from django.db import models
from cloudinary.models import CloudinaryField

class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=50, blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()
    media = CloudinaryField("media",  blank=True, null=True,  validators=[validate_image_size])

    def __str__(self):
        return f"{self.user.username} - {self.published_at}"

    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Adverts"
        ordering = ["published_at"]