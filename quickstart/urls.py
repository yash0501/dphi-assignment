from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get_data),
    # path('post/', views.post_data),
    path('add_user/', views.add_user),
    path('add_hackathon_organizer/', views.add_hackathon_organizer),
    path('add_hackathon/', views.add_hackathon),
    path('get_hackathons/', views.get_hackathons),
    path('register_for_hackathon/', views.register_for_hackathon),
    path('get_registered_hackathons/', views.get_registered_hackathons),
    path('submit_hackathon/', views.submit_hackathon),
    path('get_submissions/', views.get_submissions),
]