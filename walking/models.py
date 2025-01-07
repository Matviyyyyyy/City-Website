from django.db import models
from auth_system.models import *
from events.models import Event
from institutions.models import Institution


class Walk(models.Model):
    name = models.CharField(max_length=50, default="Прогулянка")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goat = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    number_members = models.PositiveIntegerField(default=1)
    type = models.CharField(max_length=50, choices=[
            ('nature', 'Nature'),
            ('city', 'City'),
            ('historic', 'Historic'),
            ('sport', 'Sport'),
        ],
        default='nature')
    status = models.CharField(max_length=20, default="scheduled", choices=[
        ('scheduled', 'Scheduled'),
        ('in_progres', 'In progres'),
        ('completed', 'Completed')
    ])
    institution = models.ManyToManyField("institutions.Institution", null=True, blank=True)
    events = models.ManyToManyField("events.Event",  null=True, blank=True)


    def duration(self):
        return round((self.end_time - self.start_time).total_seconds() / 3600, 1)  # В годинах

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"

    class Meta:
        verbose_name = "Walk"
        verbose_name_plural = "Walk"
        ordering = ["created_at"]