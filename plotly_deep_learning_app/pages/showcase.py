#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import os
#from app import app
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import decode_predictions,preprocess_input
from tensorflow.keras import utils
import numpy as np
from dash import dash_table
from apps import navigation
import dash
import dash_uploader as du
import uuid

dash.register_page(__name__,path_template='/showcase/<model_id>',title="Deep learning models")

# IMAGE_DATASET_HOME = os.path.join(os.path.dirname(__file__),'..','datasets','images')
# imagefiles_list = [f for f in os.listdir(IMAGE_DATASET_HOME) if os.path.isfile(os.path.join(IMAGE_DATASET_HOME,f))]
upload_id = uuid.uuid1()

# layout = html.Div(children=[
#     navigation.navbar,
#     # html.H1(children="This is model showcase page"),
#     # dcc.Link('Home',href="/"),
#     html.Br(),
#     html.H3(children="1. Classify image using resnet50"),
#     html.Div([
#         "Select an Image:",
#         dcc.Dropdown(id="image-dropdown",
#         options=[{'label': i, 'value': os.path.join(IMAGE_DATASET_HOME,i)} for i in imagefiles_list])
#     ]),
#     html.Div(id="output-image-upload")
# ])

def layout(model_id=None):
    showcase_page_layout = ""
    if model_id == "resnet50":
        showcase_page_layout =  html.Div(children=[
                                    navigation.navbar,
                                    # html.H1(children="This is model showcase page"),
                                    # dcc.Link('Home',href="/"),
                                    html.Br(),
                                    html.Div(children=[
                                        html.H3(children="1. Classify image using resnet50"),
                                        # html.Div([
                                        #     "Select an Image:",
                                        #     dcc.Dropdown(id="image-dropdown",
                                        #     options=[{'label': i, 'value': os.path.join(IMAGE_DATASET_HOME,i)} for i in imagefiles_list])
                                        # ]),
                                        du.Upload(
                                            id='resnet50-image-uploader',
                                            text='Drag and Drop Here to upload!',
                                            text_completed='Uploaded: ',
                                            text_disabled='The uploader is disabled.',
                                            cancel_button=True,
                                            pause_button=True,
                                            disabled=False,
                                            filetypes=['jpg','mp4'],
                                            default_style = {
                                                'width': '100%',
                                                'height': '30px',
                                                'lineHeight': '60px',
                                                'borderWidth': '2px',
                                                'borderStyle': 'dashed',
                                                'borderRadius': '5px',
                                                'textAlign': 'center',
                                                'margin': '0px',
                                                'margin-bottom' : '10px',
                                                'color' : 'green'
                                            },
                                            upload_id=upload_id,
                                            max_files=5
                                        ),
                                        dbc.Button("Classify", color="warning", className="me-1",id="resnet50-image-classify-btn"),
                                        html.Div(id="output-image-upload")
                                    ],style={"margin":"10px"}),  
                            ],
                            )
    elif model_id == "mnist":
        showcase_page_layout =  html.Div(children=[
                                navigation.navbar,
                                html.Br(),
                                html.H3(children="This is mnist model page. Work in Progress..."),
                            ])
    elif model_id == "models":
         showcase_page_layout =  html.Div(children=[
                                navigation.navbar,
                                html.Br(),
                                dcc.Link(children="resnet50",href="/showcase/resnet50"),
                                html.Br(),
                                dcc.Link(children="mnist",href="/showcase/mnist"),
                            ])
    return showcase_page_layout


@dash.callback(Output("output-image-upload","children"),
          Input("resnet50-image-classify-btn","n_clicks"))
def update_output(n):
    if n:
        image_root_path = os.path.join(os.path.dirname(__file__),"..","uploads",str(upload_id))
        returned_div = []
        for file in os.listdir(image_root_path):
            model = tf.keras.applications.resnet50.ResNet50()
            image_name = os.path.join(image_root_path,file)
            img = utils.load_img(image_name,target_size=(224,224))
            img_array = utils.img_to_array(img)
            img_batch = np.expand_dims(img_array,axis=0)
            img_preprocessed = preprocess_input(img_batch)
            img_prediction = model.predict(img_preprocessed)
            decode_img_prediction = decode_predictions(img_prediction,top=3)
            print(decode_img_prediction)
            predicted_dict = {}
            for di in decode_img_prediction[0]:
                predicted_dict[di[1]] = di[2]
            returned_div.append(html.Div([#html.H5(image_name),
            html.Hr(),
            html.Img(src=img),
            html.Div([dash_table.DataTable([predicted_dict])])
            ]))
        return returned_div

