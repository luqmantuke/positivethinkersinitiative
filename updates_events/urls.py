from django.urls import path
from .views import updates_list, updates_detail

urlpatterns = [
    path('updates-events/', updates_list, name="updates_list"),
    path('updates-events/<slug:slug>/', updates_detail, name="updates_detail"),
]
