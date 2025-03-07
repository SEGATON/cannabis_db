from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _ 


from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from localflavor.us.models import USPostalCodeField
from localflavor.us.models import USSocialSecurityNumberField

from django.conf import settings

class CustomUserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Email nich gut")
		email 		= self.normalize_email(email)
		user 		= self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save() 

		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_("contact webmaster"))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_("contact webmaster"))
		return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):

	email = models.EmailField(_("email address"), unique=True)
	phone_number = models.CharField(max_length=100,null=True,blank=True)

	is_staff 			= models.BooleanField(default=False)
	is_active 			= models.BooleanField(default=True)

	USERNAME_FIELD 		= "email"
	REQUIRED_FIELDS 		= ["username"]

	objects 			= CustomUserManager()






class Address(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
	dispensary_name = models.CharField(max_length=300, null=True, blank=True)
	phone_number = models.CharField(max_length=300, null=True, blank=True)
	address_id_name = models.CharField(max_length=1000,null=True, blank=True)

	TYPE_OF_ADDRESS = (
				('billing_address','Billing address'),
				('shipping_address','Shipping address'),
				('p_o_box_number','Post office box number'),
				('physical_address','Physical Address'),
			)

	type_of_address	=	models.CharField(max_length=1000, choices=TYPE_OF_ADDRESS, null=True, blank=True)

	#order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='order_address',null=True,blank=True)

	street_name_01	=	models.CharField(max_length=1000, null=True, blank=True)
	street_name_02	=	models.CharField(max_length=1000, null=True, blank=True)
	street_city		=	models.CharField(max_length=1000, null=True, blank=True)
	street_state	=  USStateField(null=True, blank=True)
	street_zip_code	=	USZipCodeField(null=True, blank=True)

	default_address = models.BooleanField(default=False,null=True, blank=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True,blank=True)
	date_updated = models.DateTimeField(null=True,blank=True)
	date_deleted = models.DateTimeField(null=True,blank=True)

	longtitude = models.CharField(max_length=50, null=True, blank=True)
	latitude = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return str(self.address_id_name)


