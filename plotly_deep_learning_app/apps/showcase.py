import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import os
from app import app



model_showcase_layout = html.Div(children=[
    html.H1(children="This is model showcase page"),
    dcc.Link('Home',href="/"),
    html.Br()
])


