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



