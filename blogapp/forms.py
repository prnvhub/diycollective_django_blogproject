from django.forms import fields
from . models import post
from django import forms


class ModelForm(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','body','img']

        widgets={
            'title':forms.TextInput(attrs={'class':'text-input'}),
            'body':forms.Textarea(attrs={'class':'text-input'}),
            'img':forms.FileInput(attrs={'class':'text-input'}),
        }
    