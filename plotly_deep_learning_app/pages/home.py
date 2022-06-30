
#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash

dash.register_page(__name__,path='/')

layout = html.Div(children=[
    navigation.navbar,
    html.H3(children="Welcome to Deep Learning Dash app!"),
    # dcc.Link('Home',href="/"),
    # html.Br(),
    # dcc.Link('model-showcase',href="/showcase")
])