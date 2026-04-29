from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

class Meeting(models.Model):
    
    # Meeting title (e.g. Weekly Planning)
    title = models.CharField(max_length=200)

    # Link meeting to a team
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    # User who created the meeting
    organiser = models.ForeignKey(User, on_delete=models.CASCADE)

    # Date and time
    meeting_date = models.DateField()
    meeting_time = models.TimeField()

    # Platform choices
    PLATFORM_CHOICES = [
        ('Teams', 'Teams'),
        ('Zoom', 'Zoom'),
        ('Google Meet', 'Google Meet'),
        ('In Person', 'In Person'),
    ]

    # Platform field
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)

    # Optional meeting link or location
    location_or_link = models.CharField(max_length=255, blank=True, null=True)

    # Message / description
    message = models.TextField(blank=True)

    # Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Display in admin
    def __str__(self):
        return f"{self.title} - {self.team}"