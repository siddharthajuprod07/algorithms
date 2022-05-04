import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Model Showcase", href="/showcase")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Model Showcase", href="/showcase")
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Plotly Deep Learning App",
    brand_href="/",
    color="primary",
    dark=True,
    fluid=True,
    links_left=True,
    sticky='Top'  
)