from django.contrib import admin
from .models import Strain
from .models import Brand
from .models import StrainType

from .models import StrainSpecificationsSets
from .models import StrainDetailsListItems
from .models import StrainDetailsList

from .models import ImageGallery
from .models import GalleryImagesSet
from .models import GalleryImage

from .models import DispensarySocialFollowURLICON

from .models import StrainSpecification

from .models import TerpeneDetailsSet
from .models import TerpeneDetails
from .models import TerpeneValue
#from .models import Terpene
from .models import TerpeneIcon
from .models import TerpeneDetailsItem


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

from .models import ContactMessage
from .models import AromasListSet
from .models import AromasDetailsList
from .models import AromasDetails


from .models import Keywords
from .models import KeywordsSet
from .models import MetasSet

from .models import Dispensary

from .models import DispensarySocialFollowURL
from .models import DispensarySocialFollowURLS
from .models import DispensarySocialFollows

from .models import StrainLineageDetailsList
from .models import StrainLineageDetailsListItems
from .models import StrainLineageDetailsListItem

from .models import EffectReport
from .models import EffectReportList
from .models import EffectsReportListSet

from .models import Potency
from .models import Category


from .models import  NewslettersSubscriptions

from import_export.admin import ImportExportModelAdmin


from .models import TerpeneProfile

@admin.register(TerpeneProfile)
class TerpeneProfileAdmin(ImportExportModelAdmin):
	pass

'''
@admin.register(Terpene)
class TerpeneAdmin(ImportExportModelAdmin):
	pass
'''
@admin.register(TerpeneValue)
class TerpeneValueAdmin(admin.ModelAdmin):
	pass

@admin.register(TerpeneIcon)
class TerpeneIconAdmin(admin.ModelAdmin):
	pass

@admin.register(TerpeneDetailsSet)
class TerpeneDetailsSetAdmin(admin.ModelAdmin):
	pass
@admin.register(TerpeneDetailsItem)
class TerpeneDetailsItemAdmin(admin.ModelAdmin):
	pass






@admin.register(NewslettersSubscriptions)
class NewslettersSubscriptionsAdmin(ImportExportModelAdmin):
	pass

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass





@admin.register(Potency)
class PotencyAdmin(ImportExportModelAdmin):
	pass


@admin.register(DispensarySocialFollowURLICON)
class DispensarySocialFollowURLICONAdmin(admin.ModelAdmin):
	pass


@admin.register(EffectReport)
class EffectReportAdmin(admin.ModelAdmin):
	pass


@admin.register(EffectReportList)
class EffectReportListAdmin(admin.ModelAdmin):
	pass


@admin.register(EffectsReportListSet)
class EffectsReportListSetAdmin(admin.ModelAdmin):
	pass








@admin.register(StrainLineageDetailsList)
class StrainLineageDetailsListAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}
@admin.register(StrainLineageDetailsListItems)
class StrainLineageDetailsListItemsAdmin(admin.ModelAdmin):
	pass
@admin.register(StrainLineageDetailsListItem)
class StrainLineageDetailsListItemAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}





@admin.register(DispensarySocialFollowURL)
class DispensarySocialFollowURLAdmin(admin.ModelAdmin):
	pass
@admin.register(DispensarySocialFollowURLS)
class DispensarySocialFollowURLSAdmin(admin.ModelAdmin):
	pass
@admin.register(DispensarySocialFollows)
class DispensarySocialFollowsAdmin(admin.ModelAdmin):
	pass








@admin.register(Dispensary)
class DispensaryAdmin(ImportExportModelAdmin):
	list_display = ['id','title','slug','dispensary_logo','phone_number','email_address']
	prepopulated_fields = {
		'slug':('title',)
	}
	list_display_links = ['id']
	list_editable = ['title','slug','dispensary_logo','phone_number','email_address']
	search_fields = ['id','title','slug','dispensary_logo']
@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
	pass
@admin.register(KeywordsSet)
class KeywordsSetAdmin(admin.ModelAdmin):
	pass
@admin.register(MetasSet)
class MetasAdmin(ImportExportModelAdmin):
	list_display = ['id','ms_UNIQUE_ID']
	list_editable = ['ms_UNIQUE_ID']








@admin.register(AromasListSet)
class AromasListSetAdmin(admin.ModelAdmin):
	pass
@admin.register(AromasDetailsList)
class AromasDetailsListAdmin(admin.ModelAdmin):
	pass

@admin.register(AromasDetails)
class AromasDetailsAdmin(ImportExportModelAdmin):
	list_display = ['id','title','slug','aromas_icon']
	prepopulated_fields = {
		'slug':('title','aromas_icon')
	}
	list_editable = ['title','slug','aromas_icon']




@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	pass

@admin.register(FlavorsDetailsListSet)
class FlavorsDetailsListSetAdmin(ImportExportModelAdmin):
	pass
@admin.register(FlavorsDetailsList)
class FlavorsDetailsListAdmin(ImportExportModelAdmin):
	pass
@admin.register(FlavorsDetails)
class FlavorsDetailsAdmin(ImportExportModelAdmin):
	list_display = ['id','title','slug','flavor_icon']
	prepopulated_fields = {
		'slug':('title',)
	}
	list_display_links = ['id']
	list_editable = ['title','slug','flavor_icon']



@admin.register(HelpsWithReport)
class HelpsWithReportAdmin(ImportExportModelAdmin):
	list_display = ['id','title','slug','description','helps_with_icon']
	list_display_links = ['id']
	list_editable = ['title','slug','helps_with_icon']
@admin.register(HelpsWithReportList)
class HelpsWithReportListAdmin(ImportExportModelAdmin):
	pass
@admin.register(HelpsWithReportListSet)
class HelpsWithReportListSetAdmin(ImportExportModelAdmin):
	pass


@admin.register(FeelingReport)
class FeelingReportAdmin(ImportExportModelAdmin):
	list_display = ['id','title','slug','description','type_of_feelings','feeling_icon']
	list_display_links = ['id']
	list_editable = ['title','slug','type_of_feelings','feeling_icon']
	search_fields = ['title','slug','type_of_feelings','feeling_icon']

@admin.register(FeelingReportList)
class FeelingReportListAdmin(ImportExportModelAdmin):
	pass

@admin.register(FeelingReportListSet)
class FeelingReportListSetAdmin(ImportExportModelAdmin):
	pass


@admin.register(TerpeneDetails)
class TerpeneDetailsAdmin(ImportExportModelAdmin):
	pass





@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
	list_display = ['id','title','slug','brand_logo']
	prepopulated_fields = {
		'slug':('title',)
	}
	list_editable = ['brand_logo','title','slug']
@admin.register(StrainSpecificationsSets)
class StrainSpecificationsSetsAdmin(ImportExportModelAdmin):
	list_display = ['id','sss_UNIQUE_ID']
	list_display_links = ['id']
	list_editable = ['sss_UNIQUE_ID']

@admin.register(StrainSpecification)
class StrainSpecificationAdmin(ImportExportModelAdmin):
	list_display = ['id','title','specification_value']
	list_display_links = ['id']
	list_editable = ['title','specification_value']


@admin.register(ImageGallery)
class ImageGalleryAdmin(ImportExportModelAdmin):
	pass

@admin.register(GalleryImagesSet)
class GalleryImagesSetAdmin(ImportExportModelAdmin):
	pass

@admin.register(GalleryImage)
class GalleryImageAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainDetailsListItems)
class StrainDetailsListItemsAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainDetailsList)
class StrainDetailsListAdmin(ImportExportModelAdmin):
	pass

@admin.register(Strain)
class StrainAdmin(ImportExportModelAdmin):
	list_display = ['id','title','slug','featured_image']
	list_display_links = ['id']
	prepopulated_fields = {
		'slug':('title',)
	}
	list_editable = ['title','slug','featured_image']
	search_fields = ['title','slug'] 

@admin.register(StrainType)
class StrainTypeAdmin(ImportExportModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}