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

from .models import StrainSpecification

from .models import TerpeneDetails


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


from .models import FeelingReportListSet
from .models import FeelingReportList
from .models import FeelingReport
from .models import Potency

class StrainFilter(django_filters.FilterSet):


	
	title = django_filters.CharFilter(lookup_expr='icontains')

	brand = django_filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all())
	strain_type = django_filters.ModelMultipleChoiceFilter(queryset=StrainType.objects.all())
	dispensaries = django_filters.ModelMultipleChoiceFilter(queryset=Dispensary.objects.all())
	feelings = django_filters.ModelMultipleChoiceFilter(queryset=FeelingReport.objects.all())
	terpenes_reports = django_filters.ModelMultipleChoiceFilter(queryset=TerpeneDetails.objects.all())
	may_relieve = django_filters.ModelMultipleChoiceFilter(queryset=HelpsWithReport.objects.all())
	flavors = django_filters.ModelMultipleChoiceFilter(queryset=FlavorsDetails.objects.all())
	release_year = django_filters.DateRangeFilter(field_name='date_created', lookup_expr='year')
	potency = django_filters.ModelMultipleChoiceFilter(queryset=Potency.objects.all())
	aromas = django_filters.ModelMultipleChoiceFilter(queryset=AromasDetails.objects.all())
	class Meta:
		model = Strain
		fields = ['title','brand','strain_type','dispensaries','feelings','terpenes_reports','may_relieve','flavors','potency','aromas']
		



















































