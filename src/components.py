import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import html, dcc

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
                    'fontSize': '1.2rem',
                    'fontWeight': 'bold',
                    'marginBottom': '5px'
                }),
                html.Div(id=value_id, children=[
                    html.P("Yes: 0", style={
                        'margin': '0px',
                        'color': '#60ac5a',
                        'fontSize': '1.6rem',
                        'fontWeight': 'bold'
                    }),
                    html.P("No: 0", style={
                        'margin': '0px',
                        'color': '#d16f6f',
                        'fontSize': '1.6rem',
                        'fontWeight': 'bold'
                    })
                ])
            ],
            style={
                'padding': '3px',
                'textAlign': 'center'
            }),
            className="mb-3 p-3 shadow-sm",
            style={'width': '14vw', 'height': '105%', 'textAlign': 'center'}
        )
    else:
        return dbc.Card(
            dbc.CardBody([
                html.H6(title, className="card-title", style={
                    'textAlign': 'center',
                    'fontSize': '1.2rem',
                    'fontWeight': 'bold',
                    'marginBottom': '15px'
                }),
                html.H4(id=value_id, children="...", className="card-value", 
                       style={
                           'textAlign': 'center',
                           'data-is-percentage': str(is_percentage).lower(),
                           'fontSize': '1.6rem',
                           'fontWeight': 'bold',
                           'color': '#60ac5a' if is_percentage else '#232242'  # Use green for percentage, dark blue for others
                       })
            ],
            style={
                'padding': '3px',
                'textAlign': 'center'
            }),
            className="mb-3 p-3 shadow-sm",
            style={'width': '14vw', 'height': '105%', 'textAlign': 'center'}
        )


def create_plot_card(plot_id):
    return dbc.Container([
        html.Div(
            dcc.Loading(dvc.Vega(id=plot_id, opt={'actions': False}, style={'width': '50%', 'height': '100%', 'alignItems': 'center'}), type='circle'),
            style={'backgroundColor': 'white'}
        )
    ], className="mb-6 shadow-sm p-3", fluid=True, style={'height': '100%', 'backgroundColor': 'white', 'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'})


cards = html.Div([
    html.Div([
        dbc.Col(create_stat_card([
            html.Span("Average Contacts", style={'color': '#333333'}),
            html.Br(),
            html.Span("CURRENT", style={'color': '#323579', 'fontWeight': 'bold'}),
            html.Span(" Campaign", style={'color': '#333333'})
        ], "avg_contacts_campaign")),
        dbc.Col(create_stat_card([
            html.Span("Average Contacts", style={'color': '#333333'}),
            html.Br(),
            html.Span("PREVIOUS", style={'color': '#323579', 'fontWeight': 'bold'}),
            html.Span(" Campaigns", style={'color': '#333333'})
        ], "avg_contacts_before")),
        dbc.Col(create_stat_card([
            html.Span("Average Contact Duration In Seconds", style={'color': '#333333'})
        ], "avg_last_contact")),
        dbc.Col(create_stat_card(html.Span("Proportion Subscribed", style={'color': '#333333'}), 
                                 "prop_subscribed", is_percentage=True)),
        dbc.Col(create_stat_card(html.Span("Subscribed?", style={'color': '#333333'}), 
                                 "subscribed_summary", is_summary=True)),
    ], style={'width': '100%', 'display': 'flex', 'justifyContent': 'space-between'})
], style={'display': 'flex', 'width': '100%', 'height': '100%'})

balance_plot = create_plot_card("balance_plot")
contact_plot = create_plot_card("contact_plot")
loan_plot = create_plot_card("loan_plot")
education_plot = create_plot_card("education_plot")

