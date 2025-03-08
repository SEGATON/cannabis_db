from django.shortcuts import render

# Create your views here.


def front_page(request):
	return render(request, 'addresses/front_page.html', {

		})

def addresses(request):
	return render(request, 'addresses/addresses.html', {

		})

def address(request, pk):
	return render(request, 'addresses/address.html', {

		})