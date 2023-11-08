from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Income, Expense

class Update_I(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('income','amount')

        widgets={
            'income': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class':'form-control'})
        }

class Update_E(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('expense', 'amount', 'date')

        widgets={
            'expense': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class':'form-control'}),
            'date': forms.TextInput(attrs={'class':'form-control'})
        }