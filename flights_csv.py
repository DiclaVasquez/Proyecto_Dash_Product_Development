import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sqlalchemy
from dash.dependencies import Input, Output, State

import data
import styles
from app import app, server

df = data.cant_vuelos_df
print(df)

origen_vuelo = df['origin'].unique()

content = html.Div([html.H1("Origen_del_vuelo"),
                    html.Br(),
                    html.Hr(),
                    dcc.Dropdown(id='origenes', options=origen_vuelo, value='EWR'),
                    dcc.Graph(id='serie_temporal')])

@app.callback(Output("serie_temporal","figure"),
              Input("origenes", "value"))

def set_vuelos_por_origen(origin_filtro):
    df['origin'] = df['origin'].astype(str)
    #df['month'] = pd.to_datetime(df['month'], format= '%Y-%m-%d%')
    df_filtrado = df[df['origin'] == origin_filtro]
    df_filtrado.sort_values(by='month',inplace=True)  # type: ignore
    df_final = df_filtrado.groupby(pd.Grouper(key='month', freq='1D')).sum()
    df_final.reset_index(inplace=True)
    print(df_final)
    
    fig = px.line(df_final, x='month', y='flight')
    fig.update_traces(line_color='#78c2ad')
    return fig