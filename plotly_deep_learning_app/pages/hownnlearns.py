#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash_bootstrap_components as dbc
#from app import app
import dash

dash.register_page(__name__,path='/hownnlearns')

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

initial_paragraph_content = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3(html.B("How Neural Network Learns :"))
        ])
    ]),
    dbc.Row([
        dbc.Col([
             html.P('''In this page we will learn how a neural network learns through an interactive way. We will take the MNIST dataset and try to classifiy the handwritten digits, 
                        while doing that we will try visualize each and every step and try to understand the math behind it.
                        This problem is also called the "Hello World" problem of Deep learning.''')
        ])
    ]),
],
fluid=True)


dl_content = dbc.Container([
    dbc.Row([
        dbc.Col(
            [
                html.Div(
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    html.Div(id="visualize_mnist_dataset_div")
                                ],
                                title="Step1 : Visualize MNIST dataset",
                                item_id="visualize_mnist_dataset"
                            ),
                            dbc.AccordionItem(
                                [
                                    html.Div(id="training_mnist_div")
                                ],
                                title="Step2: Model Training",
                                item_id="training_mnist"
                            ),
                            dbc.AccordionItem(
                                [
                                    html.Div(id="testing_mnist_div")
                                ],
                                title="Step2: Model Testing",
                                item_id="testing_mnist"
                            ),
                        ],
                        flush=True,
                        id="dl_accordion"
                    ),
                )
            ]
        )
    ])
],
fluid=True)

layout = html.Div([
    navigation.navbar,
    breadcrumb,
    initial_paragraph_content,
    dl_content
    ]
)


@dash.callback(
    [Output("visualize_mnist_dataset_div","children"),
    Output("training_mnist_div","children"),
    Output("testing_mnist_div","children")],
    [Input("dl_accordion","active_item")]
)
def update_accordion_items(accordion_item):
    visualize_mnist = ""
    training_mnist =""
    testing_mnist = ""
    if accordion_item == "visualize_mnist_dataset":
        visualize_mnist = "This is the content for MNIST viz"
    if accordion_item == "training_mnist":
        training_mnist = "This is the content for Model training"
    if accordion_item == "testing_mnist":
        testing_mnist = "This is the content for Model testing"
    return visualize_mnist,training_mnist,testing_mnist