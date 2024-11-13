from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views import generic
# Create your views here.

from .forms import EditProfileForm
from .forms import EditProfileSocialProfilesForm
from .forms import SubmitStrainForm
from .forms import ChangeProfilePhotoForm, CusPasswordChangeForm

from django.contrib.auth.views import PasswordChangeView
from .models import Profile
from cannabis_db.models import Rating
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ChangeUsernameForm
from django.urls import reverse_lazy
from cannabis_db.models import Strain
from django.contrib.auth.forms import PasswordChangeForm

def profile(request):
	strains = Strain.objects.filter(bookmarks=request.user)

	if request.method == 'POST':

		change_profile_photo_form = ChangeProfilePhotoForm(request.POST, request.FILES, instance=request.user.profile)
		if change_profile_photo_form.is_valid():
			saga = change_profile_photo_form.save(commit=True)
			saga.user = request.user 
			saga.save()

			return redirect('memberships:profile')
	else:
		change_profile_photo_form = ChangeProfilePhotoForm()

	return render(request, 'profile/profile.html', {
		'title':'Profile' + ' | ' + request.user.username ,
		'strains':strains,
		'change_profile_photo_form':change_profile_photo_form
		
		})

class PublicProfile(generic.DetailView):
	model = Profile
	template_name = 'profile/public_profile.html'
	object_context_name = 'profiles'

	def get_queryset(self):
		return Profile.objects.all().exclude(user=self.request.user) 
	def get_object(self, *kwargs):
		pk = self.kwargs.get('pk') 
		koko = Profile.objects.get(pk=pk)
		content = {
			'koko':koko,
			'title':'Profile' + ' | ' + koko.user.username 
		}
		return content
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)

		return context



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
			return HttpResponseRedirect(request.META['HTTP_REFERER'])
	else:
		edit_profile_form = EditProfileForm()


	if request.method == 'POST':

		instance = get_object_or_404(Profile, pk=pk)
		edit_profile_social_profiles_form = EditProfileSocialProfilesForm(request.POST, instance=instance)

		if edit_profile_social_profiles_form.is_valid():
			chagga = edit_profile_social_profiles_form.save(commit=None)
			chagga.user = request.user 
			chagga.save()
			return HttpResponseRedirect(request.META['HTTP_REFERER'])
	else:
		edit_profile_social_profiles_form = EditProfileSocialProfilesForm()


	if request.method == 'POST':
		change_profile_avatar_form = ChangeProfilePhotoForm(request.POST, request.FILES, instance=request.user.profile)
		if change_profile_avatar_form.is_valid():
			cpaf = change_profile_avatar_form.save(commit=False)
			cpaf.user = request.user 
			cpaf.save()
	else:
		change_profile_avatar_form = ChangeProfilePhotoForm()

	return render(request, 'profile/profile_edit.html', {
			'edit_profile_form':edit_profile_form,
			'edit_profile_social_profiles_form':edit_profile_social_profiles_form,
			'change_profile_avatar_form':change_profile_avatar_form,
			'title':'Edit profile' + ' | ' + request.user.username 
		})


def follow_user(request, pk):

	profile = get_object_or_404(Profile, pk=pk)
	user =request.user
	if request.user not in profile.followers.all():
		profile.followers.add(user)
	else:
		profile.followers.remove(user)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])





def unfollow_user(request, pk):

	profile = get_object_or_404(Profile, pk=pk)

	if request.user in profile.followers.all():
		profile.followers.delete(user=request.user)
	
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
def my_reviews(request, pk):

	reviews = Rating.objects.filter(user=request.user)
	return render(request, 'memberships/my_reviews.html', {
			'reviews':reviews
		})

@login_required
def my_strains(request, pk):

	return render(request, 'memberships/my_strains.html', {

		})







class ChangePassView(PasswordChangeView):
	form_class = CusPasswordChangeForm
	#messages.success(request, "Password changed successfully!")
	success_url = reverse_lazy('memberships:profile')







def password_changed_success(request):
	pass
