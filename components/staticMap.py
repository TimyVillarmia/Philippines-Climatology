import plotly.express as px


def static_map(dataframe, geoJSON):
    # Create choropleth map
    fig = px.choropleth_mapbox(data_frame=dataframe,  # excel dataset
                               geojson=geoJSON,  # GeoJSON
                               featureidkey="properties.REGION",  # properties.<key> GeoJSON feature object
                               locations='REGION',  # column name in data_frame
                               color='Jan',  # column to assign color
                               color_continuous_scale="balance",  # CSS-colors
                               range_color=(-50, 50),  # temperature range
                               mapbox_style="carto-positron",
                               center={"lat": 12.8797, "lon": -121.7740},
                               zoom=4,
                               )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      height=450,
                      mapbox_bounds={"west": 110, "east": 140, "south": 0, "north": 25},
                      coloraxis_colorbar=dict(
                          title="TEMPERATURE (°C)",
                          x=-0.1, orientation='v',
                          tickvals=[-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],
                          ticktext=["-50", "-40", "-30", "-20", "-10", "0", "10", "20", "30", "40", "50"])

                      )
    return fig
