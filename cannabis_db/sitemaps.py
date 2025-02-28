from django.contrib.sitemaps import Sitemap
from .models import Strain, Dispensary, Brand, Product


from django.urls import reverse





class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [ 'cannabis_db:browse_strains', 'cannabis_db:about_us','cannabis_db:contact']

    def location(self, item):
        return reverse(item)



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