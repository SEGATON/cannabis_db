from django.db import models

# Create your models here.
from django.conf import settings

from ckeditor.fields import RichTextField

from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from localflavor.us.models import USPostalCodeField
from localflavor.us.models import USSocialSecurityNumberField

from django_countries.fields import CountryField


class Address(models.Model):
	a_UNIQUE_ID = models.CharField(max_length=100)
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='address_user')

	ADDRESS_TYPE = (
			('billing_address','Billing Address',),
			('shipping_address','Shipping Address',),
			('p_o_box','P.O Box',),
		)

	address_type = models.CharField(max_length=255, choices=ADDRESS_TYPE, null=True, blank=True)

	address_street_name_line_1 = models.CharField(max_length=255, null=True, blank=True)
	address_street_name_line_2 = models.CharField(max_length=255, null=True, blank=True)

	address_city = models.CharField(max_length=255, null=True, blank=True)
	address_state = USStateField()

	address_zip_code = USZipCodeField()

	address_country = CountryField()

	notes = RichTextField()

	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	date_deleted = models.DateTimeField()



	def __str__(self):
		return str(self.user)

