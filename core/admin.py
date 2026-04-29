from django.contrib import admin
from core.models import Department, Team, TeamMember, Repository, ContactChannel, Dependency

admin.site.register(Department)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Repository)
admin.site.register(ContactChannel)
admin.site.register(Dependency)
