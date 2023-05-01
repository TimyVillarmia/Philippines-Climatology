# import packages
import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input, dash_table

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
df_mean = pd.read_excel('data.xlsx', sheet_name='mean-temp')
df_min = pd.read_excel('data.xlsx', sheet_name='min-temp')
df_max = pd.read_excel('data.xlsx', sheet_name='max-temp')
df_annual = pd.read_excel('data.xlsx', sheet_name='annual_temp')

# Prepare a lookup dictionary for selecting highlight areas in geojson
region_lookup = {feature['properties']['REGION']: feature
                 for feature in geojson['features']}


# # function to get the geojson file for highlighted area
# def get_highlights(selections, geojson=geojson, region_lookup=region_lookup):
#     geojson_highlights = dict()
#     for k in geojson.keys():
#         if k != 'features':
#             geojson_highlights[k] = geojson[k]
#         else:
#             geojson_highlights[k] = [region_lookup[selection] for selection in selections]
#     return geojson_highlights
#
#
# def get_figure(selections, select_month):
#     # Base choropleth layer --------------#
#     fig = px.choropleth_mapbox(data_frame=df_mean,  # excel dataset
#                                geojson=geojson,  # GeoJSON
#                                featureidkey="properties.REGION",  # properties.<key> GeoJSON feature object
#                                locations='REGION',  # column name in data_frame
#                                color=select_month,  # column to assign color
#                                color_continuous_scale="balance",  # CSS-colors
#                                range_color=(-50, 50),  # temperature range
#                                opacity=0.5,
#                                mapbox_style="carto-positron",
#                                center={"lat": 12.8797,
#                                        "lon": -121.7740},
#                                zoom=8
#                                )
#
#     # Second layer - Highlights ----------#
#     if len(selections) > 0:
#         # highlights contain the geojson information for only the selected region
#         highlights = get_highlights(selections)
#
#         fig.add_trace(
#             px.choropleth_mapbox(data_frame=df_mean,  # excel dataset
#                                  geojson=highlights,  # GeoJSON
#                                  featureidkey="properties.REGION",  # properties.<key> GeoJSON feature object
#                                  locations='REGION',  # column name in data_frame
#                                  color=select_month,  # column to assign color
#                                  color_continuous_scale="balance",  # CSS-colors
#                                  range_color=(-50, 50),  # temperature range
#                                  opacity=1,
#                                  mapbox_style="carto-positron",
#                                  center={"lat": 12.8797,
#                                          "lon": -121.7740},
#                                  zoom=1
#                                  ).data[0]
#         )
#
#     # ------------------------------------#
#
#     fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
#                       height=450,
#                       mapbox_bounds={"west": 110, "east": 140, "south": 0, "north": 25},
#                       coloraxis_colorbar=dict(
#                           title="TEMPERATURE (°C)",
#                           tickvals=[-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],
#                           ticktext=["-50", "-40", "-30", "-20", "-10", "0", "10", "20", "30", "40", "50"])
#
#                       )
#
#     return fig


selections = set()

# initialize the app / dash constructor
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# app components will be displayed in the web browser
app.layout = html.Div([
    navbar.navbar,
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                                 'Jan',
                                 id='select_month',
                                 style={"width": "40%"})
                )
            ]
        ),
        dbc.Row(
            [
                html.H3("Observed Annual Mean, Minimum, Maximum Temperature, 1901-2021 Philippines",
                        style={"text-align": "center"}),
                dbc.Col(dcc.Graph(figure=staticMap.static_map(df_mean, geojson), id='static_choropleth'), width=6),
                dbc.Col(dcc.Graph(figure=lineGraph.line_graph(df_annual), id='line_graph'), width=6)
            ]
        )
        # dbc.Row(
        #     [
        #         dbc.Col(dcc.Graph(figure={}, id='choropleth'))
        #     ]
        # )
    ])
])


# Add controls to build the interaction
@app.callback(
    Output('choropleth', 'figure'),
    [Input('choropleth', 'clickData'),
     Input('select_month', 'value')])
def update_graph(clickData, select_month):
    if clickData is not None:
        location = clickData['points'][0]['location']

        if location not in selections:
            selections.clear()
            selections.add(location)
        else:
            selections.remove(location)

    # return get_figure(selections, select_month)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True)
