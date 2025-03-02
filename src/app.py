from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
dash_app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = dash_app.server
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.components import cards, balance_plot, contact_plot, loan_plot, education_plot
from src.callbacks import *

dash_app.layout = html.Div([
    html.Div([
        html.H2("Bank Marketing Analytics", style={'textAlign': 'center', 'color': 'white', 'fontWeight': 'bold', 'fontSize': '35px'}),
        html.Hr(style={'color': 'gray', 'borderWidth': '5px'}),
        html.Div([
            html.H4("Filters", style={'textAlign': 'center', 'fontSize': '30px', 'marginTop': '20px'}),
            html.Div([
                html.P("Year", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                dcc.Checklist(
                    id="year_filter", 
                    options=[
                        {'label': '2008', 'value': '2008'},
                        {'label': '2009', 'value': '2009'},
                        {'label': '2010', 'value': '2010'}
                    ],
                    value=['2008', '2009', '2010'], 
                    inline=True,  
                    labelStyle={
                        'backgroundColor': '#e08136',
                        'color': 'black',
                        'padding': '10px 15px',
                        'borderRadius': '5px',
                        'fontSize': '0.8vw', 
                        'display': 'inline-flex', 
                        'alignItems': 'center', 
                        'flexGrow': 1, 
                        'margin': '0 3px', 
                    },
                    style={
                        'display': 'flex',  
                        'justifyContent': 'space-evenly',  
                        'width': '100%', 
                    }
                )
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'}),
            html.Div([
                html.P("Age", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                dcc.RangeSlider(
                    id="age_filter", 
                    min=18, max=100, step=1, value=[25, 60], 
                    marks={i: str(i) for i in range(15, 106, 10)},
                    tooltip={"placement": "bottom", "always_visible": True, "style": {"fontSize": "16px"}}
                    ),
            ], style = {'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
            html.Div([
                html.P("Marital Status", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px', 'marginBottom': '5px'}),
                dcc.Checklist(
                    id="marital_filter", 
                    options=[
                        {'label': 'Married', 'value': 'married'},
                        {'label': 'Divorced', 'value': 'divorced'},
                        {'label': 'Single', 'value': 'single'}
                    ],
                    value=['married', 'divorced', 'single'], 
                    inline=True,  
                    labelStyle={
                        'backgroundColor': '#e08136',
                        'color': 'black',
                        'padding': '8px 12px',
                        'borderRadius': '5px',
                        'fontSize': '0.8vw', 
                        'display': 'inline-flex',  
                        'alignItems': 'center',  
                        'flexGrow': 1,  
                        'margin': '0 3px',  
                    },
                    style={
                        'display': 'flex',  
                        'justifyContent': 'space-evenly',  
                        'width': '100%', 
                    }
            )], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
            html.Div([
                html.P("Job Type", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                dcc.Dropdown(
                    id="job_filter",
                    options=[
                        {'label': "Employed", 'value': 'Employed'},
                        {'label': "Retired", 'value': 'Retired'},
                        {'label': "Student", 'value': 'Student'},
                        {'label': "Unemployed", 'value': 'Unemployed'},
                        {'label': "Unknown", 'value': 'Unknown'},
                    ],
                    value='Employed',
                    clearable=False,
                    style={
                        'fontSize': '18px',
                        'color': 'black',
                        'backgroundColor': '#f8f9fa', 
                    },
                    className='dropdown-styling',
                )
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px',
                    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
            html.Div([
                html.H4("Info", style={'textAlign': 'center', 'fontSize': '30px', 'marginTop': '20px', 'color': 'black'}),
                html.Div([
                    html.P("Our Bank Marketing Dashboard helps financial institutions optimize their telemarketing strategies for term deposit subscriptions. By analyzing client demographics, financial status, and previous marketing interactions, we seek to identify key factors influencing customer decisions.",
                           style={'textAlign': 'center', 'fontSize': '20px', 'color': 'black', 'marginTop': '10px', 'marginBottom': '10px'}),
                    html.P("Copyright (c) 2025 Hrayr Muradyan, Merari Santana-Carbajal, Joseph Lim, Mason Zhang",
                           style={'textAlign': 'center', 'fontSize': '18px', 'color': 'black', 'marginTop': '10px', 'marginBottom': '10px'}),
                    html.P("The latest deployment date is 01/03/2025",
                           style={'textAlign': 'center', 'fontSize': '18px', 'color': 'black', 'marginTop': '10px', 'marginBottom': '10px'})
                ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'})
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
        ], style={'color': 'white'})
    ], style={'width': '20%', 'backgroundColor': '#232242', 'padding': '20px', 'height': '100vh',  
    'overflow-y': 'auto'}),

    html.Div([
        html.Div([
            cards
        ], style={
            'display': 'flex', 
            'flexWrap': 'wrap', 
            'justifyContent': 'space-between',  
            'boxSizing': 'border-box',  
            'height': '16%',
        }),

        html.Div([
            html.Div([
                html.Div("Proportion of Subscribed Users by Education Level", style={'height': '15%', 'padding': '5px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '20px', 'fontWeight': 'bold'}),
                html.Div([education_plot], style={'height': '82%'})
            ], style={'width': '45%', 'margin': '0.5%', 'flex-grow': 1}),

            html.Div([
                html.Div("Balance Distribution by Subscription Status", style={'height': '15%', 'padding': '5px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '20px', 'fontWeight': 'bold'}),
                html.Div([balance_plot], style={'height': '82%'})
            ], style={'width': '45%', 'margin': '0.5%', 'flex-grow': 1}),

            html.Div([
                html.Div("Campaign Contact and Subscription Status", style={'height': '15%', 'padding': '5px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '20px', 'fontWeight': 'bold'}),
                html.Div([contact_plot], style={'height': '82%'})
            ], style={'width': '45%', 'margin': '0.5%', 'flex-grow': 1}),

            html.Div([
                html.Div("Distribution of Personal Loan by Subscription Status", style={'height': '15%', 'padding': '5px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '20px', 'fontWeight': 'bold'}),
                html.Div([loan_plot], style={'height': '82%'})
            ], style={'width': '45%', 'margin': '0.5%', 'flex-grow': 1})
        ], style={'display': 'flex', 'flexWrap': 'wrap'})
    ], style={'width': '80%', 'backgroundColor': '#d3d3d3', 'padding': '20px', 'height': '100vh', 'position': 'fixed', 'right': 0, 'top': 0})
], style={'display': 'flex'})

if __name__ == '__main__':
    dash_app.run_server(debug=True)
    


