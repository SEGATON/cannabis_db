from django import forms

from .models import Profile
from cannabis_db.models import Strain
from accounts.models import CustomUser

class EditProfileForm(forms.ModelForm):
	
	biography = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'custom_ta','placeholder':'Biography'}))
	
	class Meta:
		model = Profile 
		fields = ['biography']

class EditProfileSocialProfilesForm(forms.ModelForm):
	
	website_url = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'Website URL'}))
	twitter = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'X'}))
	facebook = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'Facebook'}))
	youtube = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'YouTube'}))
	instagram = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'Instagram'}))
	
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
