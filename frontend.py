#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 00:20:01 2019

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

app = dash.Dash('Weight-Web-App Frontend')

data_dict = {'Weight':weight,
             'BMI':bmi    
        }

