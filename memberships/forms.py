from django import forms

from .models import Profile

class EditProfileForm(forms.ModelForm):
	biography = forms.CharField(widget=forms.Textarea(attrs={}))
	class Meta:
		model = Profile 
		fields = ['biography']

class EditProfileSocialProfilesForm(forms.ModelForm):
	website_url = forms.CharField(widget=forms.TextInput(attrs={}))
	twitter = forms.CharField(widget=forms.TextInput(attrs={}))
	facebook = forms.CharField(widget=forms.TextInput(attrs={}))
	youtube = forms.CharField(widget=forms.TextInput(attrs={}))
	instagram = forms.CharField(widget=forms.TextInput(attrs={}))
	class Meta:
		model = Profile 
		fields = ['website_url','twitter','facebook','youtube','instagram']