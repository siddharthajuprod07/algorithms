import dash_html_components as html
import dash_core_components as dcc



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