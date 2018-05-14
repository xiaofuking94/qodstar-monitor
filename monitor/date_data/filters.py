import django_filters

from .models import DateData

import datetime


class DateDataFilter(django_filters.FilterSet):

	period = django_filters.NumberFilter(name='created', method='filter_period')
	
	def filter_period(self, queryset, name, value):
		if value != 0 and not value:
			return queryset
		date_to = datetime.datetime.today()
		date_from = None
		if value == 0:
			"当月"
			date_from = 1
		
		if value == 1:
			"季度"
			date_from = 90
		
		if value == 2:
			"半年"
			date_from = 180
		
		if value == 3:
			"一年"
			date_from = 365
		if date_from:
			return queryset.filter(created__range=[date_to - datetime.timedelta(days=date_from), date_to])
		else:
			return queryset
	
	class Meta:
		model = DateData
		fields = ('period', )
