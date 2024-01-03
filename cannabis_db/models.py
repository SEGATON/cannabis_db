from django.db import models
from django.urls import reverse
# Create your models here.

from ckeditor.fields import RichTextField
from accounts.models import CustomUser
from django.template.defaultfilters import slugify
class StrainType(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)

	def __str__(self):
			return self.title
##################################################################################################################################

class StrainDetailsListItem(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)	

	def __str__(self):
		return self.title

class StrainDetailsListItems(models.Model):
	strain_details_list_items = models.ManyToManyField(StrainDetailsListItem)	

class StrainDetailsList(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	strain_details_list_items = models.ForeignKey(StrainDetailsListItems, on_delete=models.CASCADE, null=True,blank=True)	
	
	def __str__(self):
		return self.title

##################################################################################################################################


class StrainKeywords(models.Model):
	keyword 			= models.CharField(max_length=300)

	def __str__(self):
		return str(self.keyword)

class StrainKeywordsSet(models.Model):
	keywords 			= models.ManyToManyField(StrainKeywords)

	def __str__(self):
		return str(self.keywords)

class StrainMetas(models.Model):
	strain_meta_title 	= models.CharField(max_length=60)
	strain_meta_description = models.TextField(max_length=160)
	strain_meta_keywords 	= models.ForeignKey(StrainKeywordsSet, on_delete=models.CASCADE ,max_length=300)

	def __str__(self):
		return str(self.strain_meta_title)

##################################################################################################################################

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
	helps_with_report_list = models.ForeignKey(HelpsWithReportList, on_delete=models.CASCADE,null=True, blank=True )

##################################################################################################################################

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
		return self.title

class FeelingReportList(models.Model):
	feeling_report_list = models.ManyToManyField(FeelingReport)

class FeelingReportListSet(models.Model):
	feeling_report_list_set = models.ForeignKey(FeelingReportList, on_delete=models.CASCADE,null=True, blank=True )

##################################################################################################################################

class StrainGalleryImage(models.Model):
	image_name = models.CharField(max_length=300)
	image = models.ImageField(upload_to='media/CANNABIS_DB/GALLERY_IMAGES/', null=True, blank=True, max_length=500)	

class StrainGalleryImagesSet(models.Model):
	images = models.ManyToManyField(StrainGalleryImage) 	

class StrainImageGallery(models.Model):
	gallery_name = models.CharField(max_length=300)
	images = models.ForeignKey(StrainGalleryImagesSet, on_delete=models.CASCADE)


##################################################################################################################################


class TerpeneDetails(models.Model):
	terpene_name 	= models.CharField(max_length=1000)
	terpene_value = models.CharField(max_length=1000)


class TerpeneDetailsList(models.Model):
	terpenes = models.ManyToManyField(TerpeneDetails)

class TerpeneDetailsListSet(models.Model):
	terpene_set_name = models.CharField(max_length=1000)
	terpene_set 	= models.ForeignKey(TerpeneDetailsList, on_delete=models.CASCADE)

##################################################################################################################################

class AromasDetails(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	aromas_icon = models.ImageField(upload_to='media/CANNABIS_DB/GALLERY_IMAGES/', null=True, blank=True, max_length=500)	

class AromasDetailsList(models.Model):
	aromas_list = models.ManyToManyField(AromasDetails)

class AromasListSet(models.Model):
	aromas_list_set_name = models.CharField(max_length=1000)
	aromas_list_set 	= models.ForeignKey(AromasDetailsList, on_delete=models.CASCADE)

##################################################################################################################################



class FlavorsDetails(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	flavor_icon = models.ImageField(upload_to='media/CANNABIS_DB/GALLERY_IMAGES/', null=True, blank=True, max_length=500)	

class FlavorsDetailsList(models.Model):
	flavors_list = models.ManyToManyField(FlavorsDetails)

class FlavorsDetailsListSet(models.Model):
	flavors_list_set_name = models.CharField(max_length=1000)
	flavors_list_set 	= models.ForeignKey(FlavorsDetailsList, on_delete=models.CASCADE)

##################################################################################################################################

class StrainSpecification(models.Model):
	SPEC_NAME = {
		('thc','THC'),
		('cbd','CBD'),
		('cbg','CBG ')
	}
	specification_name 	= models.CharField(max_length=1000, choices=SPEC_NAME)
	specification_value = models.DecimalField(max_digits=10, decimal_places=2,max_length=1000)

	def __str__(self):
		return f'{self.specification_name} | {self.specification_value}'

class StrainSpecifications(models.Model):
	specifications = models.ManyToManyField(StrainSpecification)

class StrainSpecificationsSets(models.Model):
	specifications_set_name = models.CharField(max_length=1000)
	specifications_set 	= models.ForeignKey(StrainSpecifications, on_delete=models.CASCADE)


##################################################################################################################################
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
	title = models.CharField(max_length=1000)
	slug = models.SlugField(max_length=1000)
	tagline = models.CharField(max_length=1000)
	websiteURL = models.URLField(max_length=300, null=True, blank=True)
	phone_number = models.CharField(max_length=300, null=True, blank=True)
	email_address = models.EmailField(max_length=300, null=True, blank=True)
	brand_logo	= models.ImageField(upload_to='media/CANNABIS_DB/BRAND_LOGOS/', null=True, blank=True)
	brand_cover	= models.ImageField(upload_to='media/CANNABIS_DB/BRAND_COVERS/', null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	brand_social_follow	= models.ForeignKey(BrandSocialFollows, on_delete=models.CASCADE, null=True, blank=True)
	brand_products = models.ManyToManyField('Strain', related_name='brand_strains', null=True, blank=True)
	brand_followers	= models.ManyToManyField(CustomUser, related_name='strain_brand_followers')

	def get_absolute_url(self):
		return reverse('cannabis_db:brand', args=[self.slug])
	def __str__(self):
		return str(self.title) 

##################################################################################################################################

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

##################################################################################################################################

class Strain(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

	strain_metas_set = models.ForeignKey(StrainMetas, on_delete=models.CASCADE, related_name='strain_metas',null=True, blank=True)

	STRAIN_TYPE = {
		('indica','Indica'),
		('sativa','Sativa'),
		('hybrid','Hybrid'),
	}
	strain_type_label = models.CharField(max_length=70, choices=STRAIN_TYPE)
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	headline = models.CharField(max_length=50)
	strain_type = models.ForeignKey(StrainType, on_delete=models.CASCADE, null=True, blank=True)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
	strain_details_list = models.ForeignKey(StrainDetailsList, on_delete=models.CASCADE, null=True,blank=True)
	strain_specifications = models.ForeignKey(StrainSpecificationsSets, on_delete=models.CASCADE, null=True,blank=True)
	description = RichTextField(max_length=5000, null=True,blank=True)
	
	featured_image = models.ImageField(upload_to='media/CANNABIS_DB/STRAINS/FEATURED_IMAGES/', null=True, blank=True)

	image_galley= models.ForeignKey(StrainImageGallery, on_delete=models.CASCADE, related_name='product_image_gallery',null=True, blank=True)

	feelings_reports = models.ForeignKey(FeelingReportListSet, on_delete=models.CASCADE,null=True, blank=True)
	terpenes_reports = models.ForeignKey(TerpeneDetailsListSet, on_delete=models.CASCADE,null=True, blank=True)
	flavor_reports = models.ForeignKey(FlavorsDetailsListSet, on_delete=models.CASCADE,null=True, blank=True )
	aromas_reports = models.ForeignKey(AromasListSet, on_delete=models.CASCADE,null=True, blank=True )
	helps_with_reports = models.ForeignKey(HelpsWithReportListSet, on_delete=models.CASCADE,null=True, blank=True )
	


	vendors = models.ManyToManyField(Vendor)

	ratings = models.ManyToManyField('Rating', null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):

		return reverse('cannabis_db:strain', args=[self.slug])

	def get_total_ratings(self):
		pass

		


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
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Rating, self).save(*args, **kwargs)





class DispensarySocialFollowURL(models.Model):
	dispensary_social_profile_name= models.CharField(max_length=300, null=True, blank=True)
	dispensary_social_profile_URL= models.URLField(null=True, blank=True)

class DispensarySocialFollowURLS(models.Model):
	social_profiles_URLS = models.ManyToManyField(DispensarySocialFollowURL,  blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS) 

class DispensarySocialFollows(models.Model):
	dispensary_social_follows_name= models.CharField(max_length=300, null=True, blank=True)
	social_profiles_URLS = models.ForeignKey(DispensarySocialFollowURLS, on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS) 

class Dispensary(models.Model):
	title = models.CharField(max_length=1000)
	slug = models.SlugField(max_length=1000)
	tagline = models.CharField(max_length=1000)
	websiteURL = models.URLField(max_length=300, null=True, blank=True)
	phone_number = models.CharField(max_length=300, null=True, blank=True)
	email_address = models.EmailField(max_length=300, null=True, blank=True)
	dispensary_logo	= models.ImageField(upload_to='media/CANNABIS_DB/BRAND_LOGOS/', null=True, blank=True)
	dispensary_cover_image	= models.ImageField(upload_to='media/CANNABIS_DB/BRAND_COVERS/', null=True, blank=True)
	dispensarydescription = RichTextField(null=True, blank=True)
	dispensary_social_follow	= models.ForeignKey(BrandSocialFollows, on_delete=models.CASCADE, null=True, blank=True)
	dispensary_products = models.ManyToManyField('Strain', null=True, blank=True)
	dispensary_followers	= models.ManyToManyField(CustomUser)

	def get_absolute_url(self):
		return reverse('cannabis_db:dispensary', args=[self.slug])
	def __str__(self):
		return str(self.title) 
