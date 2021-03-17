from django.shortcuts import render
from .models import OurImpacts
from .filters import OurImpactsFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def ourimpacts_list(request):
    ourimpacts = OurImpacts.objects.all()
    paginator = Paginator(ourimpacts, 15)
    page = request.GET.get('page')
    recent_post = OurImpacts.objects.all()[:3]
    try:
        ourimpacts_list = paginator.page(page)
    except PageNotAnInteger:
        ourimpacts_list = paginator.page(1)
    except EmptyPage:
        ourimpacts_list = paginator.page(paginator.num_pages)
    myFilter = OurImpactsFilter(request.GET, queryset=ourimpacts)
    ourimpacts = myFilter.qs
    context = {
        'ourimpacts': ourimpacts,
        'myfilter': myFilter,
        'ourimpacts_list': ourimpacts_list,
        'recent_post': recent_post
    }
    return render(request, 'ourimpacts/ourimpacts.html', context)


def ourimpacts_detail(request, slug):
    query = OurImpacts.objects.filter(slug__iexact=slug)
    recent_post = OurImpacts.objects.all()[:3]
    if query.exists:
        query = query.first()
    else:
        query = render(request, '404.html', status=404)

    context = {
        'ourimpacts': query,
        'recent_post': recent_post
    }

    return render(request, 'ourimpacts/ourimpacts_detail.html', context)
