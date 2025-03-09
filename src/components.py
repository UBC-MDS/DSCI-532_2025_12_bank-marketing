import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import html

def create_stat_card(title, value_id, is_percentage=False, is_summary=False):
    """
    Creates a single statistic card component.
    :param title: Title of the metric
    :param value_id: ID for the value to be updated dynamically
    :param is_percentage: If True, the value will be displayed as a percentage
    :param is_summary: If True, this is the subscribed summary card
    """
    if is_summary:
        return dbc.Card(
            dbc.CardBody([
                html.H6(title, className="card-title", style={
                    'textAlign': 'center',
                    'fontSize': '1.1rem',
                    'fontWeight': 'bold',
                    'marginBottom': '15px'
                }),
                html.Div(id=value_id, children=[
                    html.P("Yes: 0", style={
                        'margin': '0px',
                        'color': '#60ac5a',
                        'fontSize': '1.8rem',
                        'fontWeight': 'bold'
                    }),
                    html.P("No: 0", style={
                        'margin': '0px',
                        'color': '#d16f6f',
                        'fontSize': '1.8rem',
                        'fontWeight': 'bold'
                    })
                ])
            ],
            style={
                'padding': '3px',
                'textAlign': 'center'
            }),
            className="mb-3 p-3 shadow-sm",
            style={'width': '100%', 'height': '100%', 'textAlign': 'center'}
        )
    else:
        return dbc.Card(
            dbc.CardBody([
                html.H6(title, className="card-title", style={
                    'textAlign': 'center',
                    'fontSize': '1.1rem',
                    'fontWeight': 'bold',
                    'marginBottom': '15px'
                }),
                html.H4(id=value_id, children="...", className="card-value", 
                       style={
                           'textAlign': 'center',
                           'data-is-percentage': str(is_percentage).lower(),
                           'fontSize': '1.8rem',
                           'fontWeight': 'bold',
                           'color': '#60ac5a' if is_percentage else '#232242'  # Use green for percentage, dark blue for others
                       })
            ],
            style={
                'padding': '3px',
                'textAlign': 'center'
            }),
            className="mb-3 p-3 shadow-sm",
            style={'width': '100%', 'height': '100%', 'textAlign': 'center'}
        )


def create_plot_card(plot_id):
    return dbc.Container([
        html.Div(
            dvc.Vega(id=plot_id, style={'width': '100%', 'height': '100%'}),
            style={'backgroundColor': 'white'}
        )
    ], className="mb-6 shadow-sm p-3", fluid=True, style={'height': '100%', 'backgroundColor': 'white'})


cards = html.Div([
    # Left group - 3 cards
    html.Div([
        dbc.Col(create_stat_card([
            html.Span("Average Contacts", style={'color': '#666666'}),
            html.Br(),
            html.Span("CURRENT", style={'color': '#232242', 'fontWeight': 'bold'}),
            html.Span(" Campaign", style={'color': '#666666'})
        ], "avg_contacts_campaign")),
        dbc.Col(create_stat_card([
            html.Span("Average Contacts", style={'color': '#666666'}),
            html.Br(),
            html.Span("PREVIOUS", style={'color': '#232242', 'fontWeight': 'bold'}),
            html.Span(" Campaigns", style={'color': '#666666'})
        ], "avg_contacts_before")),
        dbc.Col(create_stat_card([
            "Average Last Contact",
            html.Br(),
            "Duration (Seconds)"
        ], "avg_last_contact")),
    ], style={'width': '48%', 'margin': '0 1% 0 0', 'display': 'flex', 'justifyContent': 'space-between'}),
    
    # Right group - 2 cards
    html.Div([
        dbc.Col(create_stat_card("Proportion Subscribed", "prop_subscribed", is_percentage=True)),
        dbc.Col(create_stat_card("Subscribed?", "subscribed_summary", is_summary=True)),
    ], style={'width': '48%', 'margin': '0 0 0 1%', 'display': 'flex', 'justifyContent': 'space-between'})
], style={'display': 'flex', 'width': '100%', 'height': '100%'})

balance_plot = create_plot_card("balance_plot")
contact_plot = create_plot_card("contact_plot")
loan_plot = create_plot_card("loan_plot")
education_plot = create_plot_card("education_plot")

