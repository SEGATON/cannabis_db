from django.shortcuts import render

# Create your views here.

from .forms import CreateAccountForm
from .forms import ChangeUsernameForm
from .forms import ChangePhoneNumberForm
from .forms import VendorApplicationForm


def front_page(request):
	return render(request, 'accounts/front_page.html', {
		
		})

def create_account(request):

	if request.method == 'POST':
		create_account_form = CreateAccountForm(request.POST)
		if create_account_form.is_valid():
			create_account_form.save()
			return redirect('accounts:login')
	else:
		create_account_form = CreateAccountForm()
	return render(request, 'accounts/create_account.html', {
			'create_account_form':create_account_form
		})

def account(request):
	change_username_form = ChangeUsernameForm()
	change_phone_number_form = ChangePhoneNumberForm()
	return render(request, 'account_management/account.html', {
			'change_username_form':change_username_form,
			'change_phone_number_form':change_phone_number_form
		})

def account_settings(request):
	change_username_form = ChangeUsernameForm()
	change_phone_number_form = ChangePhoneNumberForm()
	return render(request, 'account_management/account_settings.html', {
			'change_username_form':change_username_form,
			'change_phone_number_form':change_phone_number_form
		})



def privacy_settings(request):
	return render(request, 'account_management/privacy_settings.html', {

		})



def vendor_application(request):
	vendor_application_form = VendorApplicationForm()
	return render(request, 'account_management/vendor_application.html', {
			'vendor_application_form':vendor_application_form
		})

