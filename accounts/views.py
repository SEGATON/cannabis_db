from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from .forms import CreateAccountForm
from .forms import ChangeUsernameForm
from .forms import ChangePhoneNumberForm
from .forms import VendorApplicationForm
from .forms import CustomChangePasswordForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
def front_page(request):
	change_username_form = ChangeUsernameForm(request.POST)
	change_password_form = CustomChangePasswordForm(request.POST)
	return render(request, 'accounts/front_page.html', {
			'change_username_form':change_username_form,
			'change_password_form':change_password_form,
			'title':'Account' + ' | ' + request.user.username
		
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
			'create_account_form':create_account_form,
			'title':'Create new account'
		})



def delete_account_success(request, pk):
	
	account = CustomUser.objects.get(pk=pk)
	account.delete()
	messages.success(request, 'Account deleted successfully!')

	return render(request, 'accounts/account_deletion_success.html', {
			'title':'Account deletetion success!'
		})