from django.db import models
from auth_system.models import *
from django.core.validators import MinValueValidator, MaxValueValidator
from institutions.validators import validate_image_size
from cloudinary.models import CloudinaryField


class Institution(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=20, choices=[
        ('Catering', 'Catering'),
        ('Sport', 'Sport'),
        ('Entertainment', 'Entertainment'),
        ('Education', 'Education'),
        ('Trade', 'Trade'),
        ('Beauty and health', 'Beauty and health'),
    ])
    location = models.CharField(max_length=500)
    description = models.TextField()
    rating = models.IntegerField(default=50)
    media = CloudinaryField("media",  blank=True, null=True,  validators=[validate_image_size])


    def __str__(self):
        return f"{self.name} - {self.type}"

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ["name"]



class Review(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    published_at = models.DateTimeField(auto_now_add=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=50)

    def __str__(self):
        return f"{self.user.username} - {self.published_at}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-published_at"]















