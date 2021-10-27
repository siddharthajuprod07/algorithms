import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    #html.H1(children="Welcome to the dash Polling app!"),
    dcc.Location(id="url",refresh=False),
    # dcc.Link('Home',href="/"),
    # html.Br(),
    # dcc.Link('Polls',href="/polls"),
    # html.Br(),
    # dcc.Link('Poll Results',href="/poll-results"),
    html.Div(id="output-div")
])

home_layout = html.Div(children=[
    html.H1(children="Welcome to the dash Polling app!"),
    dcc.Link('Home',href="/"),
    html.Br(),
    dcc.Link('Polls',href="/polls"),
    html.Br(),
    dcc.Link('Poll Results',href="/poll-results")
])

polls_layout = html.Div(children=[
    html.H1(children="This is Polls page"),
    dcc.Link('Home',href="/")
])

polls_results_layout = html.Div(children=[
    html.H1(children="This is Poll Results page"),
    dcc.Link('Home',href="/")
])

@app.callback(Output(component_id="output-div",component_property="children"),Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/polls":
        return  polls_layout
    elif pathname == "/poll-results":
        return polls_results_layout
    else:
        return home_layout
    #output_val = "Output: {}".format(pathname)
    #return output_val


if __name__ == "__main__":
    app.run_server(debug=True)