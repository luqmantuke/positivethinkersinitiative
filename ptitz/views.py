from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from positivethinkers import settings
from django.urls import reverse
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact_message = f'User  "{name}" with the email {email}, just contacted you on PTITZ and left a message  "{message}". Please contact him as soon as possible.'

            try:
                send_mail(subject, contact_message, settings.EMAIL_HOST_USER, ['tuke.luqman@gmail.com'],
                          settings.FAIL_SILENTLY)
            except BadHeaderError:
                return HttpResponse('Invalid Header.')

            messages.success(request, f"Thank You For Contacting Us {name}, We Shall Reach You As Soon As Possible. :)")
            return HttpResponseRedirect(reverse('home'))

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')


def donations(request):
    return render(request, 'donations.html')