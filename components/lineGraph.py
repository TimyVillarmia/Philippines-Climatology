import plotly.express as px


def line_graph(dataframe):
    fig = px.line(data_frame=dataframe,
                  x='year',
                  y=['mean', 'min', 'max'])
    return fig
