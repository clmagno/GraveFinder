from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation, CustomUser
from django.contrib.auth.forms import AuthenticationForm



class RememberMeLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput)

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        widgets = {
            'password1': forms.CharField(widget=forms.TextInput(attrs={'type': 'password'})),
            'password2': forms.CharField(widget=forms.TextInput(attrs={'type': 'password'})),
        }


    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["username"]
        user.set_password(self.cleaned_data["password1"]) 
        if commit:
            user.save()
        return user

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        
        fields = ('corpse_last_name', 'corpse_first_name', 'Lot', 'date_reserved')


