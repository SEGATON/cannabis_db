from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Strain
from cannabis_db.models import Brand
from .models import StrainType, Product

from .models import StrainDetailsListItem
from .models import StrainDetailsListItems
from .models import StrainDetailsList

from .models import ImageGallery
from .models import GalleryImagesSet
from .models import GalleryImage

from .models import StrainSpecificationsSets

from .models import StrainSpecification

from .models import TerpeneDetails

from .models import Category



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


from memberships.models import Profile

from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import ContactMessage
from .forms import AddDispensaryForm, ContactForm, DispensariesSearchForm


from .filters import StrainFilter


from django.db.models import Q

from django.views import generic

from django.core.paginator import Paginator
from .forms import NewslettersSubscriptionForm

def front_page(request):
	strains = Strain.objects.all()


	latest_strains = Strain.objects.all().order_by('-date_created')[:12]
	featured_strains = Strain.objects.filter(featured=True)[:12]
	featured_brands = Brand.objects.all()[:12]
	featured_products = Product.objects.all()[:12]
	featured_dispensaries = Dispensary.objects.all()[:12]
	featured_categories = Category.objects.all()[:12]



	return render(request, 'template_parts/front_page.html', {
			'strains':strains,
			'title':'Browse All Marijuana/Cannabis Strains, Dispensaries, Brands, and Products',
			'title_description':'Browse over 6000+ marijuana/cannabis strains, dispensaries, brands, and products.',
			'latest_strains':latest_strains,
			'featured_strains':featured_strains,
			'featured_brands':featured_brands,
			'featured_products':featured_products,
			'featured_dispensaries':featured_dispensaries,
			'featured_categories':featured_categories,
		})

def strains(request):
	strains = Strain.objects.all()
	f = StrainFilter(request.GET, queryset=strains)
	paginator = Paginator(f.qs, 50)
	page_number = request.GET.get("page")
	strains_qs = paginator.get_page(page_number)
	
	return render(request, 'strains/strains.html', {
			'strains':strains_qs,
			'filter':f,
			'title':'StrainsDB | An Online Cannabis Strains Database'

		})


'''

def posts(request):
    posts = Post.objects.all()
    post_filter = PostsFilter(request.GET, queryset=posts)
    paginator = Paginator(post_filter.qs, 50)
    page_number = request.GET.get('page')
    posts_qs = paginator.get_page(page_number)
    return render(
        request,
        'posts/posts.html',
        {'posts': posts_qs.object_list, 'filter': post_filter, 'title': 'Posts'},
    )

'''

####################################################################################################################################################################

class Strains(generic.ListView):
	template_name = 'strains/strains.html'
	model = Strain 
	object_context_name = 'strains'


	def get_queryset(self):
		pass



def strain(request, slug):
	strain = get_object_or_404(Strain, slug=slug)





	return render(request, 'strains/strain.html', {
			'strain':strain,

			'title': strain.title + ' | ' + str(strain.thc)+'% thc, ' + str(strain.cbd)+'% cbd, ' + str(strain.tac)+'% tac |  '  + ' ' + ' | Cannabis strain',

			
			'dispensaries': Dispensary.objects.filter(strain=strain)[:6],
			'dispensaries_full_list': Dispensary.objects.filter(strain=strain),



		})



def brands(request):
	brands = Brand.objects.all()
	return render(request, 'views/brands.html', {
			'brands':brands
		})

def brand(request, slug):
	brand = get_object_or_404(Brand, slug=slug)

	brand_strains = Strain.objects.filter(brand=brand)

	brand_products = Product.objects.filter(brands=brand)

	brand_dispensaries = Dispensary.objects.filter(brand=brand)

	return render(request, 'views/brand.html', {
		'brand':brand,
		'brand_strains':brand_strains,
		'brand_products':brand_products,
		'brand_dispensaries':brand_dispensaries


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

# ------------------------------------------------------------------------------------------------------- #

def like_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)

	if request.user in strain.likes.all():
		strain.likes.remove(request.user)
	else:
		strain.likes.add(request.user)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])


#######################
@login_required
def dislike_strain(request, pk):
	strain = get_object_or_404(Strain, pk=pk)

	if request.user in strain.dislikes.all():
		strain.dislikes.remove(request.user)
	else:
		strain.dislikes.add(request.user)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])


# ------------------------------------------------------------------------------------------------------- #
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


@login_required
def save_dispensary(request, pk):
	dispensary = get_object_or_404(Dispensary, pk=pk)

	if dispensary.saves.filter(id=request.user.id).exists():
		dispensary.saves.remove(request.user.profile)
	else:
		dispensary.saves.add(request.user.profile)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def saved_dispensaries(request, pk):
	saved_dispensaries = Dispensary.objects.filter(saves=request.user.profile)

	
	return render(request, 'catalog/dispensaries/saved_dispensaries.html', {
			'saved_dispensaries':saved_dispensaries,

		})

def dispensaries(request):

	dispensaries = Dispensary.objects.all()

	paginator = Paginator(dispensaries, 25)

	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)

	search_dispensaries_form = DispensariesSearchForm()


	return render(request, 'views/dispensaries.html', {
				'page_obj':page_obj,
				'title': 'StrainsDB | An Internet Medical & Recreational Dispensaries Directory',
				'search_dispensaries_form':search_dispensaries_form
		})


def dispensary(request, slug):

	dispensary = get_object_or_404(Dispensary, slug=slug)
	brands = Brand.objects.filter(dispensary=dispensary)
	strains = Strain.objects.filter(dispensaries=dispensary)
	products = Product.objects.filter(dispensaries=dispensary)

	return render(request, 'views/dispensary.html', {
				'dispensary':dispensary,
				'brands':brands,
				'strains':strains,
				'products':products,
				'title': dispensary.title + ' | ' + str(dispensary.get_type_of_dispensary_display()) + ' dispensary for ' + dispensary.get_shopping_options_display()
			
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




def about_us(request):
	return render(request, 'views/static_views/about_us.html', {
			
		})

def faq_page(request):
	return render(request, 'static_pages/faq.html', {
			'title':'F.A.Q'
		})


def privacy_policy(request):
	return render(request, 'views/static_views/privacy_policy.html', {
			'title':'Privacy policy'
		})

def search_results(request):
	return render(request, 'components/search/search_results.html', {

		})


def search(request):

	search_qs = {}

	begins_with = ''

	query = request.GET.get('search_query')

	strain_search_results_qs = Strain.objects.filter(Q(title__icontains=query))

	dispensary_search_results_qs = Dispensary.objects.filter(Q(title__icontains=query))

	items = Strain.objects.all()



	return render(request, 'components/search/search_results.html', {
		'strain_search_results_qs':strain_search_results_qs
		})



def maps(request):
	dispensaries = Dispensary.objects.all()
	return render(request, 'views/map.html', {
			'dispensaries':dispensaries,
			'title':'Find dispensary | map'
		})





def newsletter_subscription_form_process_form(request):
	newsletter_subscription_form_process_form = NewslettersSubscriptionForm(request.POST)
	return {
		'newsletter_subscription_form_process_form':newsletter_subscription_form_process_form
	}

def newsletter_subscription_form_process(request):

	if request.method == 'POST':
		newsletter_subscription_form_process_form = NewslettersSubscriptionForm(request.POST)
		if newsletter_subscription_form_process_form.is_valid():
			newsletter_subscription_form_process_form.save()
	else:
		newsletter_subscription_form_process_form = NewslettersSubscriptionForm()



	return HttpResponseRedirect(request.META['HTTP_REFERER'])




















@login_required
def bookmarks(request):
	strains = Strain.objects.filter(bookmarks=request.user.profile)
	return render(request, 'cooking_recipes_app/widgets/bookmarks_list.html', {
			'strains':strains
		})


def add_to_bookmarks(request, pk):

	strain = get_object_or_404(Strain, pk=pk)
	profile = Profile.objects.filter(user=request.user)





	if strain not in request.user.profile.saved_strains.all():
		request.user.profile.saved_strains.add(strain)
	else:
		request.user.profile.saved_strains.remove(strain)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])




@login_required
def remove_from_bookmarks(request, id):

	
	
	return HttpResponseRedirect(request.META['HTTP_REFERER'])



def consumed(request, pk):
	strain = get_object_or_404(Strain, pk=pk)
	user =request.user
	if request.user not in strain.users_smoked.all():
		strain.users_smoked.add(user)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

















def contact(request):

	if request.method == 'POST':
		contact_form = ContactForm(request.POST, request.FILES)
		if contact_form.is_valid():
			contact_form.save()
	else:
		contact_form = ContactForm()


	return render(request, 'contact.html', {
			'contact_form':contact_form,
			'title':'Contact us'
		})



@login_required
def follow_dispensary(request, pk):

	dispensary = get_object_or_404(Dispensary, pk=pk)
	user = request.user
	if dispensary not in user.profile.saved_dispensaries.all():
		user.profile.saved_dispensaries.add(dispensary)
	else:
		user.profile.saved_dispensaries.remove(dispensary)


	return HttpResponseRedirect(request.META['HTTP_REFERER'])














def terms_conditions(request):

	return render(request, 'views/static_views/terms_conditions.html', {
			'title':'Terms and Conditions',
		})



def process_search_form(request):

	if request.method == 'POST':
		search_q = request.POST['search_query']

	return HttpResponseRedirect(request.META['HTTP_REFERER'])



def ai_tools(request):

	return render(request, 'views/ai_tools.html', {
			'title':'AI Tools'
		})



def strain_ai_testing(request):


	





	return render(request, 'views/strain_ai_testing.html', {
			'title':'AI Tools'
		})




def search_dispensaries(request):
	form = DispensariesSearchForm()

	q = ''
	c = ''

	results = []
	query = Q()

	if request.POST.get('action')=='post':
		search_string = str(request.POST.get('ss'))

		if search_string is not None:
			search_string = Dispensary.objects.filter(title__contains=search_string)[:5]

			data = serializers.serialize('json', list(search_string), fields=('id','title','slug'))

			return JsonResponse({'search_string': data})

	if 'q' in request.GET:
		form = DispensariesSearchForm(request.GET)
		if form.is_valid():
			q = form.cleaned_data['q']
			c = form.cleaned_data['c']

			if c is not None:
				query &= Q(dispensary=c)
			if q is not None:
				query &= Q(title__contains=q)
			results = Dispensary.objects.filter(query)
	return render(request, 'views/dispensaries.html', {
			'search_dispensaries_form':form,
			'q':q,
			'results':results
		})



def category(request, slug):
	return render(request, 'catalog/category.html', {

		})