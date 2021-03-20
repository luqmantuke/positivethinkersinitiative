from django.shortcuts import render
from .models import Projects
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from ourimpacts.models import OurImpacts
from career.models import Career


def project_list(request):
    projects = Projects.objects.all()
    paginator = Paginator(projects, 15)
    page = request.GET.get('page')
    recent_post = OurImpacts.objects.all()[:3]
    recent_jobs = Career.objects.all()[:3]
    try:
        projects_list = paginator.page(page)
    except PageNotAnInteger:
        projects_list = paginator.page(1)
    except EmptyPage:
        projects_list = paginator.page(paginator.num_pages)
    context = {
        'projects': projects,
        'project_list': projects_list,
        'recent_post': recent_post,
        'recent_jobs': recent_jobs
    }
    return render(request, 'projects/projects.html', context)


def projects_detail(request, slug):
    query = Projects.objects.filter(slug__iexact=slug)
    recent_post = OurImpacts.objects.all()[:3]
    recent_jobs = Career.objects.all()[:3]
    if query.exists:
        query = query.first()
    else:
        query = render(request, '404.html', status=404)

    context = {
        'projects': query,
        'recent_post': recent_post,
        'recent_jobs': recent_jobs
    }

    return render(request, 'projects/projects_detail.html', context)
