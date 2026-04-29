import json
from django.shortcuts import render
from .models import Department, Team, TeamMember, Repository, Dependency, Manager

def dashboard(request):
    departments = Department.objects.all()
    teams = Team.objects.all()
    managers = Manager.objects.all()

    department_labels = []
    department_team_counts = []

    for department in departments:
        department_labels.append(department.name)
        department_team_counts.append(department.teams.count())

    team_labels = []
    team_member_counts = []
    team_repo_counts = []
    team_dependency_counts = []

    for team in teams:
        team_labels.append(team.name)
        team_member_counts.append(team.members.count())
        team_repo_counts.append(team.repositories.count())
        team_dependency_counts.append(team.dependencies.count())

    manager_labels = []
    manager_team_counts = []

    for manager in managers:
        manager_labels.append(manager.name)
        manager_team_counts.append(manager.teams.count())

    context = {
        "total_teams": Team.objects.count(),
        "total_departments": Department.objects.count(),
        "total_members": TeamMember.objects.count(),
        "total_dependencies": Dependency.objects.count(),

        "department_labels": json.dumps(department_labels),
        "department_team_counts": json.dumps(department_team_counts),

        "team_labels": json.dumps(team_labels),
        "team_member_counts": json.dumps(team_member_counts),
        "team_repo_counts": json.dumps(team_repo_counts),
        "team_dependency_counts": json.dumps(team_dependency_counts),

        "manager_labels": json.dumps(manager_labels),
        "manager_team_counts": json.dumps(manager_team_counts),
    }

    return render(request, "datavis/dashboard.html", context)