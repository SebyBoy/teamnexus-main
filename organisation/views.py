from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Department, Team, Dependency


@login_required
def department_list(request):
    """Display all departments with search functionality."""
    query = request.GET.get('q', '')
    departments = Department.objects.all().prefetch_related('teams')
    
    if query:
        departments = departments.filter(name__icontains=query)
    
    return render(request, 'organisation/department_list.html', {
        'departments': departments,
        'query': query
    })


@login_required
def department_detail(request, pk):
    """Display a single department with full details."""
    department = get_object_or_404(Department, pk=pk)
    teams = department.teams.all().prefetch_related('members')
    return render(request, 'organisation/department_detail.html', {
        'department': department,
        'teams': teams
    })


@login_required
def organisation_chart(request):
    """Display the organisation chart showing team relationships."""
    departments = Department.objects.all().prefetch_related('teams')
    dependencies = Dependency.objects.select_related(
        'upstream_team', 'downstream_team'
    ).all()
    return render(request, 'organisation/organisation_chart.html', {
        'departments': departments,
        'dependencies': dependencies
    })