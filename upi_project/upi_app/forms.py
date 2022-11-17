from django import forms
from django.forms import TextInput
from .models import login_form

class application_form(forms.ModelForm):
    class Meta:
        model = login_form
        fields =["account_number","ifsc_code","name","branch_name","mobile_number"]
             #("__all__" )
        widgets={
            'account_number':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'account number'
                }),
                'ifsc_code':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'ifsc code'
                }),
                'name':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
                'branch_name':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'branch'
                }),
                'mobile_number':TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'mobile'
                }),
                }



