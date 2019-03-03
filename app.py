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

start = datetime.date(2018,1,1)
end = datetime.datetime.now()

df = pd.DataFrame.from_dict(client.get_measurements('Weight',start), orient='index',columns=['value'])


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='My Weight-Web-App!'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.value, 'type': 'line', 'name': 'weight'}
            ],
            'layout': {
                'title': 'Data Visualization of my Weight-Web-App'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)