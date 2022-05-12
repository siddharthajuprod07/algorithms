#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation



page_layout = html.Div([
    navigation.navbar,
    html.H3(children="This is deep learning fundamentals page"),
    ]
)