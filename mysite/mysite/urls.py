from django.urls import path, include

urlpatterns = [
    path('schedule/', include('schedule.urls')),
]