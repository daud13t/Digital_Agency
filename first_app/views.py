from django.shortcuts import render
from django.views import generic
from . import forms
import resend
import logging

from django.conf import settings


# Create your views here.
resend.api_key = settings.RESEND_API_KEY

class Home(generic.TemplateView):
    template_name = 'first_app/home.html'
from django.shortcuts import render
from . import forms
import resend
from django.conf import settings
import logging

resend.api_key = settings.RESEND_API_KEY
logger = logging.getLogger(__name__)

def contact_view(request):
    sent = False
    error = False
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            try:
                resend.Emails.send({
                    'from': 'Contact Form <onboarding@resend.dev>',
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

    return render(request, "first_app/contact.html", {"form": form, "sent": sent, "error": error})
