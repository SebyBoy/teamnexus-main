from django.urls import path
from . import views

app_name = 'organisation'

urlpatterns = [
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
    path('organisation/', views.organisation_chart, name='organisation_chart'),
    path("", views.department_list, name="department_list"),

]