from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=200)
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_departments')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    mission = models.TextField()
    responsibilities = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teams')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.team.name}"


class Repository(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='repositories')
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class ContactChannel(models.Model):
    CHANNEL_TYPES = [
        ('slack', 'Slack'),
        ('teams', 'Microsoft Teams'),
        ('email', 'Email'),
    ]
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='contact_channels')
    channel_type = models.CharField(max_length=20, choices=CHANNEL_TYPES)
    value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.team.name} - {self.channel_type}"


class Dependency(models.Model):
    upstream_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='downstream_dependencies')
    downstream_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='upstream_dependencies')

    def __str__(self):
        return f"{self.upstream_team.name} → {self.downstream_team.name}"