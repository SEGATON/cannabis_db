from django.contrib import admin

# Register your models here.
from .models import Rating





@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
	pass