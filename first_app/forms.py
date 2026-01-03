from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)