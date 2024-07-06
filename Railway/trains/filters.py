from .models import Trains
from django.forms.widgets import TextInput, DateInput
import django_filters

class TrainsFilter(django_filters.FilterSet):

    class Meta:
        model = Trains
        fields = ['source','destination','types','date']
      