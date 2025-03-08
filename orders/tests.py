from django.test import TestCase

# Create your tests here.

from accounts.models import CustomUser




class Order(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)