from .models import DateData

from rest_framework import response
from rest_framework.decorators import api_view
from django.db.models import Sum

import datetime


@api_view(['get'])
def date_data(request):
    query_params = request.query_params
    period = query_params.get('period')
    today = datetime.datetime.today()
    month = today.month
    year = today.year
    from_current_date = today.date()
    to_current_date = today.date() + datetime.timedelta(days=1)
    from_last_date = today.date() - datetime.timedelta(days=1)
    to_last_date = today.date()
    if period:
        period = int(period)
        if period == 0:
            "当月"
            from_current_date = datetime.date(year, month, 1)
            if month == 1:
                year -= 1
                month = 13
            from_last_date = datetime.date(year, month - 1, 1)
            to_last_date = from_current_date
    
        elif period == 1:
            "季度"
            if month in (1, 2, 3):
                from_current_date = datetime.date(year, 1, 1)
                from_last_date = datetime.date(year - 1, 10, 1)
                to_last_date = from_current_date
            elif month in (4, 5, 6):
                from_current_date = datetime.date(year, 4, 1)
                from_last_date = datetime.date(year, 1, 1)
                to_last_date = from_current_date
            elif month in (7, 8, 9):
                from_current_date = datetime.date(year, 7, 1)
                from_last_date = datetime.date(year, 4, 1)
                to_last_date = from_current_date
            else:
                from_current_date = datetime.date(year, 10, 1)
                from_last_date = datetime.date(year, 7, 1)
                to_last_date = from_current_date
                
        elif period == 2:
            "半年"
            if month < 7:
                from_current_date = datetime.date(year, 1, 1)
                from_last_date = datetime.date(year - 1, 7, 1)
                to_last_date = from_current_date
            else:
                from_current_date = datetime.date(year, 7, 1)
                from_last_date = datetime.date(year, 1, 1)
                to_last_date = from_current_date
    
        elif period == 3:
            "一年"
            from_current_date = datetime.date(year, 1, 1)
            from_last_date = datetime.date(year - 1, 1, 1)
            to_last_date = from_current_date
    
    current_data = filter_date_data(created__range=[from_current_date, to_current_date])
    last_data = filter_date_data(created__range=[from_last_date, to_last_date])
    data = {'current_data': current_data, 'last_data': last_data}
    return response.Response(data, status=200)


def filter_date_data(**conditions):
  
    return DateData.objects.filter(**conditions).aggregate(pc_page_view=Sum('pc_page_view'),
                                                           wx_page_view=Sum('wx_page_view'),
                                                           increased_user_amount=Sum('increased_user_amount'),
                                                           jobpost_amount=Sum('jobpost_amount'),
                                                           invitation_sent_amount=Sum('invitation_sent_amount'),
                                                           sale_amount=Sum('sale_amount'),
                                                           potential_user_amount=Sum('potential_user_amount'),
                                                           new_user_amount=Sum('new_user_amount'),
                                                           real_user_amount=Sum('real_user_amount'))
