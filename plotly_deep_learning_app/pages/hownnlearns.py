#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc, ctx
from dash.dependencies import Input, Output
from apps import navigation
import dash_bootstrap_components as dbc
#from app import app
import dash
import tensorflow as tf
import numpy as np
import plotly.express as px
import json
import random
import dash_mantine_components as dmc

dash.register_page(__name__,path='/hownnlearns',title="How neural network learns",description="How neural network learns",image='logo2.png')

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
                        start_collapsed= True,
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

## Callback to update accordion panel items content
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
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    if accordion_item == "visualize_mnist_dataset":
        #visualize_mnist = "This is the content for MNIST viz"
        train_image_labels, train_image_counts = np.unique(y_train, return_counts=True)
        test_image_labels, test_image_counts = np.unique(y_test, return_counts=True)
        training_fig = px.pie(names=train_image_labels,values=train_image_counts,hole=0.3)
        training_fig.update_layout(annotations=[dict(text=str(len(y_train)),x=0.5, y=0.5,font_size = 20, showarrow=False)])
        testing_fig = px.pie(names=test_image_labels,values=test_image_counts,hole=0.3)
        testing_fig.update_layout(annotations=[dict(text=str(len(y_test)),x=0.5, y=0.5,font_size = 20, showarrow=False)])
        card_content_training = [
            dbc.CardHeader("Training dataset distribution"),
            dbc.CardBody(
                [
                    dcc.Graph(figure=training_fig, id="training_fig")
                ]
            ),
        ]
        card_content_testing = [
            dbc.CardHeader("Testing dataset distribution"),
            dbc.CardBody(
                [
                    dcc.Graph(figure=testing_fig, id="testing_fig")
                ]
            ),
        ]
        # card_label_img_display = [
        #     dbc.CardHeader("Click on the donut chart to display image (choosen randomly)"),
        #     dbc.CardBody(
        #         [
        #             html.Div(id="clicked_label_img_div")
        #         ]
        #     ),
        # ]
        visualize_mnist = dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.Card(card_content_training,color="primary",outline=True)
                ],
                width={"size":"6"}),
                dbc.Col([
                    dbc.Card(card_content_testing,color="primary",outline=True)
                ],
                width={"size":"6"}),
            ]),
            dbc.Row([
                dbc.Col([
                    html.Br()
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div(id="clicked_label_img_div")
                    #dbc.Card(card_label_img_display,color="primary",outline=True)
                ])
            ])
        ])
    if accordion_item == "training_mnist":
        training_mnist = html.Div(children=[
            dbc.Container(children=[
                dbc.Row(children=[
                    dmc.ChipGroup(
                        [dmc.Chip(x, value=x) for x in ["Single Neuron", "Neural Network"]],
                        value="Single Neuron",
                        id="training_chip_group"
                    )
                ]),
                dbc.Row(children=[
                    html.Div(id="training_chips_content")
                ])
            ],fluid=True)
            
        ])
    if accordion_item == "testing_mnist":
        testing_mnist = "This is the content for Model testing"
    return visualize_mnist,training_mnist,testing_mnist


## callback for drilldown
@dash.callback(
    [Output("clicked_label_img_div","children")],
    [Input("training_fig","clickData"),
    Input("testing_fig","clickData")],
    prevent_initial_call=True
)
def render_label_img(drilldown_data_training,drilldown_data_testing):
    callback_source= ctx.triggered_id
    source_dataset= ""
    print(callback_source)
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data() # Will fix it later
    if callback_source == "training_fig":
        source_dataset = "Training"
        clicked_label = drilldown_data_training["points"][0]["label"]
        possible_indices = np.where(y_train == int(clicked_label))
        choosen_index = np.random.choice(possible_indices[0])
        fig = px.imshow(x_train[choosen_index])
    if callback_source == "testing_fig":
        source_dataset = "Testing"
        clicked_label = drilldown_data_testing["points"][0]["label"]
        possible_indices = np.where(y_test == int(clicked_label))
        choosen_index = np.random.choice(possible_indices[0])
        fig = px.imshow(x_test[choosen_index])

    card_label_img_display = [
        dbc.CardHeader("Source Dataset : {}, clicked Image : {}, chosen index : {}".format(source_dataset,clicked_label,choosen_index)),
        dbc.CardBody(
            [
                dcc.Graph(figure=fig)
            ]
        ),
    ]
    return [dbc.Card(card_label_img_display,color="primary",outline=True)]


## callback for drilldown
@dash.callback(
    Output("training_chips_content","children"),
    Input("training_chip_group","value"),
)
def render_chipgroup_item_content(selected_chip):
    training_chips_div_content = []
    if selected_chip == "Single Neuron":
        training_chips_div_content = html.Div(children=[
            dbc.Container(children=[
                dbc.Row(children=[
                    dbc.Col(children=[
                        dmc.Stack(
                            [
                                html.Div(children=[
                                    dbc.Label("Choose activation"),
                                    dbc.RadioItems(
                                        options=[
                                            {"label": "Perceptron", "value": "step"},
                                            {"label": "Sigmoid function", "value": "sigmoid"},
                                            {"label": "RELU function", "value": "relu"},
                                            {"label": "tanh function", "value": "tanh"},
                                        ],
                                        value="step",
                                        id="activation-radioitems-input",
                                    ),
                                ]),
                                dbc.InputGroup(
                                    [dbc.InputGroupText("X1"), dbc.Input(placeholder="",id="x1",value=0),
                                     dbc.InputGroupText("W1"), dbc.Input(placeholder="",id="w1",value=0)],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [dbc.InputGroupText("X2"), dbc.Input(placeholder="",id="x2",value=0),
                                     dbc.InputGroupText("W2"), dbc.Input(placeholder="",id="w2",value=0)],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [dbc.InputGroupText("X3"), dbc.Input(placeholder="",id="x3",value=0),
                                     dbc.InputGroupText("W3"), dbc.Input(placeholder="",id="w3",value=0)],
                                    className="mb-3",
                                ),
                                dbc.InputGroup(
                                    [dbc.InputGroupText("b"), dbc.Input(placeholder="",id="b",value=0)],
                                    className="mb-3",
                                ),
                                dbc.Button("Run", color="success", className="me-1"),
                                
                            ],
                            align="left",
                            spacing="sm",
                        )
                    ],width=2),
                    dbc.Col(children=[],width=4),
                    dbc.Col(children=[],width=6),
                ],justify="center",align="center")
            ],fluid=True)
        ],style={"margin":"20px"})
    elif selected_chip == "Neural Network":
        training_chips_div_content = []
    return training_chips_div_content
