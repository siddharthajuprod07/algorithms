import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


polls_results_layout = html.Div(children=[
    html.H1(children="This is Poll Results page"),
    dcc.Link('Home',href="/")
])