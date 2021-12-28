import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import os


app = dash.Dash(__name__)

url_content_layout = html.Div(children=[
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div")
])

app.layout = url_content_layout

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
    dcc.Link('Home',href="/"),
    html.Br(),
    html.Br(),
    html.Div([
        "Select a Poll:",
        dcc.Dropdown(id="polls-name-dropdown",
        options=[{'label': i, 'value': i} for i in ["Poll1","Poll2", "Poll3"]])
    ]),
     html.Br(),
    html.Br(),
    html.Div(id="polls-question-div")

])

polls_results_layout = html.Div(children=[
    html.H1(children="This is Poll Results page"),
    dcc.Link('Home',href="/")
])

app.validation_layout = html.Div([
    url_content_layout,
    home_layout,
    polls_layout,
    polls_results_layout
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


@app.callback(Output(component_id="polls-question-div",component_property="children"),Input(component_id="polls-name-dropdown",component_property="value"))
def display_poll_question(pollname):
    poll_question_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'datasets','polls.csv'))
    #print(poll_question_df)
    poll_question_filtered_df = poll_question_df.loc[poll_question_df["poll_name"] == str(pollname)]
    question_input = None
    if not poll_question_filtered_df.empty:
        question_input = html.Div([
            dbc.Label(poll_question_filtered_df["question_text"]),
            dbc.RadioItems(
            options=[
                {"label": poll_question_filtered_df["option1"], "value": 1},
               {"label": poll_question_filtered_df["option2"], "value": 2},
               {"label": poll_question_filtered_df["option3"], "value": 3},
               {"label": poll_question_filtered_df["option4"], "value": 4}
            ],
            value=1,
            id="radioitems-input",
        ),
        ])
    question_div = html.Div([
        dbc.Form([question_input]) 
    ])

    return question_div


if __name__ == "__main__":
    app.run_server(debug=True)