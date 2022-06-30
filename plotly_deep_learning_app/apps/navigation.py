import dash_bootstrap_components as dbc
#import dash_html_components as html
from dash import html
#from app import app
from dash.dependencies import Input, Output, State
import dash

# navbar = dbc.NavbarSimple(
#     children=[
#         dbc.NavItem(dbc.NavLink("Home", href="/")),
#         dbc.NavItem(dbc.NavLink("Model Showcase", href="/showcase")),
#         dbc.DropdownMenu(
#             children=[
#                 dbc.DropdownMenuItem("More pages", header=True),
#                 dbc.DropdownMenuItem("Model Showcase", href="/showcase")
#             ],
#             nav=True,
#             in_navbar=True,
#             label="More",
#         ),
#     ],
#     brand="Plotly Deep Learning App",
#     brand_href="/",
#     color="primary",
#     dark=True,
#     fluid=True,
#     links_left=True,
#     sticky='Top'  
# )

navbar = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row([
                        dbc.Col([
                            html.Img(src=dash.get_asset_url('logo2.png'), height="40px"),
                            dbc.NavbarBrand("Plotly Deep Learning App", className="ms-2")
                        ],
                        width={"size":"auto"})
                    ],
                    align="center",
                    className="g-0"),

                    dbc.Row([
                        dbc.Col([
                            dbc.Nav([
                                dbc.NavItem(dbc.NavLink("Home", href="/")),
                                #dbc.NavItem(dbc.NavLink("Fundamentals", href="/fundamentals")),
                                dbc.NavItem(dbc.DropdownMenu(
                                        children=[
                                            dbc.DropdownMenuItem("How neural network learns", href="/hownnlearns")
                                        ],
                                        nav=True,
                                        in_navbar=True,
                                        label="Fundamentals",
                                )),
                                dbc.NavItem(dbc.NavLink("Model Showcase", href="/showcase")),
                                dbc.NavItem(dbc.DropdownMenu(
                                        children=[
                                            dbc.DropdownMenuItem("More pages", header=True),
                                            dbc.DropdownMenuItem("Model Showcase", href="/showcase")
                                        ],
                                        nav=True,
                                        in_navbar=True,
                                        label="More",
                                ))
                            ],
                            navbar=True
                            )
                        ],
                        width={"size":"auto"})
                    ],
                    align="center"),
                    dbc.Col(dbc.NavbarToggler(id="navbar-toggler", n_clicks=0)),
                    
                    dbc.Row([
                        dbc.Col(
                             dbc.Collapse(
                                dbc.Nav([
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"), href="https://github.com/siddharthajuprod07/algorithms/tree/master/plotly_deep_learning_app",external_link=True) ),
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi bi-twitter"), href="https://twitter.com/splunk_ml",external_link=True) ),
                                    dbc.NavItem(dbc.NavLink(html.I(className="bi bi-youtube"), href="https://www.youtube.com/channel/UC7J8myLv3tPabjeocxKQQKw",external_link=True) ),
                                    dbc.Input(type="search", placeholder="Search"),
                                    dbc.Button( "Search", color="primary", className="ms-2", n_clicks=0 ),
                                ]
                                ),
                                id="navbar-collapse",
                                is_open=False,
                                navbar=True
                             )
                        )
                    ],
                    align="center")
                ],
            fluid=True
            ),
    color="primary",
    dark=True
)


@dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open