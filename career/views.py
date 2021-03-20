from django.shortcuts import render
from .models import Career
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from ourimpacts.models import OurImpacts


def career_list(request):
    career = Career.objects.all()
    paginator = Paginator(career, 15)
    page = request.GET.get('page')
    recent_post = OurImpacts.objects.all()[:3]
    recent_jobs = Career.objects.all()[:3]
    try:
        career_list = paginator.page(page)
    except PageNotAnInteger:
        career_list = paginator.page(1)
    except EmptyPage:
        career_list = paginator.page(paginator.num_pages)
    context = {
        'career': career,
        'career_list': career_list,
        'recent_post': recent_post,
        'recent_jobs': recent_jobs
    }
    return render(request, 'Career/Career.html', context)


def career_detail(request, slug):
    query = Career.objects.filter(slug__iexact=slug)
    recent_post = OurImpacts.objects.all()[:3]
    recent_jobs = Career.objects.all()[:3]
    if query.exists:
        query = query.first()
    else:
        query = render(request, '404.html', status=404)

    context = {
        'career': query,
        'recent_post': recent_post,
        'recent_jobs': recent_jobs
    }

    return render(request, 'Career/Career_detail.html', context)
