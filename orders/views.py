from django.shortcuts import render

# Create your views here.
from .models import Order
def front_page(request):
	orders = Order.objects.all()
	return render(request, 'orders/front_page.html', {
			'orders':orders
		})

def orders(request):
	orders = Order.objects.all()
	return render(request, 'orders/orders.html', {
			'orders':orders
		})

def order(request, pk):
	order = Order.objects.get(pk=pk)
	return render(request, 'orders/order.html', {
			'order':order
		})