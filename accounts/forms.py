
from django import forms  

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm

from localflavor.us.forms import USStateSelect
from localflavor.us.forms import USZipCodeField
from localflavor.us.forms import USSocialSecurityNumberField
from django.contrib.auth.models import User

from localflavor import generic


class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	class Meta:
		fields = '__all__'


class CreateAccountForm(UserCreationForm):


	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))



	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Create password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))
	class Meta:
		model = CustomUser
		fields = ['username','email','password1','password2']


class ChangeUsernameForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
	class Meta:
		model = CustomUser
		fields = ['username']


class ChangePhoneNumberForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['phone_number']


class VendorApplicationForm(forms.ModelForm):




	class Meta:
		model = CustomUser
		fields = [
			'first_name',
			'last_name',


			'email',
			'phone_number',


		]


class CustomChangePasswordForm(PasswordResetForm):
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Create password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))
	class Meta:
		model = User
		fields = ['password1', 'password2']