from django.contrib.sitemaps import Sitemap
from .models import Strain


from django.urls import reverse


class StrainsSitemap(Sitemap):
	changefreq = "always"
	priority = 0.8

	def items(self):
		return Strain.objects.all()