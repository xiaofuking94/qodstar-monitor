from rest_framework import serializers

from .models import DateData


class DateDataSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = DateData
		fields = '__all__'
		extra_kwargs = {'': {'allow_null': True}}
		
	# def get_pc_page_view(self, obj):
	#
