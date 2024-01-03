from django.contrib import admin
from .models import Article
from .models import Category



# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}