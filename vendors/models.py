from django.db import models

from django.conf import settings
from ckeditor.fields import RichTextField
from catalog.models import Product
from addresses.models import Address
# Create your models here.



class Vendor(models.Model):

	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)


	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	date_deleted = models.DateTimeField()

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	tagline = models.CharField(max_length=1255)

	followers = models.ManyToManyField(settings.AUTH_USER_MODEL,null=True,blank=True, related_name='vendor_followers')
	
	
	description = RichTextField(max_length=1000,null=True,blank=True)
	
	vendor_logo = models.ImageField(upload_to='media/VENDORS/VENDORS_LOGOS/', default='', null=True, blank=True)
	vendor_cover_image = models.ImageField(upload_to='media/VENDORS/VENDORS_COVER_IMAGES/', default='', null=True, blank=True)

	addresses = models.ManyToManyField(Address, null=True, blank=True)

	products = models.ManyToManyField(Product, null=True, blank=True)