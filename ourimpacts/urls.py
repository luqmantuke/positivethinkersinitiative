from django.urls import path
from .views import blog_list

urlpatterns = [
    path('ourimpacts/', blog_list, name="blog-list"),
]
