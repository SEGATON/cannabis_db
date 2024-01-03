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

def strain(request, slug):

	strain = get_object_or_404(Strain, slug=slug)
	ratings = Rating.objects.filter(strain_to_rate=strain)

	ratings_values = Rating.objects.filter(strain_to_rate=strain)

	for rating_value in ratings_values:
		rating_value
	
	return render(request, 'catalog/strain.html', {
			'strain':strain,
			'ratings':ratings,
			'ratings_values':ratings_values,
		

	
		})


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
