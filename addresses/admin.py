from django.contrib import admin

# Register your models here.
from .models import Address

from import_export.admin import ImportExportModelAdmin

@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
	list_display = ['id',
		'a_UNIQUE_ID',
		'user',
		'address_type',
		'address_street_name_line_1',
		'address_street_name_line_2',
		'address_city',
		'address_state',
		'address_zip_code',
		'address_country',
		'notes',

	]
	list_editable = ['a_UNIQUE_ID',
		'user',
		'address_type',
		'address_street_name_line_1',
		'address_street_name_line_2',
		'address_city',
		'address_state',
		'address_zip_code',
		'address_country',
		'notes',
	]
	search_fields = ['a_UNIQUE_ID',
		'user',
		'address_type',
		'address_street_name_line_1',
		'address_street_name_line_2',
		'address_city',
		'address_state',
		'address_zip_code',
		'address_country',
		'notes',
	]
	list_filter = ['a_UNIQUE_ID',
		'user',
		'address_type',
		'address_street_name_line_1',
		'address_street_name_line_2',
		'address_city',
		'address_state',
		'address_zip_code',
		'address_country',
		'notes',
	]
	