from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Goal, User


class GoalForm(forms.ModelForm):
    timespan = forms.ChoiceField(widget=forms.TextInput(attrs={'class': "form-control mb-5"}), choices=Goal.TIMESPAN_CHOICES),
    
    class Meta:
        model = Goal
        fields = ("title", "text", "timespan")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Username'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        }
    ))
    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        }
    ))