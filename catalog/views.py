from django.shortcuts import render,get_object_or_404

from .models import Category
from .models import Product

from orders.models import Order,OrderItem
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .filters import ProductFilter

# Create your views here.

def front_page(request):
	return render(request, 'catalog/front_page.html', {

		})
	
def catalog(request):

	products = Product.objects.all()
	f = ProductFilter(request.GET, queryset=Product.objects.all())
	
	return render(request, 'catalog/catalog.html', {
			'products':products,
			'filter':f
		}) 

def categories(request):
	return {
		'categories': Category.objects.all()
	}

def category(request, slug):
	
	category = get_object_or_404(Category, slug=slug)
	category_products = Product.objects.filter(categories=category)
	
	return render(request, 'catalog/categories/category.html', {
			'category':category,
			'products':category_products
		})



def products(request):
	products = Product.objects.all()
	f = ProductFilter(request.GET, queryset=Product.objects.all())
	
	return render(request, 'catalog/products/products.html', {
			'products':products,
			'filter':f
		}) 

def product(request, slug):
	product = get_object_or_404(Product, slug=slug)

	return render(request, 'catalog/catalog_item.html', {
			'product':product,


		}) 


def sort_by(request):

	

	return HttpResponseRedirect(request.META['HTTP_REFERER'])