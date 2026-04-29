from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    team_or_members = models.CharField(max_length=200)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()

    PLATFORM_CHOICES = [
        ('Teams', 'Teams'),
        ('Zoom', 'Zoom'),
        ('Google Meet', 'Google Meet'),
        ('In Person', 'In Person'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title