import plotly.express as px


def clickable_map(dataframe, geoJSON):
    # Create choropleth map
    fig = px.choropleth_mapbox(data_frame=dataframe,  # excel dataset
                               geojson=geoJSON,  # GeoJSON
                               featureidkey="properties.REGION",  # properties.<key> GeoJSON feature object
                               locations='REGION',  # column name in data_frame
                               mapbox_style="carto-positron",
                               center={"lat": 12.8797, "lon": -121.7740},  # Sets the center point of the map.
                               zoom=3,  # Sets map zoom level.
                               )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      height=450,
                      # set bounds for a map to specify an area
                      mapbox_bounds={"west": 110, "east": 140, "south": 0, "north": 25})

    return fig
