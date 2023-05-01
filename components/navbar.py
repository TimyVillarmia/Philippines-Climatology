import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Get Code", href="https://github.com/TimyVillarmia/Philippines-Climatology-Choropleth"
                                                 "-Map", target="_blank"))
    ],
    brand="Philippines - Climatology",
    brand_href="#",
    color="dark",
    dark=True,
    fluid=True,
)
