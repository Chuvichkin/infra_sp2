from django_filters import rest_framework as filters

from reviews.models import Title


class TitleFilters(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    genre = filters.CharFilter(field_name='genre__slug',)
    category = filters.CharFilter(field_name='category__slug',)

    class Meta:
        model = Title
        fields = ('year',)
