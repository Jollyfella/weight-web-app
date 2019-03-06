#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:26:49 2019

@author: richard
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
import myfitnesspal
import pandas as pd
import datetime

client = myfitnesspal.Client('Jollyfella@aol.com')

start = datetime.datetime(2018,1,1).date()
end = datetime.datetime.now().date()
delta = end - start
print(start)
print(end)
print(delta.days)
print('total number of days: ' + str(delta.days))

#df = pd.DataFrame.from_dict(client.get_measurements('Weight',start), orient='index',columns=['value'])

#df_dat = pd.DataFrame.from_dict(client.get_date(2019, 2, 25),orient='index',columns=['sodium'])

#day = client.get_date(2019, 2, 25)

#req_cals = 1977
#
day = client.get_date(end)
#print(day)
#
#total_cals = day.totals['calories']
#print(total_cals)
#print('Days Total calories: '+ str(total_cals))
#print('Calories left: ' + str(req_cals - total_cals))

#dinner = day['dinner']
#print(dinner)
#tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1))
#print(tomorrow)

#def daily_nutritional_totals(date, measure='calories'):
#    day = client.get_date(date)
#    totals = day.totals[measure]
#    return totals

#print(daily_nutritional_totals(end,'fat'))
#i=3
#x = (datetime.datetime.now().date() - datetime.timedelta(days=i))
#day = client.get_date(x)
#print(day)

results = []
for i in range(20):
    x = (datetime.datetime.now().date() - datetime.timedelta(days=i))
    #list
    day = client.get_date(x)
    with_date = day.totals
    with_date['date']=x
    results.append(with_date)
    
    df2=pd.DataFrame.from_records(results)
    
#
#print(results_date)


#app = dash.Dash()
#
#app.layout = html.Div(children=[
#    html.H1(children='My Weight-Web-App!'),
#
#    html.Div(children='''
#        Dash: A web application framework for Python.
#    '''),
#
#    dcc.Graph(
#        id='example-graph',
#        figure={
#            'data': [
#                {'x': df.index, 'y': df.value, 'type': 'line', 'name': 'weight'}
#            ],
#            'layout': {
#                'title': 'Data Visualization of my Weight-Web-App'
#            }
#        }
#    )
#])

#if __name__ == '__main__':