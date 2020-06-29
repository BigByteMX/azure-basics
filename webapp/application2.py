import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import webapp.createfigs as cf
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='fig1',),
    dcc.Input(id='npoints_input',value=20, type='number'),])

@app.callback(
    Output('fig1', 'figure'),
    [Input('npoints_input', 'value')])

def update_figure(selected_points):

    fig = cf.fig1(selected_points)

    fig.update_layout(transition_duration=500)

    return fig

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)