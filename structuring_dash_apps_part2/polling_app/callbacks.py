
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import os


from app import app


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