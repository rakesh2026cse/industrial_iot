from flask import Flask, render_template
from utils.db_utils import fetch_recent_data
import dash
from dash import html, dcc
import plotly.graph_objs as go
from threading import Thread
import time

server = Flask(__name__)

@server.route("/")
def home():
    return render_template("index.html")
app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dashboard/')

def get_plot_data():
    data = fetch_recent_data(50)
    timestamps = [d[4] for d in data]
    temps = [d[1] for d in data]
    vibs = [d[2] for d in data]
    press = [d[3] for d in data]
    return timestamps, temps, vibs, press

app.layout = html.Div(children=[
    html.H1(" Industrial Machine Monitoring Dashboard"),
    dcc.Interval(id='interval-component', interval=5*1000, n_intervals=0),

    dcc.Graph(id='live-graph'),
])

@app.callback(
    dash.dependencies.Output('live-graph', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    t, temp, vib, pres = get_plot_data()
    return {
        'data': [
            go.Scatter(x=t, y=temp, name="Temperature", line=dict(color='red')),
            go.Scatter(x=t, y=vib, name="Vibration", line=dict(color='blue')),
            go.Scatter(x=t, y=pres, name="Pressure", line=dict(color='green')),
        ],
        'layout': go.Layout(title='Live Sensor Readings', xaxis=dict(title='Time'), yaxis=dict(title='Value'))
    }

if __name__ == "__main__":
    app.run_server(debug=True)
