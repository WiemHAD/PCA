#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:30:48 2020

@author: wiem
"""

import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

#html.Img(src=app.get_asset_url('my-image.png'))