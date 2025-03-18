import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import html, dcc

def create_stat_card(title, value_id, is_percentage=False, is_summary=False):
    """
    Creates a statistic card component for a dashboard.

    Parameters
    ----------
    title : str
        Title of the metric.
    value_id : str
        Unique ID for the value to be dynamically updated.
    is_percentage : bool, optional
        If True, the value will be displayed as a percentage (default is False).
    is_summary : bool, optional
        If True, returns the summary card with 'Yes' and 'No' counts (default is False).

    Returns
    -------
    dash_html_components.Card
        A Dash HTML Card component with the specified settings.
    """
    # Check if the card is a summary card
    if is_summary:
        # Create a card with summary information
        return dbc.Card(
            dbc.CardBody([  # Card body containing the content
                html.H6(title, className="card-title", style={  # Title of the card
                    'textAlign': 'center',  # Center align the text
                    'fontSize': '1.2rem',  # Set font size for the title
                    'fontWeight': 'bold',  # Make title bold
                    'marginBottom': '5px'  # Margin below the title
                }),
                html.Div(id=value_id, children=[  # Div container for the dynamic content
                    html.P("Yes: 0", style={  # "Yes" count text
                        'margin': '0px',  # No margin around the paragraph
                        'color': '#60ac5a',  # Green color for "Yes"
                        'fontSize': '1.6rem',  # Font size for the value
                        'fontWeight': 'bold'  # Bold font weight for the value
                    }),
                    html.P("No: 0", style={  # "No" count text
                        'margin': '0px',  # No margin around the paragraph
                        'color': '#d16f6f',  # Red color for "No"
                        'fontSize': '1.6rem',  # Font size for the value
                        'fontWeight': 'bold'  # Bold font weight for the value
                    })
                ])
            ],
            style={  # Overall card style
                'padding': '3px',  # Padding inside the card
                'textAlign': 'center'  # Center align text within the card
            }),
            className="mb-3 p-3 shadow-sm",  # Apply margins, padding, and shadow
            style={'width': '14vw', 'height': '105%', 'textAlign': 'center'}  # Set width and height for the card
        )
    else:
        # Create a regular statistic card
        return dbc.Card(
            dbc.CardBody([  # Card body containing the content
                html.H6(title, className="card-title", style={  # Title of the card
                    'textAlign': 'center',  # Center align the text
                    'fontSize': '1.2rem',  # Set font size for the title
                    'fontWeight': 'bold',  # Make title bold
                    'marginBottom': '15px'  # Margin below the title
                }),
                html.H4(id=value_id, children="...", className="card-value",  # Dynamic value placeholder
                       style={  # Style for the value display
                           'textAlign': 'center',  # Center align the text
                           'data-is-percentage': str(is_percentage).lower(),  # Indicate if it's a percentage
                           'fontSize': '1.6rem',  # Font size for the value
                           'fontWeight': 'bold',  # Bold font weight for the value
                           'color': '#60ac5a' if is_percentage else '#232242'  # Set color based on percentage flag
                       })
            ],
            style={  # Overall card style
                'padding': '3px',  # Padding inside the card
                'textAlign': 'center'  # Center align text within the card
            }),
            className="mb-3 p-3 shadow-sm",  # Apply margins, padding, and shadow
            style={'width': '14vw', 'height': '105%', 'textAlign': 'center'}  # Set width and height for the card
        )


def create_plot_card(plot_id):
    """
    Creates a plot card component with a loading spinner.

    Parameters
    ----------
    plot_id : str
        The unique ID for the plot to be displayed in the card.

    Returns
    -------
    dash_html_components.Container
        A Dash container component containing the plot card with the specified ID and a loading spinner.
    """
    return dbc.Container([  
        html.Div(  
            dcc.Loading(dvc.Vega(id=plot_id, opt={'actions': False}, style={'width': '50%', 'height': '100%', 'alignItems': 'center'}), type='circle'),  # Loading spinner with plot
            style={'backgroundColor': 'white'}  # Set background color for the Div
        )
    ], className="mb-6 shadow-sm p-3", fluid=True, style={'height': '100%', 'backgroundColor': 'white', 'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'})  # Set styles for the container


# Creating a set of statistic cards for the dashboard
cards = html.Div([  
    html.Div([  
        # First statistic card: Average Contacts for the current campaign
        dbc.Col(create_stat_card([  
            html.Span("Average Contacts", style={'color': '#333333'}),  # Title part
            html.Br(),  # Line break
            html.Span("CURRENT", style={'color': '#323579', 'fontWeight': 'bold'}),  # Highlight 'CURRENT'
            html.Span(" Campaign", style={'color': '#333333'})  # Campaign text
        ], "avg_contacts_campaign")),  # Unique ID for the value section

        # Second statistic card: Average Contacts for previous campaigns
        dbc.Col(create_stat_card([  
            html.Span("Average Contacts", style={'color': '#333333'}),  # Title part
            html.Br(),  # Line break
            html.Span("PREVIOUS", style={'color': '#323579', 'fontWeight': 'bold'}),  # Highlight 'PREVIOUS'
            html.Span(" Campaigns", style={'color': '#333333'})  # Campaign text
        ], "avg_contacts_before")),  # Unique ID for the value section

        # Third statistic card: Average Contact Duration in Seconds
        dbc.Col(create_stat_card([  
            html.Span("Average Contact Duration In Seconds", style={'color': '#333333'})  # Title text
        ], "avg_last_contact")),  # Unique ID for the value section

        # Fourth statistic card: Proportion of Subscribed, displayed as percentage
        dbc.Col(create_stat_card(html.Span("Proportion Subscribed", style={'color': '#333333'}), 
                                 "prop_subscribed", is_percentage=True)),  # Marked as percentage

        # Fifth statistic card: Subscribed summary, showing 'Yes' and 'No' counts
        dbc.Col(create_stat_card(html.Span("Subscribed", style={'color': '#333333'}), 
                                 "subscribed_summary", is_summary=True)),  # Summary card type
        
    ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'space-between'})  # Flex container for spacing between cards
], style={'display': 'flex', 'width': '100%', 'height': '100%'})  # Outer container for all the cards

# Creating plot cards for various plots
balance_plot = create_plot_card("balance_plot")  # Balance plot card
contact_plot = create_plot_card("contact_plot")  # Contact plot card
loan_plot = create_plot_card("loan_plot")  # Loan plot card
education_plot = create_plot_card("education_plot")  # Education plot card

