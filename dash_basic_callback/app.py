import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Welcome to the dash Polling app!"),
    html.Div(["Input: ", dcc.Input(id="input1",type="text", value="Initial Value")]),
    html.Br(),
    html.Div(id="output-div")
])

@app.callback(Output(component_id="output-div",component_property="children"),Input(component_id="input1",component_property="value"))
def update_output_div(input_val):
    output_val = "Output: {}".format(input_val)
    return output_val


if __name__ == "__main__":
    app.run_server(debug=True)