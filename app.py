#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:28:27 2019

@author: richard
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
import myfitnesspal
import pandas as pd

client = myfitnesspal.Client('Jollyfella@aol.com')

#start = datetime.date(2018,1,1)
#end = datetime.datetime.now()
start = datetime.datetime(2018,1,1).date()
end = datetime.datetime.now().date()
delta = end - start

df = pd.DataFrame.from_dict(client.get_measurements('Weight',start), orient='index',columns=['value'])



results = []
#   for i in range(delta.days):
for i in range(30):
    x = (datetime.datetime.now().date() - datetime.timedelta(days=i))
    #list
    day = client.get_date(x)
    with_date = day.totals
    with_date['date']=x
    results.append(with_date)

df2=pd.DataFrame.from_records(results)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='My Weight-Web-App!'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='weight',
        figure={
            'data': [
                {'x': df.index, 'y': df.value, 'type': 'line', 'name': 'weight'}
            ],
            'layout': {
                'title': 'Data Visualization of my Weight'
            }
        }
    ),
    
    dcc.Graph(
        id='calories',
        figure={
            'data': [
                {'x': df2.date, 'y': df2.calories, 'type': 'bar', 'name': 'calories'}
            ],
            'layout': {
                'title': 'Daily Total Calories'
            }
        }
    ),
    
    dcc.Graph(
        id='carbs',
        figure={
            'data': [
                {'x': df2.date, 'y': df2.carbohydrates, 'type': 'bar', 'name': 'carbohydrates'}
            ],
            'layout': {
                'title': 'Daily Total Carbs'
            }
        }
    ),
    
    dcc.Graph(
        id='fat',
        figure={
            'data': [
                {'x': df2.date, 'y': df2.fat, 'type': 'bar', 'name': 'fat'}
            ],
            'layout': {
                'title': 'Daily Total Fat'
            }
        }
    ),
    
    dcc.Graph(
        id='protein',
        figure={
            'data': [
                {'x': df2.date, 'y': df2.protein, 'type': 'bar', 'name': 'carbohydrates'}
            ],
            'layout': {
                'title': 'Daily Total Protein'
            }
        }
    )  
])

if __name__ == '__main__':
    app.run_server(debug=True)