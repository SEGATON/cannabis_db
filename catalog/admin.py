from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Category


from .models import ProductGalleryImage
from .models import ProductGalleryImages
from .models import ProductGalleryImagesSet

from .models import AttributesSet
from .models import Attribute

from .models import PricingManagement
from .models import StockManagement
from mptt.admin import DraggableMPTTAdmin



from .models import Specification
from .models import SpecificationsSet


from .models import DescriptionList
from .models import DescriptionListItems
from .models import DescriptionListItem


from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets


from .models import ProductVariation
from .models import ProductVariationsSet


from .models import Tag
from .models import TagsSet

from .models import Keywords
from .models import KeywordsSet
from .models import MetasSet

from .models import ShippingSettings

@admin.register(ShippingSettings)
class ShippingSettingsAdmin(admin.ModelAdmin):
    pass

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



@admin.register(TagsSet)
class TagsSetAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass



@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductVariationsSet)
class ProductVariationsSetAdmin(admin.ModelAdmin):
    pass





@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecificationsSet)
class SpecificationsSetAdmin(admin.ModelAdmin):
    pass











@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id','title','slug']
    prepopulated_fields = {
        'slug':('title',)
    }

@admin.register(PricingManagement)
class PricingManagementAdmin(admin.ModelAdmin):
    pass


@admin.register(DescriptionList)
class DescriptionListAdmin(admin.ModelAdmin):
    pass
@admin.register(DescriptionListItems)
class DescriptionListItemsAdmin(admin.ModelAdmin):
    pass
@admin.register(DescriptionListItem)
class DescriptionListItemAdmin(admin.ModelAdmin):
    pass



#admin.site.register(Category)

class CategoryResource(resources.ModelResource):
    parent = fields.Field(
        column_name='parent',
        attribute='parent',
        widget = widgets.ForeignKeyWidget(Category, 'title'))

    class Meta: 
        model = Category
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('title','slug')
        fields = ('parent','title','slug')

        

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, ImportExportModelAdmin):
    resource_class = CategoryResource
    prepopulated_fields = {
        'slug':('title',)
    }   


admin.site.register(StockManagement)
admin.site.register(ProductGalleryImage)
admin.site.register(ProductGalleryImages)
admin.site.register(ProductGalleryImagesSet)

admin.site.register(AttributesSet)

@admin.register(Attribute)
class AttributeAdmin(ImportExportModelAdmin):
    list_display = ['id','title','slug']
    prepopulated_fields = {
        'slug':('title',)
    } 
