from django import forms
from .models import ContactMessage

_field_attrs = {'class': 'form-field'}


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={**_field_attrs, 'placeholder': 'Your full name'}),
            'email':   forms.EmailInput(attrs={**_field_attrs, 'placeholder': 'your@email.com'}),
            'phone':   forms.TextInput(attrs={**_field_attrs, 'placeholder': '+254 700 000 000'}),
            'subject': forms.TextInput(attrs={**_field_attrs, 'placeholder': 'How can we help?'}),
            'message': forms.Textarea(attrs={**_field_attrs, 'rows': 5, 'placeholder': 'Your message...'}),
        }
