#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import tensorflow as tf
from tensorflow.keras.datasets import mnist


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(len(y_train))

page_layout = html.Div([
    navigation.navbar,
    html.H3(children="This is deep learning fundamentals page"),
    ]
)