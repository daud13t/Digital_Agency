from django.shortcuts import render
from django.views import generic
from . import forms
import resend
import logging

from django.conf import settings


# Create your views here.
resend.api_key = settings.RESEND_API_KEY
logger = logging.getLogger(__name__)



class Home(generic.TemplateView):
    template_name = 'first_app/home.html'

class About(generic.TemplateView):
    template_name = 'first_app/about.html'

class Studio(generic.TemplateView):
    template_name = 'first_app/studio.html'

class Work(generic.TemplateView):
    template_name = 'first_app/work.html'

class Web1(generic.TemplateView):
    template_name = 'first_app/web1.html'
class Web2(generic.TemplateView):
    template_name = 'first_app/web2.html'
class Web3(generic.TemplateView):
    template_name = 'first_app/web3.html'
class Web4(generic.TemplateView):
    template_name = 'first_app/web4.html'


def contact_view(request):
    sent = False
    form = forms.ContactForm()
    error = False

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            try:
                resend.Emails.send({
                    'from': 'Contact Form <onboarding@bellatrix.com>',
                    'to': ['daud13t@gmail.com'],
                    'subject': f'New contact from {name}',
                    'html': f"""
                        <p><strong>Name:</strong> {name}</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p><strong>Message:</strong> {message}</p>
                    """
                })
                sent = True
                form = forms.ContactForm()
            except Exception as e:
                logger.error(f"Resend email failed: {e}")
                error = True

    return render(request, "first_app/contact.html", {
        "form": form,
        "sent": sent,
        'error':error
    })