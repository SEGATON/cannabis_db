import django_filters

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

from .models import DispensarySocialFollowURL
from .models import DispensarySocialFollowURLS
from .models import DispensarySocialFollows

from .models import StrainLineageDetailsList
from .models import StrainLineageDetailsListItems
from .models import StrainLineageDetailsListItem



class StrainFilter(django_filters.FilterSet):
	
	title = django_filters.CharFilter(looup_expr='icontains')

	class Meta:
		model = Strain
		fields = ['title']

	@property
	def qs(self):
		parent = super().qs

		return 
	


















































