import dash
import dash_bootstrap_components as dbc



app = dash.Dash(__name__,external_stylesheets=[dbc.themes.UNITED])
server = app.server

