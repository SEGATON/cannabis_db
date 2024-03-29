from django import forms
from .models import Rating
from .models import Dispensary

from django import forms


class AddDispensaryForm(forms.ModelForm):
	class Meta:
		model = Dispensary
		fields = '__all__'
		exclude = ['slug','dispensary_social_follow','dispensary_products','dispensary_followers']