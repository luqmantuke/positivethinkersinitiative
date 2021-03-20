from django.urls import path
from .views import project_list, projects_detail

urlpatterns = [
    path('projects/', project_list, name="projects_list"),
    path('projects/<slug:slug>/', projects_detail, name="projects_detail"),
]
