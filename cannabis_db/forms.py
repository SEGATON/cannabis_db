from django import forms

from .models import Dispensary
from .models import Category
from .models import ContactMessage,NewslettersSubscriptions
from django import forms


class AddDispensaryForm(forms.ModelForm):
	class Meta:
		model = Dispensary
		fields = '__all__'
		exclude = ['slug','dispensary_social_follow','dispensary_products','dispensary_followers']


class ContactForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	file = forms.CharField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'File'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
	message =forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}))

	class Meta:
		model = ContactMessage
		fields = '__all__'


class NewslettersSubscriptionForm(forms.ModelForm):
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email address','id':'newsletter_subscription_form_tf'}))
	class Meta:
		model = NewslettersSubscriptions
		fields =  ['email']



class DispensariesSearchForm(forms.Form):
	q = forms.CharField()
	c = forms.ModelChoiceField(
			queryset=Dispensary.objects.all().order_by('title'))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['c'].label = ''
		self.fields['c'].required = False
		self.fields['c'].label = 'Dispensary'
		self.fields['q'].label = 'Search for'
		self.fields['q'].widget.attrs.update({'class':'form-control menudd'})
		self.fields['q'].widget.attrs.update({'class':'dropdown'})
