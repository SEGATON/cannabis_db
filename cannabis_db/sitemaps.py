from django.contrib.sitemaps import Sitemap
from .models import Strain, Dispensary, Brand, Product


from django.urls import reverse





class StaticViewsSitemap(Sitemap):
	changefreq = "always"
	priority = 0.8

	def items(self):
		return ["strains", "about_us"]




class StrainsSitemap(Sitemap):
	changefreq = "always"
	priority = 0.8

	def items(self):
		return Strain.objects.all()

class DispensarySitemap(Sitemap):
	changefreq = "always"
	priority = 0.8

	def items(self):
		return Dispensary.objects.all()


class BrandSitemap(Sitemap):
	changefreq = "always"
	priority = 0.8

	def items(self):
		return Brand.objects.all()


class ProductSitemap(Sitemap):
	changefreq = "always"
	priority = 0.8

	def items(self):
		return Product.objects.all()