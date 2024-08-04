from django import forms
from django.forms import ModelForm
from .models import Reservation
from django.contrib.auth.models import User
import datetime


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['car_make', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget(),
        }


class AvailabilityForm(forms.Form):
    default = datetime.date.today()
    check_availability = forms.DateField(widget=forms.SelectDateWidget(), initial=default)

    # attrs={'type': 'datetime-local'}

    # class Meta:
    #     model = Reservation
    #     fields = ['chk_availability']
    #     widgets = {
    #         'chk_availability': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    #     }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password do not match')
        return cd['password2']
