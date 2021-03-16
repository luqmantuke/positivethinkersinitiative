import django_filters
from .models import *


class OurImpactsFilter(django_filters.FilterSet):
    class Meta:
        model = OurImpacts
        fields = ['category']
