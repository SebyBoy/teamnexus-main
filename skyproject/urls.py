from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # IMPORT NECESAR

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include messaging app URLs
    path('', include('messaging.urls')),

    path("datavis/", include("datavis.urls")),

    #  login system 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='messaging/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]