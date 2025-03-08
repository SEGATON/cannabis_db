from django.shortcuts import render

# Create your views here.

def front_page(request):
	return render(request, 'vendors/front_page.html', {

		})



def vendors(request):

	return render(request, 'vendors/vendors.html', { 


		})

def vendor(request, slug):

	return render(request, 'vendors/vendor.html', { 


		})


def dashboard(request, pk):

	return render(request, 'vendors/vendor.html', { 


		})