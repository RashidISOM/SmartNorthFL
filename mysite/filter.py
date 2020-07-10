from .models import Pantry
import django_filters

class PantryFilter(django_filters.FilterSet):

    class Meta:
        model = Pantry
        fields = ['zipCode', 'city', 'state']
