from django.shortcuts import render
from django.views import generic
from . import forms
import resend
from django.conf import settings


# Create your views here.
resend.api_key = settings.RESEND_API_KEY

class Home(generic.TemplateView):
    template_name = 'first_app/home.html'

def contact_view(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']

            resend.Emails.send({
                'from':'Contact Form <onboarding@resend.dev>',
                'to':['daud13t@gmail.com'],
                'subject': f'new contact from {name}',
                'html':f"""
                    <p><strong>Name</strong>{name}</p>
                    <p><strong>Email</strong>{email}</p>
                    <p><strong>Message</strong>{message}</p>
                """
            })

            form = forms.ContactForm()

    return render(request,"first_app/contact.html", {"form":form})