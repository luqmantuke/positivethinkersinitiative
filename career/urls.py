from django.urls import path
from .views import career_list, career_detail

urlpatterns = [
    path('career/', career_list, name="career_list"),
    path('career/<slug:slug>/', career_detail, name="career_detail"),
]
