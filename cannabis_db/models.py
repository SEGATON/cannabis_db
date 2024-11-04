from django.db import models
from django.urls import reverse


from ckeditor.fields import RichTextField
from accounts.models import CustomUser

from django.template.defaultfilters import slugify


from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from localflavor.us.models import USPostalCodeField
from localflavor.us.models import USSocialSecurityNumberField

from django.conf import settings













class Category(models.Model):
	title = models.CharField(max_length=1000)
	slug = models.SlugField(max_length=1000)
	tagline = models.CharField(max_length=1000)

	description = models.TextField(max_length=400)
	category_icon	= models.ImageField(upload_to='media/CANNABIS_DB/CATEGORY_ICONS/', null=True, blank=True)

	def get_absolute_url(self):
		return reverse('cannabis_db:category', args=[self.slug])
	def __str__(self):
		return str(self.title)





#__________________________________________________________________________________________________________________________________


class Address(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
	dispensary_name = models.CharField(max_length=300, null=True, blank=True)
	phone_number = models.CharField(max_length=300, null=True, blank=True)
	address_id_name = models.CharField(max_length=1000)

	TYPE_OF_ADDRESS = (
				('billing_address','Billing address'),
				('shipping_address','Shipping address'),
				('p_o_box_number','Post office box number'),
				('physical_address','Physical Address'),
			)

	type_of_address	=	models.CharField(max_length=1000, choices=TYPE_OF_ADDRESS)

	#order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='order_address',null=True,blank=True)

	street_name_01	=	models.CharField(max_length=1000, null=True, blank=True)
	street_name_02	=	models.CharField(max_length=1000, null=True, blank=True)
	street_city		=	models.CharField(max_length=1000, null=True, blank=True)
	street_state	=  USStateField()
	street_zip_code	=	USZipCodeField()

	default_address = models.BooleanField(default=False,null=True, blank=True)

	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address_id_name


class StrainType(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)

	def __str__(self):
			return self.title


#__________________________________________________________________________________________________________________________________


class StrainLineageDetailsListItem(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	STRAIN_LINEAGE = {
		('sativa','Sativa'),
		('indica','Indica'),
		('hybrid','Hybrid'),
	}
	strain_lineage_01 = models.CharField(choices=STRAIN_LINEAGE, max_length=50, null=True,blank=True)
	strain_lineage_value_01 = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)

	strain_lineage_02 = models.CharField(choices=STRAIN_LINEAGE, max_length=50, null=True,blank=True)
	strain_lineage_value_02 = models.DecimalField(max_digits=9, decimal_places=2, null=True,blank=True)

	def __str__(self):
		return self.title


class StrainLineageDetailsListItems(models.Model):
	strain_lineage_details_list_items = models.ManyToManyField(StrainLineageDetailsListItem)


class StrainLineageDetailsList(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	strain_lineage_details_list_items = models.ForeignKey(StrainLineageDetailsListItems, on_delete=models.CASCADE, null=True,blank=True)

	def __str__(self):
		return self.title


#__________________________________________________________________________________________________________________________________


class StrainDetailsListItem(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	def __str__(self):
		return self.title


class StrainDetailsListItems(models.Model):
	sdlis_UNIQUE_ID = models.CharField(max_length=50, null=True,blank=True)
	strain_details_list_items = models.ManyToManyField(StrainDetailsListItem)

	def __str__(self):
		return str(self.sdlis_UNIQUE_ID)

class StrainDetailsList(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	strain_details_list_items = models.ForeignKey(StrainDetailsListItems, on_delete=models.CASCADE, null=True,blank=True)

	def __str__(self):
		return self.title


#__________________________________________________________________________________________________________________________________


class StrainKeywords(models.Model):
	keyword 			= models.CharField(max_length=300)

	def __str__(self):
		return str(self.keyword)


class StrainKeywordsSet(models.Model):
	keywords 			= models.ManyToManyField(StrainKeywords)

	def __str__(self):
		return str(self.keywords)


class StrainMetasSet(models.Model):
	sms_UNIQUE_ID 	= models.CharField(max_length=60)
	strain_meta_description = models.TextField(max_length=160,null=True, blank=True)
	strain_meta_keywords 	= models.ForeignKey(StrainKeywordsSet, on_delete=models.CASCADE ,max_length=300,null=True, blank=True )

	def __str__(self):
		return str(self.sms_UNIQUE_ID)


#__________________________________________________________________________________________________________________________________


class HelpsWithReport(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	description = models.TextField(max_length=500, null=True,blank=True)
	helps_with_icon = models.ImageField(upload_to='media/CANNABIS_DB/HELPS_WITH_ICONS/', null=True, blank=True, max_length=500)

	def __str__(self):
		return self.title


class HelpsWithReportList(models.Model):
	helps_with_report_list = models.ManyToManyField(HelpsWithReport)


class HelpsWithReportListSet(models.Model):
	hw_UNIQUE_ID = models.CharField(max_length=50, null=True,blank=True)
	helps_with_report_list = models.ForeignKey(HelpsWithReportList, on_delete=models.CASCADE,null=True, blank=True )


	def __str__(self):
		return str(self.hw_UNIQUE_ID)
#__________________________________________________________________________________________________________________________________

class EffectReport(models.Model):
	TYPE_OF_EFFECT = {
		('neutrial','Neutrial'),
		('negative','Negative'),
		('positive','Positive'),
	}
	type_of_effects = models.CharField(max_length=50,choices=TYPE_OF_EFFECT)

	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	description = models.TextField(max_length=500, null=True,blank=True)
	effect_icon = models.ImageField(upload_to='media/CANNABIS_DB/EFFECTS_ICONS/', null=True, blank=True, max_length=500)
	
	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name_plural = 'Effects'

class EffectReportList(models.Model):
	erl_UNIQUE_ID = models.CharField(max_length=50, null=True,blank=True)
	effect_report_list = models.ManyToManyField(EffectReport)
	def __str__(self):
		return str(self.erl_UNIQUE_ID)


class EffectsReportListSet(models.Model):
	erls_UNIQUE_ID = models.CharField(max_length=50, null=True,blank=True)
	effect_report_list_set = models.ForeignKey(EffectReportList, on_delete=models.CASCADE,null=True, blank=True )

	
	def __str__(self):
		return str(self.erls_UNIQUE_ID)


#__________________________________________________________________________________________________________________________________





class FeelingReport(models.Model):
	TYPE_OF_FEELING = {
		('generic','Generic'),
		('negative','Negative'),
		('positive','Positive'),
	}
	type_of_feelings = models.CharField(max_length=50,choices=TYPE_OF_FEELING)

	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	description = models.TextField(max_length=500, null=True,blank=True)
	feeling_icon = models.ImageField(upload_to='media/CANNABIS_DB/FEELINGS_ICONS/', null=True, blank=True, max_length=500)
	
	def __str__(self):
		return str(self.title)

	class Meta:
		verbose_name_plural = 'Feelings'


class FeelingReportList(models.Model):
	frl_UNIQUE_ID = models.CharField(max_length=50, null=True,blank=True)
	feeling_report_list = models.ManyToManyField(FeelingReport)
	def __str__(self):
		return str(self.frl_UNIQUE_ID)

class FeelingReportListSet(models.Model):
	frls_UNIQUE_ID = models.CharField(max_length=50, null=True,blank=True)
	feeling_report_list_set = models.ForeignKey(FeelingReportList, on_delete=models.CASCADE,null=True, blank=True )

	
	def __str__(self):
		return str(self.frls_UNIQUE_ID)


#__________________________________________________________________________________________________________________________________


class StrainGalleryImage(models.Model):
	title = models.ImageField(upload_to='media/CANNABIS_DB/GALLERY_IMAGES/', null=True, blank=True, max_length=500)
	def __str__(self):
		return str(self.title)



class StrainGalleryImagesSet(models.Model):
	si_UNIQUE_ID = models.CharField(max_length=300)
	images = models.ManyToManyField(StrainGalleryImage, null=True, blank=True, max_length=500)

	def __str__(self):
		return str(self.images)
class StrainImageGallery(models.Model):
	sig_UNIQUE_ID = models.CharField(max_length=300)
	images = models.ForeignKey(StrainGalleryImagesSet, on_delete=models.CASCADE, null=True, blank=True, max_length=500)
	def __str__(self):
		return str(self.sig_UNIQUE_ID)

#__________________________________________________________________________________________________________________________________


class TerpeneDetails(models.Model):
	title 	= models.CharField(max_length=1000)
	slug 	= models.SlugField(max_length=1000)
	description = RichTextField(null=True, blank=True)
	terpene_icon = models.ImageField(default='media/CANNABIS_DB/STRAINS/TERPENES_REPORTS/TERPENE_ICONS/default.jpg/', upload_to='media/CANNABIS_DB/STRAINS/TERPENES_REPORTS/TERPENE_ICONS/', null=True, blank=True, max_length=500)
	def __str__(self):
		return self.title








#__________________________________________________________________________________________________________________________________


class AromasDetails(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	aromas_icon = models.ImageField(upload_to='media/CANNABIS_DB/GALLERY_IMAGES/', null=True, blank=True, max_length=500)


class AromasDetailsList(models.Model):
	aromas_list = models.ManyToManyField(AromasDetails)


class AromasListSet(models.Model):
	als_UNIQUE_ID = models.CharField(max_length=1000)
	aromas_list_set 	= models.ForeignKey(AromasDetailsList, on_delete=models.CASCADE)


#__________________________________________________________________________________________________________________________________










class FlavorsDetails(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	flavor_icon = models.ImageField(upload_to='media/CANNABIS_DB/FLAVORS_ICONS/', null=True, blank=True, max_length=500)

	def get_absolute_url(self):
		return reverse('cannabis_db:flavor', args=[self.slug])

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Flavors'


class FlavorsDetailsList(models.Model):
	flavors_list = models.ManyToManyField(FlavorsDetails)


class FlavorsDetailsListSet(models.Model):
	flavors_list_set_name = models.CharField(max_length=1000)
	flavors_list_set 	= models.ForeignKey(FlavorsDetailsList, on_delete=models.CASCADE)













#__________________________________________________________________________________________________________________________________


















class StrainSpecification(models.Model):
	SPEC_NAME = {
		('thc','THC'),
		('cbd','CBD'),
		('cbg','CBG '),
		('htcv','THCV '),
		('tac','TAC '),
		('cbda','CBDA '),
		('thca','THCA '),


	}
	title 	= models.CharField(max_length=1000, choices=SPEC_NAME,null=True, blank=True)



	specification_value = models.DecimalField(max_digits=10, decimal_places=2,max_length=1000,null=True, blank=True)



	SPECIFICATION_VALUE_LABEL = {
		('percentage','%'),
		('mg','mg'),


	}
	specification_value_label 	= models.CharField(max_length=1000, choices=SPECIFICATION_VALUE_LABEL,null=True, blank=True)






	def __str__(self):
		return f'{self.title} | {self.specification_value}'












class StrainSpecificationsSets(models.Model):
	sss_UNIQUE_ID = models.CharField(max_length=1000)
	specifications 	= models.ManyToManyField(StrainSpecification, null=True, blank=True)

	def __str__(self):
		return str(self.sss_UNIQUE_ID)


#__________________________________________________________________________________________________________________________________













class BrandSocialFollowURL(models.Model):
	brand_social_profile_name		= models.CharField(max_length=300, null=True, blank=True)
	brand_social_profile_URL		= models.URLField(null=True, blank=True)













class BrandSocialFollowURLS(models.Model):
	social_profiles_URLS 		= models.ManyToManyField(BrandSocialFollowURL,  blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS)













class BrandSocialFollows(models.Model):
	brand_social_follows_name	= models.CharField(max_length=300, null=True, blank=True)
	social_profiles_URLS 		= models.ForeignKey(BrandSocialFollowURLS, on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS)


 











class Brand(models.Model):
	title = models.CharField(max_length=1000, null=True, blank=True)
	slug = models.SlugField(max_length=1000)
	tagline = models.CharField(max_length=1000, null=True, blank=True)
	websiteURL = models.URLField(max_length=300, null=True, blank=True)
	phone_number = models.CharField(max_length=300, null=True, blank=True)
	email_address = models.EmailField(max_length=300, null=True, blank=True)
	brand_logo	= models.ImageField(upload_to='media/CANNABIS_DB/BRAND_LOGOS/', null=True, blank=True)
	brand_cover	= models.ImageField(upload_to='media/CANNABIS_DB/BRAND_COVERS/', null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	brand_social_follow	= models.ForeignKey(BrandSocialFollows, on_delete=models.CASCADE, null=True, blank=True)
	brand_products = models.ManyToManyField('Strain', related_name='brand_strains', null=True, blank=True)
	brand_followers	= models.ManyToManyField(CustomUser, related_name='strain_brand_followers', null=True, blank=True)

	dispensary = models.ManyToManyField('Dispensary',null=True, blank=True )

	claimed = models.BooleanField(default=False,null=True, blank=True )


	def get_absolute_url(self):
		return reverse('cannabis_db:brand', args=[self.slug])
	def __str__(self):
		return str(self.title)












#__________________________________________________________________________________________________________________________________


















class DispensarySocialFollowURL(models.Model):
	dispensary_social_profile_name		= models.CharField(max_length=300, null=True, blank=True)
	dispensary_social_profile_URL		= models.URLField(null=True, blank=True)











class DispensarySocialFollowURLS(models.Model):
	dispensary_profiles_URLS 		= models.ManyToManyField(DispensarySocialFollowURL,  blank=True)

	def __str__(self):
		return str(self.id)











class DispensarySocialFollows(models.Model):
	dispensary_social_follows_name	= models.CharField(max_length=300, null=True, blank=True)
	social_profiles_URLS = models.ForeignKey(DispensarySocialFollowURLS, on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return self.dispensary_social_follows_name









class Dispensary(models.Model):
	TYPE_OF_DISPENSARY = {
		('medical','Medical'),
		('recreational','Recreational'),
		('Medical_recreational','Medical & Recreational'),
	}
	type_of_dispensary = models.CharField(max_length=50, choices=TYPE_OF_DISPENSARY, null=True, blank=True)
	SHOPPING_OPTIONS = {
		('all','All'),
		('pickup','Pickup'),
		('delivery','Delivery'),
	}
	shopping_options = models.CharField(max_length=50, choices=SHOPPING_OPTIONS, null=True, blank=True)
	title = models.CharField(max_length=1000)
	slug = models.SlugField(max_length=1000)
	tagline = models.CharField(max_length=1000, null=True, blank=True)
	websiteURL = models.URLField(max_length=300, null=True, blank=True)
	phone_number = models.CharField(max_length=300, null=True, blank=True)
	email_address = models.EmailField(max_length=300, null=True, blank=True)
	dispensary_logo	= models.ImageField(default='media/default.jpg', upload_to='media/CANNABIS_DB/DISPENSARY_LOGOS/', null=True, blank=True)
	dispensary_cover = models.ImageField(upload_to='media/CANNABIS_DB/DISPENSARY_COVERS/', null=True, blank=True)
	dispensary_description = RichTextField(null=True, blank=True)
	dispensary_social_follow = models.ForeignKey(DispensarySocialFollows, on_delete=models.CASCADE, null=True, blank=True)
	dispensary_strains = models.ManyToManyField('Strain', related_name='dispensary_products', null=True, blank=True)
	dispensary_brands = models.ManyToManyField(Brand, related_name='dispensary_brands', null=True, blank=True)
	dispensary_followers = models.ManyToManyField(CustomUser, related_name='dispensary_followers', null=True, blank=True)
	dispensary_address = models.ManyToManyField(Address, null=True, blank=True)
	saves = models.ManyToManyField('memberships.Profile', null=True,blank=True, related_name='dispensary_saves')
	followers = models.ManyToManyField('memberships.Profile', related_name='dispensary_followers', null=True, blank=True)
	longtitude = models.CharField(max_length=50, null=True, blank=True)
	latitude = models.CharField(max_length=50, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('cannabis_db:dispensary', args=[self.slug])

	def __str__(self):
		return str(self.title)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Dispensary, self).save(*args, **kwargs)
















#__________________________________________________________________________________________________________________________________


















class Vendor(models.Model):
	user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=300, null=True, blank=True)
	description = RichTextField()
	websiteURL = models.URLField(max_length=300, null=True, blank=True)
	products = models.ManyToManyField('Strain', related_name='vendor_profile_product', blank=True)

	vendor_logo = models.ImageField(upload_to='VENDORS/LOGOS/', null=True, blank=True)
	vendor_cover_image = models.ImageField(upload_to='VENDORS/COVER_IMAGES/', null=True, blank=True)

	phone_number = models.CharField(max_length=300, null=True, blank=True)
	email_address = models.EmailField(max_length=300, null=True, blank=True)

	followers = models.ManyToManyField('self', blank=True)

	vendor_is_top_vendor		= models.BooleanField(default=False)
	vendor_is_featured 		= models.BooleanField(default=False)
	vendor_is_bestseller 		= models.BooleanField(default=False)
	vendor_is_on_sale 		= models.BooleanField(default=False)
	vendor_high_sell_through 		= models.BooleanField(default=False)

	headline = models.CharField(max_length=1000)



	def __str__(self):
		return str(self.user)


#__________________________________________________________________________________________________________________________________



'''


STRAIN MODEL



'''







class Strain(models.Model):
	user = models.ManyToManyField(CustomUser, null=True, blank=True)
	strain_metas_set = models.ForeignKey(StrainMetasSet, on_delete=models.CASCADE, related_name='strain_metas',null=True, blank=True)
	STRAIN_TYPE = {
		('indica','Indica'),
		('sativa','Sativa'),
		('hybrid','Hybrid'),
	}
	strain_type_label = models.CharField(max_length=70, choices=STRAIN_TYPE,null=True, blank=True)
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	headline = models.CharField(max_length=150, null=True, blank=True)
	strain_type = models.ForeignKey(StrainType, on_delete=models.CASCADE, null=True, blank=True)
	brand = models.ManyToManyField(Brand, null=True, blank=True)
	strain_details_list = models.ForeignKey(StrainDetailsList, on_delete=models.CASCADE, null=True,blank=True)	
	strain_specifications = models.ForeignKey(StrainSpecificationsSets, on_delete=models.CASCADE, null=True,blank=True)
	description = RichTextField(max_length=5000, null=True,blank=True)

	featured_image = models.ImageField(default='media/CANNABIS_DB/STRAINS/FEATURED_IMAGES/default.jpg/', upload_to='media/CANNABIS_DB/STRAINS/FEATURED_IMAGES/', null=True, blank=True)
	image_gallery= models.ForeignKey(StrainImageGallery, on_delete=models.CASCADE, related_name='product_image_gallery',null=True, blank=True)
	feelings_reports = models.ForeignKey(FeelingReportListSet, on_delete=models.CASCADE,null=True, blank=True)
	effects_reports = models.ForeignKey(EffectsReportListSet, on_delete=models.CASCADE,null=True, blank=True)	
	terpenes_reports = models.ManyToManyField(TerpeneDetails, null=True, blank=True)	
	flavor_reports = models.ForeignKey(FlavorsDetailsListSet, on_delete=models.CASCADE,null=True, blank=True )	
	aromas_reports = models.ForeignKey(AromasListSet, on_delete=models.CASCADE,null=True, blank=True )	
	helps_with_reports = models.ForeignKey(HelpsWithReportListSet, on_delete=models.CASCADE,null=True, blank=True )
	strain_lineage_details_list = models.ForeignKey(StrainLineageDetailsList, on_delete=models.CASCADE, null=True,blank=True)
	vendors = models.ManyToManyField(Vendor, null=True, blank=True)
	ratings = models.ManyToManyField('Rating', null=True, blank=True)
	likes = models.ManyToManyField(CustomUser, related_name='strain_likes', null=True,blank=True)
	dislikes = models.ManyToManyField(CustomUser, related_name='strain_dislikes', null=True,blank=True)
	saves = models.ManyToManyField('memberships.Profile', null=True,blank=True, related_name='strain_saves')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(null=True,blank=True)
	dispensaries = models.ManyToManyField(Dispensary, null=True,blank=True)

	feelings = models.ManyToManyField(FeelingReport, null=True,blank=True)

	author_review = RichTextField(max_length=5000, null=True,blank=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):

		return reverse('cannabis_db:strain', args=[self.slug])

	def get_total_ratings(self):
		pass

	class Meta:
		ordering = ('-date_created',)


#__________________________________________________________________________________________________________________________________















class Rating(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='strain_rating')
	strain_to_rate = models.ForeignKey(Strain, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=300)
	slug = models.CharField(max_length=300)
	headline = models.CharField(max_length=300)
	RATING = {
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
	}
	rating = models.CharField(max_length=5, choices=RATING)
	comment = models.TextField(max_length=500, null=True, blank=True)
	date_published = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=True)
	replies = models.ManyToManyField('self')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Rating, self).save(*args, **kwargs)










class Comment(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='strain_discussion_comment')
	strain_to_rate = models.ForeignKey(Strain, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=300)
	slug = models.CharField(max_length=300)
	headline = models.CharField(max_length=300)
	RATING = {
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
	}
	rating = models.CharField(max_length=5, choices=RATING)
	comment = models.TextField(max_length=500, null=True, blank=True)
	date_published = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=True)
	replies = models.ManyToManyField('self')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Rating, self).save(*args, **kwargs)





