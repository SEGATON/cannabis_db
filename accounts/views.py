from django.shortcuts import render
# Create your views here.
from .forms import CreateAccountForm
from .forms import ChangeUsernameForm
from .forms import ChangePhoneNumberForm
from .forms import VendorApplicationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

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

@login_required
def account_settings(request):
	if request.method == 'POST':
		change_username_form = ChangeUsernameForm(request.POST, instance=request.user)
		if change_username_form.is_valid():
			paganka = change_username_form.save(commit=None)
			paganka.instance = request.user
			paganka.save() 
	else:
		change_username_form = ChangeUsernameForm()
	if request.method == 'POST':
		change_password_form = PasswordChangeForm(user=request.user, data=request.POST)
		if change_password_form.is_valid():
			poka = change_password_form.save()
			update_session_auth_hash(request, form.user)
	else:
		change_password_form = PasswordChangeForm(user=request.user)

	change_phone_number_form = ChangePhoneNumberForm()
	return render(request, 'account_management/account_settings.html', {
			'change_username_form':change_username_form,
			'change_phone_number_form':change_phone_number_form,
			'change_password_form':change_password_form
		})

def privacy_settings(request):
	return render(request, 'account_management/privacy_settings.html', {

		})

def vendor_application(request):
	vendor_application_form = VendorApplicationForm()
	return render(request, 'account_management/vendor_application.html', {
			'vendor_application_form':vendor_application_form
		})



def change_password(request):

	return render(request, 'accounts/change_password.html', {

		})