from django.shortcuts import render
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

from .models import HelpsWithReport
from .models import HelpsWithReportList
from .models import HelpsWithReportListSet
from .models import Vendor
# Create your views here.
from .models import Rating

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

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

	liked = bool
	unliked = bool


	for rating_value in ratings_values:
		rating_value
	
	return render(request, 'catalog/strain.html', {
			'strain':strain,
			'ratings':ratings,
			'ratings_values':ratings_values,
			'title': strain.title + ' | ' + 'Cannabis strain' + ' | ' + str(strain.get_strain_type_label_display()),

			'liked':liked,
			'unliked':unliked
	
	
		})


####################################################################################################################################################################
def brands(request):
	return render(request, 'catalog/brands/brands.html', {
		})

def brand(request, slug):
	return render(request, 'catalog/brands/brand.html', {
		})
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







def save_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)

	user = strain

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def unsave_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])







