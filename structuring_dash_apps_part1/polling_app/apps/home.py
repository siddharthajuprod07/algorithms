
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output



home_layout = html.Div(children=[
    html.H1(children="Welcome to the dash Polling app!"),
    dcc.Link('Home',href="/"),
    html.Br(),
    dcc.Link('Polls',href="/polls"),
    html.Br(),
    dcc.Link('Poll Results',href="/poll-results")
])