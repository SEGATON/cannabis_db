from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views import generic
# Create your views here.
from .forms import EditProfileForm
from .forms import EditProfileSocialProfilesForm
from .forms import SubmitStrainForm

from .models import Profile

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def profile(request):

	return render(request, 'memberships/profile.html', {
		
		})

class PublicProfile(generic.DetailView):
	model = Profile
	template_name = 'memberships/public_profile.html'
	object_context_name = 'profiles'

	def get_queryset(self):
		return Profile.objects.all().exclude(user=self.request.user) 
	def get_object(self, *kwargs):
		pk = self.kwargs.get('pk') 
		koko = Profile.objects.get(pk=pk)
		content = {
			'koko':koko
		}
		return content
	def get_context_data(self, *args, **kwargs):
		context = supser().get_context_data(**kwargs)

		return context

def edit_profile(request, pk):
	
	return render(request, 'memberships/edit_profile.html', {
		
		})

def delete_profile(request, pk):
	
	return render(request, 'memberships/delete_profile.html', {
		
		})

def follow_profile(request, pk):
	pass



def edit_profile(request, pk):

	if request.method == 'POST':

		instance = get_object_or_404(Profile, pk=pk)
		edit_profile_form = EditProfileForm(request.POST, instance=instance)

		if edit_profile_form.is_valid():
			chuchut = edit_profile_form.save(commit=True)
			chuchut.user = request.user
			chuchut.save()
			return redirect('memberships:profile')
	else:
		edit_profile_form = EditProfileForm()


	if request.method == 'POST':

		instance = get_object_or_404(Profile, pk=pk)
		edit_profile_social_profiles_form = EditProfileSocialProfilesForm(request.POST, instance=instance)

		if edit_profile_social_profiles_form.is_valid():
			chagga = edit_profile_social_profiles_form.save(commit=None)
			chagga.user = request.user 
			chagga.save()
			return redirect('memberships:profile')
	else:
		edit_profile_social_profiles_form = EditProfileSocialProfilesForm()

	return render(request, 'manage_profile/edit_profile.html', {
			'edit_profile_form':edit_profile_form,
			'edit_profile_social_profiles_form':edit_profile_social_profiles_form,
		})

@login_required
def follow_user(request, pk):

	return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def submit_strain(request, pk):
	if request.method == 'POST':
		submit_strain_form = SubmitStrainForm()
	else:
		submit_strain_form = SubmitStrainForm()
	return render(request, 'memberships/submit_strain.html', {
			'submit_strain_form':submit_strain_form
		})

@login_required
def my_strains(request, pk):

	return render(request, 'memberships/my_strains.html', {

		})