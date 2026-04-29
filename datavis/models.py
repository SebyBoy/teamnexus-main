from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="teams")
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True, related_name="teams")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return self.name


class Repository(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="repositories")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Dependency(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="dependencies")
    depends_on = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="dependent_teams")

    def __str__(self):
        return f"{self.team.name} depends on {self.depends_on.name}"