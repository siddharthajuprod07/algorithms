from dash import html
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__,title="Page not found")

layout =html.Div(children=[
        dbc.Button("Go back to Home", size="lg", id="home_btn_404",href="/"),
],className="bg")


