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





