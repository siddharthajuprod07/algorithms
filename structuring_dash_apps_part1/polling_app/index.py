
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from app import app
from apps import home,polls,polls_results

url_content_layout = html.Div(children=[
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div")
])

app.layout = url_content_layout

app.validation_layout = html.Div([
    url_content_layout,
    home.home_layout,
    polls.polls_layout,
    polls_results.polls_results_layout
])


@app.callback(Output(component_id="output-div",component_property="children"),Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/polls":
        return  polls.polls_layout
    elif pathname == "/poll-results":
        return polls_results.polls_results_layout
    else:
        return home.home_layout


if __name__ == "__main__":
    app.run_server(debug=True)