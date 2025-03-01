from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components import cards
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
from callbacks import *

app.layout = html.Div([
    html.Div([
        html.H2("Bank Marketing Analytics", style={'textAlign': 'center', 'color': 'white', 'fontWeight': 'bold', 'fontSize': '50px'}),
        html.Hr(style={'color': 'gray', 'borderWidth': '5px'}),
        html.Div([
            html.H4("Filters", style={'textAlign': 'center', 'fontSize': '35px', 'marginTop': '20px'}),
            html.Div([
                html.P("Year", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                dcc.Checklist(
                    id="year_filter", # so callback function can detect changes
                    options=[
                        {'label': '2008', 'value': '2008'},
                        {'label': '2009', 'value': '2009'},
                        {'label': '2010', 'value': '2010'}
                    ],
                    value=['2008', '2009', '2010'], # default selection
                    inline=True,  
                    labelStyle={
                        'backgroundColor': '#e08136', 
                        'color': 'black',
                        'padding': '10px 15px', 
                        'marginRight': '11px',
                        'marginLeft': '11px', 
                        'borderRadius': '5px',
                        'fontSize': '18px'
                    }
                )
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'}),
            html.Div([
                html.P("Age", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                dcc.RangeSlider(
                    id="age_filter", # so callback function can access the selected age range
                    min=18, max=100, step=1, value=[25, 60], 
                    marks={i: str(i) for i in range(18, 101, 5)},
                    tooltip={"placement": "bottom", "always_visible": True, "style": {"fontSize": "16px"}}
                    ),
            ], style = {'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
            html.Div([
                html.P("Marital Status", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px', 'marginBottom': '5px'}),
                dcc.Checklist(
                    id="marital_filter", # so callback function can access changes
                    options=[
                        {'label': 'Married', 'value': 'married'},
                        {'label': 'Divorced', 'value': 'divorced'},
                        {'label': 'Single', 'value': 'single'}
                    ],
                    value=['married', 'divorced', 'single'],  # Default selection
                    inline=True,  
                    labelStyle={
                        'backgroundColor': '#e08136', 
                        'color': 'black',
                        'padding': '10px 15px', 
                        'marginRight': '20px',
                        'marginLeft': '20px',
                        'marginTop': '10px', 
                        'borderRadius': '5px',
                        'fontSize': '18px'
                    }
                )
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
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
                    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'})
        ], style={'color': 'white'})
    ], style={'width': '20%', 'backgroundColor': '#232242', 'padding': '20px', 'height': '100vh'}),

    html.Div([
        html.Div([
            cards
        ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '15px', 'height': '15%'}),

        html.Div([
            html.Div([
                html.Div("Education", style={'height': '15%', 'padding': '10px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '30px', 'fontWeight': 'bold'}),
                html.Div(style={'height': '85%', 'backgroundColor': 'white'})
            ], style={'width': '45%', 'margin': '1%'}),
            html.Div([
                html.Div("Number of Contacts", style={'height': '15%', 'padding': '10px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '30px', 'fontWeight': 'bold'}),
                html.Div(style={'height': '85%', 'backgroundColor': 'white'})
            ], style={'width': '45%', 'margin': '1%'}),
            html.Div([
                html.Div("Balance", style={'height': '15%', 'padding': '10px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '30px', 'fontWeight': 'bold'}),
                html.Div(style={'height': '85%', 'backgroundColor': 'white'})
            ], style={'width': '45%', 'margin': '1%', 'marginTop':'30px'}),
            html.Div([
                html.Div("Loan", style={'height': '15%', 'padding': '10px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '30px', 'fontWeight': 'bold'}),
                html.Div(style={'height': '85%', 'backgroundColor': 'white'})
            ], style={'width': '45%', 'margin': '1%', 'marginTop':'30px'})
        ], style={'display': 'flex', 'flexWrap': 'wrap', 'height': '700px'})
    ], style={'width': '80%', 'backgroundColor': '#d3d3d3', 'padding': '20px', 'height': '100vh'})
], style={'display': 'flex'})

if __name__ == '__main__':
    app.run_server(debug=True)


