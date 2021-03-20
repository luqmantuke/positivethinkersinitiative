from django.shortcuts import render
from .models import Updates
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from ourimpacts.models import OurImpacts
from career.models import Career


def updates_list(request):
    updates = Updates.objects.all()
    recent_post = OurImpacts.objects.all()[:3]
    recent_jobs = Career.objects.all()[:3]

    context = {
        'updates': updates,
        'recent_post': recent_post,
        'recent_jobs': recent_jobs
    }
    return render(request, 'updates/updates.html', context)


def updates_detail(request, slug):
    query = Updates.objects.filter(slug__iexact=slug)
    recent_post = OurImpacts.objects.all()[:3]
    recent_jobs = Career.objects.all()[:3]
    if query.exists:
        query = query.first()
    else:
        query = render(request, '404.html', status=404)

    context = {
        'updates': query,
        'recent_post': recent_post,
        'recent_jobs': recent_jobs
    }

    return render(request, 'updates/updates_detail.html', context)
