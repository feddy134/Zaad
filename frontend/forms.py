from django.forms import ModelForm
from django.forms import (CharField,TextInput,EmailInput,EmailField, Textarea)
from .models import Contact , validate_phonenumber

class ContactForm(ModelForm):

    name = CharField(label='Full Name', widget=TextInput(attrs={'class': 'input100',
                                                                'placeholder': 'Enter full name'}))

    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'input100',
                                                                'placeholder': 'Enter email addess',
                                                                                  }))
    phone = CharField(label='Phone', validators=[validate_phonenumber],
                      widget=TextInput(attrs={'class': 'input100',
                                                       'placeholder': 'Enter phone number',
                                              }))
    message = CharField(label='Message', widget=Textarea(attrs={'class': 'input100',
                                                                'placeholder': ' Your Comment...',
                                                                'style':'margin-top: 0px; margin-bottom: 0px; height: 127px;'}))
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']


