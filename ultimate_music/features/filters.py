import django_filters
from django_filters import CharFilter
from .models import *

class SongFilter(django_filters.FilterSet):

	title = CharFilter(field_name='title', lookup_expr="icontains")
	artist = CharFilter(field_name='artist', lookup_expr="icontains")

	class Meta:
		model = Song
		fields = ['title','artist']