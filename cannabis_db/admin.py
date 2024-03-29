from django.contrib import admin
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

from .models import Address

from .models import AromasListSet
from .models import AromasDetailsList
from .models import AromasDetails
from .models import Rating

from .models import StrainKeywords
from .models import StrainKeywordsSet
from .models import StrainMetas

from .models import Dispensary
from .models import Comment
from .models import DispensarySocialFollowURL
from .models import DispensarySocialFollowURLS
from .models import DispensarySocialFollows

from .models import StrainLineageDetailsList
from .models import StrainLineageDetailsListItems
from .models import StrainLineageDetailsListItem

from import_export.admin import ImportExportModelAdmin

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
	pass

@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
	list_display = ['id','address_id_name',
		'address_id_name',
		'phone_number',
		'dispensary_name',
		'street_name_01',
		'street_name_02',
		'street_city',
		'street_state',
		'street_zip_code',
	]
	list_editable = ['address_id_name',
		'address_id_name',
		'phone_number',
		'dispensary_name',
		'street_name_01',
		'street_name_02',
		'street_city',
		'street_state',
		'street_zip_code',
	]
	search_fields = ['address_id_name',
		'address_id_name',
		'phone_number',
		'dispensary_name',
		'street_name_01',
		'street_name_02',
		'street_city',
		'street_state',
		'street_zip_code',
	]
	list_filter = ['address_id_name',
		'address_id_name',
		'phone_number',
		'dispensary_name',
		'street_name_01',
		'street_name_02',
		'street_city',
		'street_state',
		'street_zip_code',
	]
	



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
@admin.register(StrainKeywords)
class StrainKeywordsAdmin(admin.ModelAdmin):
	pass
@admin.register(StrainKeywordsSet)
class StrainKeywordsSetAdmin(admin.ModelAdmin):
	pass
@admin.register(StrainMetas)
class StrainMetasAdmin(admin.ModelAdmin):
	pass








@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}

@admin.register(AromasListSet)
class AromasListSetAdmin(admin.ModelAdmin):
	pass
@admin.register(AromasDetailsList)
class AromasDetailsListAdmin(admin.ModelAdmin):
	pass
@admin.register(AromasDetails)
class AromasDetailsAdmin(admin.ModelAdmin):
	pass




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

@admin.register(TerpeneDetailsList)
class TerpeneDetailsListAdmin(ImportExportModelAdmin):
	pass

@admin.register(TerpeneDetailsListSet)
class TerpeneDetailsListSetAdmin(ImportExportModelAdmin):
	pass


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}
@admin.register(StrainSpecificationsSets)
class StrainSpecificationsSetsAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainSpecifications)
class StrainSpecificationsAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainSpecification)
class StrainSpecificationAdmin(ImportExportModelAdmin):
	list_display = ['id','specification_name','specification_value']
	list_display_links = ['id']
	list_editable = ['specification_name','specification_value']


@admin.register(StrainImageGallery)
class StrainImageGalleryAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainGalleryImagesSet)
class StrainGalleryImagesSetAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainGalleryImage)
class StrainGalleryImageAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainDetailsListItem)
class StrainDetailsListItemAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainDetailsListItems)
class StrainDetailsListItemsAdmin(ImportExportModelAdmin):
	pass

@admin.register(StrainDetailsList)
class StrainDetailsListAdmin(ImportExportModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}

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