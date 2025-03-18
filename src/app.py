from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
dash_app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], assets_folder='../assets')
dash_app._favicon = "favicon.ico"
dash_app.title = "Bank Marketing Dashboard"
server = dash_app.server
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from components import cards, balance_plot, contact_plot, loan_plot, education_plot
from callbacks import *

dash_app.layout = html.Div([

    # Left column (20%) Filters, Info
    html.Div([
        # Title and Separator
        html.H2("Bank Marketing Analytics", style={'textAlign': 'center', 'color': 'white', 'fontWeight': 'bold', 'fontSize': '35px'}),
        html.Hr(style={'color': 'gray', 'borderWidth': '5px'}),

        # Tabs for navigation
        dcc.Tabs([
            # Filters Tab
            dcc.Tab(label='Filters', children=[
                html.Div([
                    # Filters Section Title
                    html.H4("Filters", style={'textAlign': 'center', 'fontSize': '30px', 'marginTop': '20px'}),
                    html.Div([

                        # Buttons for Reset and Export Data
                        html.Div([
                            html.Button(
                                "Reset All Filters",
                                id="reset-button",
                                style={
                                    'width': '48%',
                                    'padding': '10px',
                                    'backgroundColor': '#e08136',  # Button Color
                                    'color': 'black',  # Text Color
                                    'border': 'none',
                                    'borderRadius': '5px',  # Rounded Corners
                                    'fontSize': '18px',
                                    'cursor': 'pointer',
                                    'fontWeight': 'bold'
                                }
                            ),
                            html.Button(
                                "Export Data",
                                id="download_button",
                                style={
                                    'width': '48%',
                                    'padding': '10px',
                                    'backgroundColor': '#60ac5a',  # Button Color
                                    'color': 'white',  # Text Color
                                    'border': 'none',
                                    'borderRadius': '5px',  # Rounded Corners
                                    'fontSize': '18px',
                                    'cursor': 'pointer',
                                    'fontWeight': 'bold'
                                }
                            )
                        ], style={
                            'display': 'flex',  # Flexbox for layout
                            'justifyContent': 'space-between',  # Space between buttons
                            'marginBottom': '20px'
                        }),

                        # Download Data Component
                        dcc.Download(id="download_data")
                    ]),

                    # Filter for Year
                    html.Div([
                        html.P("Year", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                        dcc.Checklist(
                            id="year_filter", 
                            options=[
                                {'label': '2008', 'value': '2008'},
                                {'label': '2009', 'value': '2009'},
                                {'label': '2010', 'value': '2010'}
                            ],
                            value=['2008', '2009', '2010'],  # Default Selected Values
                            inline=True,  # Horizontal Layout
                            labelStyle={
                                'backgroundColor': '#e08136',  # Background Color of Labels
                                'color': 'black',
                                'padding': '10px 15px',
                                'borderRadius': '5px',  # Rounded Corners
                                'fontSize': '0.8vw',  # Font Size relative to viewport width
                                'display': 'inline-flex',  # Flexbox for labels
                                'alignItems': 'center',
                                'flexGrow': 1,  # Flex growth for equal distribution
                                'margin': '0 3px',  # Margin between items
                            },
                            style={
                                'display': 'flex',  
                                'justifyContent': 'space-evenly',  # Even space between checklist options
                                'width': '100%',  # Full width
                            }
                        )
                    ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'}),

                    # Filter for Age Range
                    html.Div([
                        html.P("Age", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                        dcc.RangeSlider(
                            id="age_filter", 
                            min=18, max=100, step=1, value=[25, 60],  # Default age range
                            marks={i: str(i) for i in range(15, 106, 10)},  # Age Marks
                            tooltip={"placement": "bottom", "always_visible": True, "style": {"fontSize": "16px"}}
                        ),
                    ], style = {'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),

                    # Filter for Marital Status
                    html.Div([
                        html.P("Marital Status", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px', 'marginBottom': '5px'}),
                        dcc.Checklist(
                            id="marital_filter", 
                            options=[
                                {'label': 'Married', 'value': 'married'},
                                {'label': 'Divorced', 'value': 'divorced'},
                                {'label': 'Single', 'value': 'single'}
                            ],
                            value=['married', 'divorced', 'single'],  # Default Values
                            inline=True,  # Horizontal Layout
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
                        )
                    ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),

                    # Filter for Job Type (Dropdown)
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
                            value='Employed',  # Default Selected Option
                            clearable=False,
                            style={
                                'fontSize': '18px',
                                'color': 'black',
                                'backgroundColor': '#f8f9fa',  # Dropdown Background Color
                            },
                            className='dropdown-styling',
                        )
                    ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
                ], style={'color': 'white'})
            ]),

            # About Tab
            dcc.Tab(label='About', children=[
                html.Div([
                    html.H4("Info", style={'textAlign': 'center', 'fontSize': '30px', 'marginTop': '20px', 'color': 'black'}),
                    html.Div([

                        # Info about the Dashboard
                        html.P("Our Bank Marketing Dashboard helps financial institutions optimize their telemarketing strategies for term deposit subscriptions. By analyzing client demographics, financial status, and previous marketing interactions, we seek to identify key factors influencing customer decisions.",
                            style={'textAlign': 'center', 'fontSize': '15px', 'color': 'black', 'marginTop': '10px', 'marginBottom': '10px'}),

                        # Repository Link
                        html.P([
                            html.Span("Repository Link:", style={'fontSize': '15px', 'color': 'black', 'fontWeight': 'bold'}),
                            html.A("Click Here", 
                                href="https://github.com/UBC-MDS/DSCI-532_2025_12_bank-marketing",
                                style={'fontSize': '15px', 'color': 'black', 'marginLeft': '15px'})
                        ], style={'textAlign': 'center', 'marginTop': '10px', 'marginBottom': '10px'}),

                        # Copyright Info and Deployment Date
                        html.P("Copyright (c) 2025 Hrayr Muradyan, Merari Santana-Carbajal, Joseph Lim, Mason Zhang",
                            style={'textAlign': 'center', 'fontSize': '15px', 'color': 'black', 'marginTop': '10px', 'marginBottom': '10px'}),
                        html.P("The latest deployment date is 01/03/2025",
                            style={'textAlign': 'center', 'fontSize': '15px', 'color': 'black', 'marginTop': '10px', 'marginBottom': '10px'})
                    ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'})
                ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
            ])
        ])
    ], style={'width': '20%', 'backgroundColor': '#232242', 'padding': '20px', 'height': '130vh'}),

    # Right column (80%) the summary cards and plots.
    html.Div([

        # Cards Section (e.g., summary statistics, KPIs)
        html.Div([
            cards  # Display the card elements (like summary statistics, KPIs)
        ], style={
            'display': 'flex',  # Use flexbox layout
            'flexWrap': 'wrap',  # Allow the cards to wrap if necessary
            'justifyContent': 'space-between',  # Distribute cards with space in between
            'boxSizing': 'border-box',  # Include padding and border in the element's total width and height
            'height': '16%',  # Set a fixed height for the cards section
            'margin': '0 0 20px 0'  # Add space at the bottom of the section
        }),

        # Main Content Section (Charts/Visualizations)
        html.Div([

            # Education level vs Subscription status plot
            html.Div([
                html.Div("Percentage of Subscribed Users by Education Level", style={
                    'height': '15%',  # Set height for the title
                    'padding': '5px',  # Add padding inside the title section
                    'backgroundColor': '#232242',  # Set background color
                    'textAlign': 'center',  # Center the title
                    'color': 'white',  # Title text color
                    'fontSize': '20px',  # Title font size
                    'fontWeight': 'bold'  # Bold font style
                }),
                html.Div([education_plot], style={'height': '82%'})  # Render the education plot with 82% height
            ], style={'width': '48%', 'margin': '0 1% 1% 0'}),  # Set width and margins for the layout

            # Loan status vs Subscription status plot
            html.Div([
                html.Div("Distribution of Personal Loan by Subscription Status", style={
                    'height': '15%',  # Set height for the title
                    'padding': '5px',  # Add padding inside the title section
                    'backgroundColor': '#232242',  # Set background color
                    'textAlign': 'center',  # Center the title
                    'color': 'white',  # Title text color
                    'fontSize': '20px',  # Title font size
                    'fontWeight': 'bold'  # Bold font style
                }),
                html.Div([loan_plot], style={'height': '82%'})  # Render the loan plot with 82% height
            ], style={'width': '48%', 'margin': '0 0 1% 1%'}),  # Set width and margins for the layout

            # Campaign contact vs Subscription status plot
            html.Div([
                html.Div("Campaign Contact and Subscription Status", style={
                    'height': '15%',  # Set height for the title
                    'padding': '5px',  # Add padding inside the title section
                    'backgroundColor': '#232242',  # Set background color
                    'textAlign': 'center',  # Center the title
                    'color': 'white',  # Title text color
                    'fontSize': '20px',  # Title font size
                    'fontWeight': 'bold'  # Bold font style
                }),
                html.Div([contact_plot], style={'height': '82%'})  # Render the contact plot with 82% height
            ], style={'width': '48%', 'margin': '0 1% 1% 0'}),  # Set width and margins for the layout

            # Balance distribution vs Subscription status plot
            html.Div([
                html.Div("Balance Distribution by Subscription Status", style={
                    'height': '15%',  # Set height for the title
                    'padding': '5px',  # Add padding inside the title section
                    'backgroundColor': '#232242',  # Set background color
                    'textAlign': 'center',  # Center the title
                    'color': 'white',  # Title text color
                    'fontSize': '20px',  # Title font size
                    'fontWeight': 'bold'  # Bold font style
                }),
                html.Div([balance_plot], style={'height': '82%'})  # Render the balance plot with 82% height
            ], style={'width': '48%', 'margin': '0 0 1% 1%'}),  # Set width and margins for the layout

        ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'flex-start'}),  # Flexbox layout for charts

    ], style={'width': '80%', 'backgroundColor': '#d3d3d3', 'padding': '20px', 'height': '100vh', 'position': 'fixed', 'right': 0, 'top': 0})  # Main content section style
], style={'display': 'flex'})

if __name__ == '__main__':
    dash_app.run_server(debug=True)
    


