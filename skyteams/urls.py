from django.urls import path, include

urlpatterns = [
    path("schedule/", include("schedule.urls")),
    path("datavis/", include("datavis.urls")),
    path("messaging/", include("messaging.urls")),    
    path("teams/", include("teams.urls")),
    path("organisation/", include("organisation.urls")),
    path("core/", include("core.urls")),
    ]