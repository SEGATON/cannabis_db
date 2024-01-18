from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Strain
from .models import Brand
from .models import StrainType

from .models import StrainDetailsListItem
from .models import StrainDetailsListItems
from .models import StrainDetailsList

from .models import StrainImageGallery
from .models import StrainGalleryImagesSet
from .models import StrainGalleryImage

from .models import StrainSpecificationsSets
from .models import StrainSpecifications
from .models import StrainSpecification

from .models import TerpeneDetails
from .models import TerpeneDetailsList
from .models import TerpeneDetailsListSet

from .models import FlavorsDetailsListSet
from .models import FlavorsDetailsList
from .models import FlavorsDetails

from .models import FeelingReport
from .models import FeelingReportList
from .models import FeelingReportListSet

from .models import Dispensary

from .models import DispensarySocialFollowURL
from .models import DispensarySocialFollowURLS
from .models import DispensarySocialFollows


from .models import HelpsWithReport
from .models import HelpsWithReportList
from .models import HelpsWithReportListSet
from .models import Vendor
# Create your views here.
from .models import Rating

from memberships.models import Profile

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required


from .forms import AddDispensaryForm

def front_page(request):
	strains = Strain.objects.all()
	return render(request, 'cannabis_db/front_page.html', {
			'strains':strains
		})

def strains(request):
	strains = Strain.objects.all()

	return render(request, 'catalog/strains.html', {
			'strains':strains,

		})
####################################################################################################################################################################



def strain(request, slug):
	strain = get_object_or_404(Strain, slug=slug)
	ratings = Rating.objects.filter(strain_to_rate=strain)
	ratings_values = Rating.objects.filter(strain_to_rate=strain)

	saved = bool
	if strain.saves.filter(id=request.user.id).exists():
		saved = True


	for rating_value in ratings_values:
		rating_value
	
	return render(request, 'catalog/strain.html', {
			'strain':strain,
			'ratings':ratings,
			'ratings_values':ratings_values,
			'title': strain.title + ' | ' + 'Cannabis strain' + ' | ' + str(strain.get_strain_type_label_display()),

			'saved':saved,

	
	
		})


####################################################################################################################################################################
def brands(request):
	return render(request, 'catalog/brands/brands.html', {
		})

def brand(request, slug):
	return render(request, 'catalog/brands/brand.html', {
		})

def brands_menu(request):
	return {
		'brands_menu': Brand.objects.all()
	}

@login_required
def process_strain_review(request, pk):

	if request.method == 'POST':
		strain = get_object_or_404(Strain, pk=pk)

		title = request.POST['title']
		headline = request.POST['headline']
		rating = request.POST.get('rate')
		comment = request.POST.get('five_star_rating_comment_ta')

		r = Rating(user=request.user, strain_to_rate=strain, title=title, headline=headline, rating=rating, comment=comment)
		r.save()

		return HttpResponseRedirect(request.META['HTTP_REFERER'])
	return HttpResponseRedirect(request.META['HTTP_REFERER'])
	
@login_required
def delete_review_rating(request, pk):
	rating = get_object_or_404(Rating, pk=pk)
	rating.delete()

	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def flavors(request):
	flavors = FlavorsDetails.objects.all()
	return render(request, 'catalog/flavors.html', {
			'flavors':flavors
		})

def flavor(request, slug):
	flavors = get_object_or_404(FlavorsDetails, slug=slug)
	return render(request, 'catalog/flavors.html', {
			'flavors':flavors
		})

def flavors_menu(request):
	return {
		'flavors_menu':FlavorsDetails.objects.all()
	}

def feelings_menu(request):
	return {
		'feelings_menu':FeelingReport.objects.all()
	}

def helps_with_menu(request):
	return {
		'helps_with_menu':HelpsWithReport.objects.all()
	}

def terpenes_menu(request):
	return {
		'terpenes_menu':TerpeneDetails.objects.all()
	}




def like_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)

	if request.user in strain.likes.all():
		pass
	else:
		strain.likes.add(request.user)




	return HttpResponseRedirect(request.META['HTTP_REFERER'])











def unlike_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)


	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def dislike_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)

	if request.user in strain.dislikes.all():
		pass
	else:
		strain.dislikes.add(request.user)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def undislike_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)

	if request.user in strain.dislikes.all():
		pass
	return HttpResponseRedirect(request.META['HTTP_REFERER'])





@login_required
def saved_strains(request, pk):
	saved_strains = Strain.objects.filter(saves=request.user.profile)

	
	return render(request, 'catalog/saved_strains.html', {
			'saved_strains':saved_strains,

		})




@login_required
def save_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)
	if strain.saves.filter(id=request.user.id).exists():
		strain.saves.remove(request.user.profile)
	else:
		strain.saves.add(request.user.profile)


	return HttpResponseRedirect(request.META['HTTP_REFERER'])



def unsave_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])





def dispensaries(request):

	dispensaries = Dispensary.objects.all()
	return render(request, 'catalog/dispensaries/dispensaries.html', {
				'dispensaries':dispensaries
		})


def dispensary(request, slug):

	dispensary = get_object_or_404(Dispensary, slug=slug)

	return render(request, 'catalog/dispensaries/dispensary.html', {
				'dispensary':dispensary,
			
		})

def add_dispensary(request):

	if request.method == 'POST':
		add_dispensary_form = AddDispensaryForm(request.POST, request.FILES)
		if add_dispensary_form.is_valid():
			add_dispensary_form.save()
			return redirect('cannabis_db:dispensaries')
	else:
		add_dispensary_form = AddDispensaryForm()
	return render(request, 'catalog/dispensaries/add_dispensary.html', {
				'add_dispensary_form':add_dispensary_form
		})


def remove_dispensary(request, pk):

	dispensary = get_object_or_404(Dispensary, pk=pk)
	dispensary.delete()

	return redirect('cannabis_db:dispensaries')



def faq_page(request):
	return render(request, 'static_pages/faq.html', {

		})





