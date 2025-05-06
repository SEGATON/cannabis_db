from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField



from django.conf import settings
from accounts.models import CustomUser

from mptt.models import MPTTModel, TreeForeignKey












class BrandSocialFollowURL(models.Model):

	brand_social_profile_name		= models.CharField(max_length=300, null=True, blank=True)
	brand_social_profile_URL		= models.URLField(null=True, blank=True)
class BrandSocialFollowURLS(models.Model):
	social_profiles_URLS 		= models.ManyToManyField(BrandSocialFollowURL,  blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS)
class BrandSocialProfile(models.Model):
	brand_social_follows_name	= models.CharField(max_length=300, null=True, blank=True)
	social_profiles_URLS 		= models.ForeignKey(BrandSocialFollowURLS, on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS)



class Brand(models.Model):
	title = models.CharField(max_length=1000, null=True, blank=True)
	slug = models.SlugField(max_length=1000)

	brand_metas = models.ForeignKey('cannabis_db.MetasSet', on_delete=models.CASCADE,  null=True, blank=True, related_name='brand_meta_set')

	tagline = models.CharField(max_length=1000, null=True, blank=True)
	
	websiteURL = models.URLField(max_length=300, null=True, blank=True)
	phone_number = models.CharField(max_length=300, null=True, blank=True)
	email_address = models.EmailField(max_length=300, null=True, blank=True)
	
	brand_logo	= models.ImageField(upload_to='media/CANNABIS_DB/BRAND_LOGOS/', null=True, blank=True)
	brand_cover	= models.ImageField(upload_to='media/CANNABIS_DB/BRAND_COVERS/', null=True, blank=True)

	brand_address = models.ManyToManyField('addresses.Address', null=True, blank=True, related_name='catalog_brand_address')
	
	description = RichTextField(null=True, blank=True)
	
	
	brand_social_profile	= models.ForeignKey(BrandSocialProfile, on_delete=models.CASCADE, null=True, blank=True)
	

	brand_products = models.ManyToManyField('catalog.Product', null=True, blank=True, related_name='catalog_brand_products')
	brand_strains = models.ManyToManyField('cannabis_db.Strain', null=True, blank=True, related_name='catalog_brand_strains')
	
	brand_followers	= models.ManyToManyField('memberships.Profile',  null=True, blank=True, related_name='catalog_brand_followers')

	dispensary = models.ManyToManyField('cannabis_db.Dispensary',null=True, blank=True , related_name='catalog_brand_dispensary')

	author = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='catalog_brand_author')
	
	claimed = models.BooleanField(default=False,null=True, blank=True )

	date_created = models.DateTimeField(auto_now_add=True, null=True,blank=True)
	date_updated = models.DateTimeField(null=True,blank=True)
	date_deleted = models.DateTimeField(null=True,blank=True)


	def get_absolute_url(self):
		return reverse('cannabis_db:brand', args=[self.slug])
	def __str__(self):
		return str(self.title)


























class Keywords(models.Model):
	keyword 			= models.CharField(max_length=300)

	def __str__(self):
		return str(self.keyword)


class KeywordsSet(models.Model):
	keywords 			= models.ManyToManyField(Keywords)

	def __str__(self):
		return str(self.keywords)


class MetasSet(models.Model):
	ms_UNIQUE_ID 	= models.CharField(max_length=160)
	strain_meta_description = models.TextField(max_length=160,null=True, blank=True)
	strain_meta_keywords 	= models.ForeignKey(KeywordsSet, on_delete=models.CASCADE ,max_length=300,null=True, blank=True )

	def __str__(self):
		return str(self.ms_UNIQUE_ID)





class ShippingSettings(models.Model):
	ss_UNIQUE_ID = models.CharField(max_length=50)
	WEIGHT_LABEL = (
			('gm','Gm'),
			('kg','Kg'),
			('ounce','Oz'),
			('lbs','Lb'),
		)

	weight_label = models.CharField(max_length=50,choices=WEIGHT_LABEL,null=True, blank=True)

	dimension_length = models.DecimalField(max_digits=9, decimal_places=2)
	dimension_width = models.DecimalField(max_digits=9, decimal_places=2)
	dimension_height = models.DecimalField(max_digits=9, decimal_places=2)







class Tag(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)

class TagsSet(models.Model):
	ts_UINIQUE_ID = models.CharField(max_length=50)
	tags = models.ManyToManyField(Tag)
'''
class Brand(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)

	description = RichTextField(max_length=1000,null=True,blank=True)
	
	brand_logo = models.ImageField(upload_to='media/DJANGO_ECOMMERCE/BRANDS/BRANDS_LOGOS/', default='')

	products = models.ManyToManyField('Product',null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	date_deleted = models.DateTimeField()	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Brands'

	def get_absolute_url(self):
		return reverse('django_ecommerce:brand', args=[self.slug])

'''


class Category(MPTTModel):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	
	description = RichTextField(max_length=1000,null=True,blank=True)
	
	category_icon = models.ImageField(upload_to='media/DJANGO_ECOMMERCE/CATEGORIES/CATEGORY_ICONS/', default='', null=True, blank=True)

	products = models.ManyToManyField('Product',null=True,blank=True)
	
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	date_deleted = models.DateTimeField()
	def __str__(self):
		return self.title

	class MPTTMeta:
		verbose_name_plural = 'Categories'
		order_insertion_by = ['title']

	def get_absolute_url(self):
		return reverse('django_ecommerce:category', args=[self.slug])



############# SPECIFICATIONS STARTS #############


class Specification(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)

	specification_label = models.CharField(max_length=1000, null=True, blank=True)
	specification_value = models.CharField(max_length=1000, null=True, blank=True)
	
	specification_details = RichTextField(max_length=300, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('django_ecommerce:specification', args=[self.slug])



class SpecificationsSet(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)

	specifications = models.ManyToManyField(Specification,null=True,blank=True)


############# SPECIFICATIONS ENDS #############



############# ATTRIBUTES STARTS #############


class Attribute(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)

	attribute_details = RichTextField(max_length=300, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('django_ecommerce:attribute', args=[self.slug])


class AttributesSet(models.Model):
	as_UNIQUE_ID = models.CharField(max_length=255)

	attributes = models.ManyToManyField(Attribute,null=True,blank=True)
	


############# ATTRIBUTES ENDS #############


############# IMAGE GALLERY STARTS #############


class ProductGalleryImage(models.Model):
	image = models.ImageField(upload_to='media/DJANGO_ECOMMERCE/PRODUCT_GALLERY_IMAGES', default='')

class ProductGalleryImages(models.Model):
	gallery_images = models.ManyToManyField(ProductGalleryImage)

class ProductGalleryImagesSet(models.Model):
	pgis_UNIQUE_ID = models.CharField(max_length=255)
	gallery_images_set = models.ForeignKey(ProductGalleryImages, on_delete=models.CASCADE, null=True, blank=True)


#############  IMAGE GALLERY ENDS  #############



class StockManagement(models.Model):
	sm_UNIQUE_ID = models.CharField(max_length=255)
	STOCK_STATUS = (
			('out_of_stocl','Out of stock',),
			('in_stock','In stock',),
			('backordered','Backordered',),
		)

	stock_status = models.CharField(max_length=255, choices=STOCK_STATUS)

	stock_quantity = models.IntegerField()

	low_stock_alert = models.BooleanField(default=False )
	low_stock_alert_min = models.IntegerField()


class PricingManagement(models.Model):
	p_UNIQUE_ID = models.CharField(max_length=255)
	price_sale = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
	price_regular = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)



class DescriptionListItem(models.Model):
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	description_list_item_short_description = RichTextField(max_length=30000,null=True,blank=True)
	description_list_item_image = models.ImageField(upload_to='media/DJANGO_ECOMMERCE/PRODUCTS/DESCRIPTION_LIST_ITEMS_IMAGES/', default='')



class DescriptionListItems(models.Model):
	description_list_items = models.ManyToManyField(DescriptionListItem,  null=True, blank=True)



class DescriptionList(models.Model):
	dl_UNIQUE_ID = models.CharField(max_length=255)
	description_list_items = models.ForeignKey(DescriptionListItems, on_delete=models.CASCADE)



############################################################



class ProductVariation(models.Model):

	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	variation_SKU = models.CharField(max_length=50,null=True, blank=True)
	variation_thumbnail = models.ImageField(upload_to='media/DJANGO_ECOMMERCE/PRODUCTS/VARIATIONS/VARIATIONS_THUMBNAILS/', default='')
	variation_product_gallery = models.ForeignKey(ProductGalleryImagesSet, on_delete=models.CASCADE, null=True,blank=True)
	variation_pricing_management = models.ForeignKey(PricingManagement, on_delete=models.CASCADE, null=True, blank=True)
	variation_stock_management = models.ForeignKey(StockManagement, on_delete=models.CASCADE, null=True, blank=True)
	variation_attributes_set = models.ForeignKey(AttributesSet, on_delete=models.CASCADE, null=True, blank=True)
	variation_short_description = RichTextField(max_length=30000,null=True,blank=True)
	variation_full_description = RichTextField(max_length=30000,null=True,blank=True)
	variation_description_list_set = models.ForeignKey(DescriptionList, on_delete=models.CASCADE, max_length=255, null=True, blank=True)

class ProductVariationsSet(models.Model):
	pvs_UNIQUE_ID = models.CharField(max_length=255)
	variations = models.ManyToManyField(ProductVariation)

############################################################




class Product(models.Model):


	PRODUCT_STATUS = (
			('inactive','Inactive'),
			('pending','Pending'),
			('active','Active'),

		)

	product_status = models.CharField(max_length=255, choices=PRODUCT_STATUS, null=True, blank=True )

	PRODUCT_VISIBILITY = (
			('hidden','Hidden'),
			('private','Private'),
			('visible','Visible'),
		
		)

	product_visibility = models.CharField(max_length=255, choices=PRODUCT_VISIBILITY, null=True, blank=True )
	
	PRODUCT_TYPE = (
			('single_product','Single product'),
			('variable_product','Variable product'),
			('digital_product','Digital product'),
			('dropship_product','Dropship product'),


		)

	product_type = models.CharField(max_length=255, choices=PRODUCT_TYPE, null=True, blank=True )

	product_metas_set = models.ForeignKey(MetasSet, on_delete=models.CASCADE, related_name='strain_metas', null=True, blank=True)

	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	
	authors = models.ManyToManyField(CustomUser)
	
	short_description = RichTextField(max_length=30000,null=True,blank=True)
	full_description = RichTextField(max_length=30000,null=True,blank=True)

	description_list_set = models.ForeignKey(DescriptionList, on_delete=models.CASCADE, max_length=255, null=True, blank=True)

	brands = models.ForeignKey('cannabis_db.Brand', on_delete=models.CASCADE, null=True, blank=True)
	
	featured_image = models.ImageField(upload_to='media/DJANGO_ECOMMERCE/PRODUCTS/FEATURED_IMAGES/', default='')

	product_gallery = models.ForeignKey(ProductGalleryImagesSet, on_delete=models.CASCADE, null=True,blank=True)
	
	categories = models.ManyToManyField(Category, null=True,blank=True)

	attributes_set = models.ForeignKey(AttributesSet, on_delete=models.CASCADE, null=True, blank=True)

	specifications_set = models.ForeignKey(SpecificationsSet, on_delete=models.CASCADE, null=True, blank=True)
	stock_management = models.ForeignKey(StockManagement, on_delete=models.CASCADE, null=True, blank=True)

	pricing_management = models.ForeignKey(PricingManagement, on_delete=models.CASCADE, null=True, blank=True)

	on_sale = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	bestseller = models.BooleanField(default=False)

	product_variations = models.ForeignKey(ProductVariationsSet, on_delete=models.CASCADE,null=True, blank=True) # only if product_type variable_product=True

	product_SKU = models.CharField(max_length=255, null=True, blank=True)
	product_UPC = models.CharField(max_length=255, null=True, blank=True)

	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	date_deleted = models.DateTimeField()

	tags_set = models.ForeignKey(TagsSet, on_delete=models.CASCADE, null=True, blank=True)

	shipping_settings = models.ForeignKey(ShippingSettings, on_delete=models.CASCADE, null=True, blank=True)

	dispensaries = models.ManyToManyField('cannabis_db.Dispensary', null=True, blank=True)

	def __str__(self):

		return self.title
		
	class Meta:

		verbose_name_plural = 'Products'


	def get_absolute_url(self):

		return reverse('catalog:product', args=[self.slug])



