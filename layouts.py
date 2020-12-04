#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:32:59 2020

@author: wiem
"""

import dash_core_components as dcc
import dash_html_components as html
from app import app

layout1 = html.Div([
    html.H3('App 1'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 2', href='/apps/app2')
])


layout2 = html.Div([
    html.H3('2nd Page: Graphs'),
    html.Div(html.Img(id='image',src=app.get_asset_url('eboulis_valeurs_propres.png'))),
    html.Div(html.Img(id='image',src=app.get_asset_url('cercle_correlation1.png'))),
    html.Div(html.Img(id='image',src=app.get_asset_url('cercle_correlation2.png'))),
    html.Div(html.Img(id='image',src=app.get_asset_url('ecercle_correlation3.png'))),
            ]
    ),
html.Div(id='app-2-display-value'),
dcc.Link('Go to App 1', href='/apps/app1')


