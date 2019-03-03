#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:28:27 2019

@author: richard
"""
import dash
# Event no longer available in Dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import deque
import datetime
import myfitnesspal
import pandas as pd

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

# Import data from MyFitnessPal
client = myfitnesspal.Client('Jollyfella@aol.com')

# dates
start = datetime.date(2018,1,1)
end = datetime.datetime.now()

df = pd.DataFrame.from_dict(client.get_measurements('Weight',start), orient='index',columns=['value'])


app = dash.Dash(__name__)

app.layout = html.Div(
        [
                dcc.Graph(id='live-graph',animate=True),
                dcc.Interval(
                        id='graph-update',
                        interval=1000
                        )
                ]
        )

@app.callback(Output('live-graph','figure'),
              events=[Event('graph-update','interval')]
              )
def update_graph():
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1,0.1)))
    
    data = go.scatter(
            x=list(X),
            y=list(Y),
            name='scatter',
            mode='lines+markers'
            )
    return{'data':[data],'layout':go.layout(xaxis=dict(range=[min(X),max(X)]),
                                            yaxis=dict(range=[min(Y),max(Y)]))}

                
                
#    dcc.Graph(
#        id='example-gr                
#        figure={
#            'data': [
#                {'x': df.index, 'y': df.value, 'type': 'line', 'name': 'weight'}
#            ],
#            'layout': {
#                'title': 'Data Visualization of my Weight-Web-App'
#            }
#        }
#    )


if __name__ == '__main__':
    app.run_server(debug=True)