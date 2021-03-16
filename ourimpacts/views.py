from django.shortcuts import render
from .models import OurImpacts
from .filters import OurImpactsFilter
# Create your views here.


def blog_list(request):
    ourimpacts = OurImpacts.objects.all()
    myFilter = OurImpactsFilter(request.GET, queryset=ourimpacts)
    ourimpacts = myFilter.qs
    context = {
        'ourimpacts': ourimpacts,
        'myfilter': myFilter,
    }
    return render(request, 'ourimpacts/ourimpacts.html', context)