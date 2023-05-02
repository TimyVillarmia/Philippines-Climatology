# import packages
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input, dash

# import components
from components import navbar, staticMap, lineGraph

# Load the geojson file
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/macoymejia/geojsonph/master/Regions/Regions.json') as response:
    geojson = json.load(response)

# creating dataframe
# philippines - climatology datasets
# Monthly Climatology of Mean,Min,Max Temperature & Precipitation 1991-2020 Philippines
# https://climateknowledgeportal.worldbank.org/country/philippines/climate-data-historical
df_sheet_all = pd.read_excel('data.xlsx', sheet_name=None)

# Prepare a lookup dictionary for selecting highlight areas in geojson
region_lookup = {feature['properties']['REGION']: feature
                 for feature in geojson['features']}

selections = set()

# initialize the app / dash constructor
app = dash.Dash(__name__, title='Philippines Climatology',
                external_stylesheets=[dbc.themes.BOOTSTRAP])

# app components will be displayed in the web browser
app.layout = html.Div([
    navbar.navbar,
    dbc.Container([
        html.H3("Observed Annual Mean, Minimum, Maximum Temperature, 1901-2021 Philippines",
                style={"text-align": "center",
                       "padding": 20}),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(options=[
                        {'label': 'Mean-Temperature', 'value': 'mean-temp'},
                        {'label': 'Min-Temperature', 'value': 'min-temp'},
                        {'label': 'Max-Temperature', 'value': 'max-temp'}
                    ],
                        value='mean-temp',
                        id='select_variable',
                        style={"width": "40%"})
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure={}, config={'displayModeBar': False},
                                  id='static_choropleth'), lg=6),
                dbc.Col(dcc.Graph(figure=lineGraph.line_graph(df_sheet_all['monthly_ph'],
                                                              'category',
                                                              ['mean', 'min', 'max'],
                                                              'Month',
                                                              'TEMPERATURE (°C)'),
                                  config={'displayModeBar': False},
                                  id='line_chart'), lg=6),
            ]
        ),
        dbc.Row(
            [
                html.H3("Observed Average Annual Mean-Temperature of Philippines for 1901-2021",
                        style={"text-align": "center"}),
                dbc.Col(dcc.Graph(figure=lineGraph.line_graph(df_sheet_all['annual_temp'], 'year', 'mean', 'Year',
                                                              'TEMPERATURE (°C)'), config={'displayModeBar': False},
                                  id='line_graph'), width=12)
            ]
        )
    ])
])


@app.callback(
    Output(component_id='static_choropleth', component_property='figure'),
    Input(component_id='select_variable', component_property='value')
)
def update_graph(variable_chosen):
    if variable_chosen == 'mean-temp':
        return staticMap.static_map(df_sheet_all['mean-temp'], geojson)

    elif variable_chosen == 'min-temp':
        return staticMap.static_map(df_sheet_all['min-temp'], geojson)
    else:
        return staticMap.static_map(df_sheet_all['max-temp'], geojson)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True)
