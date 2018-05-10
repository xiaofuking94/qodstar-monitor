from date_data.models import DateData

import psycopg2

import datetime


# def update_func():
today = datetime.datetime.today().date()
yestoday = (today - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
with psycopg2.connect(database='qodstar_dev') as conn:
	with conn.cursor() as cursor:
		cursor.execute("select count(distinct i1.owner_id) from invitations_invitation i1 where not EXISTS (select * from invitations_invitation i2 where i2.status >=1 and i2.created <= '{}' and i1.owner_id = i2.owner_id) and i1.created > '{}' and i1.status>=1".format(yestoday, yestoday))
		real_user_amount = cursor.fetchone()[0]
		
		cursor.execute("select count(distinct owner_id) from conversations_sequenceprogress where created >= '{}'".format(yestoday))
		potential_user_amount = cursor.fetchone()[0]
		
		cursor.execute("select count(distinct owner_id) from companies_company where  created >='{}'".format(yestoday))
		new_user_amount = cursor.fetchone()[0]
		
		cursor.execute("select count(DISTINCT owner_id) from companies_company where companies_company.created >= '{}'".format(yestoday))
		increased_user_amount = cursor.fetchone()[0]
		
		cursor.execute("select count(DISTINCT id) from jobposts_jobpost where created >= '{}'".format(yestoday))
		jobpost_amount = cursor.fetchone()[0]
		
		cursor.execute("select count(DISTINCT id) from invitations_invitation where test_sent >= '{}'".format(yestoday))
		invitation_sent_amount = cursor.fetchone()[0]
	
# TODO
pc_page_view = 0
wx_page_view = 0
sale_amount = 0

DateData(real_user_amount=real_user_amount, potential_user_amount=potential_user_amount,
         new_user_amount=new_user_amount, increased_user_amount=increased_user_amount,
		 jobpost_amount=jobpost_amount, invitation_sent_amount=invitation_sent_amount,
		 pc_page_view=pc_page_view, wx_page_view=wx_page_view, sale_amount=sale_amount,
         ).save()
