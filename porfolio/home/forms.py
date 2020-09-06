from django import forms
from django.forms import ModelForm

from .models import *

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['name', 'email', 'msg']