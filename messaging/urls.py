from django.urls import path
from . import views

urlpatterns = [
    # Messaging system
    path('', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent'),
    path('drafts/', views.drafts, name='drafts'),
    path('send/', views.send_message, name='send'),
    path('message/<int:id>/', views.message_detail, name='detail'),

    # NEW  features for voting system
    path('vote/', views.vote_view, name='vote'),
    path('summary/', views.summary_view, name='summary'),
]