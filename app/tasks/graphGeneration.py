
# coding: utf-8

# In[316]:


#save the json data into text file
from flask import Flask
from flask import request
import requests
import json
from flask import render_template
import psycopg2
import time
from datetime import datetime
import celery

# In[317]:


#first close the localhost window then interrupt kernel


# #Data Visualization through Graphs

# In[318]:


import pygal
import json
from datetime import datetime
import time
from flask import request


# In[319]:
hostname = 'postgressql-cryptocurrency.cibilq8azida.us-east-2.rds.amazonaws.com'
username = 'acms_user'
password = 'acms1234'
database = 'CryptocurrencyDb'
port = '5432'

"""hostname = 'baasu.db.elephantsql.com'
username = 'dbuzkqmi'
password = 'vi24qSFc5TG77k5GPa4aQr3XlnLOBIRf'
database = 'dbuzkqmi'
port='5432'
"""

@celery.task()
def GraphCreationDay():
	conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database,port=port)
	#conn=connection()
	cur=conn.cursor()    
        for cryptoname in ['BTC','ETH','XRP','LTC']:
	    cur.execute("Refresh materialized view "+cryptoname+"_min;")
	    cur.execute("Refresh materialized view "+cryptoname+"_day;")
	    conn.commit();
            cur.execute("select price_usd_day,last_updated_day from "+cryptoname+"_day ;")
            rows=cur.fetchall()
            #plotting interactive svg
            cryptod_x_axis_data=[]
            cryptod_y_axis_data=[]
            for i in range(len(rows)):
                tupl= rows[i]
                var= tupl[1]
                if type(var)==float:
                    cryptod_x_axis_data.append((datetime.fromtimestamp(tupl[1])).strftime('%Y-%m-%d %H:%M:%S'))
                    cryptod_y_axis_data.append(tupl[0])
            #conn.close()
            chart=pygal.Line(x_label_rotation=45,x_labels_major_every=10,show_minor_x_labels=False)
            chart.x_labels=cryptod_x_axis_data
            chart.add(cryptoname+" day",cryptod_y_axis_data)
            #if you want to download graph uncomment below
            path='/home/urja/flask_app/DataLoader/app/tasks/static/images/'+cryptoname+'Day.svg'
            query =  "INSERT INTO filepath (crypto_name, duration, path) VALUES (%s, %s, %s)"
            data= (cryptoname,'day',path )
            cur.execute(query,data)
            conn.commit()
            chart.render_to_file(path)
            chart=chart.render_data_uri()
	conn.close()
        


# In[320]:

@celery.task()
def GraphCreationMonth():
	conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database,port=port)
	#conn=connection()
	cur=conn.cursor()
        for cryptoname in ['BTC','ETH','XRP','LTC','BCH'] :
	    cur.execute("Refresh materialized view "+cryptoname+"_min;")
	    cur.execute("Refresh materialized view "+cryptoname+"_day;")
	    cur.execute("Refresh materialized view "+cryptoname+"_month;")
	    conn.commit();
            cur.execute("select price_usd_month,last_updated_month from "+cryptoname+"_month ;")
            rows=cur.fetchall()
            #plotting interactive svg
            cryptod_x_axis_data=[]
            cryptod_y_axis_data=[]
            for i in range(len(rows)):
                tupl= rows[i]
                var= tupl[1]
                if type(var)==float:
                    cryptod_x_axis_data.append((datetime.fromtimestamp(tupl[1])).strftime('%Y-%m-%d %H:%M:%S'))
                    cryptod_y_axis_data.append(tupl[0])
            #conn.close()
            chart=pygal.Line(x_label_rotation=45,x_labels_major_every=10,show_minor_x_labels=False)
            chart.x_labels=cryptod_x_axis_data
            chart.add(cryptoname+" month",cryptod_y_axis_data)
            #if you want to download graph uncomment below
            path='/home/urja/flask_app/DataLoader/app/tasks/static/images/'+cryptoname+'month.svg'
            query =  "INSERT INTO filepath (crypto_name, duration, path) VALUES (%s, %s, %s)"
            data= (cryptoname,'month',path )
            cur.execute(query,data)
            conn.commit()
            chart.render_to_file(path)
            chart=chart.render_data_uri()
        #return "Invalid Paramters"
        
        conn.close()

# In[321]:

@celery.task()
def ComparisonGraphDay():
	    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database,port=port)
	    #conn=connection()
	    cur=conn.cursor()
	    
   	    coins=['BTC','ETH','LTC','XRP']
            chart=pygal.Line(x_label_rotation=45,x_labels_major_every=10,show_minor_x_labels=False)
            for cryptoname in coins:

		cur.execute("Refresh materialized view "+cryptoname+"_min;")
	    	cur.execute("Refresh materialized view "+cryptoname+"_day;")
	    	conn.commit();
                cur.execute("select price_usd_day,last_updated_day from {}".format(cryptoname)+"_day;")
                rows=cur.fetchmany(49)    
                cryptod_y_axis_data=[]
                for i in range(len(rows)):
                    tupl= rows[i]
                    var= tupl[1]
                    if type(var)==float:
                        cryptod_y_axis_data.append(tupl[0])
            
                chart.add(cryptoname+" Day",cryptod_y_axis_data)
            cryptod_x_axis_data=[]
    
            for i in range(len(rows)):
                tupl=rows[i]
                var=tupl[1]
                if type(var)==float:
                    cryptod_x_axis_data.append((datetime.fromtimestamp(tupl[1])).strftime('%Y-%m-%d %H:%M:%S'))
            chart.x_labels=cryptod_x_axis_data
            #uncomment next line if you want to save graph in file 
            path='/home/urja/flask_app/DataLoader/app/tasks/static/images/AllDay.svg'
            query =  "INSERT INTO filepath (crypto_name, duration, path) VALUES (%s, %s, %s)"
            data= ('All','day',path )
            cur.execute(query,data)
            conn.commit()
            chart.render_to_file(path)
            #uncomment next 2 lines if graph response embedded in html is needed
            #chart=chart.render_data_uri()
            #return render_template( 'charts.html', chart = chart)
            #return chart.render_response()
            conn.close()


# In[322]:

@celery.task()
def ComparisonGraphMonth():
	    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database,port=port)
	    #conn=connection()
	    cur=conn.cursor()
   	    coins=['BTC','ETH','LTC','XRP','BCH']
            chart=pygal.Line(x_label_rotation=45,x_labels_major_every=10,show_minor_x_labels=False)
            for cryptoname in coins:
	   	cur.execute("Refresh materialized view "+cryptoname+"_min;")	  
	    	cur.execute("Refresh materialized view "+cryptoname+"_day;")
	    	cur.execute("Refresh materialized view "+cryptoname+"_month;")
	    	conn.commit();
                
                cur.execute("select price_usd_month,last_updated_month from {}".format(cryptoname)+"_month;")
                rows=cur.fetchall()    
                cryptod_y_axis_data=[]
                for i in range(len(rows)):
                    tupl= rows[i]
                    var= tupl[1]
                    if type(var)==float:
                        cryptod_y_axis_data.append(tupl[0])
            
                chart.add(cryptoname+" Month",cryptod_y_axis_data)
            cryptod_x_axis_data=[]
    
            for i in range(len(rows)):
                tupl=rows[i]
                var=tupl[1]
                if type(var)==float:
                    cryptod_x_axis_data.append((datetime.fromtimestamp(tupl[1])).strftime('%Y-%m-%d %H:%M:%S'))
            chart.x_labels=cryptod_x_axis_data
            #uncomment next line if you want to save graph in file 
            path='/home/urja/flask_app/DataLoader/app/tasks/static/images/AllMonth.svg'
            query =  "INSERT INTO filepath (crypto_name, duration, path) VALUES (%s, %s, %s)"
            data= ('All','month',path )
            cur.execute(query,data)
            conn.commit()
            chart.render_to_file(path)
            
            #uncomment next 2 lines if graph response embedded in html is needed
            #chart=chart.render_data_uri()
            #return render_template( 'charts.html', chart = chart)
            #return chart.render_response()
            conn.close()


# In[323]:


    
