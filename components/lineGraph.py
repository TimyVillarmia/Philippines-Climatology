import plotly.express as px


def line_graph(dataframe, x_axis, y_axis, x_title, y_title):
    fig = px.line(data_frame=dataframe,
                  x=x_axis,
                  y=y_axis)

    fig.update_layout(xaxis_title=x_title,
                      yaxis_title=y_title,
                      height=450,
                      yaxis_ticksuffix=" °C"
                      )

    return fig
