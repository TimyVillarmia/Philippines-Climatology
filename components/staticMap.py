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
                               center={"lat": 12.8797, "lon": -121.7740},  # Sets the center point of the map.
                               zoom=3,  # Sets map zoom level.
                               )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      height=450,
                      # set bounds for a map to specify an area
                      mapbox_bounds={"west": 110, "east": 140, "south": 0, "north": 25},
                      coloraxis_colorbar=dict(
                          title="TEMPERATURE (°C)",
                          title_side="top",  # location of color-bar's title
                          orientation='h',  # orientation of color-bar
                          x=0.5,  # sets the x position of the color bar (in plot fraction)
                          y=-0.1,  # sets the y position of the color bar (in plot fraction)
                          yanchor='middle',  # Sets the y position of the color bar (in plot fraction)
                          tickvals=[-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50],  # Sets the values at which ticks
                          # on this axis appear
                          ticktext=["-50", "-40", "-30", "-20", "-10", "0", "10", "20", "30", "40", "50"])  # Sets the
                      # text displayed at the ticks position via `tickvals`
                      )
    return fig
