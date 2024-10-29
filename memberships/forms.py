from django import forms

from .models import Profile
from cannabis_db.models import Strain
from accounts.models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
class EditProfileForm(forms.ModelForm):
	
	biography = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Biography'}))
	
	class Meta:
		model = Profile 
		fields = ['biography']

class EditProfileSocialProfilesForm(forms.ModelForm):
	
	website_url = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Website URL'}))
	twitter = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'X'}))
	facebook = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Facebook'}))
	youtube = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'YouTube'}))
	instagram = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Instagram'}))
	
	class Meta:
		model = Profile 
		fields = ['website_url','twitter','facebook','youtube','instagram']

class SubmitStrainForm(forms.ModelForm):

	class Meta:
		model = Strain
		fields = '__all__'



class ChangeUsernameForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = '__all__'


class ChangeProfilePhotoForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_photo']


class CusPasswordChangeForm(PasswordChangeForm):
	old_password = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Old password'}))
	new_password1 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'New password'}))
	new_password2 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm new password'}))

	class Meta:
		model = User
		fields = ['old_password','new_password1','new_password2']