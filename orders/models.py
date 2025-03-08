from django.db import models

# Create your models here.
from django.conf import settings
from addresses.models import Address

from catalog.models import Product


class OrderItem(models.Model):
	order= models.ForeignKey('Order', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	product_quantity = models.IntegerField()

	def get_item_total(self):

		if self.product.pricing_management.price_sale:

			total = self.product_quantity * self.product.pricing_management.price_sale

		else:
			total = self.product_quantity * self.product.pricing_management.price_regular

		return total




	def __str__(self):
		return self.product.title


class Order(models.Model):

	ORDER_STATUS = (
			('pending','Pending',),
			('processed','Processed',),
			('on_hold','On hold',),
			('canceled','Canceled',),
		)

	order_status = models.CharField(max_length=255, choices=ORDER_STATUS, null=True, blank=True)


	ORDER_STYPE = (
			('physical_product','Physical Product',),
			('digital_product','Digital Product',),
			('dropship_product','Dropship Product',),

		)

	order_type = models.CharField(max_length=255, choices=ORDER_STYPE, null=True, blank=True)

	order_number = models.CharField(max_length=255, null=True, blank=True)

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


	billing_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='billing_address', null=True, blank=True)
	shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE,related_name='shipping_address', null=True, blank=True)

	order_items = models.ManyToManyField(OrderItem, null=True, blank=True, related_name='order_items')

	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)
	date_canceled = models.DateTimeField(auto_now_add=False, null=True, blank=True)


	def get_order_shipping_rate_total(self):
		return "order shipping_rate_total"

	def get_order_tax_total(self):
		return "order tax_total"

	def get_order_sub_total(self):
		total = 0
		for order_item in self.order_items.all():
			total += order_item.get_item_total() # why += to total? explain
		return total

	def get_order_coupon_code(self):
		return "order sub_total"

	def get_order_grand_total(self):
		return "order grand_total"


	def __str__(self):
		return str(self.order_number)