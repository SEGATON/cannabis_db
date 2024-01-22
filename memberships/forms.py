from django import forms

from .models import Profile
from cannabis_db.models import Strain

class EditProfileForm(forms.ModelForm):
	
	biography = forms.CharField(widget=forms.Textarea(attrs={'class':'custom_ta','placeholder':'Biography'}))
	
	class Meta:
		model = Profile 
		fields = ['biography']

class EditProfileSocialProfilesForm(forms.ModelForm):
	
	website_url = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'Website URL'}))
	twitter = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'X'}))
	facebook = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'Facebook'}))
	youtube = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'YouTube'}))
	instagram = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'Instagram'}))
	
	class Meta:
		model = Profile 
		fields = ['website_url','twitter','facebook','youtube','instagram']

class SubmitStrainForm(forms.ModelForm):

	class Meta:
		model = Strain
		fields = '__all__'