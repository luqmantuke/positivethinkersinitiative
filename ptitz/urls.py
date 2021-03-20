from django.urls import path
from .views import home, contact, about, donations

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('aboutus/', about, name='about'),
    path('donations/', donations, name='donations'),
]
