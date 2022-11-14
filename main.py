import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from flask import Flask, request
import requests
import styles

#llamada a paginas externas
import pages.flights_csv as flights_csv
import pages.flights_csv2 as flights_csv2
import pages.flights_csv3 as flights_csv3
import pages.error as error

#admin123
from app import app
from app import server
import data

sidebare = html.Div(children=[
    html.H1("Dashboard"),
    html.Hr(),
    dbc.Nav([
        dbc.NavLink('Cantidad de Vuelos', href="/flights_csv", active="exact"),
        dbc.NavLink('Cantidad de Vuelos2', href="/flights_csv2", active="exact"),
        dbc.NavLink('Cantidad de Vuelos3', href="/flights_csv3", active="exact"),
    ],
    vertical=True,
    pills=True),
    ],style=styles.SIDEBAR_STYLE
)

content = html.Div(id="page-content", style=styles.CONTENT_STYLE)

app.layout = html.Div(children=[dcc.Location(id="url"), sidebare, content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/flights_csv':
        return flights_csv.content
    elif pathname == '/flights_csv2':
        return flights_csv2.content
    elif pathname == '/flights_csv3':
        return flights_csv3.content
    else:
        return error.content
    
    
if __name__ == '__main__':
    app.run_server(port=4050)

