from django.urls import path
from .views import ourimpacts_list, ourimpacts_detail

urlpatterns = [
    path('ourimpacts/', ourimpacts_list, name="ourimpacts_list"),
    path('ourimpacts/<slug:slug>/', ourimpacts_detail, name="ourimpacts_detail"),
]
