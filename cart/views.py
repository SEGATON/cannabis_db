from django.shortcuts import render
from orders.models import Order 
# Create your views here.

from catalog.models import Product


def front_page(request):

	return render(request, 'cart/front_page.html', {

		})

def cart(request, pk):
	order = Order.objects.get(pk=pk)
	return render(request, 'cart/cart.html', {
				'order':order
		})




def add_product_to_cart(request, pk):
	pass

def update_product_in_cart(request, pk):
	pass

def delete_product_from_cart(request, pk):
	pass