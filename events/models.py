from django.db import models
from auth_system.models import *
# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    event_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, null=True, blank=True, default="Локація")

    def __str__(self):
        return f"{self.title} - {self.user}"

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["title"]
