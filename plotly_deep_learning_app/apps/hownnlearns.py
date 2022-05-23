#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash_bootstrap_components as dbc


breadcrumb=dbc.Container(
    dbc.Row(
        dbc.Col(
            dbc.Breadcrumb(
                items=[
                    {"label": "Home", "href": "/", "external_link": False},
                    {
                        "label": "Fundamentals"
                    },
                    {"label": "How Neural network Learns", "active": True},
                ],
            )
        )
    ),
    fluid=True
)

page_layout = html.Div([
    navigation.navbar,
    breadcrumb,
    html.H3(children="This is how neural network learns page"),
    ]
)