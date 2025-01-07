from django.db import models
from auth_system.models import *
from cloudinary.models import CloudinaryField
# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=200, default="Some title")
    text = models.CharField(max_length=500)
    published_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=[
        ('sport', 'Sport'),
        ('policy', 'Policy'),
        ('inf', 'Infrastructure'),
        ('life', 'Life')
    ])
    file = CloudinaryField("media",  blank=True, null=True,  validators=[validate_image_size])
    def __str__(self):
        return f"Новина #{self.pk}"

    class Meta:
        verbose_name= "New"
        verbose_name_plural = "News"
        ordering = ["pk"]

