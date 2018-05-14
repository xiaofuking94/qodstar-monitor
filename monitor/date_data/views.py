from .serializers import DateDataSerializer
from .models import DateData
from .filters import DateDataFilter

from rest_framework import viewsets, response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum

import datetime


# class DateDateViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = DateDataSerializer
#     queryset = DateData.objects.all()
#     filter_backends = (DjangoFilterBackend, )
#     filter_class = DateDataFilter
#
#     def list(self, request, *args, **kwargs):
#         return super(DateDateViewSet, self).list(request, *args, **kwargs)

@api_view(['get'])
def date_data(request):
    query_params = request.query_params
    period = query_params.get('period')
    date_to = datetime.datetime.today()
    date_from = 1
    if period:
        period = int(period)
        if period == 0:
            "当月"
            date_from = 30
    
        elif period == 1:
            "季度"
            date_from = 90
    
        elif period == 2:
            "半年"
            date_from = 180
    
        elif period == 3:
            "一年"
            date_from = 365
    date_data = DateData.objects.filter(created__range=[date_to - datetime.timedelta(days=date_from), date_to]).\
        aggregate(pc_page_view=Sum('pc_page_view'), wx_page_view=Sum('wx_page_view'),
                  increased_user_amount=Sum('increased_user_amount'), jobpost_amount=Sum('jobpost_amount'),
                  invitation_sent_amount=Sum('invitation_sent_amount'), sale_amount=Sum('sale_amount'),
                  potential_user_amount=Sum('potential_user_amount'), new_user_amount=Sum('new_user_amount'),
                  real_user_amount=Sum('real_user_amount'))
    return response.Response(date_data, status=200)
